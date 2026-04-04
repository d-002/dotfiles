import decman
from decman.plugins import pacman, aur, systemd

class TerminalAppsModule(decman.Module):
    def __init__(self):
        super().__init__('base')

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
