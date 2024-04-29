# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import kivymd.icon_definitions
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivymd.app import MDApp
from kivy.core.window import Window

a = Analysis(
    ['D:/01_Desktop/Developer/Softwares/Python/CashExFlow/App.py'],
    pathex=[],
    binaries=[],
    datas=[
	('D:/01_Desktop/Developer/Softwares/Python/CashExFlow/View', './View'),
	('D:/01_Desktop/Developer/Softwares/Python/CashExFlow/Assets', './Assets'),
	('D:/01_Desktop/Developer/Softwares/Python/CashExFlow/CashExFlow_database.db', '.')],
    hiddenimports=['../ViewModel', '../View', '../Assets'],
    hookspath=['../ViewModel/GeneratorPage.py'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
splash = Splash(
    'D:/01_Desktop/Developer/Softwares/Python/CashExFlow/Assets/Logo_Associate.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=False,
)

exe = EXE(
    pyz,
    a.scripts,
    splash,
    [],
    exclude_binaries=True,
    name='CashExFlow',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\01_Desktop\\Developer\\Softwares\\Python\\CashExFlow\\Assets\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    splash.binaries,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CashExFlow',
)
