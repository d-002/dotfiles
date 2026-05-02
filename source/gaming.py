import os
import decman
import subprocess
from decman.plugins import pacman, aur, systemd

class GamingModule(decman.Module):
    def __init__(self):
        super().__init__('gaming')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'gamescope',
            'mangohud',
            'steam',
            'gamemode',
            'wine',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'asusctl',
            'multimc-bin',
            'rog-control-center',
            'envycontrol',
            'protonup-qt',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'nvidia-persistenced',
            'asusd',
        }

    def before_update(self, store) -> None:
        print('GamingModule: custom before hook')

        print(' - Making sure /etc/asusd dir exists')
        if not os.path.exists('/etc/asusd'):
            os.mkdir('/etc/asusd')

    def after_update(self, store) -> None:
        print('GamingModule: custom after hook')

        print(' - Setting mode to hybrid...')
        current_mode = subprocess.check_output(
            ['envycontrol', '-q'], text=True).strip()
        target_mode = 'hybrid'
        if current_mode == target_mode:
            print('Mode already set.')
        else:
            cp = subprocess.run(['envycontrol', '-s', target_mode])
            assert cp.returncode == 0
