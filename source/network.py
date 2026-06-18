import decman
from decman.plugins import pacman, systemd


class NetworkModule(decman.Module):
    def __init__(self):
        super().__init__('network')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'bluetui',
            'bluez',
            'bluez-deprecated-tools',
            'bluez-utils',
            'inetutils',
            'networkmanager',
            'nss-mdns',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'NetworkManager.service',
            'bluetooth.service',
        }
