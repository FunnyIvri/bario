# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py', 'player.py', 'audio_manager.py', 'enemy_manager.py', 'levels.py', 'text.py', 'level_manager.py'],

    pathex=[],
    binaries=[],
    datas=[
    ('win.png', '.'),
    ('lava.png', '.'),
    ('inverted_bario.png', '.'),
    ('ground.jpg', '.'),
    ('enemy.png', '.'),
    ('eleavtor.png', '.'),
    ('door.png', '.'),
    ('coin.png', '.'),
    ('bario.mp3','.'),
    ('bario_jump.mp3','.'),
    ('bario_win.mp3','.')
],
    hiddenimports = ['pygame', 'keyboard'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    icon='src\icon.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


