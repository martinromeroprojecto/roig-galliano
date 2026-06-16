# WhatsApp Scripts — Funnel de Reunión 1:1 Importación China

Guion completo de mensajes para operar el funnel desde WhatsApp después del pago por Mercado Pago. Tono argentino (voseo), cálido pero profesional, sin emojis cringe, sin chamuyo de gurú. Cada mensaje está listo para copiar y pegar — las variables van entre `{{llaves}}`.

> **Política de identidad (importante):** WhatsApp lo opera una persona fija del equipo, NO el dueño. El dueño aparece recién en el Zoom — esto preserva la autoridad del experto y permite que la operación escale. Por eso TODOS los scripts firman como **equipo de {{nombre_dueno}}**, nunca como el dueño en primera persona. Esto está alineado con FUNNEL.md sección 4.1 y resuelve la disonancia previa entre documentos.

**Variables más usadas:**
- `{{nombre}}` — nombre del cliente
- `{{producto}}` — producto / rubro que dijo que quiere importar
- `{{horario}}` — día y hora del Zoom (ej: "martes 18/06 a las 16hs")
- `{{link_zoom}}` — link de la reunión de Zoom
- `{{nombre_dueno}}` — nombre del dueño que atiende el Zoom (NO firma WhatsApp)
- `{{nombre_operador}}` — nombre de la persona del equipo que opera WhatsApp
- `{{link_form}}` — link al formulario de 5 preguntas pre-Zoom
- `{{link_grabacion}}` — link de la grabación del Zoom
- `{{link_pdf}}` — link al PDF resumen + checklist + plantilla
- `{{link_mp_retry}}` — link de Mercado Pago para reintentar el pago

**Horario operativo:** lun a sáb, 9 a 21hs (hora Argentina). Toda promesa de tiempos de respuesta aplica dentro de este horario.

---

## 1) Mensaje del cliente al llegar (pre-cargado desde la Thank You)

Mensaje pre-cargado en el link `wa.me` del botón de la Thank You. Se mantiene **corto y sin placeholders para editar** — la fricción de pedirle al cliente que reemplace `[NOMBRE]`, `[EMAIL]`, `[PRODUCTO]` dentro del input de WhatsApp en mobile hace que muchos manden el mensaje con los corchetes literales o no lo manden nunca. El operador pide nombre/email/producto en su primera respuesta (Script 2).

```
¡Hola! Acabo de pagar mi reunión 1:1 de importación de China por Mercado Pago. Te paso el comprobante para activarla.
```

*(Junto con este mensaje el cliente adjunta la captura del comprobante de Mercado Pago.)*

> **Nota técnica:** lo ideal es capturar nombre/email/producto en un mini-form de la propia Thank You ANTES de generar el link `wa.me`, e inyectarlos en el `text=` del query string. Hasta que eso esté implementado, el mensaje corto de arriba es la versión rápida y sin fricción.

---

## 2) Respuesta humana 1 — "Recibí el comprobante, lo verifico"

Primer mensaje del operador. Objetivo: confirmar recepción dentro del SLA (<30 min en horario hábil), bajar ansiedad, comprar 5-15 min para verificar el pago en MP, y **pedir los datos** que ya no vienen pre-cargados (nombre, email, producto).

```
¡Hola! Soy {{nombre_operador}}, del equipo de {{nombre_dueno}} (el que va a estar del otro lado del Zoom).

Recibí tu comprobante y ya lo estoy verificando con Mercado Pago. En unos minutos te confirmo que está todo OK y arrancamos a coordinar día y hora de la reunión.

Para terminar de activarte, mandame en este chat, en 3 líneas:

1) Nombre y apellido
2) Email
3) Producto o rubro que querés importar (ej: "indumentaria deportiva", "accesorios de celular", o link de Alibaba si ya estuviste mirando algo concreto)

Mientras tanto, anotate: la reunión son 60 minutos por Zoom, 1 a 1, con {{nombre_dueno}}. Si tenés volumen estimado y presupuesto a mano, tenelos cerca para cuando agendemos — esos 60 minutos rinden el triple cuando llegás con esos datos.

Ya te vuelvo a escribir con la verificación.
```

