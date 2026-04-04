import decman
from decman.plugins import pacman, aur, systemd

class UnclassifiedModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        s = {
            'biber',
            'brightnessctl',
            'bun',
            'clinfo',
            'docker',
            'eza',
            'fd',
            'git',
            'jupyter-notebook',
            'luarocks',
            'man-db',
            'man-pages',
            'npm',
            'perl-image-exiftool',
            'php',
            'php-sqlite',
            'pnpm',
            'postgresql',
            'pre-commit',
            'rsync',
            'rust',
            'typst',
            'unzip',
            'uvicorn',
            'zig',
            'zip',
            'zsh',
        }

        s |= {
            'texlive-basic',
            'texlive-bibtexextra',
            'texlive-binextra',
            'texlive-context',
            'texlive-fontsextra',
            'texlive-fontsrecommended',
            'texlive-fontutils',
            'texlive-formatsextra',
            'texlive-games',
            'texlive-humanities',
            'texlive-latex',
            'texlive-latexextra',
            'texlive-latexrecommended',
            'texlive-luatex',
            'texlive-mathscience',
            'texlive-metapost',
            'texlive-music',
            'texlive-pictures',
            'texlive-plaingeneric',
            'texlive-pstricks',
            'texlive-publishers',
            'texlive-xetex',
        }

        return s

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'manim',
            'pacseek',
        }
