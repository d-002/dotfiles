import decman
from os.path import join, isdir
from glob import glob
from decman import File

from common import HOME

root_dir = f'{HOME}/dotfiles/system_root'
for subpath in glob('**', root_dir=root_dir, recursive=True):
    source_file = join(root_dir, subpath)

    if isdir(source_file):
        continue
    decman.files['/' + subpath] = File(source_file=source_file)
