# -*- coding: utf-8 -*-
"""
build_video.py — assemble a video (long-form or a short) from script_data scenes.

Per scene: render a still (PIL) + synth narration (TTS) -> a scene clip
(image held for narration length, with a subtle zoom + fade) via ffmpeg.
Concatenate scene clips, then mix an ambient BGM bed underneath.

Usage:
    python3 build_video.py long      -> output/ningen_shikkaku_long.mp4   (16:9)
    python3 build_video.py short1    -> output/ningen_shikkaku_short1.mp4 (9:16)
    python3 build_video.py short2 / short3
"""
import os, sys, subprocess, wave, contextlib
import imageio_ffmpeg
import visuals as V
import bgm as BGM
import tts as TTS
import script_data as S

FF = imageio_ffmpeg.get_ffmpeg_exe()
OUT = os.path.join(os.path.dirname(__file__), "output")
TMP = os.path.join(OUT, "_tmp")
os.makedirs(TMP, exist_ok=True)

FPS = 30


def render_bg(spec, size):
    fn = spec["bg"]
    a = spec.get("bgargs", {})
    if fn == "title":
        return V.draw_title(V.bg_dark(size), **a)
    if fn == "mask":
        return V.bg_mask(size, **a)
    if fn == "crowd":
        return V.bg_crowd(size, **a)
    if fn == "phone":
        return V.bg_phone(size, **a)
    if fn == "manuscript":
        return V.bg_manuscript(size)
    if fn == "mirror":
        return V.bg_mirror(size)
    if fn == "dark":
        return V.bg_dark(size, **a)
    raise ValueError(fn)


def wav_dur(path):
    with contextlib.closing(wave.open(path, "r")) as w:
        return w.getnframes() / w.getframerate()


def build_scene(scene, size, idx, portrait):
    # 1) image (background + telop burned in)
    img = render_bg(scene, size)
    if scene.get("telop"):
        px = scene.get("telop_px")
        img = V.draw_text_block(img, scene["telop"], pos=scene.get("pos", "bottom"),
                                size_px=px)
    png = os.path.join(TMP, f"{scene['id']}.png")
    img.save(png)

    # 2) narration audio
    wav = os.path.join(TMP, f"{scene['id']}.wav")
    TTS.synth(scene.get("narr", ""), wav)
    dur = max(wav_dur(wav), 1.4)

    # 3) scene clip: subtle slow zoom (zoompan) + fade in/out, with narration
    clip = os.path.join(TMP, f"{scene['id']}.mp4")
    w, h = size
    total_frames = int(dur * FPS)
    # gentle zoom 1.0 -> 1.06
    zexpr = f"zoom='min(zoom+0.0006,1.06)':d={total_frames}:s={w}x{h}:fps={FPS}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
    fade = f"fade=t=in:st=0:d=0.4,fade=t=out:st={max(dur-0.4,0):.3f}:d=0.4"
    vf = f"scale={w*2}:{h*2},zoompan={zexpr},{fade},format=yuv420p"
    cmd = [FF, "-y", "-loop", "1", "-i", png, "-i", wav,
           "-t", f"{dur:.3f}",
           "-vf", vf, "-r", str(FPS),
           "-c:v", "libx264", "-preset", "medium", "-crf", "20",
           "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
           "-pix_fmt", "yuv420p", "-shortest", clip]
    subprocess.run(cmd, check=True, capture_output=True)
    return clip, dur


def assemble(kind):
    if kind == "long":
        scenes = S.LONG
        size = (1920, 1080)
        portrait = False
        out = os.path.join(OUT, "ningen_shikkaku_long.mp4")
    else:
        scenes = S.SHORTS[kind]
        size = (1080, 1920)
        portrait = True
        out = os.path.join(OUT, f"ningen_shikkaku_{kind}.mp4")

    clips = []
    total = 0.0
    for i, sc in enumerate(scenes):
        clip, dur = build_scene(sc, size, i, portrait)
        clips.append(clip)
        total += dur
        print(f"  [{kind}] scene {sc['id']:<5} {dur:5.1f}s  (cum {total:6.1f}s)", flush=True)

    # concat list
    listf = os.path.join(TMP, f"concat_{kind}.txt")
    with open(listf, "w") as f:
        for c in clips:
            f.write(f"file '{c}'\n")
    joined = os.path.join(TMP, f"joined_{kind}.mp4")
    subprocess.run([FF, "-y", "-f", "concat", "-safe", "0", "-i", listf,
                    "-c", "copy", joined], check=True, capture_output=True)

    # BGM bed
    bgm_wav = os.path.join(TMP, f"bgm_{kind}.wav")
    BGM.make_bgm(total + 2, bgm_wav, gain=0.13 if kind == "long" else 0.11)

    # mix narration (from joined) with bgm; narration kept dominant
    cmd = [FF, "-y", "-i", joined, "-i", bgm_wav,
           "-filter_complex",
           "[1:a]afade=t=in:st=0:d=2,afade=t=out:st=%.2f:d=2[bg];"
           "[0:a][bg]amix=inputs=2:duration=first:weights=1 0.5:normalize=0,"
           "loudnorm=I=-14:TP=-1.5:LRA=11[a]" % max(total - 2, 0),
           "-map", "0:v", "-map", "[a]",
           "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
           "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True, capture_output=True)
    return out, total


if __name__ == "__main__":
    kind = sys.argv[1] if len(sys.argv) > 1 else "long"
    print(f"TTS available: {TTS.available()}")
    out, total = assemble(kind)
    sz = os.path.getsize(out) / 1e6
    print(f"DONE {out}  ({total:.1f}s, {sz:.1f} MB)")
