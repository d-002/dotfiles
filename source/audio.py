import decman
from decman.plugins import pacman, aur, systemd

class AudioModule(decman.Module):
    def __init__(self):
        super().__init__('base')

    @pacman.packages
    def pacman_pkgs(self) -> set[str]:
        return {
            'alsa-utils',
            'faac',
            'faad2',
            'pavucontrol',
            'pipewire-alsa',
            'pipewire-audio',
            'pipewire-pulse',
            'sof-firmware',
            'vlc',
            'vlc-plugin-ffmpeg',
            'vpl-gpu-rt',
            'wavpack',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'alsa-restore.service',
            'alsa-state.service',
        }
