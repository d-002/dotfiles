import decman
from decman.plugins import pacman, aur, systemd

class CModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'autoconf-archive',
            'cmake',
            'criterion',
            'gcovr',
            'gdb',
            'mingw-w64-gcc',
            'musl',
            'patchelf',
            'valgrind',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'glm-git',
            'mingw-w64-zlib',
        }