---

## 3) Respuesta humana 2 — "Verificado, vamos a agendar" + opciones de horarios

Segundo mensaje, dentro de los 30-60 min siguientes. Objetivo: cerrar el horario con 3 opciones concretas (no abrir agenda infinita).

```
Listo {{nombre}}, pago verificado. Ya estás dentro.

Te tiro 3 opciones de horario para el Zoom con {{nombre_dueno}}, elegí la que mejor te queda:

- Opción A: {{opcion_1}} (ej: martes 18/06 a las 16hs)
- Opción B: {{opcion_2}} (ej: jueves 20/06 a las 11hs)
- Opción C: {{opcion_3}} (ej: sábado 22/06 a las 10hs)

Si ninguna te sirve, decime 2 o 3 ventanas tuyas y veo cómo lo acomodo. Atendemos de lunes a sábado de 9 a 21hs (hora Argentina).

Una vez que confirmes, te paso el link de Zoom y un formulario corto de 5 preguntas para que aprovechemos los 60 minutos al máximo.
```

---

## 4) Respuesta humana 3 — Confirmación del horario con link de Zoom

Tercer mensaje, apenas el cliente elige horario. Objetivo: confirmar, dar el link de Zoom, mandar formulario pre-reunión y dejar las reglas claras (puntualidad, qué tener a mano, política de reprogramación completa).

```
Perfecto {{nombre}}, te confirmo:

REUNIÓN ZOOM 1:1 con {{nombre_dueno}}
{{horario}} (hora Argentina)
Duración: 60 minutos
Link de Zoom: {{link_zoom}}

Antes del Zoom, hacé estas 3 cosas:

1) Completá este formulario de 5 preguntas (te lleva 3-4 min) — le sirve a {{nombre_dueno}} para llegar al Zoom ya sabiendo qué necesitás:
{{link_form}}

2) Tené a mano: link o foto del producto que querés importar, presupuesto aproximado en USD, y cualquier cotización que ya hayas pedido a algún proveedor (si la tenés).

3) Reservate los 60 min sin interrupciones, con buena conexión. Si podés con auriculares mejor — la calidad de audio cambia mucho la conversación.

Política de reprogramación:
- Hasta 24hs antes del Zoom: la movemos libre y sin costo.
- Con menos de 24hs: tenés UNA reprogramación de cortesía sin cargo.
- A partir de la segunda inasistencia o cancelación tardía: la reagendada queda sujeta a disponibilidad y puede tener cargo.

Nos vemos el {{horario_corto}}. Cualquier cosa antes, escribime por acá.
```

---

## 5) Recordatorio 24h antes del Zoom

Automatizable o manual. Objetivo: bajar tasa de no-show, recordar form si no lo completó, recordar qué traer.

```
¡Hola {{nombre}}! Recordatorio: mañana {{horario}} es el Zoom con {{nombre_dueno}}.

Link: {{link_zoom}}

Tres cosas rápidas:
1) Si todavía no completaste el formulario de 5 preguntas, hacelo cuando puedas: {{link_form}} — le permite a {{nombre_dueno}} arrancar la reunión yendo directo a lo tuyo.
2) Tené el link o foto de {{producto}} a mano, más el presupuesto que tenés pensado.
3) Si surgió algo y necesitás moverlo, contame hasta el final del día de hoy y lo reacomodamos sin drama (dentro de la política de reprogramación que te pasé).

Estamos listos. Hablamos mañana.
```

---

## 6) Recordatorio 1h antes del Zoom

Último empujón. Objetivo: que el cliente esté frente a la compu en hora.

```
¡{{nombre}}! En 1 hora arrancamos.

Link de Zoom: {{link_zoom}}

{{nombre_dueno}} te espera a las {{hora_exacta}}. Si por algo se te complica entrar en hora, mandame un mensaje corto y lo resolvemos.
```

---

