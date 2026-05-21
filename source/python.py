import decman
from decman.plugins import pacman, aur, systemd
from common import HOME

class PythonModule(decman.Module):
    def __init__(self):
        super().__init__('python')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'jupyter-notebook',
            'python-certifi',
            'python-colorama',
            'python-cvxpy',
            'python-fastapi',
            'python-grpcio',
            'python-hatch',
            'python-matplotlib',
            'python-mido',
            'python-numpy',
            'python-pip',
            'python-pydub',
            'python-pygame',
            'python-pylatexenc',
            'python-pyqt6',
            'python-pytest-cov',
            'python-python-multipart',
            'python-soundfile',
            'python-typing_extensions',
            'uvicorn',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'python-latex-ocr-server',
            'python-moderngl-window',
            'python-py-cord-git',
            'python-pyglm',
            'python-pynput',
            'python-sounddevice',
        }

decman.symlinks[f'{HOME}/.ipython/profile_default/ipython_config.py'] = \
        f'{HOME}/dotfiles/python/ipython_config.py'
