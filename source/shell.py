import decman

from common import HOME, USERNAME

decman.symlinks[f'{HOME}/.bashrc'] = f'{HOME}/dotfiles/shell/bashrc'
decman.symlinks[f'{HOME}/.zshrc'] = f'{HOME}/dotfiles/shell/zshrc'
