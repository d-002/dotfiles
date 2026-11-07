import decman
from os.path import join, isdir
from glob import glob
from decman import File

from common import HOMES

for home in HOMES:
    root_dir = f'{home}/dotfiles/system_root'
    for subpath in glob('**', root_dir=root_dir, recursive=True):
        source_file = join(root_dir, subpath)

        if isdir(source_file):
            continue
        decman.files['/' + subpath] = File(source_file=source_file)
