import decman
from decman import Directory

from decman.plugins import pacman, aur, systemd

from common import HOME, USERNAME

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

decman.symlinks[f'{HOME}/.vimrc'] = f'{HOME}/dotfiles/vim/vimrc'
decman.directories[f'{HOME}/.config/nvim'] = Directory(source_directory=f'{HOME}/dotfiles/nvim', owner=USERNAME)
