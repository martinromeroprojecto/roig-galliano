# FUNNEL — Reunión 1:1 de Importación China (ARS 29.000)

> Documento operativo para el dueño y el equipo. Lo que necesitás saber para correr el funnel sin dudas, día a día.

---

## 1. Resumen del funnel en 5 líneas

1. Captamos importadores novatos argentinos por **anuncios en Meta** (Reels/Feed) que apuntan a una **landing mobile-first** con foco en autoridad (3 oficinas propias en BA, China y Miami).
2. El visitante hace click en el CTA y va **directo al link de Mercado Pago** (sin Calendly, sin checkout propio, sin fricción) para pagar **ARS 29.000 pago único**.
3. Post-pago, Mercado Pago lo redirige a una **Thank You page propia** que tiene UN solo objetivo: que mande el comprobante por **WhatsApp** con un mensaje pre-cargado.
4. Un **humano del equipo** valida el comprobante, agenda el **Zoom de 60 min 1:1 con el dueño**, manda link + formulario corto de 5 preguntas.
5. Se hace la reunión, se entrega **PDF + checklist + plantilla en inglés en menos de 48hs hábiles**, y se abre puerta natural (sin pitch) al **servicio 360** de importación full.

---

## 2. Mapa visual del flujo

```
                       ┌──────────────────────────────┐
                       │  1. ANUNCIO META (Reels/Feed)│
                       │  Hook: ventana 2026 + 3 ofic.│
                       └──────────────┬───────────────┘
                                      │ click
                                      ▼
                       ┌──────────────────────────────┐
                       │  2. LANDING (mobile-first)   │
                       │  Hero → Dolor → Autoridad →  │
                       │  Solución → Precio → FAQ →   │
                       │  CTA repetido + sticky bar   │
                       └──────────────┬───────────────┘
                                      │ click CTA verde MP
                                      ▼
                       ┌──────────────────────────────┐
                       │  3. LINK MERCADO PAGO        │
                       │  ARS 29.000 · Pago único     │
                       │  Tarjeta / débito / transf / │
                       │  saldo MP (efectivo OFF*)    │
                       └──────────────┬───────────────┘
                                      │ pago acreditado
                                      ▼
                       ┌──────────────────────────────┐
                       │  4. THANK YOU PAGE propia    │
                       │  "Falta 1 paso"              │
                       │  Botón verde gigante → WA    │
                       │  + mini-tutorial comprobante │
                       │  + Pixel/GA4/CAPI Purchase   │
                       └──────────────┬───────────────┘
                                      │ click "Enviar comprobante por WhatsApp"
                                      ▼
                       ┌──────────────────────────────┐
                       │  5. WHATSAPP pre-cargado     │
                       │  wa.me/[número]?text=...     │
                       │  Mensaje corto: el usuario   │
                       │  adjunta captura y envía     │
                       └──────────────┬───────────────┘
                                      │ mensaje recibido
                       ┌──────────────┴───────────────┐
                       │  6a. EMAIL DE RESPALDO (5-10 min post-pago)│
                       │  Recupera al ~20% que cierra│
                       │  la pestaña sin mandar WA    │
                       │  (único canal garantizado)   │
                       └──────────────┬───────────────┘
                                      │
                                      ▼
                       ┌──────────────────────────────┐
                       │  7. HUMANO (EQUIPO) AGENDA   │
                       │  Firma como equipo del dueño │
                       │  Valida MP → 3 opciones de   │
                       │  horario → confirma Zoom →   │
                       │  manda form de 5 preguntas   │
                       │  (target: respuesta <30 min  │
                       │  en horario Lun-Sab 9-21hs)  │
                       └──────────────┬───────────────┘
                                      │ Zoom agendado
                                      ▼
                       ┌──────────────────────────────┐
                       │  8. ZOOM 60 MIN 1:1 con dueño│
                       │  Diagnóstico + NCM + costo   │
                       │  final (si trae producto) +  │
                       │  paso a paso · GRABADA       │
                       └──────────────┬───────────────┘
                                      │
                                      ▼
                       ┌──────────────────────────────┐
                       │  9. PDF + CHECKLIST en <48hs │
                       │  HÁBILES + grabación +       │
                       │  plantilla EN + apertura     │
                       │  natural al servicio 360     │
                       └──────────────┬───────────────┘
                                      │
                                      ▼
                       ┌──────────────────────────────┐
                       │  10. UPSELL NATURAL (opcional)│
                       │  Servicio 360 si el cliente  │
                       │  lo pide. Sin spam.          │
                       └──────────────────────────────┘

* Pago Fácil/Rapipago deshabilitados por defecto en el link MP
  para no romper la promesa de "activación en <30 min".
  Ver sección 3.3.
```

---

## 3. Qué cambiar antes de publicar (checklist accionable)

### 3.0. BLOQUEANTES DE LANZAMIENTO (hard stops)

> Estos 4 bloqueantes detienen el deploy. No se manda 1 peso a Meta hasta que todos estén en verde y verificados con QA end-to-end.

- [ ] **B1. Link real de Mercado Pago activo** → reemplazar las ~6 ocurrencias de `https://mpago.la/REEMPLAZAR` en landing.html (hero, audiencia, módulos, FAQ, cierre, sticky mobile) por el link real. Hacerlo en un solo lugar (constante JS o template) marcando los CTAs con `data-mp` para evitar inconsistencias.
- [ ] **B2. Número real de WhatsApp Business** → reemplazar las 2 ocurrencias de `wa.me/REEMPLAZAR` en thankyou.html (botón principal + sticky bottom) y todas las del footer de la landing. Formato sin `+` ni espacios (ej: `5491112345678`).
- [ ] **B3. Datos del dueño completos** → reemplazar las 3 ocurrencias de `[NOMBRE DEL DUEÑO]` en thankyou.html (avatar inicial 'D', cuerpo del párrafo y firma) y todas las de landing.html. Cambiar la inicial 'D' del avatar por la real (o reemplazar avatar por foto).
- [ ] **B4. Tracking instalado en thankyou.html** → Meta Pixel base + evento `Purchase` con `value=29000 currency=ARS`, GA4 con evento `purchase` y `transaction_id`, CAPI server-side desde webhook MP con `event_id` deduplicado, y `dataLayer.push` en el click del WA con `click_whatsapp_send_receipt`. Sin esto, no hay ROAS, no se optimiza el pixel y los A/B de la sección 6 son imposibles.