## 7) Mensaje post-Zoom con propuesta de servicio full + agradecimiento

Inmediatamente después del Zoom (mismo día o máx 24hs hábiles). Objetivo: entregar lo prometido (PDF + grabación), agradecer, y abrir la puerta —sin presionar— al servicio 360 de importación full.

```
{{nombre}}, gracias por el Zoom de hoy con {{nombre_dueno}}. Quedó una buena charla.

Como te adelantó, te paso todo lo que cerramos:

1) Grabación de la reunión: {{link_grabacion}}
2) PDF resumen + checklist semana por semana + plantilla en inglés para fábricas: {{link_pdf}}

Repasalo con calma esta semana. Si te surgen dudas releyendo el material, escribime por acá y las contestamos sin problema — ese soporte está incluido.

Una cosa más, sin chamuyo:

Si después de revisar el plan te das cuenta de que preferís NO hacer la operación solo y querés que nos hagamos cargo nosotros (control en origen en China, despacho, costos finales y gestión documental — los 4 pilares del servicio full que vieron en el Zoom), me avisás y te pasamos por mail una cotización para tu caso puntual de {{producto}}. Cero presión, cero seguimiento agresivo: si me decís que sí, te armamos la propuesta; si no me decís nada, no te volvemos a tocar el tema.

Lo que sí o sí va a pasar es que la primera importación, la hagas con nosotros o solo, te va a salir mucho más limpia que sin el plan que armaron hoy.

Cualquier cosa, acá estoy. Y la mejor para vos y para {{producto}}.
```

---

## 8) Recovery — Pagó y NO mandó comprobante (proactivo a las 2hs)

Caso: alguien tocó "Pagar" en MP, el pago se acreditó (webhook IPN dispara), pero nunca llegó el comprobante al WhatsApp. **Primer contacto proactivo a las 2 horas del pago acreditado, dentro de horario hábil** (alineado con FUNNEL.md sección 4.3 — no esperar al día siguiente).

> **Pre-requisito operativo:** este script asume que tenemos el teléfono del cliente vía el `payer` de Mercado Pago. Si MP no entregó número (el payer no lo cargó), este recovery proactivo por WA es imposible — el único canal garantizado es el email automático que dispara el webhook (FUNNEL.md sección 3.4). Documentar caso por caso.

```
¡Hola! Soy {{nombre_operador}}, del equipo de asesoramiento de importación de China de {{nombre_dueno}}.

Me figura que hace un rato hiciste el pago por Mercado Pago de la reunión 1:1 (ARS 29.000), pero todavía no nos llegó tu comprobante por acá para activar la reunión y coordinar el horario.

¿Pudiste verlo? Capaz se te pasó el paso de mandarlo o tuviste algún tema con WhatsApp. Para activarte necesito:

1) Captura del comprobante de Mercado Pago (en MP → Actividad → tocás el pago → Compartir comprobante).
2) Tu nombre, email y qué producto querés importar (1 línea de cada uno me alcanza).

Si tuviste algún problema con el pago, o si querés que te devolvamos la plata porque ya no es para vos, decímelo derecho y lo resolvemos en el momento. Sin vueltas.

Quedo atento.
```

> **Si el pago entró fuera de horario hábil** (ej: sábado 22hs, domingo, feriado): el primer contacto se hace al inicio del siguiente día hábil, antes de las 10hs. En paralelo, el email automático de respaldo ya salió desde el webhook a los 5-10 min del pago, así que el cliente NO está sin novedades.

---

## 9) Reagendamiento — No pudo asistir al Zoom (no-show)

Caso: pasó la hora del Zoom y el cliente no entró. Tono: empático, sin culpa, asumiendo que pasó algo. Objetivo: reagendar rápido sin perder la venta, dejando clara la política.

