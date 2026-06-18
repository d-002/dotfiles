import decman
from decman.plugins import pacman, aur


class ProgrammingModule(decman.Module):
    def __init__(self):
        super().__init__('programming')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        s = {
            'bun',
            'luarocks',
            'npm',
            'php',
            'php-sqlite',
            'pnpm',
            'postgresql',
            'rust',
            'zig',
        }

        return s

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'manim',
        }