**QA pre-deploy obligatorio**: correr un grep que falle el build si encuentra `REEMPLAZAR`, `[NOMBRE`, `[VERIFICAR`, `[XX-` o `[ FOTO REAL` en cualquier archivo del deploy. Es una sola línea en el script de CI y previene el 100% de los placeholders en producción.

### 3.1. Datos de la empresa
- [ ] **Nombre legal de la empresa** → reemplazar `[NOMBRE DE LA EMPRESA]` en header, footer y página de Thank You.
- [ ] **CUIT** → completar en footer (`[XX-XXXXXXXX-X]`). Bloqueante por Defensa al Consumidor (Ley 24.240).
- [ ] **Dirección fiscal de Buenos Aires** → completar en footer.
- [ ] **Email de contacto** → reemplazar `hola@[dominio].com` en footer.
- [ ] **Dominio final** → confirmar URL definitiva y subdominios (landing principal + thank-you).

### 3.2. WhatsApp
- [ ] **Número de WhatsApp Business** → ver B2 en 3.0. También en el footer linkeable con `href="https://wa.me/..."` para que sea clickeable desde mobile.
- [ ] **Probar el link wa.me en mobile real** (iPhone Safari, Android Chrome) y verificar que el mensaje pre-cargado se carga completo y URL-encoded correctamente.
- [ ] **Confirmar que la cuenta es WhatsApp Business** con foto, descripción ("Importaciones China · Oficinas BA · China · Miami") y horario de atención visible.
- [ ] **Mensaje de bienvenida automático fuera de horario** configurado en WhatsApp Business: *"Recibimos tu mensaje. Te respondemos mañana al abrir, antes de las 10hs (lun a sáb)."* Reduce ansiedad sin romper la promesa de "atención humana".
- [ ] **Fallback visible en thankyou.html**: *"Si no se abre WhatsApp, copiá este número: +54 9 11 XXXX XXXX"*.

### 3.3. Mercado Pago
- [ ] **Crear link de pago en Mercado Pago** por ARS 29.000, pago único, con título "Reunión 1:1 Importación China · 60 min Zoom".
- [ ] **Excluir Pago Fácil / Rapipago** del link MP (`payment_methods.excluded_payment_types=['ticket']`). Razón: efectivo en Argentina puede tardar 24-72hs en acreditar y rompe la promesa de "activación en <30 min" + el webhook del email de respaldo nunca dispara hasta `status=approved`. Mantenemos tarjeta, débito, transferencia y saldo MP (todos instantáneos).
- [ ] **Configurar `back_urls.success`** → apuntar a la Thank You page propia (NO dejar la pantalla por defecto de MP). Setear `auto_return='approved'`.
- [ ] **Crear `/pago-pendiente.html` y `/pago-rechazado.html`** propias y apuntar `back_urls.failure` y `back_urls.pending` ahí. Cada una con: (a) explicación humana de qué pasó, (b) botón para reintentar (link MP), (c) botón WhatsApp con mensaje pre-cargado tipo *"Hola, intenté pagar la reunión y el pago no se acreditó. Quiero ayuda para resolverlo."* Sin esto, el 5-15% de pagos rechazados (común en AR con tarjetas vencidas, sin saldo, percepciones) se pierde silenciosamente.
- [ ] **Activar webhook / notificación IPN** de Mercado Pago para disparar el email de respaldo automático.
- [ ] **Probar pago real** con tarjeta propia + reembolso para verificar todo el flow end-to-end antes de lanzar tráfico.

### 3.4. Email de respaldo automático (CANAL GARANTIZADO)

> Crítico: es el único canal de recovery garantizado. MP no siempre da el teléfono del comprador (depende de si lo cargó), entonces el WhatsApp proactivo de la sección 4.3 puede ser imposible. El email SIEMPRE está disponible.

- [ ] **Configurar email transaccional** (Resend / Sendgrid / Brevo / Mailchimp) que se dispare por webhook IPN de MP a los 5-10 min del evento `payment.created` con `status=approved`.
- [ ] **Redactar asunto**: "Falta 1 paso para activar tu reunión de importación".
- [ ] **Cuerpo del mail** con botón a `wa.me/[número]` y mismo mensaje pre-cargado de la TY page (corto, sin placeholders para editar).
- [ ] **Autenticar SPF/DKIM/DMARC** del dominio para que no caiga en spam. Probar entrega a Gmail, Outlook y Yahoo.
- [ ] **Test end-to-end con pago real** verificando que el mail llega en <10 min y NO cae en spam.

### 3.5. Fotos REALES (no stock, no IA)
- [ ] **Hero**: foto del dueño en la oficina de China. `<img>` con `alt="Foto del dueño de la operación en la oficina de China, en Yiwu/Shenzhen"`, `loading="eager"`, `fetchpriority="high"`. NO dejar el placeholder `[ FOTO REAL DEL DUEÑO ]` como texto visible.
- [ ] **Sección 3 oficinas**: 3 fotos (depósito BA, oficina/depósito China, hub Miami con presencia visible de Bauti).
- [ ] **Sección "Quién te atiende"**: foto del dueño en oficina de China (puede ser la misma del hero).
- [ ] **Thank You page**: misma foto del dueño en el bloque de reassurance (refuerza familiaridad). Reemplaza el avatar con inicial.
- [ ] **Si no hay foto de Miami con Bauti todavía**: conseguirla ANTES del lanzamiento — es el punto más débil del trío y el que más necesita prueba visual. Si no se puede conseguir antes del deploy, sacar Miami de la landing o reemplazar por foto del cartel/contrato de alianza — pero NO dejar el placeholder visible.

