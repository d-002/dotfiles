import decman
from decman import File, Directory

from common import HOMES

# needs to be files with root permissions and not symlinks
for home in HOMES:
    for name in ['config.toml', 'greetd.conf', 'sway-config']:
        decman.files[f'/etc/greetd/{name}'] = File(
            source_file=f'{home}/dotfiles/greeter/greetd/{name}'
        )
    decman.directories['/etc/nwg-hello/custom'] = Directory(
        source_directory=f'{home}/dotfiles/greeter/nwg-hello/custom'
    )
    decman.directories['/usr/share/nwg-hello/wallpapers'] = Directory(
        source_directory=f'{home}/dotfiles/greeter/nwg-hello/wallpapers'
    )
