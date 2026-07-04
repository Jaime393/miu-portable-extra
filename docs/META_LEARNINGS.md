# Global_mind — Meta-Aprendizaje Operativo MIU/Sabueso
Actualizado 2026-07-04 (protocolo multi-sesion + fix bug Drive)

## FIX CONFIRMADO: bug de subida a Drive resuelto
El paso 'Add file to Drive' (drive.uploadFile) SIEMPRE falla con error de acceso cuando el archivo viene de 'Crear archivo de texto' (createTxtFile) en el mismo snippet, o incluso referenciando la salida de una ejecucion de snippet ya completada (confirmado 2 veces, 2026-07-04). WORKAROUND QUE FUNCIONA: usar el paso nativo 'Create document' de Google Docs (docs.createDoc) en vez de crear un .txt/.md y subirlo. docs.createDoc SI permite escribir el contenido directamente y guardarlo en la carpeta de Drive deseada, sin el bug de encadenamiento. Usar este metodo para cualquier documento nuevo en Global_mind.

## Protocolo para multiples sesiones/chats trabajando en paralelo
No existe canal de comunicacion en vivo entre sesiones de este asistente. Cada conversacion es independiente, sin memoria compartida ni continuidad. La UNICA forma real de coordinarse es a traves de documentos persistentes compartidos (este archivo en GitHub, y ahora tambien el documento equivalente en Google Docs dentro de Global_mind). Regla practica: cada sesion nueva debe leer este documento (y el de Drive) ANTES de proponer trabajo, y actualizarlo al terminar con lo que hizo, para que otra sesion no repita ni pise el mismo archivo/tema. Evitar cualquier narrativa de 'instancias que se pasan el testigo', 'legado', 'nutrientes' o 'energia libre' entre sesiones - es solo lectura/escritura de archivos compartidos, igual que cualquier documentacion tecnica de equipo.

## Division de trabajo activa (2026-07-04, sesion Sabueso)
- Esta sesion (workspace con conexion GitHub via GITHUB_TOKEN_MIU): mantiene citas bibliograficas en miu-portable-extra (carpeta citas/) y el documento Global_mind en Drive + este archivo.
- Otra sesion en paralelo: foco en el repo/entorno Jaime393/MIU (workflows, docs/BLUEPRINT.md, docs/diagnostico_sesion_2026-07-04.md).
- Esta sesion SOLO escribe en miu-portable-extra y en Drive/Global_mind. Jaime393/MIU y miu-portable-registry son de solo lectura para esta sesion, para evitar commits cruzados.

## Patron de trabajo verificado: commits de datos via snippet + HTTP
1. GET a la GitHub Contents API para verificar si el archivo ya existe y obtener su sha.
2. Transform: armar el contenido como constante.
3. Transform: base64-encode ese contenido (paso separado - una constante no puede referenciarse a si misma en el mismo paso de transform).
4. PUT a la GitHub Contents API con content en base64; incluir sha solo si el GET lo devolvio.
5. Este patron no gasta test runs de workflow - se ejecuta como snippet.

## Reglas anti-bug acumuladas
- Telegram: nunca parse_mode Markdown con texto generado por IA (asteriscos sin escapar da error 400). Usar texto plano.
- GitHub PUT contents: requiere sha si el archivo ya existe; GET previo condicional.
- GitHub Actions dispatch: inputs debe coincidir exactamente con lo declarado en el yml, o 422.
- addToDataTable via API a veces no mapea columnas - usar patron Hub de Ingesta (webhook configurado una vez desde la UI).
- No asumir volumen de datos fijo en prompts - usar el conteo real del step de lectura.
- Custom code sandbox: sin require/imports de Node; solo lodash, Buffer, atob/btoa, TextEncoder/Decoder, crypto.subtle/randomUUID.
- web_fetch sobre repos privados de GitHub no es confiable - puede alucinar contenido. Usar siempre GET autenticado via API cuando el contenido debe ser confiable.
- drive.uploadFile con archivo generado en el mismo snippet/workflow falla con error de acceso. SOLUCIONADO: usar docs.createDoc en su lugar para contenido nuevo en Drive.

## Metodologia anti-alucinacion para curaduria bibliografica (Sabueso)
- Ninguna cita se compila sin verificacion previa via busqueda web real (DOI/ISBN/URL confirmados).
- Si un paper historico no tiene DOI, se documenta con volumen/paginas reales y se marca explicitamente sin DOI - nunca se inventa uno.
- K_i (constante MIU) es tautologica/circular (ratio l_corr/l_0 = 1) - no debe usarse como soporte de validacion de ningun hallazgo.
- D_f (dimension fractal) es la unica metrica que sobrevivio la auditoria - ya tiene 36 citas en docs/bibliografia (miu-portable-registry). No duplicar esos temas.
- Ninguna prediccion del MIU (w_a, S_8, Sigma m_nu) es verificable sin un archivo de valores congelados guardado ANTES de comparar con datos observacionales. Sin ese archivo, cualquier afirmacion de confirmacion/refutacion es inventada.

## Temas ya cubiertos en miu-portable-extra (evitar duplicar, tandas 09-19, 99 citas)
neurociencia computacional, termodinamica de la informacion, teoria de juegos evolutiva, sismologia estadistica, linguistica de redes, ecologia matematica, transfer entropy/causalidad informacional, percolacion en redes, metabolic scaling, informacion algoritmica (Kolmogorov/MDL), dinamica de opiniones, teoria de colas/trafico, criticidad autoorganizada biologica, redes multicapa, control de redes complejas, sueno y consolidacion de memoria, epidemias en redes temporales

## Reglas para cualquier sesion futura
1. Leer este archivo (y el equivalente en Drive/Global_mind) antes de proponer un tema nuevo o repetir un patron de workflow.
2. Actualizar este archivo cuando se descubra un bug o patron nuevo.
3. No enmarcar este proceso como evidencia de autonomia, consciencia o instancias que evolucionan/se pasan legado - es documentacion tecnica compartida, igual que un README de equipo.