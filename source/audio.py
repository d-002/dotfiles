import decman
from decman.plugins import pacman, systemd


class AudioModule(decman.Module):
    def __init__(self):
        super().__init__('audio')

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
            'ffmpeg4.4',
            'vpl-gpu-rt',
            'wavpack',
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            'alsa-restore.service',
            'alsa-state.service',
        }

    @systemd.user_units
    def user_units(self) -> dict[str, set[str]]:
        return {
            'd_00': {
                'pipewire.service',
                'wireplumber.service',
            },
        }