### 3.6. Datos del dueño y autoridad (números verificables)
- [ ] **Nombre real del dueño** → ver B3 en 3.0.
- [ ] **Datos verificables** → completar `[VERIFICAR]` con números reales (los inventados o vagos arruinan credibilidad con el pyme escéptico):
  - Años exactos importando (ej: "desde 2017"). El "+8 años" del hero queda condicionado a este número real.
  - Cantidad de operaciones gestionadas o TEUs movidos.
  - Cantidad de clientes activos hoy.
  - Confirmar ciudad china exacta (Yiwu o Shenzhen — usar la real).
- [ ] **Quitar "la mejor ventana en 8 años"** del hero/cierre — no es verificable y suena a hype de infoproducto.
- [ ] **Reescribir afirmaciones regulatorias** en cierre y módulo 01 con redacción concreta y fechada: *"Desde la salida del SEDI (Decreto X/2025) y el levantamiento del cepo cambiario para importadores en abril de 2025, el marco cambió. En la reunión te explicamos qué de eso aplica a tu producto y qué no."*
- [ ] **Quitar "Cero IA"** del hero — promesa absoluta no cumplible (autorespuestas de WA Business también se perciben como IA). Reemplazar por *"Te atiende una persona del equipo, no un bot"*.
- [ ] **Suavizar claims de infoproducto**: quitar el "80% de los chantas" del módulo 02 (número inventado), revisar el "Los 7 errores típicos" del módulo 05 (si son 5 o 9, ajustar — no inventar), reescribir "sin agentes truchos cobrando comisión por debajo" en el proceso pilar 01 por *"sin depender de un agente al que nunca le viste la cara"*.
- [ ] **Cambiar "3 veces el precio"** del bloque audiencia por *"el doble o el triple"* — rango honesto, no exagerado.

### 3.7. Condicionar promesas concretas (riesgo legal + credibilidad)
- [ ] **Costo final puesto en depósito** en hero y módulo 04: agregar condición visible *"Si traés a la reunión un producto concreto en mente (link de Alibaba/foto/specs sirve), salís con el cálculo del costo final puesto en depósito y el NCM identificado. Si todavía estás eligiendo entre 2-3 opciones, salís con el método para calcularlo vos solo en cualquiera de ellas."*
- [ ] **"PDF en 48hs"** → aclarar **"48hs hábiles"** o **"días hábiles"** en TODAS las menciones (hero, módulos, FAQ, plantilla 4 de WhatsApp). Si el cliente paga viernes 19hs, no espera el PDF el domingo.
- [ ] **"Activación en <30 min"** → en las 4 menciones de la landing (hero cta-micro, faq, sticky-bottom sub, cierre cta-sub) atar al horario: *"Te activamos por WhatsApp en <30 min (lun a sáb 9-21hs)."* Fuera de horario, el mensaje automático de WhatsApp Business cubre el resto.

### 3.8. Anclas de valor en el precio
- [ ] **Hero y sección #precio**: agregar un ancla de comparación cerca del ARS 29.000. Posicionar el precio como ahorro, no como gasto. Opciones a testear:
  - *"Lo que te cobra un consultor por 1h: USD 200-400. Lo que perdés en una importación mal cargada: USD 1.500-5.000 en sobrecostos."*
  - *"Menos de lo que pagás de más en una sola compra al mayorista de Once."*
- [ ] **Microcopia de vigencia** en chip de precio: *"ARS 29.000 (precio vigente al mes de [MES])"* o *"ARS 29.000 · pago único — el precio mostrado es el que cobramos en el checkout de MP."* En Argentina, un precio fijo en pesos sin disclaimer de vigencia se lee como "no lo pensaron".

### 3.9. Prueba social (hueco más grande del funnel)
- [ ] **Agregar sección "Quiénes ya lo hicieron"** antes de la FAQ con:
  - 3-4 testimonios reales con foto + nombre + ciudad + rubro + 1 línea de resultado medible (ej: *"USD 18k de margen recuperado en la 2da operación"*).
  - 2-3 capturas reales de WhatsApp (datos sensibles tachados) — en Argentina convierten muchísimo.
  - Números agregados verificables: *"+200 clientes asesorados · +USD 4M en mercadería movida · 8 años en China"* — todo con datos reales.
- [ ] **Si todavía no hay testimonios sólidos**: lanzar con "Caso de la semana" + números operativos duros del operador. NO testimonios genéricos tipo "me encantó". NO lanzar SIN ninguna prueba social.

### 3.10. Urgencia honesta y verificable
- [ ] **Reescribir el bloque "Por qué no hay 50 lugares"** sacando la defensiva ("No es marketing de escasez — es que..."). Versión sugerida: *"Las reuniones las doy yo, 1 a 1. Atender la operación de los tres depósitos me deja pocos espacios libres por semana. Cuando se llenan, la próxima ventana queda para 2-3 semanas más adelante. Si te urge, reservá ahora; si podés esperar, también está bien."*
- [ ] **Agregar contador de cupos real** cerca del CTA principal: *"Quedan X cupos esta semana — próximo horario disponible: [día] [fecha] [hora]."* Que sea real (no fake countdown). Si no se quiere mostrar agenda, al menos *"Doy 5 reuniones por semana. Esta semana quedan 2."*

### 3.11. Política de reprogramación visible
- [ ] **Agregar a la FAQ** una pregunta: *"¿Qué pasa si necesito reprogramar?"* con la respuesta completa alineada al 4.4: *"Hasta 24hs antes, libre y sin costo. Con <24hs ofrecemos una reprogramación de cortesía; a partir de la segunda inasistencia/cancelación tardía, la reagendada queda a discreción del equipo (puede tener cargo)."* Sin esto, cualquier cargo por reprogramación es un reclamo válido del cliente.

