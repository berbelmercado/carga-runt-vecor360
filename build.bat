@echo off
REM Genera dist\CargaRUNT.exe (requiere Python solo en la maquina de compilacion)
if not exist .venv-build (
    python -m venv .venv-build
    .venv-build\Scripts\python -m pip install --upgrade pip
    .venv-build\Scripts\python -m pip install -r requerimientos-build.txt
)
.venv-build\Scripts\pyinstaller carga_runt.spec --clean --noconfirm
if exist .env copy /Y .env dist\.env >nul
echo.
echo Ejecutable generado en dist\CargaRUNT.exe
