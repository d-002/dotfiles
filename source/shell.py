import decman

from common import HOMES

for home in HOMES:
    decman.symlinks[f'{home}/.bashrc'] = f'{home}/dotfiles/shell/bashrc'
    decman.symlinks[f'{home}/.zshrc'] = f'{home}/dotfiles/shell/zshrc'
