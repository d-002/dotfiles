import decman
from decman import File
from decman.plugins import pacman, aur, systemd

from common import HOME, USERNAME

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
            'zathura-pdf-mupdf',
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
    'polybar',
    'rofi',
    'sway',
    'swaylock',
    'waybar',
]
for name in names:
    decman.symlinks[f'{HOME}/.config/{name}'] = \
            f'{HOME}/dotfiles/desktop_apps/{name}'

decman.files[f'{HOME}/.config/picom.conf'] = File(
        source_file=f'{HOME}/dotfiles/desktop_apps/picom/picom.conf',
        owner=USERNAME)
decman.files[f'{HOME}/.config/vesktop/flags.conf'] = File(
        source_file=f'{HOME}/dotfiles/desktop_apps/vesktop/flags.conf',
        owner=USERNAME)
for name in ['config', 'config-base']:
    decman.files[f'/etc/sway/{name}'] = File(
            source_file=f'{HOME}/dotfiles/desktop_apps/sway_root/{name}')
decman.files['/etc/chromium/default'] = File(
        source_file=f'{HOME}/dotfiles/desktop_apps/chromium_root/default')
decman.files['/etc/opera/default.pacsave'] = File(
        source_file=f'{HOME}/dotfiles/desktop_apps/opera_root/default.pacsave')
