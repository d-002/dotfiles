import decman

from common import HOME

decman.symlinks['/etc/default/grub'] = f'{HOME}/dotfiles/system_root/grub'
decman.symlinks['/etc/fstab'] = f'{HOME}/dotfiles/system_root/fstab'
