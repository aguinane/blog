import os
from pathlib import Path
from invoke import task


@task
def lowercase_jpg(c):
    files = list(Path("content").rglob("*.JPG"))
    for f in files:
        old_path = str(f)
        new_path = str(f).replace('.JPG', '.jpg')
        os.rename(old_path, new_path)
