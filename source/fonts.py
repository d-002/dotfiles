import decman
from decman.plugins import pacman, aur, systemd

class FontsModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'adobe-source-sans-fonts',
            'gnu-free-fonts',
            'noto-fonts',
            'ttf-liberation',
            'ttf-opensans',
            'ttf-roboto',
            'ttf-roboto-mono',
            'ttf-ubuntu-font-family',
            'woff2-font-awesome',
        }
