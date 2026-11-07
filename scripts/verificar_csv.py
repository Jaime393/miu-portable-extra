#!/usr/bin/env python3
"""Verifica los CSV de citas de miu-portable-extra: solo mide.

Recorre los 96 archivos CSV del repo (6 en la raiz y 90 en citas/),
comprueba que la cabecera sea la de 7 columnas y reporta el conteo
de filas de datos por archivo. No afirma nada por adelantado: su
salida es el conteo medido.

Cabecera de referencia, segun MINERIA.md, seccion 1.3 (8 archivos
muestreados y leidos enteros):
    tema, autor_anio, titulo, venue, doi_isbn, hallazgo_clave,
    relevancia_gap_miu

Uso:
    python3 scripts/verificar_csv.py [--root DIR] [--salida RUTA]

Sin argumentos, toma como raiz del repo el directorio padre de
scripts/ (la ubicacion de este archivo dentro del repo).
La salida es un CSV con columnas: archivo, cabecera_ok,
cabecera_encontrada, filas_datos. La ultima fila es el total.
Solo usa la biblioteca estandar. No toca red.
"""

import argparse
import csv
import sys
from pathlib import Path

CABECERA_ESPERADA = [
    "tema",
    "autor_anio",
    "titulo",
    "venue",
    "doi_isbn",
    "hallazgo_clave",
    "relevancia_gap_miu",
]


def medir_csv(ruta):
    """Devuelve (cabecera_encontrada, cabecera_ok, filas_datos)."""
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        try:
            cabecera = next(lector)
        except StopIteration:
            return [], False, 0
        filas = sum(1 for _ in lector)
    return cabecera, cabecera == CABECERA_ESPERADA, filas


def main():
    parser = argparse.ArgumentParser(
        description="Mide cabecera y filas de datos de los CSV de citas."
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Raiz del repo (por defecto: padre de scripts/).",
    )
    parser.add_argument(
        "--salida",
        default=None,
        help="Ruta del CSV de salida (por defecto: stdout).",
    )
    args = parser.parse_args()

    raiz = Path(args.root) if args.root else Path(__file__).resolve().parent.parent
    archivos = sorted(raiz.glob("*.csv")) + sorted((raiz / "citas").glob("*.csv"))

    filas_salida = []
    total_filas = 0
    for ruta in archivos:
        cabecera, ok, n = medir_csv(ruta)
        total_filas += n
        filas_salida.append(
            {
                "archivo": str(ruta.relative_to(raiz)),
                "cabecera_ok": "si" if ok else "no",
                "cabecera_encontrada": ",".join(cabecera),
                "filas_datos": n,
            }
        )
    filas_salida.append(
        {
            "archivo": "TOTAL",
            "cabecera_ok": "",
            "cabecera_encontrada": "",
            "filas_datos": total_filas,
        }
    )

    campos = ["archivo", "cabecera_ok", "cabecera_encontrada", "filas_datos"]
    destino = open(args.salida, "w", newline="", encoding="utf-8") if args.salida else sys.stdout
    try:
        escritor = csv.DictWriter(destino, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas_salida)
    finally:
        if args.salida:
            destino.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
