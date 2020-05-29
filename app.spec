# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['app.py'],
             pathex=['/Users/labohem/Desktop/work/python/qt'],
             binaries=[('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/spiceypy/utils/spice.so','.'),
             #('/System/Library/Frameworks/Tk.framework/Tk','Tk'),
             #('/System/Library/Frameworks/Tcl.framework/Tcl','Tcl')
             ],
             datas=[("assets/*",'assets'),
             ("extracted/*","kernels")],
             hiddenimports=['pkg_resources.py2_warn','spiceypy','scipy','numpy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter', 'cryptography',
             'etc','matplotlib','notebook','PyQt5','Pyside2.Network','PyQt4','QtWebSockets'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon = 'logo.icns',
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='grav assist')
