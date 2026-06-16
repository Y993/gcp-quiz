# -*- coding: utf-8 -*-
"""
tts.py — Japanese narration via pyopenjtalk (offline HTS voice).
Falls back to generating silence of an estimated length if TTS is unavailable,
so the pipeline still produces a valid (telop-only) video.
"""
import wave, numpy as np

try:
    import pyopenjtalk
    _HAS_TTS = True
except Exception:
    _HAS_TTS = False

TARGET_SR = 44100


def _resample(x, sr_in, sr_out):
    if sr_in == sr_out:
        return x
    n_out = int(round(len(x) * sr_out / sr_in))
    xp = np.linspace(0, 1, len(x), endpoint=False)
    fp = np.linspace(0, 1, n_out, endpoint=False)
    return np.interp(fp, xp, x)


def synth(text, path, *, speed=0.96, lead=0.35, tail=0.55, gain=0.92):
    """Synthesize `text` to a 16-bit mono WAV at `path`. Returns duration sec."""
    if _HAS_TTS and text:
        x, sr = pyopenjtalk.tts(text, speed=speed)
        x = np.asarray(x, dtype=np.float64)
        if np.max(np.abs(x)) > 0:
            x = x / np.max(np.abs(x)) * gain
        x = _resample(x, sr, TARGET_SR)
    else:
        # fallback: estimate ~7.5 mora/sec; silence
        est = max(1.2, len(text or "") / 7.0)
        x = np.zeros(int(est * TARGET_SR))
    lead_n = int(lead * TARGET_SR)
    tail_n = int(tail * TARGET_SR)
    x = np.concatenate([np.zeros(lead_n), x, np.zeros(tail_n)])
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(TARGET_SR)
        w.writeframes(pcm.tobytes())
    return len(x) / TARGET_SR


def available():
    return _HAS_TTS
