import decman
from decman.plugins import pacman


class WaylandModule(decman.Module):
    def __init__(self):
        super().__init__('wayland')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'hyprpicker',
            'keyd',
            'mako',
            'sway',
            'swaybg',
            'swayidle',
            'swaylock',
            'sway-contrib',
            'waybar',
            'wayland',
            'wayland-protocols',
            'wev',
            'wmenu',
        }
