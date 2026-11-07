import decman
import subprocess
from decman import File
from decman.plugins import pacman, aur, systemd

from common import HOMES


class DesktopAppsModule(decman.Module):
    def __init__(self):
        super().__init__('desktop_apps')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'audacity',
            'baobab',
            'filezilla',
            'firefox',
            'gimp',
            'greetd',
            'kitty',
            'loupe',
            'mission-center',
            'nemo',
            'nwg-hello',
            'rofi',
            'torbrowser-launcher',
            'thunderbird',
            'zathura',
            'zathura-pdf-mupdf',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'brave-bin',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'greetd.service',
        }

    def after_update(self, store) -> None:
        print('DesktopAppsModule: setting default browser')

        subprocess.run(
            [
                'xdg-settings',
                'set',
                'default-web-browser',
                'brave-browser.desktop',
            ]
        )


names = [
    'brave-flags.conf',
    'fuzzel',
    'i3',
    'kitty',
    'polybar',
    'rofi',
    'sway',
    'swaylock',
    'waybar',
]

for home in HOMES:
    for name in names:
        decman.symlinks[f'{home}/.config/{name}'] = (
            f'{home}/dotfiles/desktop_apps/{name}'
        )

    decman.symlinks[f'{home}/.config/picom.conf'] = (
        f'{home}/dotfiles/desktop_apps/picom/picom.conf'
    )
    decman.symlinks[f'{home}/Pictures/wallpaper.jpg'] = (
        f'{home}/dotfiles/desktop_apps/wallpaper.jpg'
    )

    # these need to be files with root permissions and not symlinks for greeter
    for name in ['config', 'config-base']:
        decman.files[f'/etc/sway/{name}'] = File(
            source_file=f'{home}/dotfiles/desktop_apps/sway_root/{name}'
        )
