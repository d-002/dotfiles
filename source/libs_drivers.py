import decman
from decman.plugins import pacman, aur, systemd

class LibsDriversModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'a52dec',
            'cuda',
            'dosfstools',
            'intel-media-driver',
            'intel-ucode',
            'libmpeg2',
            'libva-intel-driver',
            'qt6-multimedia',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'openjpeg',
        }
