# -*- mode: python ; coding: utf-8 -*-

include_files = [
    ("COPYING", "."),
    ("OpenNumismat/translations", "translations"),
    ("OpenNumismat/templates", "templates"),
    ("OpenNumismat/db", "db"),
]

a = Analysis(
    ["open-numismat-portable.py"],
    pathex=[],
    binaries=[],
    datas=include_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="OpenNumismat",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="icons/main.ico",
    version="file_version_info.txt",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="OpenNumismat",
)

from OpenNumismat.version import Version, AppName

import os
import shutil
import sys

WIN32 = sys.platform == "win32"
DARWIN = sys.platform == "darwin"

if WIN32:
    bin_dir = "dist/OpenNumismat/_internal/"
    pyd_ext = ".pyd"
else:
    bin_dir = "dist/OpenNumismat.app/Contents/Frameworks/"
    pyd_ext = ".abi3.so"

for sub_folder in ("qml",):
    if WIN32:
        shutil.rmtree(bin_dir + "PySide6/" + sub_folder)
    else:
        shutil.rmtree(bin_dir + "PySide6/Qt/" + sub_folder)

for f in (
    "QtPositioning",
    "QtQml",
    "QtQuick",
    "QtQuickWidgets",
):
    try:
        os.remove(bin_dir + "PySide6/" + f + pyd_ext)
    except OSError:
        print("Missed file:", "PySide6/" + f + pyd_ext)
        pass

if WIN32:
    pass
else:
    for f in (
        "QtBluetooth",
        "QtDesigner",
        "QtLocation",
        "QtMultimedia",
        "QtMultimediaWidgets",
        "QtNfc",
        "QtQuickParticles",
        "QtQuickTemplates2",
        "QtQmlWorkerScript",
        "QtQuick3D",
        "QtQuick3DAssetImport",
        "QtQuick3DRender",
        "QtQuick3DRuntimeRender",
        "QtQuick3DUtils",
    ):
        try:
            os.remove(bin_dir + f)
        except OSError:
            print("Missed file:", f)
            pass

if os.path.exists(AppName + "-" + Version + ".zip"):
    os.remove(AppName + "-" + Version + ".zip")
shutil.make_archive(AppName + "-" + Version, "zip", "dist/")