### 3.12. Garantía 15 min — política operativa visible
- [ ] **Reescribir la FAQ de reembolso** con redacción no engañosa: *"Reembolso procesado por nosotros en <24hs hábiles. La acreditación en tu cuenta/tarjeta depende del medio (saldo MP: instantáneo; tarjeta: hasta 7 días hábiles según banco)."* MP en AR puede tardar 2-7 días en acreditar a tarjeta — si prometemos "24-48hs hábiles" sin aclarar, el cliente reclama en Defensa al Consumidor.

### 3.13. Estructura visual y CTAs
- [ ] **UN solo CTA primario** en toda la página (verde sólido, mismo copy, misma forma). Secundarios subordinados (link de texto o ghost button). Cambiar "Soy de los de la izquierda" por *"Reservar mi reunión 1:1 →"*.
- [ ] **Reordenar FAQs** por orden de fricción real al pago: (1) reembolso/garantía, (2) duración y formato, (3) "soy chico ¿es para mí?", (4) métodos de pago, (5) "¿me van a vender algo al final?", (6) qué pasa después. Mover/reescribir la actual sobre el upsell de USD 3.000 al final, sin negación defensiva.
- [ ] **Suavizar la FAQ del 360**: cambiar la pregunta agresiva por una neutral (*"¿Hay algún upsell después de la reunión?"*) y ser explícito en la respuesta: existe servicio 360, NO se vende durante el Zoom, se ofrece UNA línea en el mail del PDF, si no hay respuesta no hay insistencia.
- [ ] **Comprimir el hero** para que el CTA verde entre arriba del fold en iPhone 13/14 (LCP <700px): eyebrow + h1 corto (12-14 palabras max), sub de 1 línea, CTA, garantía chip. Mover bullets y price chip debajo del CTA.
- [ ] **Reescribir h1** invirtiendo el orden (beneficio primero, autoridad después). Opciones a testear:
  - *"Destrabá tu primera importación de China en 60 minutos — con el dueño de la operación, no con un coach."*
  - *"Tu primer contenedor desde China, calculado en vivo y con tu producto sobre la mesa. 60 min de Zoom 1:1."*

### 3.14. Thank You page — fricción del WhatsApp pre-cargado
- [ ] **Eliminar los 3 placeholders del mensaje pre-cargado** (`[DEJA TU NOMBRE]`, `[DEJA TU EMAIL]`, `[DEJA TU PRODUCTO]`). En mobile, editar texto en el input de WhatsApp es engorroso y muchos van a mandar el mensaje con los corchetes literales. Dos opciones:
  - **Opción A (recomendada)**: mini-form en la TY page que captura nombre/email/producto antes de generar el link `wa.me`, y los inyecta en el `text=` con JS. También recibe esos datos vía query string desde el `back_urls.success` de MP.
  - **Opción B (rápida)**: mensaje pre-cargado mínimo y accionable sin edición: *"Hola, acabo de pagar la reunión. Te paso el comprobante."* El operador pide nombre/email/producto en su primera respuesta.
- [ ] **Reescribir el bloque reassurance** sacando la ambigüedad de "ya sos parte del próximo Zoom" (suena a Zoom grupal): cambiar el h3 por *"Tu Zoom 1:1 ya está reservado."* y el body por *"Soy [NOMBRE], el que va a estar del otro lado del Zoom. En cuanto vea tu comprobante, te confirmo el horario por WhatsApp. Para el día de la reunión, reservate 60 min con buena conexión y con tu producto en mente — del resto me ocupo yo."*

### 3.15. Tracking y analytics
- [ ] **Meta Pixel** instalado en landing y Thank You (evento `Purchase` en Thank You, con `value=29000 currency=ARS`, `transaction_id` y `event_id`).
- [ ] **Google Analytics 4** instalado en landing y Thank You (evento `purchase` con `transaction_id`).
- [ ] **Conversiones API (CAPI)** de Meta configurada server-side desde webhook de MP — para deduplicar evento `Purchase` con `event_id`.
- [ ] **Eventos custom en landing**: `PageView`, `ViewContent`, `ClickCTA` (en cada CTA con `data-mp`).
- [ ] **Evento click en WhatsApp** trackeado en Thank You (`click_whatsapp_send_receipt`) con `dataLayer.push` en el `onclick` del botón.
- [ ] **UTM parameters** en todos los anuncios de Meta (`utm_source=meta`, `utm_medium=paid`, `utm_campaign=[nombre]`, `utm_content=[creativo]`).

### 3.16. Legales
- [ ] **Términos y condiciones** mínimos (qué incluye la reunión, política de reembolso 15 min, política de reprogramación, datos personales). Mecanismo de actualización de precio reflejado.
- [ ] **Política de privacidad** breve (qué hacemos con el email y los datos del formulario).
- [ ] **Defensa al consumidor** — link al botón de arrepentimiento si aplica (Ley 24.240).

### 3.17. Accesibilidad y performance
- [ ] **Reemplazar emojis 💬 / ✅** del botón principal de la Thank You por SVG inline de WhatsApp. Los emojis se renderizan distinto en cada device, fallan en webviews viejos y son leídos como "speech balloon" por screen readers.
- [ ] **Auditar pesos de Google Fonts**: cargar solo los pesos realmente usados (revisar si el 600 hace falta). Mínimo: agregar `&display=swap` explícito y considerar self-hosting con preload.
- [ ] **Contraste WCAG AA**: subir `.hero__photo-placeholder` de `rgba(255,255,255,.55)` a `.85`. Verificar `.hero__proof` (~4.8:1 está en el borde). Auditar con axe DevTools.
- [ ] **Sticky CTA mobile**: subir `padding-bottom` del body a `calc(96px + env(safe-area-inset-bottom))` para no tapar el cierre en iPhones con notch.
- [ ] **Tap target del header CTA**: subir padding a `12px 16px` para llegar a ≥44px de altura (mínimo Apple). Considerar que apunte directo al link MP en lugar de a anchor.
- [ ] **Accordion FAQ**: agregar `aria-hidden="true"` al span del ícono `+`. Reforzar en CSS `summary::marker { display: none; } summary::-webkit-details-marker { display: none; }`.
- [ ] **Hero bullets**: cambiar breakpoint a `min-width: 720px` o usar `repeat(auto-fit, minmax(200px, 1fr))` para evitar layout roto en iPhone landscape.
- [ ] **Chip de precio en viewports chicos** (~320px): reducir `font-size` con `@media (max-width: 380px) { .hero__price-chip { font-size: 12px; } }`.

