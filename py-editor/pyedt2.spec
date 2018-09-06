# -*- mode: python -*-

block_cipher = None


a = Analysis(['pyedt2.py'],
             pathex=['C:Users/shadow/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin', 'C:Users/shadow/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/PyQt5/Qtplugins', 'G:\\my-python\\py-editor'],
             binaries=[],
             datas=[],
             hiddenimports=['sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Python-editor',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='d:icon.ico')
