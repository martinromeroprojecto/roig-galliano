#!/usr/bin/env bash
# fetch_placeholders.sh — descarga placeholders REALES de Unsplash
# para los 11 huecos de imágenes de la landing Roig·Galliano.
#
# Requisitos: bash, curl, jq, una Access Key gratis de Unsplash
#   1) Sacá tu key en https://unsplash.com/oauth/applications (gratis, instant)
#   2) export UNSPLASH_ACCESS_KEY="tu_access_key_aqui"
#   3) ./tools/fetch_placeholders.sh
#
# Salida: ./assets/placeholders/*.jpg

set -euo pipefail

: "${UNSPLASH_ACCESS_KEY:?Falta UNSPLASH_ACCESS_KEY en el entorno. Get one at https://unsplash.com/oauth/applications}"

command -v jq >/dev/null 2>&1 || { echo "Instalá jq: brew install jq"; exit 1; }

OUT_DIR="./assets/placeholders"
mkdir -p "$OUT_DIR"

# id | query | orientation | nombre_archivo
ITEMS=(
  "IMG-01|argentine entrepreneur portrait warehouse miami|portrait|hero-video-poster.jpg"
  "IMG-02|aerial shipping port containers dusk minimal|landscape|hero-bg-port.jpg"
  "IMG-03|man portrait warehouse logistics warm light|portrait|host-bauti.jpg"
  "IMG-04|man portrait glasses dark jacket city blue hour|portrait|host-ema.jpg"
  "IMG-05|silhouette person backlit bokeh emerald|portrait|host-next.jpg"
  "IMG-06|argentine male small workshop portrait calm|squarish|testi-mariano.jpg"
  "IMG-07|argentine male entrepreneur clothing samples office|portrait|testi-martin.jpg"
  "IMG-08|argentine female entrepreneur decor showroom|portrait|testi-carolina.jpg"
  "IMG-09|argentine male desk laptop tech accessories|portrait|testi-lucas.jpg"
  "IMG-10|abstract minimal shipping containers warm light wide|landscape|og-card.jpg"
  "IMG-11|overhead desk coffee notebook smartphone wood warm|landscape|thankyou-banner.jpg"
)

for ITEM in "${ITEMS[@]}"; do
  IFS="|" read -r ID QUERY ORIENT FILENAME <<< "$ITEM"
  echo "→ $ID  ($QUERY · $ORIENT)"

  URL=$(curl -fsSL -G "https://api.unsplash.com/photos/random" \
    -H "Accept-Version: v1" \
    -H "Authorization: Client-ID $UNSPLASH_ACCESS_KEY" \
    --data-urlencode "query=$QUERY" \
    --data-urlencode "orientation=$ORIENT" \
    --data-urlencode "content_filter=high" \
    | jq -r '.urls.regular')

  if [[ -z "${URL:-}" || "$URL" == "null" ]]; then
    echo "  ! Sin resultados — saltando"
    continue
  fi

  curl -fsSL "$URL" -o "$OUT_DIR/$FILENAME"
  echo "  ✓ $OUT_DIR/$FILENAME"
done

echo ""
echo "Listo. Reemplazá los <div class=\"img-ph\"> de landing.html por <img src=\"assets/placeholders/XXX.jpg\" ...>"
echo "Cuando tengas las definitivas con IA, pisá los archivos manteniendo los nombres."
