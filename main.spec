# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['E:\\Part time languages\\pyhton\\text-summarizer'],  # Path to your project directory
    binaries=[],  # Add any additional binary files if needed
    datas=[  # Add data files like images if needed
        # Example: ('path/to/your/images/*', 'destination/folder/'),
    ],
    hiddenimports=[
        'nltk',                # For nltk (Natural Language Toolkit)
        'tkinter',             # For tkinter (GUI toolkit)
        'bs4',                 # For BeautifulSoup
        'reportlab',           # For ReportLab (PDF generation)
        'docx',                # For DOCX file handling
        'PIL',                 # For PIL (Python Imaging Library)
        'urllib',              # For urllib (URL handling)
        'PIL.ImageTk',         # For ImageTk from PIL (image handling in tkinter)
        'tkinter.filedialog',  # For tkinter file dialog
        'tkinter.messagebox',  # For tkinter messagebox
        'tkinter.ttk',         # For tkinter themed widgets
    ],  
    hookspath=[],  # If you have any custom hooks, you can add them here
    hooksconfig={},
    runtime_hooks=[],  # If you need any runtime hooks, specify them here
    excludes=[],  # Exclude any unnecessary modules here
    noarchive=False,  # This can be set to True for specific use cases
    optimize=0,
)

# Create the PYZ archive with bundled Python code
pyz = PYZ(a.pure)

# Add runtime hooks to set the environment variables for TCL and TK
runtime_hooks = [
    # Hook to set the TCL and TK environment variables
    """
import os
os.environ['TCL_LIBRARY'] = "C:/Program Files/Python313/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Program Files/Python313/tcl/tk8.6"
    """
]

# Define the EXE, which is the actual executable to run
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',  # The name of the executable file
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Compress the executable
    upx_exclude=[],  # Exclude files from UPX compression if needed
    runtime_tmpdir=None,  # Can specify a temp directory if needed
    console=True,  # Keep the console output (set to False for GUI applications)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    runtime_hooks=runtime_hooks,  # Add runtime hooks here
)
