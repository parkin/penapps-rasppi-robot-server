from distutils.core import setup, Extension

import os

if not os.path.exists('settings.json'):
    import settings
    settings.setup()

# define the extension module
pennapprobot = Extension('pennapprobot', sources=['pennapprobot.c'])

# run the setup
setup(ext_modules=[pennapprobot])
