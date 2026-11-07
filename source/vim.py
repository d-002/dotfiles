import decman
from decman import Directory
from decman.plugins import pacman, aur

from common import HOMES, USERNAMES


class VimModule(decman.Module):
    def __init__(self):
        super().__init__('vim')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'ex-vi-compat',
            'neovim',
            'tree-sitter-cli',
            'vim',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'vundle',
        }


for home, username in zip(HOMES, USERNAMES):
    decman.symlinks[f'{home}/.vimrc'] = f'{home}/dotfiles/vim/vimrc'
    decman.directories[f'{home}/.config/nvim'] = Directory(
        source_directory=f'{home}/dotfiles/nvim', owner=username
    )
