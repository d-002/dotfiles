import decman
from decman.plugins import pacman, aur, systemd

from common import HOME

class LocaleModule(decman.Module):
    def __init__(self):
        super().__init__('locale')

    @systemd.units
    def units(self) -> set[str]:
        return {
            'systemd-timesyncd.service',
        }

decman.symlinks['/etc/locale.conf'] = f'{HOME}/dotfiles/locale/locale.conf'
decman.symlinks['/etc/locale.gen'] = f'{HOME}/dotfiles/locale/locale.gen'
decman.symlinks['/etc/vconsole.conf'] = f'{HOME}/dotfiles/locale/vconsole.conf'
decman.symlinks['/etc/hostname'] = f'{HOME}/dotfiles/locale/hostname'
