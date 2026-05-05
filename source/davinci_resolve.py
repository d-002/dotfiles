import decman
from decman.plugins import aur

class DaVinciResolveModule(decman.Module):
    def __init__(self):
        super().__init__('DaVinci Resolve')

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            # tip: for large packages like qt5-location, qt5-webengine, use a
            # prebuilt binary to avoid compiling 24k source files:
            # e.g. https://mirror.cachyos.org/repo/x86_64/cachyos
            'gtk2',
            'libpng12',
            'qt5-location',
            'qt5-webchannel',
            'qt5-webengine',
            'qt5-websockets',
            'davinci-resolve',
        }
