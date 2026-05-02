import os
import decman
from decman.plugins import pacman, aur, systemd
from subprocess import run

class GamingModule(decman.Module):
    def __init__(self):
        super().__init__('gaming')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'steam',
            'gamemode',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'asusctl',
            'rog-control-center',
            'supergfxctl',
            'protonup-qt',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'nvidia-persistenced',
            'asusd',
            'supergfxd',
        }

    def before_update(self, store) -> None:
        print('GamingModule: custom before hook')

        print(' - Making sure /etc/asusd dir exists')
        if not os.path.exists('/etc/asusd'):
            os.mkdir('/etc/asusd')

    def after_update(self, store) -> None:
        print('GamingModule: custom after hook')

        print(' - Setting mode to hybrid...')
        cp = run(['supergfxctl', '-m', 'Hybrid'])
        assert cp.returncode == 0