```
¡Hola {{nombre}}! {{nombre_dueno}} te esperó hoy a las {{horario}} en el Zoom pero no llegaste a entrar.

Imagino que se te complicó algo de último momento — pasa. Te quería avisar tres cosas:

1) Tu reunión sigue activa, no perdiste nada. La movemos para cuando puedas.
2) Te tiro 3 nuevas opciones de horario para esta semana y la próxima:
   - Opción A: {{opcion_1}}
   - Opción B: {{opcion_2}}
   - Opción C: {{opcion_3}}
3) Si ninguna te sirve, decime 2 o 3 ventanas tuyas y lo acomodo.

Por política, esta primera reagendada va de cortesía. Si me confirmás un nuevo horario en las próximas 48hs lo cerramos sin más vuelta. Si más adelante hubiera una segunda inasistencia sin aviso, ahí la reagendada ya quedaría sujeta a disponibilidad y puede tener cargo.

Acá estoy cuando puedas.
```

---

## 10) Reembolso pre-Zoom — El cliente se arrepiente antes de la reunión

Caso: el cliente pagó, recibió la confirmación, pero antes del Zoom escribe para cancelar y pedir reembolso (cambio de opinión, urgencia personal, decidió no importar, etc.). Tono: nada de retención forzada — devolvemos limpio, dejamos la puerta abierta. La política es generosa porque la reputación vale más que ARS 29.000.

```
{{nombre}}, sin drama. Procesamos el reembolso del 100%.

Te confirmo el proceso:

1) Hoy mismo (dentro de las próximas 24hs hábiles) lo proceso desde Mercado Pago.
2) La acreditación en tu cuenta depende del medio de pago que usaste:
   - Si pagaste con saldo de Mercado Pago: lo ves casi al instante.
   - Si pagaste con tarjeta de débito o crédito: la acreditación a tu tarjeta puede tardar hasta 5-7 días hábiles según el banco (es el tiempo que tarda la red de tarjetas, no nosotros).
   - Si pagaste por transferencia: en 24-48hs hábiles.

Te aviso por acá en cuanto lo cierre de mi lado, así te queda registro.

Si más adelante cambia tu situación y querés retomar, escribime y reactivamos sin tener que pagar de nuevo durante los próximos 90 días. Y si simplemente cerramos el tema, también está perfecto — gracias por avisar en lugar de dejarlo colgado.
```

---

## 11) Activación de garantía 15 min — DURANTE el Zoom el cliente dice "no me sirve"

Caso: en los primeros 15 minutos del Zoom el cliente activa la garantía (es la promesa del hero). Objetivo: cerrar la llamada con dignidad para ambos lados y confirmar el reembolso por escrito en WhatsApp **el mismo día**. El proceso operativo está atado a FUNNEL.md sección 4.5.

```
{{nombre}}, como te confirmamos en el Zoom: activamos la garantía de 15 min, no hay nada que aclarar.

Cierro el proceso:

1) Hoy mismo, {{nombre_dueno}} dio el OK y yo proceso el reembolso del 100% (ARS 29.000) desde Mercado Pago en las próximas 24hs hábiles.
2) La plata se acredita en tu cuenta según el medio que usaste:
   - Saldo de Mercado Pago: casi instantáneo una vez procesado.
   - Tarjeta de débito o crédito: hasta 5-7 días hábiles según banco (tiempo de la red de tarjetas, no nuestro).
   - Transferencia: 24-48hs hábiles.

Te paso captura cuando lo cierre, así te queda registro.

Te deseo lo mejor con {{producto}}, en serio. Si en algún momento querés cruzar consultas puntuales por acá, escribime — sin compromiso.
```

---

## 12) Reprogramación tardía — Pide mover el Zoom con <24hs

Caso: el cliente pide reprogramar con menos de 24hs de anticipación. Política según FUNNEL.md sección 4.4: una reprogramación de cortesía; segunda con cargo. El operador tiene que dejar la política clara sin sonar a multa.

