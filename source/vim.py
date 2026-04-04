import decman
from decman.plugins import pacman, aur, systemd

class VimModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'neovim',
            'tree-sitter-cli',
            'vim',
        }
