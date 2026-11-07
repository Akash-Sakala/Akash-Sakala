#!/usr/bin/env bash
# Renders the animated profile assets with HyperFrames (HTML -> video) and
# encodes them as looping WebP for the README.
#   usage: bash profile-src/build.sh          (from the repo root)
# Needs Node 22+, FFmpeg with libwebp, and Chrome (HyperFrames finds or installs it).
set -euo pipefail
cd "$(dirname "$0")"
HF="npx --yes hyperframes@0.9.19"
OUT=../assets
CACHE=.cache
mkdir -p "$OUT" "$CACHE/fonts" "$CACHE/img"

fetch() { [ -s "$2" ] || curl -fsSL --retry 3 -o "$2" "$1"; }

# Fonts: Mona Sans (GitHub, OFL) + Noto Sans for Kannada / Telugu / Devanagari
MONA=https://raw.githubusercontent.com/github/mona-sans/main/fonts/webfonts/static
for f in MonaSans-Medium MonaSans-SemiBold MonaSansDisplay-ExtraBold; do fetch "$MONA/$f.woff2" "$CACHE/fonts/$f.woff2"; done
for s in kannada telugu devanagari; do
  fetch "https://cdn.jsdelivr.net/fontsource/fonts/noto-sans-$s@latest/$s-600-normal.woff2" "$CACHE/fonts/NotoSans-$s.woff2"
done

# Real AgriQNet 2.0 screenshots, straight from that repo
AQ=https://raw.githubusercontent.com/Akash-Sakala/AgriQNet-2.0/main/docs/demo_assets
declare -A SHOTS=(
  [d_home]=03-home-desktop.png [d_map]=20-alert-network-map-desktop.png
  [d_library]=23-library-chat-citations-desktop.png [d_weather]=08-weather-forecast-desktop.png
  [p_crop]=10-crop-result-phone.jpg [p_pest]=14-pest-detected-phone.jpg
  [p_kannada]=06-home-kannada-phone.jpg [p_weather]=19-alerts-weather-sms-phone.jpg
)
for k in "${!SHOTS[@]}"; do
  src="$CACHE/img/${SHOTS[$k]}"; fetch "$AQ/${SHOTS[$k]}" "$src"
  [ -s "$CACHE/img/$k.jpg" ] || ffmpeg -v error -y -i "$src" -vf "scale='min(1360,iw)':-2" -q:v 3 "$CACHE/img/$k.jpg"
done

# name  width  (canvas sizes live in each index.html)
render() {
  local name=$1 width=$2
  mkdir -p "$name/assets/fonts"
  cp "$CACHE"/fonts/*.woff2 "$name/assets/fonts/"
  if [ "$name" = agri ]; then mkdir -p agri/assets/img && cp "$CACHE"/img/{d,p}_*.jpg agri/assets/img/; fi
  (cd "$name" && $HF render --quality looks -o "../$CACHE/$name.mp4")
  ffmpeg -v error -y -i "$CACHE/$name.mp4" -vf "fps=20,scale=$width:-1:flags=lanczos" \
    -c:v libwebp_anim -q:v 62 -compression_level 6 -loop 0 "$OUT/$name.webp"
  echo "✓ $OUT/$name.webp ($(du -h "$OUT/$name.webp" | cut -f1))"
}

render hero 1280
render agri 1280
render clipper 1280
render audiocnn 1280
render kriya 1280
render timeline 1280
