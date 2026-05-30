import decman

from minimum_viable import MinimumViableModule
from unclassified import UnclassifiedModule

import greeter
import shell
import system_root

from audio import AudioModule
from c import CModule
from desktop_apps import DesktopAppsModule
from davinci_resolve import DaVinciResolveModule
from fonts import FontsModule
from gaming import GamingModule
from latex_typst import LatexTypstModule
from libs_drivers import LibsDriversModule
from locale_ import LocaleModule
from network import NetworkModule
from python import PythonModule
from programming import ProgrammingModule
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
    #"flatpak",
    "systemd"
]

decman.modules += [
    MinimumViableModule(),
    UnclassifiedModule(),

    AudioModule(),
    CModule(),
    #DaVinciResolveModule(),
    DesktopAppsModule(),
    FontsModule(),
    GamingModule(),
    LatexTypstModule(),
    LibsDriversModule(),
    LocaleModule(),
    NetworkModule(),
    PythonModule(),
    ProgrammingModule(),
    RemoteFSModule(),
    TerminalAppsModule(),
    VideoModule(),
    VimModule(),
    WaylandModule(),
    X11Module(),
]

if __name__ == '__main__':
    import subprocess

    print('Manual config override: installing all aur packages with yay')

    packages = set()
    for module in decman.modules:
        try:
            packages = packages.union(module.aur_pkgs())
        except AttributeError:
            pass

    subprocess.run(["yay", "-Syu", *packages])