```
¡Hola {{nombre}}! Tranquilo, lo movemos.

Esta primera reprogramación con menos de 24hs va de cortesía (no hace falta que pagues nada extra). Si más adelante volviera a pasar una segunda vez con poca antelación, ahí ya tendríamos que ver costo extra o sujetarlo a la agenda disponible — te lo cuento ahora para que quede claro y no te llegue de sorpresa.

Te tiro 3 opciones nuevas para esta semana y la próxima:
- Opción A: {{opcion_1}}
- Opción B: {{opcion_2}}
- Opción C: {{opcion_3}}

Decime cuál te queda mejor o pasame 2-3 ventanas tuyas si ninguna sirve.
```

---

## 13) Consulta por servicio 360 ANTES del Zoom — redirección

Caso: el cliente, antes de la reunión, pregunta por la cotización del servicio 360 (importación full). Es tentador venderlo ya, pero rompe la promesa "los 60 min del Zoom son tuyos, sin venta encima" y baja la calidad de la reunión. Hay que redirigir cálido pero firme: primero el Zoom, después el servicio 360 por mail si el cliente lo pide.

```
¡Buena pregunta {{nombre}}! Te respondo en orden:

El servicio 360 (control en origen en China, despacho, costos finales y gestión documental) existe y se lo armamos a la medida de cada operación — por eso no hay un precio de tabla, depende de tu producto, volumen y forma de pago.

Lo que te propongo es esto: vamos primero al Zoom con {{nombre_dueno}}, donde te muestra el plan completo y vos ves si te conviene hacerlo solo o con nosotros. Si después de esa charla querés cotización del 360 para {{producto}}, me lo decís y te la pasamos por mail dentro de las 48hs hábiles. Si te das cuenta que preferís hacerlo solo con el plan que armamos, también está perfecto — el Zoom es tuyo y no te vamos a empujar nada durante la reunión.

¿Te parece? ¿Cerramos el horario del Zoom?
```

---

## 14) Calificación pre-pago — Consulta por rubros borde antes de pagar

Caso: alguien escribe ANTES de pagar para preguntar si la reunión aplica a su rubro / país / situación. Especialmente importante para rubros con regulación específica (alimentos, medicamentos, electrónica con homologación, juguetes con certificación, cosmética, productos infantiles). Mejor calificar honesto pre-pago que reembolsar post-pago.

```
¡Hola! Soy {{nombre_operador}}, del equipo de {{nombre_dueno}}. Te respondo derecho:

La reunión 1:1 está pensada para importadores PYME que arrancan desde Argentina. {{nombre_dueno}} tiene oficina propia en BA, China y Miami, y la mayor parte de las consultas que resolvemos son sobre indumentaria, accesorios, deco, herramientas, electrónica de consumo (sin homologación ENACOM compleja) y rubros similares.

Hay rubros donde la asesoría es más limitada porque hay regulación específica argentina que requiere despachante y trámites separados antes de mover mercadería:
- Alimentos, suplementos y bebidas (ANMAT / SENASA)
- Medicamentos y dispositivos médicos (ANMAT)
- Cosmética con principios activos (ANMAT)
- Productos infantiles y juguetes con certificación obligatoria
- Electrónica con homologación ENACOM (routers, equipos RF)

En esos rubros igual podemos charlar, pero te lo cuento antes para que no te lleves una sorpresa: vas a salir del Zoom con el plan logístico y de costos, pero NO con la habilitación regulatoria resuelta (eso necesita despachante + organismo).

¿Tu producto cae en alguno de esos rubros, o es uno de los de mayor volumen? Contame y te digo derecho si te conviene reservar la reunión o no.
```

---

## 15) Disculpa por SLA roto — Pasaron >30 min sin respuesta

Caso: por la razón que sea (volumen alto, persona fuera de horario en horario operativo, error operativo), pasaron más de 30 minutos desde que llegó el comprobante y el cliente todavía no recibió la primera respuesta. La promesa de "<30 min" está en hero, FAQ y Thank You — romperla genera ansiedad y dispara reclamos. Hay que reconocer rápido y compensar.

