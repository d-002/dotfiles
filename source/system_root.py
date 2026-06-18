import decman
from decman import File

from common import HOME

decman.files['/etc/default/grub'] = File(
    source_file=f'{HOME}/dotfiles/system_root/grub'
)
