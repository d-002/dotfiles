import decman
from decman.plugins import pacman, aur, systemd

from common import HOMES


class UnclassifiedModule(decman.Module):
    def __init__(self):
        super().__init__('unclassified')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        s = {
            'bc',
            'bind',
            'brightnessctl',
            'clinfo',
            'fd',
            'git',
            'man-db',
            'man-pages',
            'pacman-contrib',
            'perl-image-exiftool',
            'reflector',
            'rsync',
            'unzip',
            'vim',
            'zip',
            'zsh',
        }

        return s

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'pacseek',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'containerd.service',
            'docker.service',
            'docker.socket',
            'reflector.service',
        }


for home in HOMES:
    decman.symlinks[f'{home}/.clang-format'] = (
        f'{home}/dotfiles/unclassified/clang-format'
    )
    decman.symlinks[f'{home}/.gitconfig'] = (
        f'{home}/dotfiles/unclassified/gitconfig'
    )
    decman.symlinks[f'{home}/.local/bin'] = f'{home}/dotfiles/unclassified/bin'
