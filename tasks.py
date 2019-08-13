import os
from pathlib import Path
from invoke import task

CONFIG = {
    'deploy_path': 'public',
    'github_pages_branch': 'gh-pages',
}


@task
def lowercase_jpg(c):
    files = list(Path("content").rglob("*.JPG"))
    for f in files:
        old_path = str(f)
        new_path = str(f).replace('.JPG', '.jpg')
        os.rename(old_path, new_path)


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    c.run("hugo")
    c.run("ghp-import -b {github_pages_branch} {deploy_path} -p".format(
        **CONFIG))
