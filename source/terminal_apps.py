import decman
from decman.plugins import pacman

from common import HOMES


class TerminalAppsModule(decman.Module):
    def __init__(self):
        super().__init__('terminal_apps')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'btop',
            'fastfetch',
            'fzf',
            'github-cli',
            'htop',
            'inxi',
            'lsof',
            'lynx',
            'openbsd-netcat',
            'ripgrep',
            's-tui',
            'tmux',
            'tree',
            'zoxide',
        }


for home in HOMES:
    decman.symlinks[f'{home}/.config/btop'] = (
        f'{home}/dotfiles/terminal_apps/btop'
    )
    decman.symlinks[f'{home}/.config/htop'] = (
        f'{home}/dotfiles/terminal_apps/htop'
    )
