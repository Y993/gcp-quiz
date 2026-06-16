"""
bgm.py — generate a somber ambient pad (minor, slow) with numpy.
No samples/external audio. Output: 16-bit PCM WAV, 44.1kHz stereo.
"""
import numpy as np, wave, struct

SR = 44100

def _note(freq, dur, sr=SR):
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    # soft pad: fundamental + octave + fifth, gentle detune, slow vibrato
    sig = np.zeros_like(t)
    for mult, amp in [(1.0, 1.0), (2.0, 0.35), (1.5, 0.25), (0.5, 0.4)]:
        detune = 1 + 0.0008 * np.sin(2 * np.pi * 0.13 * t)
        sig += amp * np.sin(2 * np.pi * freq * mult * detune * t)
    sig /= 2.0
    return t, sig

def _adsr(n, a=0.25, r=0.35, sr=SR):
    env = np.ones(n)
    na, nr = int(a * sr), int(r * sr)
    if na > 0:
        env[:na] = np.linspace(0, 1, na)
    if nr > 0:
        env[-nr:] = np.linspace(1, 0, nr)
    return env

# A minor-ish progression of slow chords (Hz). Am - F - C - G feel, low octave.
_PROG = [
    [110.00, 130.81, 164.81],  # A C E  (Am)
    [87.31, 110.00, 130.81],   # F A C  (F)
    [98.00, 123.47, 146.83],   # G B D  (G)
    [82.41, 98.00, 123.47],    # E G B  (Em)
]

def make_bgm(total_sec, path, chord_sec=6.0, gain=0.16):
    n_total = int(SR * total_sec)
    out = np.zeros(n_total)
    pos = 0
    ci = 0
    while pos < n_total:
        chord = _PROG[ci % len(_PROG)]
        _, mix = _note(chord[0], chord_sec)
        for f in chord[1:]:
            _, s = _note(f, chord_sec)
            mix = mix + s
        mix /= len(chord)
        mix *= _adsr(len(mix), a=1.2, r=1.6)
        end = min(pos + len(mix), n_total)
        out[pos:end] += mix[:end - pos]
        pos += int(len(mix) * 0.82)  # overlap chords for smoothness
        ci += 1
    # subtle low-pass via moving average + normalize
    k = 24
    out = np.convolve(out, np.ones(k) / k, mode="same")
    out = out / (np.max(np.abs(out)) + 1e-9) * gain
    # gentle stereo widening
    left = out
    right = np.roll(out, 220)
    stereo = np.stack([left, right], axis=1)
    pcm = (stereo * 32767).astype(np.int16)
    with wave.open(path, "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    return path

if __name__ == "__main__":
    make_bgm(30, "output/_bgm_test.wav")
    print("bgm written")
