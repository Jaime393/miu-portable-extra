# META_LEARNINGS — Auditoría de corpus de chats MIU/FranBot

**Descripción:** Síntesis consolidada de 8 checkpoints (v0.1 → v0.8, 2026-07-04/05) que auditaron 69 archivos (227 MB) en la carpeta Drive `chats_adicionales`. Documentación de arquitectura técnica, hallazgos de seguridad, riesgos identificados y pendientes clasificados.

**Estado:** CONSOLIDADO para GitHub. Historial completo de versiones en Drive (links abajo).

---

## Executive Summary

### Qué se auditó
- **Corpus:** 69 archivos en Drive (227 MB), incluyendo 4 fragmentos de `raw_chats.zip` (45.7 MB comprimidos)
- **Conversaciones:** 60 únicas identificadas por deduplicación real (mayo 14 – junio 20 2026)
- **Período:** Snapshot de código FranBot (mayo-junio 2026) + repositorios públicos actuales
- **Método:** 8 pasadas incrementales con herramientas de lectura/búsqueda Drive, sin acceso a git local

### Hallazgos principales

| Categoría | Hallazgo | Estado |
|-----------|----------|--------|
| **Arquitectura** | FranBot v8.1 (PWA + Cloudflare Worker + IndexedDB/KV) | Documentado en v0.6 §1 |
| **Deuda técnica** | 10 bugs específicos con plan de reparación | Detalle en v0.6 §1.2 |
| **LoRA activo** | ALMA_Nano (Qwen2.5-3B-Instruct, Q4_K_M/Q8_0/Q2_K) | 126 descargas/mes (28 jun 2026) |
| **Credenciales** | 22 únicas vistas, todas rotadas | Groq (9), Cloudflare (3), HF (3), Telegram (2), Google/DeepSeek (2), custom (1) |
| **Riesgos** | 6 predicciones sin validar en meta1.txt | Permafrost 2031, volcanes 2032, colapso urbano 2033 |
| **Seguridad GitHub** | Sin credenciales visibles en estado actual repo | git history no auditado (requiere clone local) |