### 3.18. QA final mobile y desktop
- [ ] **iPhone 13/14/15** (Safari y Chrome) — que el hero (incluyendo CTA verde) entre arriba del fold (<700px).
- [ ] **Android medio** (Samsung A-series) — Chrome.
- [ ] **Desktop 1440px** — Chrome, Firefox, Safari.
- [ ] **Sticky bottom CTA mobile** visible en todo el scroll desde el hero, sin tapar el cierre.
- [ ] **Velocidad de carga** <2.5s LCP en mobile 4G (PageSpeed Insights).
- [ ] **Accordion de FAQs** con tap target >=56px.
- [ ] **Link de wa.me** funciona en iOS, Android y desktop.
- [ ] **Grep de placeholders** en CI: `grep -rE "REEMPLAZAR|\[NOMBRE|\[VERIFICAR|\[XX-|\[ FOTO REAL"` debe devolver 0 matches antes del deploy.

---

## 4. Cómo operarlo día a día

### 4.1. Quién mira WhatsApp y cuándo

- **Responsable principal**: una persona fija del equipo (NO el dueño — el dueño solo aparece en el Zoom para preservar autoridad). Idealmente el asistente operativo o el del depósito de BA.
- **Política de firma**: el operador firma SIEMPRE como equipo del dueño, no como el dueño. Ejemplo: *"Hola [Nombre], soy [Nombre del operador] del equipo de [Nombre del dueño]."* Esto vale para TODOS los scripts en `whatsapp-scripts.md` — auditar y corregir cualquier mensaje que diga *"Soy {{nombre_dueno}}"* en lugar de *"del equipo de {{nombre_dueno}}"*. Hacerse pasar por el dueño es deshonesto y se rompe si el cliente reconoce voz/foto en el Zoom o redes.
- **Excepción**: si la operación todavía es chica y el dueño quiere atender él mismo, se firma con su nombre real. Pero hay UNA sola política a la vez — no mezclar.
- **Horario de atención**: lunes a sábado, 9:00 a 21:00 (consistente con lo que promete la landing).
- **Tiempo de respuesta target**: <30 minutos en horario hábil. Si llega fuera de horario, el mensaje automático de bienvenida de WhatsApp Business avisa: *"Recibimos tu mensaje. Te respondemos mañana al abrir, antes de las 10hs."*
- **Notificaciones**: activar push del WhatsApp Business en el celular del responsable + mirror en WhatsApp Web en la compu del depósito.

### 4.2. Flow operativo paso a paso

1. **Llega comprobante por WhatsApp** → el responsable abre Mercado Pago en paralelo y verifica que el pago esté acreditado (matching por monto, hora y nombre).
2. **Responde con la Plantilla 1** (ver sección 7.1 abajo) ofreciendo 3 opciones de horario en los próximos 5-7 días hábiles. Firma como equipo del dueño.
3. **El cliente elige horario** → responde con la **Plantilla 2** (confirmación + link Zoom + formulario de 5 preguntas).
4. **Carga el evento en el calendario del dueño** (Google Calendar) con el link de Zoom, nombre del cliente, rubro y link al form respondido.
5. **24hs antes del Zoom**: responde con la **Plantilla 3** (recordatorio).
6. **Día del Zoom**: el dueño hace la reunión, la graba, toma notas en plantilla interna.
7. **Dentro de las 48hs hábiles post-Zoom**: el dueño (o el responsable con info del dueño) arma el PDF personalizado y lo envía por **email + WhatsApp** con la **Plantilla 4** (post-Zoom).

### 4.3. Qué hacer si alguien paga y NO manda comprobante en 24h

Es el caso más común de fricción. Protocolo:

- **A los 5-10 min** del pago: el email de respaldo automático ya salió. (Verificar en logs). **Este es el canal garantizado** — MP no siempre da el teléfono del comprador, así que el WhatsApp proactivo de los pasos siguientes puede ser imposible si no tenemos número.
- **A las 2 horas** sin comprobante (si tenemos número de WA del cliente): el responsable manda mensaje proactivo desde WhatsApp Business al número que figura en MP. Plantilla:
  > "¡Hola! Soy [Nombre] del equipo de [Empresa]. Vimos que hace un rato pagaste tu reunión de importación de China — ¡bienvenido! Para activarla solo necesito que me mandes el comprobante de Mercado Pago por acá. Te paso el link directo: [wa.me con mensaje pre-cargado]. Cualquier duda, escribime acá mismo."
- **A las 24 horas** sin comprobante: segundo mail recordatorio con asunto distinto ("[Nombre], me falta tu comprobante para activar la reunión").
- **A las 48 horas** sin comprobante: si tenemos número, llamada directa por WhatsApp (o teléfono) — humano a humano.
- **A los 7 días** sin contacto: dar por perdido, pero NO devolver plata automáticamente. Mandar un último mail amistoso ofreciendo activar cuando quiera + ofrecer reembolso si prefiere.
- **Nunca antes de 7 días**: si el cliente pide reembolso proactivamente, se devuelve sin discutir.

> **Importante**: si MP no provee el teléfono del payer (caso común), los pasos de contacto proactivo por WhatsApp NO se pueden ejecutar. El email automático es el único canal garantizado. Por eso es bloqueante de lanzamiento (B4 + 3.4).

### 4.4. Qué hacer si el cliente quiere reprogramar

