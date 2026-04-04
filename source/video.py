import decman
from decman.plugins import pacman, aur, systemd

class VideoModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'mesa-utils',
            'nvidia-open',
            'nvidia-prime',
            'nvidia-settings',
            'nvidia-utils',
            'opencl-mesa',
            'opencl-nvidia',
            'vulkan-intel',
            'vulkan-mesa-layers',
            'vulkan-nouveau',
            'vulkan-tools',
            'xf86-video-intel',
            'xf86-video-vesa',
        }
