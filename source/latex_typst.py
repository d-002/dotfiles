import decman
from decman.plugins import pacman

from common import HOMES


class LatexTypstModule(decman.Module):
    def __init__(self):
        super().__init__('latex_typst')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        s = {
            'biber',
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
            'typst',
        }

        return s


for home in HOMES:
    decman.symlinks[f'{home}/.local/share/typst/packages/local'] = (
        f'{home}/dotfiles/typst/local'
    )
