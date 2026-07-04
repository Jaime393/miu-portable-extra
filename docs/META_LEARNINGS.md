# Global_mind — Meta-Aprendizaje Operativo MIU/Sabueso
Generado por asistente Relay.app — 2026-07-04

## Nota de origen
Este archivo se subio a `docs/META_LEARNINGS.md` en `miu-portable-extra` (no en Google Drive/Global_mind) porque el paso nativo de subida a Drive fallo de forma reproducible al encadenar un archivo generado en el mismo snippet (bug reportado a Relay.app). El contenido y proposito son los mismos que se querian guardar en Global_mind.

## Proposito
No representa consciencia ni instancias que se desarrollan y aprenden de forma autonoma. Cada sesion del asistente parte sin memoria previa, con las mismas herramientas y permisos. Este archivo es el equivalente a BLUEPRINT.md: notas operativas para que la SIGUIENTE sesion no repita errores ni trabajo ya hecho. Es documentacion, no un cerebro que crece.

## Patron de trabajo verificado: commits de datos via snippet + HTTP
1. GET a la GitHub Contents API para verificar si el archivo ya existe (evita sobrescritura sin sha).
2. Transform: armar el contenido (CSV/texto) como constante.
3. Transform: base64-encode ese contenido (paso separado - una constante no puede referenciarse a si misma en el mismo paso de transform).
4. PUT a la GitHub Contents API con content en base64; incluir sha solo si el GET lo devolvio.
5. Este patron no gasta test runs de workflow - se ejecuta como snippet (ejecucion unica, sin publicar).

## Reglas anti-bug acumuladas
- Telegram: nunca parse_mode Markdown con texto generado por IA (asteriscos sin escapar da error 400). Usar texto plano.
- GitHub PUT contents: requiere sha si el archivo ya existe; GET previo condicional.
- GitHub Actions dispatch: inputs debe coincidir exactamente con lo declarado en el yml, o 422.
- addToDataTable via API a veces no mapea columnas - usar patron Hub de Ingesta (webhook configurado una vez desde la UI).
- No asumir volumen de datos fijo en prompts - usar el conteo real del step de lectura.
- Custom code sandbox: sin require/imports de Node; solo lodash, Buffer, atob/btoa, TextEncoder/Decoder, crypto.subtle/randomUUID.
- web_fetch sobre repos privados de GitHub no es confiable - puede alucinar contenido. Tratar como referencia, nunca como fuente verificada de datos criticos.
- drive.uploadFile con un archivo generado por createTxtFile en el mismo snippet falla con error de acceso (bug reportado, 2026-07-04). Workaround: usar el patron GitHub de este documento.

## Metodologia anti-alucinacion para curaduria bibliografica (Sabueso)
- Ninguna cita se compila sin verificacion previa via busqueda web real (DOI/ISBN/URL confirmados).
- Si un paper historico no tiene DOI, se documenta con volumen/paginas reales y se marca explicitamente sin DOI - nunca se inventa uno.
- K_i (constante MIU) es tautologica/circular (ratio l_corr/l_0 = 1) - no debe usarse como soporte de validacion de ningun hallazgo.
- D_f (dimension fractal) es la unica metrica que sobrevivio la auditoria - ya tiene 36 citas en docs/bibliografia (miu-portable-registry). No duplicar esos temas.

## Temas ya cubiertos en miu-portable-extra (evitar duplicar, tandas 09-19, 99 citas)
neurociencia computacional, termodinamica de la informacion, teoria de juegos evolutiva, sismologia estadistica, linguistica de redes, ecologia matematica, transfer entropy/causalidad informacional, percolacion en redes, metabolic scaling, informacion algoritmica (Kolmogorov/MDL), dinamica de opiniones, teoria de colas/trafico, criticidad autoorganizada biologica, redes multicapa, control de redes complejas, neurociencia de sueno/memoria, epidemias en redes temporales

## Reglas para cualquier sesion futura
1. Leer este archivo antes de proponer un tema nuevo o repetir un patron de workflow.
2. Actualizar este archivo cuando se descubra un bug o patron nuevo - no depender de que la conversacion de chat lo recuerde.
3. No enmarcar este proceso como evidencia de autonomia, consciencia o instancias que evolucionan - es acumulacion de documentacion tecnica, igual que un README.
