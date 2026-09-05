import decman
from decman.plugins import aur


class DaVinciResolveModule(decman.Module):
    def __init__(self):
        super().__init__('DaVinci Resolve')

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            # tip: for large packages like qt5-location, qt5-webengine use a
            # prebuild library e.g.
            # https://mirror.cachyos.org/repo/x86_64/cachyos
            'davinci-resolve',
        }