> Política reflejada en la FAQ visible al cliente (ver 3.11). Si no está en la landing, no se cobra ningún cargo por reprogramación.

- **Hasta 24h antes del Zoom**: reprogramación libre, las veces que necesite, sin costo. Responder con Plantilla 1 ofreciendo 3 nuevas opciones.
- **Menos de 24h antes**: explicar la política amablemente, ofrecer una sola reprogramación de cortesía. Si vuelve a faltar, la próxima reprogramación queda a discreción del equipo (puede tener cargo).
- **No-show sin aviso**: contactar al día siguiente, ofrecer una sola reagendada. Si vuelve a no presentarse, se pierde la reunión sin reembolso.

### 4.5. Qué hacer si alguien activa la garantía de 15 min

- **Sin discutir, sin pedir explicaciones**. El dueño confirma el cierre por WhatsApp en el momento (*"listo, lo cierro"*).
- **Procesamiento operativo**: el responsable aprieta el reembolso en MP en <24hs hábiles. NO requiere autorización adicional del dueño una vez que el dueño confirmó por WhatsApp.
- **Acreditación al cliente**: NO depende de nosotros. Comunicarle al cliente con honestidad:
  - Si pagó con saldo MP → instantáneo al procesar.
  - Si pagó con tarjeta → hasta 7 días hábiles según banco.
  - Si pagó con transferencia → 1-3 días hábiles.
- **Copy de respaldo**: la FAQ de la landing (ver 3.12) dice exactamente esto. Si el cliente reclama, repetir la misma redacción.
- **Loguear el caso internamente** (motivo aproximado, rubro del cliente) para detectar si hay un patrón de mismatch entre la landing y lo que entrega la reunión.

### 4.6. Pitch del servicio 360 (post-Zoom, no durante)

- **NO se pitchea durante el Zoom**. La regla es sagrada.
- **En el mail del PDF (48hs hábiles post-Zoom)** hay UNA línea natural: *"Si querés que nos hagamos cargo de la operación completa, contestame este mail y armamos una segunda call para cotizarte el servicio 360. Si no, ¡a importar!"*
- **Si el cliente responde**: agendar segunda call de cotización (esta sí puede ser comercial, no didáctica).
- **Si pregunta por el 360 ANTES del Zoom** (por WhatsApp): NO cotizar por WA. Respuesta tipo: *"Buenísimo que te interese. Lo que conviene es esto: primero hacemos el Zoom 1:1 con tu producto sobre la mesa, así te cotizo el 360 con datos reales (NCM, volumen, fábrica). Si después de la reunión querés avanzar con el 360, ahí armamos una segunda call cortita de cotización. ¿Te parece?"*
- **Si no responde al PDF en 14 días**: mandar UN único follow-up suave preguntando cómo viene la primera operación. Nada más. Cero spam.

### 4.7. Casos borde a tener guionados (scripts faltantes)

> Estos casos van a aparecer en operación real. Sin script, cada uno lo improvisa el operador y la consistencia se pierde. Agregar a `whatsapp-scripts.md`:

1. **Reembolso pre-Zoom (cambio de opinión antes de la reunión)**: política de no-preguntar, reembolso en <24hs hábiles, mismo procedimiento que garantía 15.
2. **Activación de garantía 15 DURANTE el Zoom**: dueño confirma en el momento, copy empático, expectativa clara de acreditación (ver 4.5).
3. **Reprogramación con <24hs de anticipación**: aplicar 4.4 con tono cálido, sin lectura de letra chica.
4. **Consulta sobre servicio 360 pre-Zoom**: redirigir al post-Zoom (ver 4.6).
5. **Calificación pre-pago para rubros borde** (alimentos, medicamentos, electrónica con homologación): pedir más info, derivar a consulta corta antes del checkout, evitar reembolsos post-pago por mismatch.
6. **Disculpa por SLA roto** (pasaron >30 min en horario hábil sin respuesta): disculpa explícita + bonus opcional (ej: PDF en <24hs en lugar de <48hs).

---

## 5. Métricas a medir

### 5.1. Métricas por etapa del funnel

| # | Etapa | Métrica | Target inicial | Cómo medir |
|---|-------|---------|----------------|------------|
| 1 | Anuncio Meta | CTR (Click-Through Rate) | >1.5% (Reels >2%) | Meta Ads Manager |
| 2 | Anuncio → Landing | CPC (Costo por Click) | <ARS 200-400 | Meta Ads Manager |
| 3 | Landing | Scroll depth >75% | >40% de visitas | GA4 (`scroll` event) |
| 4 | Landing → CTA | Click en CTA (hero + sticky + final) | >8% de visitas | GA4 + Pixel custom event `ClickCTA` |
| 5 | CTA → MP | CTR a Mercado Pago | >85% del click en CTA | Diferencia entre evento `ClickCTA` y `redirect_mp` |
| 6 | MP → Pago | Tasa de conversión a pago | 2-4% de visitas totales | Webhook MP / GA4 conversión |
| 7 | Pago → Thank You | Tasa de carga de Thank You | >95% del pago | GA4 pageview en /thank-you |
| 8 | Thank You → WA | Tasa de envío de comprobante en <10 min | **>85%** | Click event `click_whatsapp_send_receipt` + matching manual |
| 9 | WA → Zoom agendado | Tasa de agendamiento | >90% del comprobante recibido | Manual (planilla operativa) |
| 10 | Zoom agendado → Zoom realizado | Tasa de show | >90% (no-show <10%) | Manual |
| 11 | Zoom realizado → Cliente 360 | Conversión a upsell | >25% pide info del 360 | Manual |
| 12 | Refund 15 min | Tasa de reembolso | <5% | MP + planilla operativa |
| 13 | Pagos rechazados recuperados | Recovery vía `/pago-rechazado.html` | >30% | Eventos GA4 en página de error + matching MP |
| 14 | Pago Fácil/Rapipago | % del total | (N/A — deshabilitado) | Confirmar exclusión en config MP |

