import decman
from decman.plugins import pacman, aur, systemd

class PythonModule(decman.Module):
    def __init__(self):
        super().__init__('python')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
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
            'python-pytorch',
            'python-soundfile',
            'python-tensorflow',
            'python-torchvision',
            'python-typing_extensions',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            'python-latex-ocr-server',
            'python-moderngl-window',
            'python-py-cord-git',
            'python-pyglm',
            'python-pynput',
            'python-sentence-transformers',
            'python-sounddevice',
        }
