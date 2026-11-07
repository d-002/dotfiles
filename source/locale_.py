import decman
from decman.plugins import systemd

from common import HOMES


class LocaleModule(decman.Module):
    def __init__(self):
        super().__init__('locale')

    @systemd.units
    def units(self) -> set[str]:
        return {
            'systemd-timesyncd.service',
        }


for home in HOMES:
    decman.symlinks['/etc/locale.conf'] = f'{home}/dotfiles/locale/locale.conf'
    decman.symlinks['/etc/locale.gen'] = f'{home}/dotfiles/locale/locale.gen'
    decman.symlinks['/etc/vconsole.conf'] = (
        f'{home}/dotfiles/locale/vconsole.conf'
    )