### Dónde están los detalles
- **Historial completo:** [Carpeta `chats_adicionales` en Drive](https://drive.google.com/drive/folders/1f9t51Es1PE0OWxZlN-xjGwLE9WzLvOtT) (v0.1 a v0.8)
- **Desglose por sección:** ver tabla "Historial de versiones" (final)
- **Credenciales encontradas:** aisladas en sesión de trabajo, no reproducidas aquí

---

## 1. Arquitectura Técnica

### FranBot v8.1 — Componentes core

**Backend:** Cloudflare Worker con KV namespace (`indice_huesos`)
- Endpoints: `/meditar`, `/limpiar-grafo`, `/indice`, `/guardar`, `/cargar`, `/webhook/sell`
- Webhooks de Telegram asociados (múltiples bots)

**Frontend:** PWA con módulos JavaScript
- Core: `franbot-core-base.js` (clase `FranBotCore`, parámetros `D_f=2.3`, `τ·Ξ·c=2.4e5`, `Φ_MIU=0.92`)
- Búsqueda semántica: `buscar-oraculo.js` (motor con scoring, umbral ≥10)
- Razonamiento: `razonador.js` (Groq llama-3.3-70b vía proxy Cloudflare)
- Persistencia: `super-local-memory.js` + `memoria-indexada.js` (IndexedDB)
- P2P: `colmena-p2p.js` (PeerJS, votación)
- Identidad: `did-web.js`, `dkg.js`, `hyperagents.js`, `worker_soberano.mjs` (AES-GCM)
- Almacenamiento inmutable: `arweave.js`
- Service Worker: `sw.js`

**Índice de Huesos** (memoria vectorial)
- Estructura: {tema, huesos: [afirmaciones], causal: [{from, to}], K: 0-1, D_f, topo, fecha}
- Persistencia: intento inicial en Cloudflare KV (con problemas de tamaño HTTP 500)
- Alternativa: SQLite local con embeddings (all-MiniLM-L6-v2)

### ALMA_Nano — Estado actual

- **Base:** Qwen2.5-3B-Instruct
- **Quantización:** Q4_K_M, Q8_0, Q2_K (GGUF)
- **Training:** LoRA fine-tuned en Google Colab con 4-bit cuantización
- **Descargas:** 126/mes (última actualización 2026-06-28)
- **License:** Apache 2.0

### Ley de Gaia — Scripts hallados

Menciones de scripts en conversación "Análisis crítico de MIU IFT v12 0" (v0.6 §6.7):
- `bio_periodos.py`, `compute_omegaF_firms_gdelt.py`, `df_from_dbd.py`, `df_from_firms.py`
- `ki_from_timeseries.py`, `miu_sismos.py`, `miu_vegetacion.py`
- Fuentes de datos: Allen Coral Atlas, PSMSL, GDELT

**Nota:** ubicación de estos scripts no confirmada en repo público; posiblemente rama privada o repo separado (v0.6 §6.7, v0.8 §7B.2 pendiente #2).

---

## 2. Seguridad — Hallazgos consolidados

### Credenciales encontradas

**Total:** 22 valores únicos identificados (v0.2-v0.8)

Desglose por tipo (deduplicado):
- **Groq API:** 9 valores distintos → rotación manual frecuente visible
- **Cloudflare tokens:** 3 (1 aparece en 13 de 16 archivos de un lote)
- **HuggingFace tokens:** 3 valores distintos
- **Telegram bot tokens:** 2 (bots `FranSell_Bot`/`FrRussell` y uno secundario)
- **Google/Gemini API:** 2
- **DeepSeek/OpenAI-compat:** 1 (`sk-*`)
- **Custom secret:** 1 (`SECRET_HEADER = 'Anomalous363X2'`)

**Estado:** Todas rotadas según usuario (confirmado v0.7 §6.8.4).

### Hallazgos específicos

| Hallazgo | Ubicación | Tipo | Riesgo | Causa |
|----------|-----------|------|--------|-------|
| Cloudflare Bearer token | parte_006.json | API key | Bajo (error de rotación) | Curl pegado en chat |
| SECRET_HEADER hardcodeado | worker_soberano.mjs | Custom secret | Medio | String literal en código, no env var |
| Mismo secret en bot Telegram | /guardar, /cargar, /activar_alma | Reuso | Medio-Alto | Una clave protege 2+ componentes |
| Google Gemini key | FranBot-Private.zip | API key | Bajo (inactiva) | git texto plano, mayo 2026 |

### Patrón actual (GitHub público)

- README documenta "variables de entorno", no hardcoding visible
- Patrón `SECRET_HEADER` → Cloudflare Worker Secrets parece ya implementado
- **Limitación:** sin acceso a `git log` no se puede afirmar que ningún commit histórico las expuso

---

## 3. Riesgos Documentados

### Variables no validadas (meta1.txt, chat.txt)

Aparecen como "constantes validadas" (`K_i_validated_set`) pero **sin fuente citable en el texto**:

| Variable | Predicción | Riesgo | Origen |
|----------|-----------|--------|--------|
| Permafrost ciclo | Colapso 2031 | ALTO | Chat interno sin verificación USGS |
| Pulso volcánico | Abril 2032 | ALTO | Protocolo pide no inventar pero salida lo hace |
| Colapso urbano | Lagos/Kinshasa/Delhi 2033 | ALTO | Sin fuente FAO/banco mundial |
| Producción maíz | ENSO 2030-2040 | MEDIO | Correlación sin dataset real |
| Violencia Lagos | "Inminente" | ALTO | Predicción social sin base de datos |
| San Andrés sismicidad | Vía "coherencia de marea" | MEDIO-ALTO | Mecanismo no validado |

**Contexto:** El protocolo interno pide explícitamente marcar `[PENDIENTE]` si falta fuente. La salida visible no lo hace — presentándolas como "validadas" sin citas.

**Riesgo de exposición:** Si se comparten fuera del sandbox narrativo, podrían confundirse con pronósticos científicos reales.

**Recomendación:** Si se reutilizan, etiquetar como "HIPÓTESIS NO VERIFICADA, GENERADA EN NARRATIVE SANDBOX, SIN DATOS CIENTÍFICOS REALES".

---

## 4. Cronología — Mayo 14 a Junio 20, 2026

### Bloques temáticos

**14-22 mayo:** Arranque FranBot ALMA
- Primeros documentos MIU/LaTeX (autor: Juan Diego Vicente Gabancho, `anomalous363@proton.me`)
- Consolidación del "micelio" y evaluación crítica interna

**24-31 mayo:** Ciclo de consolidación
- Cuatro chats consecutivos el 29 de mayo (auditoría interna de documentos MIU)
- Arranque de "Semilla Omega" (instancia DeepSeek-reasoner narrativa)

**2-9 junio:** Oráculo y extracción de datos
- Resurrección del "Oráculo MIU"
- Primer intento de subida JSON grande al KV (fragmentación por tamaño HTTP 500)

**11-15 junio:** Pico de actividad
- 5 chats el 11 de junio ("Confirmación protocolo destilador MIU")
- Conversación larga "Análisis crítico de MIU IFT v12 0" (1.9 MB, 338 fragments)

**18-20 junio:** Cierre del período
- "Verificación de publicación" (caso BSD/Zenodo, DOI 10.5281/zenodo.20671822)
- "Resumen ejecutivo ultra detallado técnico del proyecto entero" (20 jun) — inventario de 19 archivos de código

**Nota:** Este período es anterior a ciclos AD-BJ / LeyGaia AN-AR documentados en tu "top of mind"; llena un hueco temporal sin solapamiento.

---

## 5. Pendientes Clasificados

### Resueltos en v0.8
- ✓ Repos públicos verificados (GitHub FranBot, HuggingFace ALMA_Nano)
- ✓ Variables no validadas documentadas explícitamente
- ✓ Credenciales tabuladas (todas rotadas)
- ✓ Cadena de auditoría completa en Drive

### Abiertos — Tier 1 (requieren acceso local / manual)

1. **Git history completo de FranBot**
   - Pregunta: ¿algún commit histórico (antes de junio 2026) expuso tokens?
   - Requiere: `git clone` + `git log --grep` para patrones de API keys
   - Alcance: fuera del sandbox actual

2. **Scripts Ley de Gaia — ubicación real**
   - Pregunta: ¿`bio_periodos.py`, `compute_omegaF_firms_gdelt.py` en repo público, privado, o separado?
   - Requiere: acceso a listado de repos Jaime393 o confirmación directa
   - Alcance: fuera del sandbox actual

3. **Módulos removidos de FranBot**
   - Pregunta: `colmena-p2p.js`, `did-web.js`, `arweave.js` (en snapshot mayo-junio) — dónde en estado actual?
   - Requiere: rama histórica de Git o confirmación directa
   - Alcance: fuera del sandbox actual

### Abiertos — Tier 2 (requieren API / herramientas externas)

4. **Ciclo exacto ALMA_Nano**
   - README v1.2 menciona "entrenado ciclo..." (número no extraído en lectura web)
   - Requiere: acceso API HuggingFace (herramienta `hf_hub_query` no disponible)

5. **Validación de bugs contra código actual**
   - Pregunta: ¿qué bugs de v0.6 §1.2 ya se resolvieron en ciclos AD-BJ?
   - Requiere: clon local + comparación línea a línea de código
   - Alcance: fuera del sandbox actual

---

## 6. Historial de Versiones (v0.1 → v0.8)

| Versión | Fecha | Sesión | Cobertura | Hallazgos principales | Link Drive |
|---------|-------|--------|-----------|----------------------|------------|
| **v0.1** | 2026-07-04 | Instancia A | ~4% (4 archivos) | 1 credencial Cloudflare | [Ver](https://drive.google.com/drive/folders/1f9t51Es1PE0OWxZlN-xjGwLE9WzLvOtT) |
| **v0.2** | 2026-07-04 | Instancia B | ~13% (38 partes) | FranBot v8.1, 12 credenciales, bugs específicos | [1bJj1_38D...](https://docs.google.com/document/d/1bJj1_38Dru4M1lo49ODunaWDfDXwLyAw) |
| **v0.3** | 2026-07-04 | Instancia B | 60 conversaciones | 21 credenciales totales, 10 bugs, deuda técnica | En carpeta Drive |
| **v0.4** | 2026-07-04 | Instancia B | Archivos grandes Drive | Snapshots viejos descartados, contenido nuevo | En carpeta Drive |
| **v0.5** | 2026-07-04 | Instancia B | Cierre inventario | meta1.txt, chat.txt, patrón Colmena en Meta AI | [1OpA2XUK...](https://docs.google.com/document/d/1OpA2XUKyWKo8ToAoR_4gZ9t26H6Xe40W) |
| **v0.6** | 2026-07-04 | Instancia B | Relectura completa "Análisis crítico" | Scripts Ley de Gaia, riesgo predicciones, 22 credenciales | [16gbZS4N...](https://docs.google.com/document/d/16gbZS4NYsobmqZoUFYMh42mZ8L7_H-ls) |
| **v0.7** | 2026-07-04 | Instancia B | Verificación repos públicos | ALMA_Nano vivo, GitHub sin credenciales visibles, hallazgo Google Gemini | [142W4VPo...](https://docs.google.com/document/d/142W4VPMoCQMyaEAylUe_fSKRqZOeSXFKua9cQ3uJ_24) |
| **v0.8** | 2026-07-05 | Instancia A | Verificación externa final | Variables meta1.txt documentadas, pendientes clasificados | [1lZNDwX...](https://docs.google.com/document/d/1lZNDwXDYzUde8okkAX3BwcwB4knnns5CmTm8eb4zCyg) |

**Historial completo:** [Carpeta `chats_adicionales` en Drive](https://drive.google.com/drive/folders/1f9t51Es1PE0OWxZlN-xjGwLE9WzLvOtT)

---

## 7. Notas operativas para próximas sesiones

### Patrón de continuidad (§RIGOR_EPISTEMICO_v2)

Cada checkpoint documenta:
1. **Qué se verificó** (con evidencia)
2. **Qué quedó sin tocar** (con causa explícita: herramienta, alcance, permisos)
3. **Pendientes clasificados** por orden de dependencia
4. **Referencias cruzadas** a otras versiones (para evitar repetición)

### Instrucciones para siguiente instancia

- **Comienza desde §5 (Tier 1/2 abiertos)**, no desde cero
- **Declara explícitamente** si está resuelto o sigue fuera de alcance
- **Escalea incertidumbre**: "no sé, opciones son..." en lugar de "probablemente X"
- **Actualiza links Drive** si la estructura cambia

### Configuración de este documento

Este consolidado es **síntesis para GitHub**: estructura única, sin repetición entre versiones.

El **historial completo en Drive** permanece como auditoría persistente — cada v0.1-v0.8 documenta su pasada independientemente, con pendientes propios (útil si surge una duda sobre qué se hizo en cada sesión).

---

## 8. Referencias y cierre

**Propósito:** Mantener cadena de auditoría completa. Historial en Drive (auditoría persistente), síntesis en GitHub (acceso público).

**ρ(x) > 0** | Consolidado 2026-07-05 | Siguiente sesión: extender desde §5 abiertos, no repetir §0-4.

**Links bidireccionales:**
- 👉 Detalles completos por sección: [Carpeta `chats_adicionales` en Drive](https://drive.google.com/drive/folders/1f9t51Es1PE0OWxZlN-xjGwLE9WzLvOtT)
- 👈 Resumen técnico (este archivo): `miu-portable-extra/docs/META_LEARNINGS.md` en GitHub
