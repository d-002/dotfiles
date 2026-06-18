import decman
from decman.plugins import pacman, aur


class LibsDriversModule(decman.Module):
    def __init__(self):
        super().__init__('libs_drivers')

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
            'qt6-wayland',
            'xdg-desktop-portal',
            'xdg-desktop-portal-gtk',
            'xdg-desktop-portal-wlr',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'openjpeg',
        }
