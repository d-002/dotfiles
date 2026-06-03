import decman
from decman.plugins import pacman, aur, systemd

from common import HOME

class UnclassifiedModule(decman.Module):
    def __init__(self):
        super().__init__('unclassified')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        s = {
            'bc',
            'brightnessctl',
            'clinfo',
            'docker',
            'docker-compose',
            'eza',
            'fd',
            'git',
            'man-db',
            'man-pages',
            'pacman-contrib',
            'perl-image-exiftool',
            'pre-commit',
            'rsync',
            'unzip',
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
        }

decman.symlinks[f'{HOME}/.clang-format'] = \
        f'{HOME}/dotfiles/unclassified/clang-format'
decman.symlinks[f'{HOME}/.gitconfig'] = \
        f'{HOME}/dotfiles/unclassified/gitconfig'
decman.symlinks[f'{HOME}/.local/bin'] = \
        f'{HOME}/dotfiles/unclassified/bin'
