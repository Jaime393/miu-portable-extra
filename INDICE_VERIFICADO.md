# INDICE_VERIFICADO — Jaime393/miu-portable-extra

- Fuente: `~/workspace/mineria/miu-portable-extra/MINERIA.md`, Parte 1 EXPORTABLE, solo SÉ verificado con fuente.
- Fecha de lectura del borrador: 2026-11-07 ~18:45–18:48 -05.
- Método del borrador: solo lectura con `/opt/hatch/bin/github call-read-tool` (`search_repositories`, `list_commits`, `get_file_contents`, `list_issues`, `list_pull_requests`). Sin push, sin modificaciones.
- HEAD verificado: `2ab26175d50ff076889b3988bfd673adb60ea47b`.
- Este archivo es nuevo y aditivo. No modifica ni reemplaza ningún archivo existente del repo.

## 1. Identidad del repo

- Repo: `Jaime393/miu-portable-extra`, id 1288664424, público, no es fork, no está archivado, rama por defecto `main`. Fuente: `search_repositories` (2026-11-07).
- Creado 2026-07-03T20:48:21Z; actualizado 2026-07-10T05:29:24Z; 0 estrellas, 0 forks, 0 issues abiertas. Fuente: `search_repositories`.
- Último commit `2ab26175d50ff076889b3988bfd673adb60ea47b`, 2026-07-10T05:29:20Z, mensaje `docs: add README (auto-generado por Auditor de Integridad MIU)`, autor y committer `Jaime393`. Fuente: `list_commits` (primer resultado).
- Issues: 0 abiertas y 0 cerradas (`list_issues`, `totalCount: 0` en ambos estados). Pull requests: lista vacía en `list_pull_requests` estado `all`.

## 2. Inventario

- Total: **100 archivos** = 7 en raíz + 90 en `citas/` + 3 en `docs/`. No hay ningún otro directorio ni archivo en el listado de `get_file_contents` en raíz, `citas/` y `docs/`.
- Por tipo: **96 archivos CSV + 4 archivos Markdown** (README.md + 3 en `docs/`). En el listado completo de 100 rutas no aparece ningún archivo de código (`.py`, `.js`, `.ts`, etc.), ni `LICENSE`, ni `setup.py` / `pyproject.toml`, ni `requirements.txt`, ni directorio `src/`, `tests/`, `.github/` ni `examples/`.
- Tamaños sumados de los tamaños listados por la API: raíz 21.011 B + `citas/` 366.700 B + `docs/` 26.126 B = **413.837 B** en total.

### 2.1 Raíz (7 archivos)

| Archivo | Tamaño (B) |
|---|---|
| `CITATIONS_EXOTIC_3.csv` | 3.816 |
| `CITATIONS_EXOTIC_4.csv` | 2.989 |
| `CITATIONS_EXOTIC_5.csv` | 2.759 |
| `CITATIONS_EXOTIC_6.csv` | 2.865 |
| `CITATIONS_EXOTIC_7.csv` | 2.357 |
| `CITATIONS_EXOTIC_8.csv` | 1.944 |
| `README.md` | 5.281 |

### 2.2 `citas/` (90 archivos CSV, 366.700 B)

- 90 archivos, todos con extensión `.csv`, con fechas en el nombre del 2026-07-03 al 2026-07-07.
- 6 archivos con fecha 2026-07-03 y prefijo `auto-`, con los temas siguientes en los nombres: criticidad en sistemas económicos; redes adaptativas; redes de regulación génica / Kauffman; sincronización de osciladores / Kuramoto; teoría de catástrofes; grafos aleatorios / mundo pequeño.
- 84 archivos con `tanda-NN` en el nombre, con NN del 09 al 93.
- Números de tanda presentes en los nombres: 80 números distintos entre 09 y 93. Números del 01 al 93 ausentes en los nombres: 01, 02, 03, 04, 05, 06, 07, 08, 20, 21, 22, 23, 24 (13 números). Esta es una observación sobre nombres de archivo, no sobre contenido.
- Números de tanda con dos archivos en el nombre (4 casos):
  - tanda-34: `2026-07-04_tanda-34_motivos-red-biologia-sistemas.csv` y `2026-07-04_tanda-34_network-motifs.csv`
  - tanda-36: `2026-07-04_tanda-36_deteccion-comunidades-redes.csv` y `2026-07-04_tanda-36_deteccion-comunidades.csv`
  - tanda-49: `2026-07-05_tanda-49_criticidad-neural-avalanchas.csv` y `2026-07-05_tanda-49_reservoir-computing-borde-caos.csv`
  - tanda-89: `2026-07-06_tanda-89_entropia-entrelazamiento-criticidad.csv` y `2026-07-06_tanda-89_materia-activa.csv`
