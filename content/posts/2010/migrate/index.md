import pathlib
import shutil

flist = []
for p in pathlib.Path('post/2010').iterdir():
    if p.is_file():
        new = pathlib.Path(f'post/2010/{p.stem}')
        new.mkdir(exist_ok=True) 
        new_path = new/'index.md'
        shutil.move(p, new_path)
        flist.append(p)