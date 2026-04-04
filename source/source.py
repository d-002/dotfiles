import decman

from minimum_viable import MinimumViableModule
from unclassified import UnclassifiedModule

from audio import AudioModule
from c import CModule
from desktop_apps import DesktopAppsModule
from fonts import FontsModule
from libs_drivers import LibsDriversModule
from network import NetworkModule
from python import PythonModule
from remote_fs import RemoteFSModule
from terminal_apps import TerminalAppsModule
from video import VideoModule
from vim import VimModule
from wayland import WaylandModule
from x11 import X11Module

decman.execution_order = [
    "files",
    "pacman",
    "aur",
    "flatpak",
    "systemd"
]

decman.modules += [
    MinimumViableModule(),
    UnclassifiedModule(),

    AudioModule(),
    CModule(),
    DesktopAppsModule(),
    FontsModule(),
    LibsDriversModule(),
    NetworkModule(),
    PythonModule(),
    RemoteFSModule(),
    TerminalAppsModule(),
    VideoModule(),
    VimModule(),
    WaylandModule(),
    X11Module(),
]
