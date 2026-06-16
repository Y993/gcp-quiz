# 人間失格 動画生成パイプライン

`docs/youtube-example-ningen-shikkaku.md` の台本を、実際の **MP4 動画**に書き出す
自己完結パイプライン。外部の画像生成API・クラウドTTSは使わず、すべてローカルで生成します。

## 生成物（`output/`）
| ファイル | 形式 | 内容 |
|---|---|---|
| `ningen_shikkaku_long.mp4` | 16:9 1920×1080 | 長尺解説（イントロ→あらすじ→読み解き3→現代接続→まとめ→CTA） |
| `ningen_shikkaku_short1.mp4` | 9:16 1080×1920 | 予告フック型 |
| `ningen_shikkaku_short2.mp4` | 9:16 1080×1920 | 名場面・考察型（笑顔＝防具） |
| `ningen_shikkaku_short3.mp4` | 9:16 1080×1920 | 問いかけ・共感型（本当の自分） |

## 構成
- `visuals.py` — 背景＋テロップ描画（PIL/numpy）。割れた仮面・群衆・スマホの光・原稿用紙・ぼやける鏡を手続き的に生成
- `bgm.py` — 沈鬱なアンビエントBGM生成（numpy・Am系の緩い進行）
- `tts.py` — 日本語ナレーション（pyopenjtalk・オフラインHTS音声）。未導入時は無音にフォールバック
- `script_data.py` — 長尺＋Shorts3本の全シーン（ナレーション・テロップ・背景指定）
- `build_video.py` — シーンごとに静止画＋音声→クリップ化（緩いズーム＋フェード）→連結→BGMミックス→`-14 LUFS`正規化

## 使い方
```bash
pip install pillow numpy imageio-ffmpeg
# 日本語ナレーション（任意・高品質化）
pip install --no-build-isolation --no-binary pyopenjtalk pyopenjtalk

python3 build_video.py long     # 長尺
python3 build_video.py short1   # ショート①
python3 build_video.py short2   # ショート②
python3 build_video.py short3   # ショート③
```

## 仕様メモ
- 30fps / H.264 / AAC / faststart
- ラウドネス `-14 LUFS`（YouTube基準）
- 著作権：原作は太宰治（1948年没＝パブリックドメイン）。ビジュアルは自作生成
- テーマを変える場合は `script_data.py` のシーン定義を差し替えるだけで再利用可能
