# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Windows desktop ETL tool (Tkinter dialogs, no main window) that loads a RUNT (Colombian vehicle registry) Excel export into SQL Server and updates license-plate data on the `Trackings` table of `dbVentasCorporativas`. Code, identifiers, docstrings, UI messages, and commit messages are in Spanish — keep that convention.

## Commands

```bash
pip install -r requerimientos.txt   # runtime deps (pandas, openpyxl, pyodbc, python-dotenv)
python carga_runt.py                # run from source (needs .env next to carga_runt.py)
build.bat                           # build dist\CargaRUNT.exe via PyInstaller (creates .venv-build on first run)
```

There are no tests, linter, or formatter configured. Running the app requires the Microsoft ODBC Driver 17 for SQL Server and access to the target database.

`.env` keys (read via `os.getenv` in `modelo/inserta_datos.py`): `SERVIDOR_DB`, `USUARIO_BD`, `CLAVE_BD`, `BD_VECORD`.

## Architecture

MVC-style layout, all classes with static or simple instance methods:

- `carga_runt.py` — entry point: loads `.env` via `resource_path`, then calls `CargarRuntControllador.etl_runt()`.
- `controlador/cargar_runt_controlador.py` — orchestrates the whole flow as a chain of boolean checks: pick file → not empty → read → transform → connect → insert. Each failure maps to a `GuiGeneral` error message box. Model methods signal failure by returning `False` (or `(False, df)`), not by raising.
- `modelo/procesar_archivo.py` — reads the Excel with pandas, builds `Fecha` from `AÑO_MATRICULA`/`MES_MATRICULA`/`DIA_MI`, keeps only `VIN, CANAL, Fecha, PLACA` (column order matters — it matches the INSERT).
- `modelo/inserta_datos.py` — pyodbc with `fast_executemany`: bulk-inserts into staging table `temp_carga_runt`, then in the same transaction runs an `UPDATE ... JOIN` into `[dbVentasCorporativas]..Trackings` (only rows where `LicensePlateDate IS NULL` and `LicensePlateDescription <> 4`, setting it to 4) and `DELETE`s the staging table, then commits. The connection is always closed in `finally`.
- `vista/gui_general.py` — thin Tkinter wrappers (file dialog, info/error message boxes).
- `utilidades/resolver_rutas.py` — two path helpers that matter for the frozen build:
  - `resource_path` → resolves inside the PyInstaller bundle (`sys._MEIPASS`); used for the embedded `.env`.
  - `ruta_ejecutable` → resolves next to the `.exe` (or the script); currently unused.

## Packaging notes

- `carga_runt.spec` embeds `.env` into the one-file exe (`datas=[('.env', '.')]`), so credential changes require a rebuild. `build.bat` aborts if `.env` is missing.
- The exe is built with `console=False`, so `print()` calls (used for error details in the model) produce no visible output in the packaged app; only message boxes reach the user.
- New runtime imports that PyInstaller can't detect statically must be added to `hiddenimports` in the spec; build-only deps go in `requerimientos-build.txt`.
