import decman
from decman.plugins import pacman, aur, systemd

from common import HOME

class DesktopAppsModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'audacity',
            'baobab',
            'dmenu',
            'filezilla',
            'firefox',
            'gimp',
            'greetd',
            'kitty',
            'libreoffice-fresh',
            'loupe',
            'mission-center',
            'nemo',
            'nwg-hello',
            'obs-studio',
            'rofi',
            'thunderbird',
            'zathura',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'brave-bin',
            'chromium-widevine',
            'vesktop',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'greetd.service',
        }

names = [
    'fuzzel',
    'i3',
    'kitty',
    'picom',
    'polybar',
    'rofi',
    'sway',
    'swaylock',
    'vesktop',
    'waybar',
]
for name in names:
    decman.symlinks[f'{HOME}/.config/{name}'] = \
            f'{HOME}/dotfiles/desktop_apps/{name}'
