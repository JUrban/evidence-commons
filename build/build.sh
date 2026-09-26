#!/bin/bash
# Build a PDF from a markdown source. Usage: build/build.sh <src.md> <out.pdf>
set -e
SRC=$1; OUT=$2
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$(dirname "$OUT")"
TMP=$(mktemp -d)
# figures are referenced relative to the source file
cp -r "$(dirname "$SRC")"/figures "$TMP"/ 2>/dev/null || true
pandoc "$SRC" -f markdown -t html5 -s --css "$HERE/style.css" --metadata title="Evidence Commons" -o "$TMP/build.html"
python3 - "$TMP/build.html" << 'PY'
import re, sys
p=sys.argv[1]; h=open(p).read()
h=re.sub(r'<header id="title-block-header">.*?</header>','',h,flags=re.S)
h=h.replace('<h1','<h1 style="margin-top:28pt"')
open(p,'w').write(h)
PY
wkhtmltopdf --disable-smart-shrinking --enable-local-file-access --page-size A4 \
  --margin-top 17mm --margin-bottom 17mm --margin-left 21mm --margin-right 21mm \
  --footer-center "[page] / [topage]" --footer-font-size 8 --footer-font-name "DejaVu Sans" \
  "$TMP/build.html" "$OUT" >/dev/null 2>&1
python3 -c "from pypdf import PdfReader; print('$OUT pages:', len(PdfReader('$OUT').pages))" 2>/dev/null || echo "built $OUT"
