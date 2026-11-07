import decman
from decman import Directory

from decman.plugins import pacman

from common import HOMES, USERNAMES


class FontsModule(decman.Module):
    def __init__(self):
        super().__init__('fonts')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'adobe-source-sans-fonts',
            'gnu-free-fonts',
            'noto-fonts',
            'noto-fonts-cjk',
            'noto-fonts-emoji',
            'ttf-firacode-nerd',
            'ttf-liberation',
            'ttf-opensans',
            'ttf-roboto',
            'ttf-roboto-mono',
            'ttf-ubuntu-font-family',
            'woff2-font-awesome',
        }


for home, username in zip(HOMES, USERNAMES):
    decman.directories[f'{home}/.fonts'] = Directory(
        source_directory=f'{home}/dotfiles/fonts', owner=username
    )