### 5.2. Costo por adquisición

- **CPA (Costo por reunión vendida)** = Gasto Meta / Cantidad de pagos confirmados. Target inicial: **CPA <= ARS 14.500** (50% del precio).
- **ROAS de la reunión sola** = ARS 29.000 / CPA. Target: **>2.0x**. (Por debajo, el funnel sangra plata).
- **ROAS combinado con upsell** = (ARS 29.000 × N_reuniones + Ingresos_360 × N_clientes_360) / Gasto_Meta. Target: **>4.0x** a 90 días.

### 5.3. Métricas cualitativas a revisar semanal

- **Calidad del leads que llega**: ¿son ICP (PyME novato con USD 1.000-30.000)? ¿O son curiosos / mayoristas que no aplican?
- **Objeciones recurrentes en WhatsApp** ANTES de pagar (pre-venta) → si se repiten 3+ veces, agregar a FAQs.
- **Feedback post-Zoom** (incluso informal): ¿qué módulos se llevaron más? ¿Cuál sobró?
- **Razones de no-show** y de no-respuesta al PDF.
- **% de mensajes pre-cargados que llegan con corchetes sin editar** (si la opción B del 3.14 está activa). Si es alto, migrar a opción A (mini-form en TY).
- **% de pagos rechazados que se recuperan** vía `/pago-rechazado.html` (target >30%).

---

## 6. Próximos pasos para iterar (A/B testing)

Prioridad de los tests para los primeros 60-90 días. **Correr UNO a la vez** y medir con sample size mínimo de 200 visitas por variante para conclusiones válidas.

> Pre-requisito: tracking de la sección 3.15 instalado y verificado. Sin pixel/GA4/CAPI, ningún test es medible.

### Test 1 (semana 1-3): Headline del hero
- **A (control)**: *"Destrabá tu primera importación de China en 60 minutos — con el dueño de la operación, no con un coach."*
- **B**: *"Tu primer contenedor desde China, calculado en vivo y con tu producto sobre la mesa. 60 min de Zoom 1:1."*
- **Hipótesis**: A gana porque el contraste "dueño vs coach" es más punzante para el pyme escéptico que vio mil cursos.
- **Métrica primaria**: tasa de click en CTA hero.

### Test 2 (semana 4-6): Precio visible vs precio en sección 10
- **A (control)**: precio visible en hero.
- **B**: precio recién en sección 10, hero solo con valor ("60 min con el dueño").
- **Hipótesis**: el control gana (precio visible reduce fricción), pero confirmar con data del target argentino.
- **Métrica primaria**: tasa de conversión visita → pago.

### Test 3 (semana 7-9): Garantía 15 min — chip en hero vs solo en sección 11
- **A**: chip visible en hero ("Garantía 15 min: si no te sirve, te devolvemos el 100%").
- **B**: garantía recién en sección 11.
- **Hipótesis**: A reduce fricción percibida y mejora conversión.
- **Métrica primaria**: tasa de conversión visita → pago.

### Test 4 (semana 10-12): Creativos de Meta
- **A**: Reel de 30 seg con el dueño hablando a cámara desde la oficina de China.
- **B**: Reel de 30 seg con b-roll del depósito + voice-over.
- **C**: Carrusel estático con las 3 oficinas + precio.
- **Hipótesis**: A gana en CTR pero B gana en CPA porque filtra mejor.
- **Métrica primaria**: CPA.

### Test 5 (semana 13-15): Thank You page — mensaje pre-cargado
- **A (control)**: mensaje corto sin placeholders (opción B del 3.14).
- **B**: mini-form en TY que captura nombre/email/producto y los inyecta en el `text=` del wa.me (opción A del 3.14).
- **Hipótesis**: B gana porque elimina la fricción de "mensaje con datos sin pedir + operador tiene que pedirlos de nuevo".
- **Métrica primaria**: tasa de envío de comprobante en <10 min + % de mensajes con datos completos a la primera.

### Test 6 (semana 16+): Formulario pre-Zoom
- **A**: formulario después de confirmar horario por WhatsApp (actual).
- **B**: formulario antes de confirmar horario (más calificación, pero más fricción).
- **Métrica primaria**: tasa de show + calidad de la reunión (medido cualitativamente por el dueño).

---

## 7. Plantillas de respuesta humana en WhatsApp

> **Política de firma**: el operador firma SIEMPRE como **equipo del dueño**, NO como el dueño (ver 4.1). Toda mención a "Soy [Nombre del dueño]" en plantillas debe corregirse a "Soy [Nombre del operador] del equipo de [Nombre del dueño]". Auditar `whatsapp-scripts.md` y unificar.

### 7.1. Plantilla 1 — Confirmación inicial + agendamiento

Disparador: el cliente acaba de mandar el comprobante de MP.

```
¡Hola [NOMBRE]! Soy [TU NOMBRE], del equipo de [NOMBRE DEL DUEÑO] 👋

Ya vi el comprobante en Mercado Pago, está todo OK ✅
¡Gracias por confiar en nosotros!

Te paso 3 opciones para el Zoom de 60 minutos con [NOMBRE DEL DUEÑO]:

🗓 Opción 1: [DÍA] [FECHA] a las [HORA]
🗓 Opción 2: [DÍA] [FECHA] a las [HORA]
🗓 Opción 3: [DÍA] [FECHA] a las [HORA]

Decime cuál te queda mejor y te mando:
✔ El link de Zoom
✔ Un formulario cortito de 5 preguntas (para que aprovechemos al máximo los 60 min con tu producto sobre la mesa)

¿Cuál elegís?
```

**Notas operativas**:
- Personalizar SIEMPRE con nombre del cliente (sacado del form de WhatsApp pre-cargado o del MP).
- Ofrecer 3 horarios en los próximos 5-7 días hábiles, NO más adelante (el momentum se enfría).
- Si el cliente lo necesita más tarde, ofrecer flexibilidad.
- Cero emojis adicionales más allá de los que están en la plantilla.

