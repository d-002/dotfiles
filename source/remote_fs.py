import decman
from decman.plugins import pacman, aur, systemd

class RemoteFSModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'cifs-utils',
            'mtpfs',
            'sshfs',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'httpfs2-2gbplus',
            'jmtpfs',
        }
