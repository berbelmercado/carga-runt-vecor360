# -*- mode: python ; coding: utf-8 -*-
# Construir con: build.bat  (o: pyinstaller carga_runt.spec --clean)

a = Analysis(
    ['carga_runt.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['openpyxl', 'pyodbc'],
    excludes=['matplotlib', 'scipy', 'IPython', 'pytest'],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CargaRUNT',
    debug=False,
    strip=False,
    upx=False,
    console=False,
)
