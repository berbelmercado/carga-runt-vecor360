@echo off
REM Genera dist\CargaRUNT.exe (requiere Python solo en la maquina de compilacion)
if not exist .env (
    echo Falta el archivo .env: se embebe dentro del ejecutable.
    exit /b 1
)
if not exist .venv-build (
    python -m venv .venv-build
    .venv-build\Scripts\python -m pip install --upgrade pip
    .venv-build\Scripts\python -m pip install -r requerimientos-build.txt
)
.venv-build\Scripts\pyinstaller carga_runt.spec --clean --noconfirm
echo.
echo Ejecutable generado en dist\CargaRUNT.exe