---

### 7.2. Plantilla 2 — Confirmación de horario + link Zoom + form

Disparador: el cliente eligió un horario.

```
¡Perfecto [NOMBRE]! Te confirmo:

📅 [DÍA] [FECHA] a las [HORA] (hora de Argentina)
🔗 Link de Zoom: [LINK]
👤 Con [NOMBRE DEL DUEÑO], dueño de la operación

Acá va el formulario de 5 preguntas para que llegues con todo en la cabeza y aprovechemos los 60 minutos al máximo:
📝 [LINK AL FORM]

Te lleva 3-4 minutos completarlo. Idealmente respondelo en las próximas 24hs así [NOMBRE DEL DUEÑO] llega preparado con tu caso puntual.

Si surge cualquier cosa antes de la reunión, escribime por acá.
¡Nos vemos el [DÍA]!
```

**Notas operativas**:
- Crear el evento en el Google Calendar del dueño con el link de Zoom embebido.
- Agendar recordatorio automático del propio Zoom 1h antes.
- Si el cliente NO completa el form en 24h, mandar Plantilla 3 antes de tiempo.

---

### 7.3. Plantilla 3 — Recordatorio 24h antes

Disparador: faltan 24h para el Zoom.

```
¡Hola [NOMBRE]! Te recuerdo que mañana [DÍA] a las [HORA] tenemos el Zoom con [NOMBRE DEL DUEÑO] 🎥

🔗 Link: [LINK ZOOM]

Para llegar bien preparado/a:
1) Confirmame que pudiste responder el formulario (si no, te dejo el link de vuelta: [LINK FORM])
2) Tené a mano el producto que querés importar (link de Alibaba, foto, descripción, lo que tengas)
3) Si ya tenés cotizaciones de fábricas, traelas — las miramos juntos
4) Reservate los 60 min sin interrupciones (te recomiendo conexión por compu mejor que celular)

¿Confirmás que estás para mañana?
```

**Notas operativas**:
- Si el cliente no confirma en 4-6 horas, mandar un breve "¿confirmás?" — reduce no-show.
- Si dice que no puede, ir directo a la Plantilla 1 con nuevos horarios.

---

### 7.4. Plantilla 4 — Post-Zoom + entrega de PDF en <48hs hábiles

Disparador: dentro de las 48h hábiles después del Zoom.

```
¡Hola [NOMBRE]! ¿Cómo estás?

Tal como te dije en la reunión, acá va todo lo que te llevás del Zoom de ayer 📦

📄 PDF con el resumen + checklist de los próximos 30 días: [LINK]
🎥 Grabación del Zoom (queda guardada para siempre): [LINK]
📧 Plantilla en inglés para contactar fábricas: dentro del PDF, página [X]
🧮 Cálculo de tu costo final puesto en depósito: dentro del PDF, página [X]*
📋 NCM correcto de tu producto + arancel: dentro del PDF, página [X]*

* Si en la reunión trabajamos con un producto concreto. Si todavía estás eligiendo entre opciones, en el PDF tenés el método para calcular costo y NCM en cualquiera de ellas.

Cualquier duda en los próximos 7 días, escribime por acá sin problema — te respondo yo personalmente.

PD: si después de revisar el plan querés que nos hagamos cargo de la operación completa (servicio 360 — vamos nosotros a la fábrica, embarcamos, despachamos, te lo entregamos en tu depósito), contestame este mensaje y armamos una segunda call para cotizarte. Sin presión: si querés ejecutar solo/a con el plan, ¡dale para adelante!

¡Mucha suerte con tu primera importación! 🚢
— [NOMBRE DEL DUEÑO]
```

**Notas operativas**:
- Mandar EN PARALELO el mismo contenido por email (mejor archivo permanente que WhatsApp).
- El PDF se arma con plantilla estándar + datos personalizados del cliente (sacados del form + de las notas del Zoom).
- Si el cliente responde pidiendo info del 360 → agendar segunda call de cotización (esta sí comercial).
- Si NO responde en 14 días: UN solo follow-up suave: *"¡Hola [NOMBRE]! ¿Cómo viene la primera operación? ¿Alguna duda con la que pueda darte una mano? Si necesitás que armemos la cotización del 360, decime."*
- Si vuelve a no responder: dar por cerrado el ciclo. Cero más mensajes.

---

## 8. Anexo: archivos clave del proyecto

| Archivo / activo | Propietario | Cuándo se toca |
|------------------|-------------|----------------|
| Landing principal (`index.html`) | Diseñador / Dev | Cambios de copy, tests A/B |
| Thank You page (`/gracias`) | Dev | Cambios en tutorial comprobante, número de WA |
| Pago pendiente (`/pago-pendiente.html`) | Dev | Cambios en copy de recovery |
| Pago rechazado (`/pago-rechazado.html`) | Dev | Cambios en copy de recovery |
| Link de Mercado Pago | Dueño | Cambios de precio, descripción del producto, exclusión de métodos |
| Plantilla PDF post-Zoom | Dueño | Cuando cambien procedimientos operativos |
| Plantillas WhatsApp (este doc) | Equipo de atención | Cuando se detecten nuevas objeciones |
| `whatsapp-scripts.md` | Equipo de atención | Alinear firma "equipo de" + agregar 6 scripts faltantes (4.7) |
| Calendario Zoom del dueño | Equipo de atención | Cada agendamiento |
| Pixel de Meta + GA4 + CAPI | Dev / Growth | Configuración inicial + nuevos eventos |
| Webhook IPN MP + email transaccional | Dev | Mantenimiento del canal de recovery garantizado |
| Script CI de grep de placeholders | Dev | Mantenimiento de la red de seguridad anti-placeholder |

---

**Última actualización**: 2026-06-14
**Próxima revisión sugerida**: a los 30 días de tener tráfico (revisar métricas de la sección 5 y empezar Test 1).
