# BRIEF.md — Roig · Galliano

> Operativo end-to-end para la landing de la charla informativa grupal sobre importación desde China.
> Negocio: Roig · Galliano · Servicio de importación China → Argentina (con hub Miami).
> Producto: Zoom grupal informativo (~90 min) · ARS 90.000 · 3 cuotas sin interés con Mercado Pago.
> Idioma de toda la pieza: español argentino (voseo), tono conversacional profesional, cero chamuyo.

---

## 0. Índice

1. Resumen ejecutivo del funnel
2. Imágenes faltantes (IDs, ubicación, tamaño, prompts hyper-optimizados)
3. SVGs inline incluidos (no se generan con IA)
4. Checklist pre-publicación
5. Stack sugerido de generación de imágenes por tipo
6. Script bash para placeholders de Unsplash
7. Notas finales de tono
8. Fixes pendientes de QA (críticos + mayores) — landing.html y thankyou.html

---

## 1. Resumen ejecutivo del funnel

```
Landing (landing.html)
   └─ CTA "Reservá tu lugar en el Zoom"
        └─ Mercado Pago (link de pago · 1 pago o 3 cuotas s/interés)
             └─ ThankYou (thankyou.html)
                  └─ Botón "Mandar comprobante por WhatsApp" (wa.me prellenado)
                       └─ Humano del equipo (BA/Miami/Shanghai) agenda Zoom
                            └─ Zoom grupal 90 min · 10 pasos · Q&A
                                 └─ Post-Zoom: grabación + PDF resumen por WhatsApp
```

Hosts visibles en TODA la landing:
- **Juan Bautista Roig** — Hub Miami · Logística USA.
- **Emanuel Galliano** — Despacho Aduana · Shanghai.

Oficinas mencionadas en footer: Buenos Aires + Shanghai + Miami (vía alianza con Bauti).

---

## 2. Imágenes faltantes