```
{{nombre}}, antes que nada: perdón por la demora.

Te prometimos respuesta en menos de 30 min en horario hábil y hoy no lo cumplimos. Reconocérselo es lo mínimo.

Recibí tu comprobante y ya está en verificación con Mercado Pago. En los próximos 10 minutos te confirmo pago OK y te tiro 3 opciones de horario para que arranquemos a coordinar el Zoom con {{nombre_dueno}}.

Como gesto por la demora, sumamos a tu reunión 15 minutos extra de soporte por WhatsApp sin cargo durante las 2 semanas posteriores al Zoom (más allá del soporte que ya viene incluido), para revisar cotizaciones, ayudarte a leer un PI que te manden o cualquier duda específica que te aparezca implementando.

Otra vez, perdón. Ya te escribo con la confirmación.
```

---

## Notas internas para el operador

- **Identidad del operador:** WhatsApp lo opera siempre el equipo, NO el dueño en primera persona. Esto está alineado con FUNNEL.md 4.1 y resuelve la disonancia previa donde el script firmaba como "soy {{nombre_dueno}}" mientras el FUNNEL decía explícitamente que no. La autoridad del dueño se preserva al aparecer recién en el Zoom.
- **Velocidad de respuesta inicial (Script 2):** ideal <30 min **dentro de horario hábil** (lun a sáb, 9 a 21hs hora Argentina). Esto está prometido en la Thank You y en el hero — romperlo dispara el Script 15. Configurar en WhatsApp Business un mensaje de bienvenida automático FUERA de horario que diga "Recibimos tu mensaje. Te respondemos mañana al abrir, antes de las 10hs" para bajar ansiedad sin romper la promesa.
- **Cero chatbot visible:** la landing dice "te atiende una persona del equipo, no un bot". Las plantillas son punto de partida — personalizar siempre con 1-2 líneas específicas del producto/rubro del cliente. Evitar lenguaje robótico de plantilla pegada.
- **Recovery proactivo (Script 8):** primer contacto a las **2 horas** del pago acreditado (no al día siguiente). Si el pago entró fuera de horario hábil, el contacto se hace al inicio del siguiente día hábil antes de las 10hs. El email automático de respaldo del webhook (FUNNEL.md 3.4) ya cubrió el hueco temporal.
- **No-show >1 vez:** si el cliente reagenda y vuelve a no aparecer sin avisar, mandar el Script 9 una vez más; si vuelve a fallar, ofrecer reembolso del 100% antes que dejar el caso colgado. Mejor cerrar limpio que arrastrar.
- **Reembolso (garantía 15 min y reembolso pre-Zoom):** procesar desde MP en <24hs hábiles. **Comunicar siempre que la acreditación a tarjeta puede tardar 5-7 días hábiles** según banco — es la red de tarjetas, no nosotros. Nunca decir "te llega en 24-48hs" sin esa aclaración: si el cliente paga con tarjeta y se demora la acreditación, reclama en Defensa al Consumidor y tiene razón porque la promesa fue ambigua.
- **Aprobación de reembolsos:** confirmación del dueño en el momento por WA al cliente ("listo, lo cierro"); el operador procesa en MP en <24hs hábiles; se manda captura de confirmación del procesado al cliente para que tenga registro escrito.
- **Pitch del servicio 360 (Script 7):** NUNCA durante el Zoom. Solo en el mensaje post-reunión y solo una vez. Si el cliente no responde, no insistir. Si pregunta ANTES del Zoom, usar Script 13 (redirección cálida al Zoom primero).
- **Política de reprogramación (Scripts 4, 9, 12):** hasta 24hs antes sin costo; con <24hs UNA reprogramación de cortesía; segunda con cargo o sujeta a disponibilidad. Esta política está documentada en FAQ de la landing y en Script 4 — el operador la repite en Script 12 sin sonar a multa.
- **Calificación de rubros borde (Script 14):** mejor decir que no antes del pago que reembolsar después. Costo de oportunidad bajo vs. costo de reputación alto.
- **Cuando MP no provee teléfono del payer:** el recovery proactivo por WhatsApp no es posible — el único canal garantizado es el email automático del webhook. Documentar caso por caso en el CRM/planilla operativa.
