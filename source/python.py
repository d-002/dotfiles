import decman
from decman.plugins import pacman, aur
from common import HOMES


class PythonModule(decman.Module):
    def __init__(self):
        super().__init__('python')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'jupyter-notebook',
            'mypy',
            'python-hatch',
            'python-numpy',
            'python-pip',
            'python-pygame',
            'python-pyqt6',
            'python-typing_extensions',
            'ruff',
            'uv',
            'uvicorn',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'python-pynput',
            'python-sounddevice',
        }


for home in HOMES:
    decman.symlinks[f'{home}/.ipython/profile_default/ipython_config.py'] = (
        f'{home}/dotfiles/python/ipython_config.py'
    )
