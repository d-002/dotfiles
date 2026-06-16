import decman
from decman.plugins import pacman, aur, systemd

class RemoteFSModule(decman.Module):
    def __init__(self):
        super().__init__('remote_fs')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'cifs-utils',
            'mtpfs',
            'nginx'
            'sshfs',
            'openssh',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'httpfs2-2gbplus',
            'jmtpfs',
        }

    """
    @systemd.units
    def units(self) -> set[str]:
        return {
            'sshd.service',
        }
    """