Convención general para TODOS los prompts:
- Estilo base: editorial moderno, foto realista, cinematic, premium SaaS / fintech feel.
- Paleta global de marca: emerald (#10b981 / #059669) como acento, neutros cálidos (off-white, beige #f5f1eb, charcoal #1a1a1a), toques de oro pálido muy sutil.
- Negativos globales (agregar al final de TODO prompt): `no text, no logos, no watermarks, no captions, no UI overlays, no extra fingers, no warped hands, no plastic skin, no waxy skin, no oversaturation, no HDR halo, no AI artifacts, no cartoon, no anime, no 3D render look, no stock photo cliché, no flag of China, no Chinese characters, no Argentine flag, no US flag`.
- Resolución: exportar a 2x del tamaño de display, comprimir a WebP (calidad 82) + fallback JPG.

---

### IMG-01 — Hero · Video card poster (mientras carga el embed)

- **Ubicación**: `landing.html` → sección `hero` → tarjeta de video, antes del play del Zoom de muestra.
- **Tamaño display**: 640 × 800 px · ratio **4:5** (vertical) en desktop · en mobile 16:9 recorte centrado.
- **Export**: 1280 × 1600 px · WebP + JPG.
- **Formato**: foto editorial, dos retratos compuestos en split screen vertical (Bauti arriba/izq, Ema abajo/der) con sutil overlay glass.
- **Prompt hyper-optimizado**:

```
Editorial split-frame portrait, two Argentine male entrepreneurs in their late thirties shown in a vertical 4:5 composition.
Top-left: man with short dark hair, light stubble, wearing a charcoal merino sweater, photographed inside a sun-lit Miami logistics hub, blurred shipping containers and warehouse racks in the background, golden hour window light coming from camera-right, warm rim light on his cheekbone, looking slightly off-camera with a calm confident expression.
Bottom-right: man with medium-length brown hair, glasses, wearing an unbranded navy field jacket, photographed on a quiet Shanghai customs office mezzanine at blue hour, soft cool ambient light, distant cargo cranes and shipping yard lights in deep bokeh behind him, looking directly at the camera with a focused, serious-but-friendly expression.
The two frames are separated by a thin emerald-green light beam #10b981 as a subtle divider, slight film grain, cinematic color grade with warm highlights and cool teal shadows, 50mm lens, f/2.0, shallow depth of field, Kodak Portra 400 vibe, premium fintech-meets-editorial mood.
Negative: no text, no logos, no watermarks, no captions, no UI overlays, no extra fingers, no warped hands, no plastic skin, no waxy skin, no oversaturation, no HDR halo, no AI artifacts, no cartoon, no anime, no 3D render look, no stock photo cliché, no flag of China, no Chinese characters, no Argentine flag, no US flag.
```

---

### IMG-02 — Hero · Background ambient texture

- **Ubicación**: `landing.html` → sección `hero` → background absolute, opacidad 0.18.
- **Tamaño display**: 1920 × 1080 px · ratio **16:9**.
- **Export**: 2560 × 1440 px · WebP.
- **Formato**: textura abstracta, no fotográfica de personas.
- **Prompt hyper-optimizado**:

```
Abstract aerial top-down photograph of a stylized shipping port at dusk, neat grid of muted teal and beige cargo containers, faint warm sodium dock lights, very soft mist over the water, ultra-wide composition, almost cartographic feel, dreamy desaturated palette with one accent of emerald #10b981 reflected on wet concrete, shot on Phase One medium format, f/8, sharp but soft, dreamlike, premium editorial aerial photo, designed to live as a background under text with plenty of negative space toward the center.
Negative: no text, no logos, no watermarks, no captions, no flag, no Chinese characters, no people, no boats with brand markings, no oversaturation, no HDR halo, no AI artifacts, no cartoon, no 3D render look, no stock photo cliché.
```

---

### IMG-03 — Host card · Juan Bautista Roig (Hub Miami)

- **Ubicación**: `landing.html` → sección `hosts` → primera tarjeta de host.
- **Tamaño display**: 520 × 640 px · ratio **13:16** (semi-vertical).
- **Export**: 1040 × 1280 px · WebP + JPG.
- **Formato**: retrato editorial, ambiente logístico Miami.
- **Prompt hyper-optimizado**:

```
Editorial half-body portrait of a 36-year-old Argentine male entrepreneur named "Bauti" archetype: short dark hair neatly combed back, light stubble, warm olive skin, friendly intelligent eyes, wearing an off-white linen henley and a thin silver chain barely visible.
He is standing inside a modern Miami logistics hub office at late afternoon: floor-to-ceiling windows behind him showing softly out-of-focus stacked shipping containers and a sliver of palm trees, warm golden-hour sunlight wrapping his left side, soft fill bounce on his right.
He is leaning casually on a matte black metal railing, arms relaxed, slight smile, looking directly at camera with quiet authority.
85mm lens, f/1.8, shallow depth of field, Kodak Portra 800 color science, warm highlights, gentle teal shadows, very fine natural skin texture, subtle emerald #10b981 ambient accent reflected on the railing.
Negative: no text, no logos, no watermarks, no captions, no UI overlays, no extra fingers, no warped hands, no plastic skin, no waxy skin, no oversaturation, no HDR halo, no AI artifacts, no cartoon, no anime, no 3D render look, no stock photo cliché, no flag of USA, no brand names on clothing.
```

---

### IMG-04 — Host card · Emanuel Galliano (Despacho Aduana · Shanghai)

- **Ubicación**: `landing.html` → sección `hosts` → segunda tarjeta de host.
- **Tamaño display**: 520 × 640 px · ratio **13:16**.
- **Export**: 1040 × 1280 px · WebP + JPG.
- **Formato**: retrato editorial, ambiente despacho aduanero Shanghai.
- **Prompt hyper-optimizado**:

```
Editorial half-body portrait of a 38-year-old Argentine male customs broker named "Ema" archetype: medium-length wavy dark brown hair, neat short beard, light frame glasses, fair-medium skin, wearing a charcoal merino crewneck under a dark technical field jacket.
He is standing on a quiet mezzanine overlooking the Shanghai customs and port logistics area at blue hour: distant glow of cargo cranes and container yard lights softly blurred in the background, cool ambient light, subtle reflection of warm interior lamps on his glasses.
He is holding a slim leather folio under his arm, body slightly angled, looking directly at camera with a calm, methodical, problem-solver expression.
85mm lens, f/2.0, shallow depth of field, Fujifilm Pro 400H color science, cool ambient with warm key, fine natural skin texture, subtle emerald #10b981 highlight reflected on his jacket zipper.
Negative: no text, no logos, no watermarks, no captions, no UI overlays, no extra fingers, no warped hands, no plastic skin, no waxy skin, no oversaturation, no HDR halo, no AI artifacts, no cartoon, no anime, no 3D render look, no stock photo cliché, no flag of China, no Chinese characters visible on signage, no brand names on clothing.
```

---

### IMG-05 — Host card · "Vos. Próximo importador." (blurred placeholder)

- **Ubicación**: `landing.html` → sección `hosts` → tarjeta final blurreada.
- **Tamaño display**: 520 × 640 px · ratio **13:16**.
- **Export**: 1040 × 1280 px · WebP.
- **Formato**: foto deliberadamente fuera de foco, silueta neutra.
- **Prompt hyper-optimizado**:

```
Editorial out-of-focus portrait silhouette of a generic young entrepreneur seen from behind, soft warm beige and emerald ambient background, large bokeh, no facial features visible, no skin detail, no hair detail, just the suggestion of a person about to step into a frame, intentionally dreamy and abstract, designed to read as "the next one could be you" without being literal.
85mm lens, f/1.4, extremely shallow depth of field, Kodak Portra 400 palette, soft window light, premium editorial mood.
Negative: no text, no logos, no watermarks, no captions, no faces, no recognizable features, no extra fingers, no AI artifacts, no cartoon, no anime, no 3D render look, no stock photo cliché.
```

---

### IMG-06 — Precio · Testimonio lateral (Mariano Pereyra)

- **Ubicación**: `landing.html` → sección `precio` → tarjeta lateral con quote.
- **Tamaño display**: 96 × 96 px · ratio **1:1** (avatar circular).
- **Export**: 256 × 256 px · WebP + JPG.
- **Prompt hyper-optimizado**:

```
Editorial square portrait of a 40-year-old Argentine male entrepreneur from Córdoba, short dark hair with subtle gray on the sides, light beard, warm olive skin, wearing a simple heather-gray crew T-shirt, photographed in a small clothing workshop with soft natural window light, slight emerald #10b981 ambient reflection in the background bokeh, looking directly at camera with a genuine, grounded, "this actually worked" expression, 85mm lens, f/2.0, Kodak Portra 400 color science.
Negative: no text, no logos, no watermarks, no captions, no extra fingers, no plastic skin, no oversaturation, no AI artifacts, no cartoon, no 3D render look, no stock photo cliché, no flag, no brand names on clothing.
```

---

### IMG-07, IMG-08, IMG-09 — Testimonios · Video thumbs

Usar EXACTAMENTE los `video_thumb_prompt` del JSON del copy, agregando esta cola común a cada uno:

```
…, 4:5 vertical composition, 1024 x 1280 export, soft film grain, Kodak Portra 400 palette, premium editorial mood, designed to sit inside a rounded glass card UI.
Negative: no text, no logos, no watermarks, no captions, no UI overlays, no extra fingers, no warped hands, no plastic skin, no waxy skin, no oversaturation, no HDR halo, no AI artifacts, no cartoon, no anime, no 3D render look, no stock photo cliché, no flag, no brand names on clothing.
```

- **IMG-07** Martín Pereyra · Córdoba — base prompt del JSON `testimonials[0].video_thumb_prompt`.
- **IMG-08** Carolina Méndez · CABA — base prompt del JSON `testimonials[1].video_thumb_prompt`.
- **IMG-09** Lucas Bianchi · Rosario — base prompt del JSON `testimonials[2].video_thumb_prompt`.

Display: 360 × 450 px · ratio **4:5** · Export: 720 × 900 px · WebP + JPG.

---

### IMG-10 — OG / Twitter card

- **Ubicación**: `<meta property="og:image">` en `<head>`.
- **Tamaño display**: 1200 × 630 px · ratio **1.91:1**.
- **Export**: 1200 × 630 px · JPG calidad 86.
- **Formato**: imagen sin texto (el texto se compone en CSS si se hace versión social, o se agrega aparte en Figma).
- **Prompt hyper-optimizado**:

```
Premium editorial wide composition for an Open Graph share card, ratio 1.91:1.
Left half: stylized aerial photo of stacked muted-teal shipping containers at dusk, soft mist, one subtle emerald #10b981 glowing edge.
Right half: clean warm off-white #f5f1eb area with very soft natural light gradient, intentionally empty for typography overlay added later in design tool.
Cinematic color grade, Kodak Portra 400 palette, Phase One medium format sharpness, very low contrast on the right side to keep text legibility.
Negative: no text, no logos, no watermarks, no captions, no Chinese characters, no flag, no people, no AI artifacts, no cartoon, no 3D render look, no stock photo cliché, no HDR halo, no oversaturation.
```

---

### IMG-11 — ThankYou · Top illustration / poster

- **Ubicación**: `thankyou.html` → bloque superior, encima de los 3 pasos.
- **Tamaño display**: 880 × 360 px · ratio **22:9** (banner).
- **Export**: 1760 × 720 px · WebP.
- **Formato**: foto editorial cálida con espacio para overlay.
- **Prompt hyper-optimizado**:

```
Warm editorial overhead photograph of a wooden desk, top-down composition, ratio 22:9.
On the desk: a smartphone showing a neutral abstract green-tinted screen (no UI visible), a small white ceramic mug of coffee, a leather notebook closed, a pen, and a small folded printed boarding-style ticket placed at a slight angle, all arranged on the right side.
The left half of the frame is mostly empty wood surface with soft natural window light from the upper left, designed for text overlay later.
Subtle emerald #10b981 ambient bounce on the mug edge, Kodak Portra 400 palette, Phase One medium format crispness, shallow depth of field on the smartphone, premium fintech-meets-editorial mood.
Negative: no text, no logos, no watermarks, no captions, no UI screenshots, no recognizable apps, no Chinese characters, no flag, no extra fingers, no AI artifacts, no cartoon, no 3D render look, no stock photo cliché.
```

---

## 3. SVGs inline incluidos (no generar con IA)

Estos se escriben directamente en el HTML/CSS. No requieren generación con modelos.

### 3.1 Logo Roig · Galliano (wordmark inline SVG)

```html
<svg viewBox="0 0 220 40" xmlns="http://www.w3.org/2000/svg" aria-label="Roig · Galliano">
  <text x="0" y="28" font-family="'Inter', system-ui, sans-serif"
        font-weight="700" font-size="24" letter-spacing="-0.02em" fill="currentColor">
    Roig
  </text>
  <circle cx="78" cy="20" r="3" fill="#10b981"/>
  <text x="92" y="28" font-family="'Inter', system-ui, sans-serif"
        font-weight="500" font-size="24" letter-spacing="-0.02em" fill="currentColor">
    Galliano
  </text>
</svg>
```

### 3.2 Icon set (lucide-style stroke 1.75, currentColor)

Usar **Lucide** vía CDN o inline. Icons requeridos por el copy:
`ship`, `trending-down`, `rocket`, `list-check`, `users`, `star`, `map-pin`, `shopping-cart`, `truck`, `package`, `globe`, `credit-card`, `message-circle`, `help-circle`, `shirt`, `cpu`, `lamp`, `sparkles`, `store`.

Snippet de carga (inline, sin texto en imágenes):

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<script>lucide.createIcons();</script>
<!-- uso: <i data-lucide="ship"></i> -->
```

### 3.3 Mockup UI · Gauge percent (card "Reservás tu lugar")

```html
<svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Gauge de progreso de reserva">
  <defs>
    <linearGradient id="gaugeGrad" x1="0" x2="1">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>
  <path d="M20 100 A80 80 0 0 1 180 100" fill="none" stroke="#1f2937" stroke-opacity="0.15" stroke-width="14" stroke-linecap="round"/>
  <path d="M20 100 A80 80 0 0 1 160 50" fill="none" stroke="url(#gaugeGrad)" stroke-width="14" stroke-linecap="round"/>
  <text x="100" y="92" text-anchor="middle" font-family="'Inter', system-ui, sans-serif" font-weight="700" font-size="28" fill="currentColor">82%</text>
  <text x="100" y="112" text-anchor="middle" font-family="'Inter', system-ui, sans-serif" font-weight="500" font-size="11" fill="currentColor" opacity="0.6">cupos llenos</text>
</svg>
```

### 3.4 Mockup UI · Flow icons (card "Recibís el link por WhatsApp")

```html
<svg viewBox="0 0 280 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flujo de WhatsApp a Zoom">
  <g fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
    <rect x="20" y="30" width="56" height="56" rx="14"/>
    <path d="M34 58c0 8 7 14 14 14l4-4 6 2 2-6c-2 0-14-2-14-14l-6 2-2 6Z"/>
    <path d="M84 60 H120" stroke-dasharray="3 4"/>
    <circle cx="140" cy="60" r="14"/>
    <path d="M134 60h12M140 54v12"/>
    <path d="M164 60 H200" stroke-dasharray="3 4"/>
    <rect x="208" y="30" width="56" height="56" rx="10"/>
    <path d="M218 50h26M218 58h20M218 66h22"/>
    <circle cx="252" cy="40" r="6" fill="#10b981" stroke="none"/>
  </g>
</svg>
```

### 3.5 Mockup UI · Cost breakdown (card "Te conectás 90 minutos en vivo")

```html
<svg viewBox="0 0 280 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Desglose de costos de importación">
  <g font-family="'Inter', system-ui, sans-serif" font-size="11" fill="currentColor">
    <rect x="10" y="10" width="260" height="120" rx="14" fill="none" stroke="currentColor" stroke-opacity="0.15"/>
    <text x="22" y="32" font-weight="600">Costo final por unidad</text>
    <text x="248" y="32" text-anchor="end" font-weight="700">USD 14,80</text>
    <g opacity="0.9">
      <rect x="22" y="46" width="160" height="8" rx="4" fill="#10b981"/>
      <text x="22" y="68" opacity="0.7">FOB China</text>
      <text x="248" y="68" text-anchor="end">USD 8,20</text>
      <rect x="22" y="76" width="60" height="6" rx="3" fill="#10b981" fill-opacity="0.6"/>
      <text x="22" y="96" opacity="0.7">Flete + seguro</text>
      <text x="248" y="96" text-anchor="end">USD 2,40</text>
      <rect x="22" y="104" width="40" height="6" rx="3" fill="#10b981" fill-opacity="0.4"/>
      <text x="22" y="124" opacity="0.7">Aduana + IVA + ARS</text>
      <text x="248" y="124" text-anchor="end">USD 4,20</text>
    </g>
  </g>
</svg>
```

---

## 4. Checklist pre-publicación

### 4.1 Mercado Pago

- [ ] Crear preferencia de pago en cuenta `Roig · Galliano` (MP Argentina).
- [ ] Monto: **ARS 90.000**.
- [ ] Habilitar `installments: 3` con `interest_free` aplicado por el comercio.
- [ ] Tipo de checkout: **link de pago** (no Checkout Pro embebido en v1).
- [ ] `back_urls.success` → `https://roig-galliano.com/thankyou.html`.
- [ ] `back_urls.failure` → `https://roig-galliano.com/landing.html#precio`.
- [ ] `auto_return: approved`.
- [ ] Reemplazar todos los `href="#mp-link"` por la URL real del checkout en `landing.html`.
- [ ] Probar pago test con tarjeta `APRO 4509 9535 6623 3704`.

### 4.2 WhatsApp (wa.me)

- [ ] Número operativo unificado de equipo (recomendado: WhatsApp Business API o número Argentina con horario BA).
- [ ] Reemplazar el placeholder `+5491100000000` en TODOS los `wa.me/...` (footer, thank you, sticky mobile, hosts).
- [ ] Verificar que el mensaje URL-encoded del thank you se mantenga intacto.
- [ ] Probar el flujo en iOS y Android (algunos clientes recortan mensajes >160 chars).
- [ ] Configurar respuesta automática Business: "Hola, recibimos tu mensaje. Te contestamos en menos de 24hs hábiles para agendarte el Zoom."

### 4.3 Imágenes

- [ ] Generar IMG-01 a IMG-11 con los prompts del bloque 2.
- [ ] Comprimir a WebP calidad 82 + fallback JPG.
- [ ] Setear `<picture><source type="image/webp">…</picture>` en cada uso.
- [ ] Definir `width` y `height` HTML para evitar CLS.
- [ ] `loading="lazy"` en todas menos IMG-01 e IMG-02 (above the fold).
- [ ] `alt` descriptivo en español, sin keyword stuffing.
- [ ] Subir `og:image` (IMG-10) y validar en `https://www.opengraph.xyz/`.

### 4.4 Video hero embed

- [ ] Grabar o editar un video corto (45-60s) de Bauti + Ema hablando a cámara: "Te lo contamos en 90 min. Reservá tu lugar."
- [ ] Hostear en **Mux** o **Cloudflare Stream** (mejor performance que YouTube para landing).
- [ ] Embed con `preload="metadata"`, `poster=` apuntando a IMG-01.
- [ ] Autoplay **muted** + `playsinline` para iOS.
- [ ] Botón overlay de play accesible (role=button, aria-label).
- [ ] Caption "90 min en vivo · Grupal · No es un curso" visible debajo.

### 4.5 Precio

- [ ] Verificar que en TODA la landing se mantenga `ARS 90.000` (no aparecer 89.999 ni mezclar moneda).
- [ ] Verificar que el desglose en cuotas siempre sea `3 cuotas de ARS 30.000 sin interés con Mercado Pago`.
- [ ] Sticky mobile con misma frase.
- [ ] Si MP cambia la política de cuotas sin interés, actualizar copy en hero, precio, final CTA, footer y sticky.

### 4.6 Operativo extra

- [ ] Agregar `<link rel="canonical">` apuntando al dominio final.
- [ ] Setear `<html lang="es-AR">`.
- [ ] Favicon + apple-touch-icon a partir del SVG del logo (3.1).
- [ ] Schema.org `Event` + `Offer` en JSON-LD para SEO.
- [ ] Pixel de Meta y GA4 con evento `Purchase` disparado en `thankyou.html`.
- [ ] UTM coherentes en los wa.me (`?utm_source=landing&utm_medium=whatsapp&utm_campaign=zoom_charla`).
- [ ] Test mobile real (iPhone SE 375px + iPhone 15 Pro Max 430px + Pixel 7).
- [ ] Lighthouse > 90 en Performance, > 95 en Accesibilidad.
- [ ] Política de reembolso publicada (FAQ habla de 48hs, debe quedar por escrito en `#reembolso`).
- [ ] Términos y condiciones publicados en `#terminos`.

---

## 5. Stack sugerido de generación de imágenes por tipo

| Tipo | Imágenes | Modelo recomendado | Por qué |
|---|---|---|---|
| Retratos editoriales de hosts | IMG-03, IMG-04 | **Midjourney v6.1** (`--style raw --ar 13:16 --stylize 200`) | Mejor skin texture y coherencia editorial cinematográfica. |
| Retratos testimonios | IMG-06, IMG-07, IMG-08, IMG-09 | **Midjourney v6.1** o **Flux 1.1 Pro** | Flux Pro da consistencia étnica argentina muy buena y manos correctas. |
| Hero split-frame compuesto | IMG-01 | **GPT-Image-1** (alta edición compositiva) o Nano Banana para retoques | GPT-Image-1 respeta mejor instrucciones de layout multi-panel. Banana sirve para corregir manos/ojos. |
| Background ambient port | IMG-02 | **Midjourney v6.1** (`--ar 16:9 --stylize 350`) | Texturas aéreas abstractas con grano editorial. |
| OG card sin texto | IMG-10 | **Midjourney v6.1** o **Sora image** | Composición wide limpia, área negativa para tipografía posterior. |
| ThankYou overhead desk | IMG-11 | **Flux 1.1 Pro** o **Midjourney v6.1** | Top-down still life sin caras = Flux es muy estable. |
| Out-of-focus placeholder | IMG-05 | Cualquiera + blur en CSS | Generar baseline simple y aplicar `filter: blur(18px) saturate(1.05)`. |
| Iconos + logo + mockups UI | Bloque 3 | **SVG inline a mano** | Cero IA, control total, peso < 2 KB cada uno. |

Tip de workflow:
1. Generar el batch en MJ v6.1 / Flux Pro.
2. Pasar por **Nano Banana** (`nanobanana-mcp`) para retocar manos, ojos, cualquier texto fantasma o glitches.
3. Comprimir con **Squoosh** (WebP q82) y subir.

---

## 6. Script bash · placeholders Unsplash

> Descarga rápida de placeholders mientras se generan las imágenes finales con IA.
> Requiere `curl` y `jq`. Lee `UNSPLASH_ACCESS_KEY` del entorno.
> Guardar como `tools/fetch_placeholders.sh` y `chmod +x`.

```bash
#!/usr/bin/env bash
# tools/fetch_placeholders.sh
# Descarga placeholders de Unsplash para la landing Roig · Galliano.
# Uso:
#   export UNSPLASH_ACCESS_KEY="tu_access_key_aqui"
#   ./tools/fetch_placeholders.sh
#
# Salida en ./assets/placeholders/

set -euo pipefail

: "${UNSPLASH_ACCESS_KEY:?Falta UNSPLASH_ACCESS_KEY en el entorno}"

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
  echo "→ Buscando $ID  ($QUERY · $ORIENT)"

  URL=$(curl -fsSL -G "https://api.unsplash.com/photos/random" \
    -H "Accept-Version: v1" \
    -H "Authorization: Client-ID $UNSPLASH_ACCESS_KEY" \
    --data-urlencode "query=$QUERY" \
    --data-urlencode "orientation=$ORIENT" \
    --data-urlencode "content_filter=high" \
    | jq -r '.urls.regular')

  if [[ -z "${URL:-}" || "$URL" == "null" ]]; then
    echo "  ! Sin resultados para $ID — saltando"
    continue
  fi

  curl -fsSL "$URL" -o "$OUT_DIR/$FILENAME"
  echo "  ✓ Guardado $OUT_DIR/$FILENAME"
done

echo "Listo. Recordá reemplazar los placeholders por las imágenes finales generadas con IA antes de publicar."
```

Notas operativas del script:
- Es solo para placeholders. **No publicar Unsplash en producción** sin verificar licencia de cada foto puntual.
- Los nombres de archivo ya están listos para reemplazar uno a uno por los finales (`hero-video-poster.webp`, etc.).
- Si se quiere correr en CI, agregar rate-limit handling (50 req/h en plan free de Unsplash).

---

## 7. Notas finales de tono

- En toda la pieza: voseo argentino (`reservá`, `pagás`, `mandás`, `te llevás`).
- Cero promesa de resultado garantizado fuera del refund de 48hs ya escrito.
- Nunca decir "curso", "masterclass" ni "mentoría". Siempre **"charla informativa grupal por Zoom"**.
- Nunca decir "1:1" en la landing. Es grupal.
- Mantener la dupla Bauti + Ema visible en hero, hosts, precio, final CTA y thank you.

---

## 8. Fixes pendientes de QA (críticos + mayores)

> Auditoría de QA sobre `landing.html` y `thankyou.html`. Resolver todo lo `critical` antes de pasar a staging; lo `major` antes de publicar a producción.
> Convención: cada fix indica archivo, sección/líneas afectadas, el issue detectado y la acción correctiva. Marcar con `[x]` al ir resolviendo.

### 8.1 Críticos — bloquean publicación

#### 8.1.1 HERO · Headline estructura (landing.html, líneas 1490-1496)

- **Issue**: el headline NO sigue el patrón Closify de 2 líneas con la mini-icon-cuadrado-verde inline acompañando UNA palabra clave en la segunda línea. Hay UNA SOLA línea (`Importá desde China sin [icon] perder margen.`) seguida de un `.hero__second-line` en color muted que actúa como subhead, no como segunda línea del headline. Pierde el impacto visual del big headline 2-line de Closify.
- **Fix**: reestructurar como dos líneas del MISMO `<h1>` (mismo size/weight/color). Ejemplo:

  ```html
  <h1 class="h1">Importá desde China<br>sin <span class="headline-icon-inline">[icon]</span> perder margen.</h1>
  ```

  Mover `90 minutos por Zoom...` a `.hero__subheadline` (eliminar `.hero__second-line` o convertirlo en subhead real con color muted PERO sin pretender ser línea de headline).
- [ ] Resuelto

#### 8.1.2 HERO · CTA único (landing.html, líneas 1499-1506)

- **Issue**: Closify usa UN solo CTA pill blanco `Start now` centrado. Acá hay 3 elementos apilados verticalmente (`.hero__cta` con `flex-direction:column`): CTA blanco grande + sub text ARS + CTA outline `Ver temario`. Rompe la jerarquía minimalista de Closify.
- **Fix**: dejar solo el CTA blanco principal en el hero. Mover el outline `Ver temario completo` FUERA del hero (o convertirlo en link discreto debajo). El sub-text de cuotas puede quedar pero más chico y debajo del único CTA.
- [ ] Resuelto

#### 8.1.3 HEADER · Estructura logo + login (landing.html, líneas 1453-1473)

- **Issue**: falta el botón `Login` que en Closify aparece a la izquierda del `Sign Up` pill blanco. La referencia tiene: logo izq | nav 4 items center | Login (text link) + Sign Up (pill blanco) der. Acá hay WhatsApp icon + pill `Reservá tu Zoom`. WhatsApp con icono+texto rompe el minimalismo. Además el logo `Roig · Galliano` es solo texto sin glifo: Closify usa wordmark con símbolo a la izquierda.
- **Fix**: reemplazar el botón WhatsApp en header por un link `Iniciar sesión` (o `Acceder`) estilo text-link muted, dejando solo el pill blanco `Reservá tu Zoom` como CTA primario. Mantener WhatsApp en otros lugares (sticky mobile, hosts cards). Agregar un mini-mark SVG al logo (dot/ship esmeralda).
- [ ] Resuelto

#### 8.1.4 PRECIO · Card oscura con contraste (landing.html, líneas 1755-1789)

- **Issue**: falta el contraste de fondo OSCURO del pricing card de Closify. `.pricing-card` usa `--bg-tertiary` (#0F1411) que es PRÁCTICAMENTE IGUAL al `bg-base` (#0A0F0D). La diferenciación visual desaparece.
- **Fix**: cambiar background a un mix más oscuro o agregar gradient interno + box-shadow inset:

  ```css
  background: linear-gradient(180deg, #08100D 0%, #050908 100%);
  box-shadow: inset 0 0 80px rgba(0, 232, 154, 0.08);
  ```

  Aumentar `border-emerald-soft` a 0.20-0.25 alpha.
- [ ] Resuelto

#### 8.1.5 HERO · Precio visible above-the-fold (landing.html)

- **Issue**: el hero NO muestra el precio dentro del headline ni en un anchor visible above-the-fold. El precio (ARS 90.000 / 3 cuotas) aparece solo como `.btn-sub` debajo del CTA en texto 12px gris muted, lo que pasa desapercibido. Un visitante que decide en 5 segundos no ve el ancla de precio antes de hacer scroll.
- **Fix**: elevar el precio a un price-anchor visible en el hero: pill arriba del CTA con `ARS 90.000 · 3 cuotas de $30.000 sin interés · 90 min Zoom en vivo` en font-weight 600, color emerald sobre fondo emerald-glow-08, font-size 14-15px. Agregar arriba del CTA un micro-stack social proof (`+500 importadores · 4.9 estrellas`). Subir el `btn-sub` a font-size 13-14px y color `text-display` en vez de muted.
- [ ] Resuelto

#### 8.1.6 Sticky mobile CTA (landing.html, líneas 2070-2080)

- **Issue**: el sticky mobile aparece desde el primer scroll (siempre visible si ≤768px) y solapa el hero CTA en el primer pliegue, generando doble-CTA confuso. El botón dice solo `Reservar` sin precio ni urgencia. El sub-label `ARS 90.000 · 3 cuotas sin interés` ocupa 11px (muy chico, no legible). El contenedor no tiene safe-area-inset para iPhone con notch.
- **Fix**:
  1. Mostrar el sticky solo después de scrollear pasado el hero (IntersectionObserver sobre `.hero__cta`, añadir `.is-visible` cuando se sale del viewport del hero).
  2. Subir el sub a 12-13px y label a 15px.
  3. Cambiar texto del botón a `Reservar Zoom` o agregar flecha →.
  4. Agregar `padding-bottom: max(12px, env(safe-area-inset-bottom))` y al body `padding-bottom: calc(80px + env(safe-area-inset-bottom))`.
  5. Ocultar el sticky cuando el usuario esté dentro de `#precio` o `#final-cta` (ya hay CTA visible).
- [ ] Resuelto

#### 8.1.7 FAQ · Objeciones reales (landing.html, líneas 1930-1994)

- **Issue**: faltan 3 objeciones críticas de conversión: (a) `¿Cuándo es la próxima fecha?`; (b) `¿Está en español argentino o me van a hablar en chino/inglés?`; (c) `¿Funciona si vivo en el interior / fuera de CABA?`. La garantía de reembolso (FAQ 8) está enterrada como la última pregunta, no destacada como reverse-risk.
- **Fix**:
  1. Agregar 3 `details/summary` al inicio del FAQ con esas objeciones (`Próximas fechas disponibles`, `En qué idioma se da el Zoom`, `Sirve si vivo en el interior`).
  2. Elevar la garantía de reembolso a un módulo independiente arriba del pricing-card (badge `Garantía 48hs · 100% devolución` con icono shield) y duplicar en el footer del pricing como sub-CTA.
  3. Reordenar FAQ priorizando: fecha → duración → precio/cuotas → 1:1 vs grupal → si no puedo conectarme → garantía → material → upsell.
- [ ] Resuelto

#### 8.1.8 Urgencia / escasez honesta (landing.html)

- **Issue**: no hay ningún elemento de urgencia o escasez (próxima fecha, cupos limitados, deadline). Para una charla grupal en vivo con fecha concreta esto es la palanca de conversión más alta. El hero, el precio y el final-CTA no comunican `cuándo` ni `cuántos lugares quedan`.
- **Fix**: agregar bloque de urgencia honesta (sin contadores falsos): pill arriba del hero CTA + en pricing-card que diga `Próxima fecha: Jueves 26 de junio · 19hs ARG · 18 cupos disponibles` con icono `calendar` y dot pulsante. Dinamizar con JS leyendo de un JSON. Si no hay fecha cerrada, usar `Próxima fecha en los próximos 7-10 días · te confirmamos al pagar`. En el sticky mobile agregar línea adicional `Próxima: Jue 26 · 19hs`.
- [ ] Resuelto

#### 8.1.9 CTAs / placeholders sin reemplazar (landing.html, líneas 1465, 1470, 1501, 1674, 1713, 1727, 1788, 2019, 2047, 2078)

- **Issue**: todos los enlaces de conversión apuntan a placeholders sin sustituir: `https://mpago.la/REEMPLAZAR` (6 ocurrencias) y `https://wa.me/5491100000000` (4 ocurrencias). Si la página se publica tal cual, ningún CTA convierte. En `thankyou.html` el problema se repite con `https://wa.me/REEMPLAZAR` (líneas 752 y 818).
- **Fix**: reemplazar las 10 ocurrencias por la URL real de la preferencia de Mercado Pago (ARS 90.000, 3 cuotas sin interés, `back_urls` apuntando a `thankyou.html`) y por el número WhatsApp Business definitivo en formato internacional sin `+`. Validar con tarjeta de test APRO antes de pasar a producción. Marcar los placeholders con un grep CI:

  ```bash
  grep -nE 'REEMPLAZAR|5491100000000' *.html && exit 1 || exit 0
  ```

- [ ] Resuelto

#### 8.1.10 Carga de fuentes (landing.html, líneas 9-12)

- **Issue**: cuatro `@import url(fonts.googleapis.com/...)` consecutivos dentro de `<style>` inline. Bloquea el render, no paraleliza, dispara 4 round-trips a Google Fonts sin `preconnect`. En `thankyou.html` ya se hizo bien con un `<link>` único + `preconnect`.
- **Fix**: borrar los cuatro `@import` y reemplazar en `<head>` por:

  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  ```

- [ ] Resuelto

#### 8.1.11 WhatsApp Mega CTA contraste (thankyou.html, líneas 423-447, 750-767)

- **Issue**: texto blanco `#FFFFFF` sobre fondo verde WhatsApp `#25D366` da un ratio de contraste ~2.27:1. Aunque el texto principal es 22px/700 (large text), está debajo del 3:1 requerido por WCAG AA. Es la principal call-to-action de la página y es prácticamente ilegible para usuarios con baja visión.
- **Fix**: cambiar el color de fondo a `var(--wpp-deep)` `#128C7E` (contraste de blanco ~4.6:1). Alternativa: WhatsApp oficial dark `#075E54` (~6:1). Ajustar `:hover` a `#0E7060` y mantener el shadow box verde brillante para conservar la identidad visual.
- [ ] Resuelto

#### 8.1.12 .wpp-btn__sub contraste (thankyou.html, líneas 471-475)

- **Issue**: subtítulo `Respuesta humana < 24 horas hábiles` usa font-size 12px con `opacity:0.85` en blanco sobre `#25D366`. Ratio resultante ~1.9:1, muy debajo del 4.5:1 WCAG AA. Info clave (SLA de respuesta) inaccesible.
- **Fix**:
  1. Resolver primero el background del botón (ver 8.1.11).
  2. Subir font-size a 13-14px y eliminar `opacity:0.85`, usando un color sólido. Sobre `#128C7E` el blanco a 13px da ~4.6:1.
  3. Mejor todavía: extraer la sub-info fuera del botón verde (debajo, como ya hace `.wpp-cta-meta`).
- [ ] Resuelto

### 8.2 Mayores — bloquean producción pero no staging

#### 8.2.1 PRECIO · Video testimonial al lado (landing.html, líneas 1791-1801)

- **Issue**: el brief Closify pide CARD VIDEO TESTIMONIAL al lado del pricing card. Acá hay `.testimonial-side` con solo quote-icon + texto + avatar inicial. Falta el thumbnail de video con play verde 16:9.
- **Fix**: reemplazar el aside `.testimonial-side` por una `testimonio-card` con thumb 16:9 (`img-ph` con prompt), play button verde, rating estrellas, quote corta y autor. Alternativa: agregar un thumbnail/play encima del quote actual.
- [ ] Resuelto

#### 8.2.2 GLOW SYSTEM · Cobertura por sección (landing.html, líneas 158-207, 1564, 1622, 1734, 1807, 1910)

- **Issue**: el glow se posiciona en `bottom:0` SIEMPRE. Closify alterna: glow saliendo del CENTRO de la sección, del top, del bottom según el bloque. `final-cta` no tiene `glow-section` detrás del bloque.
- **Fix**: crear variantes `.glow-section--top`, `.glow-section--center`, `.glow-section--bottom` y rotar entre secciones. Agregar `.glow-section` detrás de `final-cta`. Glow secundario sutil en `logos-band-section`.
- [ ] Resuelto

#### 8.2.3 HOSTS · Botones acciones (landing.html, líneas 1672-1678, 1711-1717)

- **Issue**: los 2 botones internos de person-card usan `.btn` (radius-pill 999px). Closify usa botones RECTANGULARES con radius mediano (8-12px). Paddings asimétricos (12px 24px vs 10px 16px).
- **Fix**: crear variant `.btn--rect` (`border-radius: 10px`) para los botones internos. Igualar paddings: ambos a 10px 16px o 12px 18px. CTAs grandes siguen siendo pills, internos de card son rect.
- [ ] Resuelto

#### 8.2.4 HEADLINE-ICON-INLINE · Color del icono (landing.html, líneas 318-338)

- **Issue**: el icono inline interno (`.headline-icon-inline svg`) usa `color:white + stroke:white`. En Closify el icono dentro del cuadrado verde es NEGRO/INVERSO (#0A0F0D). Mismo problema en `.section-pill__icon svg` (línea 308).
- **Fix**: cambiar a `color: var(--text-inverse); stroke: var(--text-inverse);` en `.headline-icon-inline svg` y `.section-pill__icon svg`. Esto da el look "mini chip verde con glifo negro" característico.
- [ ] Resuelto

#### 8.2.5 LOGOS BAND · Estilo wordmarks (landing.html, líneas 577-620, 1535-1561)

- **Issue**: Closify pide "banda de logos clientes gris claro 4-5 logos" (logos reales o marcas), no iconos+texto de SECTORES. Funciona como social proof débil pero visualmente difiere mucho.
- **Fix**: si no hay logos reales, mantener los sectores PERO usar wordmarks tipográficos más grandes y planos (sin icono), todos en mismo gris uniforme, sin hover color. Alternativa: si hay logos de medios (TN, La Nación, Apertura), usarlos. Sino, agregar disclaimer chico `logos representativos por categoría`.
- [ ] Resuelto

#### 8.2.6 PERSON-CARD · Tercera card blurred (landing.html, líneas 1722-1729)

- **Issue**: la "tercera persona difuminada con CTA Sign Up" debería simular una PERSONA blurreada (silueta + nombre/role placeholder) detrás del CTA, no un fondo de gradient genérico. `.person-card--blurred__bg` es solo un linear-gradient blurreado.
- **Fix**: agregar dentro del `__bg` los mismos sub-elementos de una person-card real (foto placeholder + nombre + role + metric chips) blurreados con `filter:blur(8px)`. Comunica visualmente "tu cara va acá".
- [ ] Resuelto

#### 8.2.7 TESTIMONIOS · Rating estrellas color (landing.html, líneas 1836-1842, 1862-1868, 1888-1894)

- **Issue**: las 5 estrellas del rating se renderizan con color emerald. Closify usa estrellas DORADAS (`#FFB800` o similar), NO verde esmeralda. El verde-en-todo satura.
- **Fix**: cambiar `.testimonio-card__rating { color: #FFB800; }` o crear `--rating-gold: #F5B400`. Mantener verde solo para iconos de acción.
- [ ] Resuelto

#### 8.2.8 FAQ · Borde emerald (landing.html, líneas 1091-1101)

- **Issue**: Closify pide "Items con borde verde glow + verde en círculo". El borde inicial usa `--border-emerald-soft` (15% alpha), muy tenue. Solo en `:hover` aparece el glow real. El estado base debería tener borde emerald visible.
- **Fix**: aumentar borde base a `border: 1px solid var(--border-emerald-hover);` (30% alpha) y conservar el box-shadow glow en hover/open. Opcional: animación `border-glow-breathe` sutil en estado base (ya definida en línea 1315).
- [ ] Resuelto

#### 8.2.9 TIPOGRAFÍA · h1 line-height (landing.html, línea 100)

- **Issue**: el h1 tiene `line-height:0.95`, agresivo para textos largos en español. Con headline de 2 líneas genera overlap de descenders/ascenders, especialmente con el inline-icon que tiene `transform:translateY(-4px)`.
- **Fix**: subir `line-height` a 1.05-1.1 para h1 multi-línea. Si se reestructura en 2 líneas reales (ver 8.1.1), `line-height: 1.05` es seguro.
- [ ] Resuelto

#### 8.2.10 Garantía 48hs · Formato y visibilidad (landing.html, FAQ 8, líneas 1987-1993)

- **Issue**: la garantía de reembolso 100% en 48hs es el reverse-risk más fuerte de la oferta y está escondida como FAQ 8 (la última). No aparece como bullet del pricing-card ni como badge en hero/final-CTA.
- **Fix**:
  1. Agregar como 5to bullet del pricing-card: `Garantía 100%: si en 48hs no te sumó, te devolvemos el pago sin formularios`.
  2. Badge horizontal arriba del `btn--block` del pricing card con icono shield-check y texto `Garantía 48hs · sin preguntas`.
  3. Repetir el badge en el final-CTA debajo del botón.
  4. Reescribir el copy en positivo: `Garantía 48hs: 100% del pago de vuelta`.
- [ ] Resuelto

#### 8.2.11 Sección temario inexistente (landing.html)

- **Issue**: el hero ofrece 2 CTAs. El segundo (`Ver el temario completo`) lleva a `#temario` que es el ID del pricing-card, no de una sección de temario detallado. El user que hace click espera ver una lista de 10 pasos, encuentra el pricing card y se siente engañado. El header navega a `Temario` apuntando al mismo destino fantasma.
- **Fix**:
  - Opción A (rápida): renombrar el segundo CTA a `Ver precio y temario` y dejar el ancla `#precio`.
  - Opción B (mejor): agregar una sección real entre `Cómo funciona` y `Hosts` titulada `Temario completo · 10 pasos` con grid de 10 micro-cards numeradas (Incoterm, FOB vs CIF, despacho, etc.), y apuntar `#temario` a esa sección.
- [ ] Resuelto

#### 8.2.12 Tabs de pricing UX engañosa (landing.html, líneas 1757-1760)

- **Issue**: las tabs `1 pago` / `3 cuotas` cambian solo el texto del subtitle pero el precio mostrado sigue siendo 90.000 en ambos casos sin diferenciar el descuento (si lo hubiera). Tampoco hay `aria-controls`/`aria-labelledby` para a11y.
- **Fix**:
  - Si NO hay descuento por pago único: eliminar las tabs, dejar solo el bloque `3 cuotas sin interés` con el precio único y debajo una línea fina `También podés pagarlo en 1 cuota`.
  - Si SÍ hay descuento: hacer que `.pricing-card__price` cambie dinámicamente (ej. 81.000 con strike-through del 90.000 al lado, mostrando -10%), agregar `aria-controls` a las tabs y `role=tabpanel` al contenido.
- [ ] Resuelto

#### 8.2.13 Steps thank-you · Fricción de comprobante (thankyou.html, líneas 772-792)

- **Issue**: el paso 01 dice "Mandá el comprobante" pero falta un fallback en caso de que el botón no funcione (email, teléfono alternativo). No hay confirmación visible del número WhatsApp que va a contactar al usuario. El paso 02 dice "< 24 horas hábiles" pero no aclara qué pasa fuera de horario hábil ni el huso horario.
- **Fix**:
  1. Agregar debajo del botón WhatsApp un micro-bloque `O escribinos a charla@roiggalliano.com · respuesta < 24h hábiles`.
  2. En el paso 02 cambiar a `En menos de 24 horas hábiles (lun-vie 10-19hs ARG) te confirmamos día y horario`.
  3. Paso 04 opcional `Mientras tanto, guardá este link y miralo desde el celular` con un mini calendario `.ics` descargable.
  4. Confirmar visualmente el monto pagado (`Recibimos tu pago de ARS 90.000 · MP confirmará por mail`).
- [ ] Resuelto

#### 8.2.14 wa.me hardcodeado +5491100000000 (landing.html, líneas 1465, 1674, 1713, 2047)

- **Issue**: el número de WhatsApp en 4 puntos de la landing es el placeholder `5491100000000` sin marcar con comentario `<!-- REEMPLAZAR -->` (sí está hecho para mpago). Si se publica sin reemplazar, todos los CTA secundarios de WhatsApp llevan a un número inexistente.
- **Fix**:
  1. Reemplazar `+5491100000000` en las 4 ocurrencias por `REEMPLAZAR` y agregar `<!-- wa.me REEMPLAZAR -->` arriba de cada `<a href="https://wa.me/...">`.
  2. Pre-poblar todos los `wa.me` con `?text=...` urlencoded contextual (header: "Hola, vi la landing y tengo una consulta"; hosts: "Hola Bauti/Ema, quiero info sobre el Zoom"; footer: "Hola, consulta general").
- [ ] Resuelto

#### 8.2.15 .headline-icon-inline transform conflict (landing.html, líneas 319-332)

- **Issue**: el selector aplica `transform: translateY(-4px)` y al mismo tiempo `animation: icon-pulse 2.5s infinite`. `@keyframes icon-pulse` (línea 1295) anima `transform: scale(...)`. Las animaciones CSS sobreescriben por completo la propiedad `transform` durante la ejecución, así que el `translateY(-4px)` se pierde apenas arranca el ciclo.
- **Fix**: combinar ambas transforms en los keyframes:

  ```css
  @keyframes icon-pulse-headline {
    0%, 100% { transform: translateY(-4px) scale(1); }
    50%      { transform: translateY(-4px) scale(1.08); }
  }
  ```

  Aplicar esa animación solo a `.headline-icon-inline`. Alternativa: envolver el SVG en un wrapper.
- [ ] Resuelto

#### 8.2.16 Pricing tabs ARIA roto (landing.html, líneas 1757-1759, 2102-2119)

- **Issue**: los `<button>` tienen `role="tab"` y se actualiza `aria-selected`, pero no hay `aria-controls`, no hay `role="tabpanel"` y no se gestiona navegación con flechas. Para un screen reader el patrón está roto.
- **Fix**:
  - Opción rápida: bajar a `role="group"` en el contenedor y quitar `role="tab"`/`aria-selected` de los botones (simples toggles con `aria-pressed`).
  - Opción correcta: añadir `aria-controls="pricing-detail"`, envolver el bloque en `<div id="pricing-detail" role="tabpanel" aria-labelledby="tab-3cuotas">`, agregar handler de flechas izq/der.
- [ ] Resuelto

#### 8.2.17 Footer anchors a IDs inexistentes (landing.html, líneas 2048-2049, 2055-2057)

- **Issue**: 5 links del footer (`#reembolso`, `#terminos`, `#oficinas` x3) apuntan a IDs que no existen. El handler de smooth scroll (línea 2138-2139) hace `document.querySelector(href)` y si no encuentra target hace `return` sin `preventDefault`, así que el navegador salta al top.
- **Fix**: crear las páginas reales `/reembolso` y `/terminos` y usar URLs absolutas, o renderizar inline esas secciones con los IDs correspondientes. Para `#oficinas` (BA/SHA/MIA) crear una sección real o convertir los `<a>` en `<span>`.
- [ ] Resuelto

#### 8.2.18 Botones play sin handler (landing.html, líneas 1512-1514, 1831-1833, 1857-1859, 1883-1885)

- **Issue**: 4 `<button aria-label="Reproducir video/testimonio...">` con animación de pulse y caret esmeralda pero ningún listener JS. Click no abre nada. Rompe la promesa visual ("hay un video"). El placeholder `img-ph` declara la imagen `hero_video_thumb 1280x720` que tampoco existe.
- **Fix**:
  - Opción A: convertir los `<button>` en `<a href="#" data-video="...">` que abran un `<dialog>` con `<iframe src="https://player.mux.com/...">`.
  - Opción B mínima: handler que dispare evento de analytics (`gtag('event','click_video_placeholder')`) y muestre un toast `Próximamente`.
- [ ] Resuelto

#### 8.2.19 Mockups SVG hard-coded fuera de paleta (landing.html, línea 1598+, card #2 y #3)

- **Issue**: el SVG `flow_icons` usa colores `#2A2F3A`, `#3A4150`, `#9AA3B2`, `#1A1D24`, `#6B7280` (Tailwind azulados/grises) que NO están en la paleta `:root`. La card #3 usa `#1F2A24`, `#A8B3AD`, `#2A3530`. Además el BRIEF §3.3 especifica gauge a **82%** (`cupos llenos`), pero la card #1 muestra `96% EFICIENCIA · Operaciones liberadas`.
- **Fix**: reemplazar los hex hard-coded por las variables del root:
  - `#1A1D24` → `var(--bg-card-hover)`
  - `#9AA3B2`/`#A8B3AD` → `var(--text-muted)` (#8B9491)
  - `#2A2F3A`/`#3A4150` → `var(--border-hairline)`/`var(--border-divider)`
  - Usar `style="color: var(...); stroke: var(...)"` y `currentColor` dentro del SVG.
  - Alinear los textos del gauge al brief (82% / cupos llenos).
- [ ] Resuelto

#### 8.2.20 SEO / structured data ausente (landing.html, head, líneas 3-7)

- **Issue**: no hay Open Graph (`og:title`, `og:image`, `og:url`), no hay Twitter Card, no hay JSON-LD `Event`+`Offer`. Al compartir el link en WhatsApp/Instagram aparece sin preview.
- **Fix**:
  - Agregar en `<head>` los OG mínimos (`og:title`, `og:description`, `og:image` 1200x630, `og:url`, `og:type=website`).
  - Twitter Card (`twitter:card=summary_large_image`).
  - Bloque `<script type="application/ld+json">` con `@type:Event`, `offers:{@type:Offer, price:90000, priceCurrency:ARS, availability:InStock}`, `location:{@type:VirtualLocation, url:zoom}`, `performer:[Bauti, Ema]`, `startDate`.
  - En `thankyou.html`: `<script>gtag('event','purchase',{value:90000, currency:'ARS'})</script>`.
- [ ] Resuelto

#### 8.2.21 Ticker husos horarios (thankyou.html, líneas 832-851)

- **Issue**: `setInterval(tick, 30000)` arranca a tiempo cero y refresca cada 30s sin alinearse al minuto natural — los relojes quedan con offset visible hasta 30s. Si la pestaña está inactiva, `setInterval` se throttlea y al volver puede tardar otro tick en refrescar.
- **Fix**: calcular el delay hasta el próximo minuto exacto:

  ```js
  function schedule() {
    const ms = 60000 - (Date.now() % 60000);
    setTimeout(() => { tick(); setInterval(tick, 60000); }, ms);
  }
  tick();
  schedule();
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) tick();
  });
  ```

- [ ] Resuelto

#### 8.2.22 Imágenes ausentes / CLS (landing.html, placeholders líneas 1511, 1645, 1684, 1830, 1856, 1882)

- **Issue**: los 6 `<div class="img-ph">` no tienen `aspect-ratio` o `width/height` propios; heredan de los contenedores. Cuando se reemplacen por `<img>` reales habrá CLS fuerte. Los `data-img-prompt` (~250 caracteres) se renderizan literalmente como texto.
- **Fix**: al reemplazar los placeholders:

  ```html
  <picture>
    <source srcset="...webp" type="image/webp">
    <img src="...jpg" width="1280" height="720"
         alt="Bauti en Miami y Ema en Shanghai"
         loading="lazy" decoding="async">
  </picture>
  ```

  Marcar la imagen del hero como `fetchpriority="high"` (es LCP candidate) y NO ponerle `loading="lazy"`.
- [ ] Resuelto

#### 8.2.23 .logo-item contraste (landing.html, líneas 601-616, 1538-1559)

- **Issue**: los items de la logos band tienen `opacity:0.35` por defecto. Colapsa el contraste del texto `#F5F7F6` sobre `#0A0F0D` de ~17:1 a ~2:1, debajo del 4.5:1 WCAG AA. Son nombres de sectores (info sustantiva).
- **Fix**: subir la opacidad de base a 0.6-0.65 (ratio ~7-8:1) y conservar la transición a 1 en hover. O bajar el color directamente con `--text-muted` (#8B9491) que ya pasa 5.5:1, sin usar `opacity` sobre texto.
- [ ] Resuelto

#### 8.2.24 .pricing-card__tabs ARIA tablist (landing.html, líneas 757-760, 1757-1760)

- **Issue**: usa `role="tablist"` y `role="tab"` pero no implementa el patrón ARIA completo: sin manejo de flechas izq/der, sin tabindex roving, sin `role="tabpanel"`, sin `aria-controls`.
- **Fix**:
  - Opción A (recomendada): eliminar `role="tablist"`, `role="tab"` y `aria-selected`. Convertir en botones segmentados normales con `aria-pressed="true/false"`.
  - Opción B: implementar patrón completo — agregar `aria-controls="panel-1pago"/"panel-3cuotas"` y `role="tabpanel"` + `aria-labelledby`, manejar `keydown` Arrow Left/Right, aplicar `tabindex="-1"` al tab no seleccionado.
- [ ] Resuelto

#### 8.2.25 Touch targets debajo del mínimo (landing.html, múltiples)

- **Issue**: varios elementos interactivos quedan debajo de 44x44:
  1. `.person-card__actions .btn` → `min-height` 40px (líneas 785-789).
  2. `.sticky-mobile .btn` → 40px (línea 1284), el más usado en mobile.
  3. `.pricing-card__tab` → padding 8px 20px y font-size 13px → altura efectiva ~34px (líneas 871-877).
  4. `.header__nav a` y `.header__wpp` son texto inline sin min-height ni padding vertical generoso.
- **Fix**: restaurar `min-height:44px` en `.person-card__actions .btn` y `.sticky-mobile .btn`. Para `.pricing-card__tab` subir padding vertical a 12px y agregar `min-height:40px`. Para nav header agregar `padding:10px 0` a los `<a>`.
- [ ] Resuelto

#### 8.2.26 Skip link missing (landing.html, header líneas 1452-1473)

- **Issue**: no existe "Skip to main content" link. Usuarios de teclado y lectores de pantalla deben tabular por todo el header en cada visita. WCAG 2.4.1 Bypass Blocks (Level A) lo requiere.
- **Fix**: agregar como primer elemento del `<body>`:

  ```html
  <a href="#main-content" class="sr-only-focusable">Saltar al contenido</a>
  ```

  Agregar `id="main-content"` al `<main>`. CSS:

  ```css
  .sr-only-focusable { position: absolute; left: -9999px; }
  .sr-only-focusable:focus {
    left: 16px; top: 16px;
    padding: 12px 20px;
    background: var(--emerald);
    color: var(--text-inverse);
    border-radius: 8px;
    z-index: 1000;
  }
  ```

- [ ] Resuelto

#### 8.2.27 Person-card LinkedIn placeholder links (landing.html, líneas 1673, 1712)

- **Issue**: los enlaces `Ver perfil LinkedIn` en ambas person-cards tienen `href="#"`. Para usuarios de teclado son focusables y el click ejecuta el smooth-scroll handler (que retorna sin acción), pero el comportamiento es confuso y `href="#"` puede saltar al inicio en algunos navegadores.
- **Fix**: reemplazar por URLs reales de LinkedIn de Bauti y Ema. Si no están disponibles aún:
  - (a) ocultar los botones hasta tenerlos, o
  - (b) convertir en `<button disabled aria-label="Perfil LinkedIn próximamente">`.

  Nunca dejar `href="#"` en producción.
- [ ] Resuelto

#### 8.2.28 Hero play button sin función (landing.html, líneas 1512-1514)

- **Issue**: el botón `.hero__play` tiene `aria-label="Reproducir video"` pero no tiene handler de click ni `<video>` asociado. Mismo problema en los 3 `.testimonio-card__play` (líneas 1831, 1857, 1883). Viola WCAG 4.1.2 (Name, Role, Value).
- **Fix**: mientras no haya video real:
  - Cambiar `aria-label` a `Video próximamente` y agregar `aria-disabled="true"` + `tabindex="-1"`.
  - O reemplazar el `<button>` por un `<div>` decorativo con `aria-hidden="true"`.
  - Cuando el video esté listo (IMG-01 `hero_video_thumb`), conectar handler que reemplace el thumb por `<video controls autoplay>` o que abra Mux/Cloudflare Stream player.
- [ ] Resuelto

#### 8.2.29 Clocks ticker oculto en mobile (thankyou.html, líneas 225-228, 693-698)

- **Issue**: el bloque `.clocks` tiene `display:none` en `max-width:640px`. El JS de `tick()` sigue corriendo cada 30s actualizando elementos invisibles, gastando ciclos en mobile. Impacta usuarios mobile (menos batería/cpu).
- **Fix**: en el script, antes del `setInterval` verificar:

  ```js
  const mq = matchMedia('(min-width: 641px)');
  if (mq.matches) {
    tick();
    setInterval(tick, 30000);
  }
  mq.addEventListener('change', (e) => {
    // arrancar/detener cuando rota el dispositivo
  });
  ```

- [ ] Resuelto

---

### 8.3 Resumen de severidad

| Severidad | Cantidad | Estado bloqueo |
|---|---|---|
| Critical | 12 | Bloquea publicación |
| Major | 29 | Bloquea producción (staging OK) |

### 8.4 Orden sugerido de ejecución

1. **Hotfix de placeholders** (8.1.9, 8.2.14) — sin esto nada convierte.
2. **Hero + headline + CTA** (8.1.1, 8.1.2, 8.1.5, 8.1.8) — primer impacto de conversión.
3. **Pricing card visual + tabs** (8.1.4, 8.2.12) — el bloque de decisión.
4. **Sticky mobile + thank you accesibilidad** (8.1.6, 8.1.11, 8.1.12, 8.2.13) — conversión mobile.
5. **FAQ + garantía + objeciones** (8.1.7, 8.2.10) — reverse-risk.
6. **Performance + fuentes** (8.1.10, 8.2.22, 8.2.21, 8.2.29) — LCP/CLS.
7. **A11y** (8.2.16, 8.2.24, 8.2.25, 8.2.26, 8.2.27, 8.2.28) — WCAG AA.
8. **SEO + structured data** (8.2.20) — sharing y discovery.
9. **Polish visual** (8.2.1–8.2.9, 8.2.15, 8.2.18, 8.2.19) — design system parity.
10. **Contenido faltante** (8.2.11, 8.2.17) — secciones y páginas legales.
