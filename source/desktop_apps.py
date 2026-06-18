import decman
import subprocess
from decman import File
from decman.plugins import pacman, aur, systemd

from common import HOME


class DesktopAppsModule(decman.Module):
    def __init__(self):
        super().__init__('desktop_apps')

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

    def after_update(self, store) -> None:
        print('DesktopAppsModule: setting default browser')

        subprocess.run(
            ['xdg-settingssetdefault-web-browserbrave-browser.desktop']
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
for name in names:
    decman.symlinks[f'{HOME}/.config/{name}'] = (
        f'{HOME}/dotfiles/desktop_apps/{name}'
    )

decman.symlinks[f'{HOME}/.config/picom.conf'] = source_file = (
    f'{HOME}/dotfiles/desktop_apps/picom/picom.conf'
)
decman.symlinks[f'{HOME}/.config/vesktop/flags.conf'] = source_file = (
    f'{HOME}/dotfiles/desktop_apps/vesktop/flags.conf'
)
decman.symlinks[f'{HOME}/Pictures/wallpaper.jpg'] = (
    f'{HOME}/dotfiles/desktop_apps/wallpaper.jpg'
)

# these need to be files with root permissions and not symlinks for greeter
for name in ['config', 'config-base']:
    decman.files[f'/etc/sway/{name}'] = File(
        source_file=f'{HOME}/dotfiles/desktop_apps/sway_root/{name}'
    )

decman.symlinks['/etc/chromium/default'] = (
    f'{HOME}/dotfiles/desktop_apps/chromium_root/default'
)
decman.symlinks['/etc/opera/default.pacsave'] = (
    f'{HOME}/dotfiles/desktop_apps/opera_root/default.pacsave'
)
