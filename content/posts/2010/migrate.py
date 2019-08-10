import pathlib
import shutil


flist = []
year = 2010
for p in pathlib.Path(f'post/{year}').iterdir():
    if p.is_dir():
        with open(f'post/{year}/{p.name}/index.md', "r") as f:
            filedata = f.read()
        filedata = filedata.replace(f'({p.name}/', '(')
        #filedata = filedata.replace(f'(/', '(')
        with open(f'post/{year}/{p.name}/index.md', 'w') as f:
            f.write(filedata)
