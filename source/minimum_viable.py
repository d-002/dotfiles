import decman
from decman import File
from decman.plugins import pacman, aur

from common import HOME

class MinimumViableModule(decman.Module):
    def __init__(self):
        super().__init__('minimum_viable')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'base',
            'base-devel',
            'devtools',
            'efibootmgr',
            'grub',
            'intel-ucode',
            'linux',
            'linux-firmware',
            'nano',
            'os-prober',
            'sudo',
            'texinfo',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'decman',
            'yay',
        }

decman.files[f'/etc/pacman.conf'] = File(
        source_file=f'{HOME}/dotfiles/pacman/pacman.conf')
