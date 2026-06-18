import decman
from decman.plugins import pacman


class VideoModule(decman.Module):
    def __init__(self):
        super().__init__('video')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            # Intel iGPU
            'lib32-mesa',
            'lib32-vulkan-icd-loader',
            'lib32-vulkan-intel',
            'mesa',
            'vulkan-intel',
            # Nvidia dGPU
            'lib32-nvidia-utils',
            'nvidia-open',
            'nvidia-prime',
            'nvidia-settings',
            'nvidia-utils',
            # Utilities, tools
            'opencl-mesa',
            'opencl-nvidia',
            'vulkan-tools',
        }