- El archivo con fecha de nombre más tardía es `citas/2026-07-07_tanda-93_redes-polinizacion.csv` (tanda-93); el otro archivo con fecha 2026-07-07 en el nombre es `citas/2026-07-07_tanda-91_envejecimiento-perdida-complejidad.csv` (tanda-91).
- La lista nominal completa de los 90 archivos de `citas/` no está en el borrador. Solo constan en el borrador los agregados de esta sección y los nombres de archivo listados aquí (los 4 pares duplicados, tanda-91 y tanda-93, y el archivo `auto-` de Kuramoto citado en §3). El detalle por tanda está en `citas/INDICE_TANDAS.csv`, con la columna de archivos vacía donde el borrador no da el nombre.

### 2.3 `docs/` (3 archivos Markdown, 26.126 B)

| Archivo | Tamaño (B) | Contenido verificado (lo que el archivo dice) |
|---|---|---|
| `docs/GAPS_REPORT.md` | 5.137 | Su primera línea dice: generado automáticamente el 2026-07-05 sobre 34 tandas de citas commiteadas en miu-portable-extra. Dice explícitamente que NO contiene citas nuevas ni hallazgos confirmados y que las brechas listadas llevan el nivel indicado en el propio documento. |
| `docs/META_LEARNINGS.md` | 8.075 | Encabezado: "Global_mind — Meta-Aprendizaje Operativo MIU/Sabueso", "Actualizado 2026-07-04". Contiene secciones sobre el workflow 'Sabueso — Auto-curador de citas', rotación de modelos probada, una conjetura Kuramoto marcada en el propio documento con su nivel, reglas anti-bug y metodología anti-alucinación para curaduría bibliográfica. |
| `docs/META_LEARNINGS_PARA_GITHUB.md` | 12.914 | Se describe a sí mismo como síntesis consolidada de 8 checkpoints (v0.1 → v0.8, 2026-07-04/05) que auditaron 69 archivos (227 MB) en la carpeta Drive `chats_adicionales`. Contiene secciones de arquitectura FranBot v8.1, seguridad, riesgos documentados, cronología mayo–junio 2026, pendientes clasificados e historial de versiones. |

## 3. Esquema de los CSV

- Los 8 archivos leídos completos comparten la misma cabecera de 7 columnas: `tema, autor_anio, titulo, venue, doi_isbn, hallazgo_clave, relevancia_gap_miu`.
- Archivos muestreados y filas de datos contadas con parseo CSV:
  - `CITATIONS_EXOTIC_3.csv`: 12 filas de datos
  - `CITATIONS_EXOTIC_4.csv`: 8 filas de datos
  - `CITATIONS_EXOTIC_5.csv`: 7 filas de datos
  - `CITATIONS_EXOTIC_6.csv`: 7 filas de datos
  - `CITATIONS_EXOTIC_7.csv`: 6 filas de datos
  - `CITATIONS_EXOTIC_8.csv`: 5 filas de datos
  - Total verificado de los 6 archivos exóticos: **45 filas de datos**.
  - `citas/2026-07-07_tanda-93_redes-polinizacion.csv`: 6 filas de datos (primera fila: Bascompte, Jordano, Melián & Olesen (2003), DOI 10.1073/pnas.1633576100).
  - `citas/2026-07-03_auto-sincronizacion-de-osciladores-acoplados-modelo-de-kuramoto.csv`: 6 filas de datos (primera fila: Acebrón et al., 2005, DOI 10.1103/RevModPhys.77.137).
- Los archivos exóticos llevan la cabecera entrecomillada (`"tema","autor_anio",...`); los dos archivos de `citas/` muestreados la llevan sin comillas. Diferencia de formato observada solo en esos 8 archivos.

## 4. README.md (leído entero, 5.281 B)

- El README dice de sí mismo, en sus primeras líneas, que fue redactado "utilizando inferencia razonable a partir del patrón del nombre del repositorio".
- Describe una estructura esperada con `src/`, `tests/`, `LICENSE`, `setup.py / pyproject.toml`, `requirements.txt`, `examples/` y `docs/API.md`. Ninguno de esos archivos o directorios aparece en el listado verificado de 100 archivos (ver §2).
- Contiene una lista de tareas pendientes sin marcar (revisar la descripción, documentar la estructura real, añadir instalación, ejemplos, API, tests, contribuciones, licencia, referencias cruzadas) y una nota final de generación automática como plantilla base.
- El último commit del repo es precisamente la adición de este README (2026-07-10T05:29:20Z, ver §1).

## 5. Totales

| Agrupación | Conteo |
|---|---|
| Archivos en total | 100 |
| En raíz | 7 |
| En `citas/` | 90 |
| En `docs/` | 3 |
| Archivos CSV | 96 |
| Archivos Markdown | 4 |
| Tamaño total | 413.837 B |
| HEAD | `2ab26175d50ff076889b3988bfd673adb60ea47b` |
