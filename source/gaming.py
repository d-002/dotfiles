import os
import decman
import subprocess
import shutil
from decman.plugins import pacman, aur, systemd


class GamingModule(decman.Module):
    def __init__(self):
        super().__init__('gaming')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            # general
            'wine',
            # steam
            'steam',
            # Minecraft
            'jdk21-openjdk',
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            # general
            'multimc-bin',
        }
