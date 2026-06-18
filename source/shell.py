import decman

from common import HOME

decman.symlinks[f'{HOME}/.bashrc'] = f'{HOME}/dotfiles/shell/bashrc'
decman.symlinks[f'{HOME}/.zshrc'] = f'{HOME}/dotfiles/shell/zshrc'
