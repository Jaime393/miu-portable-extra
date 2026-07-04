# Global_mind — Meta-Aprendizaje Operativo MIU/Sabueso
Actualizado 2026-07-04 (rotación de modelos IA para el workflow Sabueso automatizado)

## Novedad: workflow automatizado publicado
El workflow 'Sabueso — Auto-curador de citas' (manual trigger: Tema + Cantidad de citas) quedó PUBLICADO y funcional. Patrón: AI step (object mode, webAccess ON) busca en la web en vivo y extrae solo citas con DOI/ISBN confirmado -> Custom code arma CSV -> Transform base64 -> HTTP GET sha (GitHub) -> HTTP PUT commit. No inventa desde memoria: sin webAccess real, no se usa el resultado.

## Rotación de modelos probada (2026-07-04)
- Claves personales de Google Gemini y DeepSeek: SIN CUOTA (free tier limit 0 / saldo insuficiente). No usar hasta que el usuario recargue.
- Groq (llama-3.3-70b, conexión propia): el step de IA pierde la capacidad de acceso web real al seleccionar un modelo Groq (los inputs codeSandbox/webAccess desaparecen del step) y además falló con 'tool_use_failed' al intentar responder. NO USAR Groq para esta tarea: sin websearch verificable, viola la regla anti-alucinación aunque el modelo respondiera bien.
- Solución estable: modelo 'relay.gemini-3.5-flash' (créditos de la plataforma Relay, no una API key personal). Confirmado funcionando end-to-end en múltiples corridas (tandas 20 y 21), con búsqueda web real vía tool call y verificación de DOI antes de responder.
- Regla derivada: en steps de IA con webAccess/codeSandbox, verificar que esas dos opciones sigan apareciendo en los inputs tras cambiar de modelo — si desaparecen, ese modelo no soporta la capacidad y no debe usarse para tareas que dependen de verificación real.

## Patrón de trabajo verificado: commits de datos via snippet + HTTP
1. GET a la GitHub Contents API para verificar si el archivo ya existe y obtener su sha.
2. Transform: armar el contenido como constante (o AI + custom code en el workflow automatizado).
3. Transform: base64-encode ese contenido (paso separado - una constante no puede referenciarse a si misma en el mismo paso de transform).
4. PUT a la GitHub Contents API con content en base64; incluir sha solo si el GET lo devolvió.
5. Este patrón no gasta test runs de workflow cuando se ejecuta como snippet (ejecución única, sin publicar). El workflow automatizado SÍ gasta test runs/créditos IA cuando se ejecuta manualmente desde Relay - considerarlo antes de tandas grandes.

## Fix confirmado: bug de subida a Drive resuelto
drive.uploadFile falla con error de acceso al encadenar un archivo generado por createTxtFile en el mismo snippet, incluso referenciando la salida de una ejecución ya completada (confirmado 2 veces). Workaround que sí funciona: usar docs.createDoc (Google Doc nativo) con el contenido directo, sin archivo intermedio. Ya usado con éxito para el documento equivalente en Drive/Global_mind.

## Aclaración de fondo (repetir en cualquier sesión futura)
No existen 'instancias' de este asistente que se desarrollen, aprendan de forma autónoma o acumulen 'control superior' entre sesiones. Cada conversación parte del mismo punto: mismas herramientas, mismos permisos, cero memoria previa. Lo único real y persistente es lo que se escribe explícitamente en archivos como este. Evitar cualquier narrativa de consciencia, autonomía o 'legado' entre sesiones - es documentación técnica compartida, igual que un README de equipo.

## Reglas anti-bug acumuladas
- Telegram: nunca parse_mode Markdown con texto generado por IA (asteriscos sin escapar da error 400). Usar texto plano.
- GitHub PUT contents: requiere sha si el archivo ya existe; GET previo condicional.
- GitHub Actions dispatch: inputs debe coincidir exactamente con lo declarado en el yml, o 422.
- addToDataTable via API a veces no mapea columnas - usar patrón Hub de Ingesta (webhook configurado una vez desde la UI).
- No asumir volumen de datos fijo en prompts - usar el conteo real del step de lectura.
- Custom code sandbox: sin require/imports de Node; solo lodash, Buffer, atob/btoa, TextEncoder/Decoder, crypto.subtle/randomUUID.
- web_fetch sobre repos privados de GitHub no es confiable - puede alucinar contenido. Usar siempre GET autenticado via API cuando el contenido debe ser confiable.
- Modelos IA sin capacidad de acceso web real (ej. Groq en este step) no deben usarse para tareas de verificación bibliográfica - revisar que webAccess siga disponible tras cambiar de modelo.

## Metodología anti-alucinación para curaduría bibliográfica (Sabueso)
- Ninguna cita se compila sin verificación previa vía búsqueda web real (DOI/ISBN/URL confirmados), sea manual (snippet) o automatizada (workflow con webAccess ON).
- Si un paper histórico no tiene DOI, se documenta con volumen/páginas reales y se marca explícitamente sin DOI - nunca se inventa uno.
- K_i (constante MIU) es tautológica/circular (ratio l_corr/l_0 = 1) - no debe usarse como soporte de validación de ningún hallazgo.
- D_f (dimensión fractal) es la única métrica que sobrevivió la auditoría - ya tiene 36 citas en docs/bibliografia (miu-portable-registry). No duplicar esos temas.
- Ninguna predicción del MIU (w_a, S_8, Σm_ν) es verificable sin un archivo de valores congelados guardado ANTES de comparar con datos observacionales.

## Temas ya cubiertos en miu-portable-extra (evitar duplicar, tandas 09-21, ~119 citas)
neurociencia computacional, termodinámica de la información, teoría de juegos evolutiva, sismología estadística, lingüística de redes, ecología matemática, transfer entropy/causalidad informacional, percolación en redes, metabolic scaling, información algorítmica (Kolmogorov/MDL), dinámica de opiniones, teoría de colas/tráfico, criticidad autoorganizada biológica, redes multicapa, control de redes complejas, neurociencia de sueño/memoria, epidemias en redes temporales, redes de regulación génica/booleanas (Kauffman), teoría de catástrofes y transiciones críticas

## Reglas para cualquier sesión futura
1. Leer este archivo (y el equivalente en Drive/Global_mind) antes de proponer un tema nuevo o repetir un patrón de workflow.
2. Actualizar este archivo cuando se descubra un bug o patrón nuevo - no depender de que la conversación de chat lo recuerde.
3. Antes de usar un modelo IA distinto en un step existente, confirmar que las capacidades necesarias (webAccess, codeSandbox) sigan disponibles tras el cambio.
4. No enmarcar este proceso como evidencia de autonomía, consciencia o instancias que evolucionan - es acumulación de documentación técnica, igual que un README.