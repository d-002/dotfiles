import decman
from decman.plugins import pacman, aur, systemd

class X11Module(decman.Module):
    def __init__(self):
        super().__init__('x11')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'feh',
            'i3-wm',
            'i3lock',
            'openbox',
            'picom',
            'polybar',
            'xdg-utils',
            'xorg-server',
            'xorg-xinit',
            'xsel',
            'xterm',
        }
