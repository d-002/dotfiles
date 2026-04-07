import decman
from decman.plugins import pacman, aur, systemd

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
