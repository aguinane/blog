import os
import re
from PIL import Image
from pathlib import Path
from invoke import task


CONFIG = {
    "deploy_path": "public",
    "github_pages_branch": "gh-pages",
    "github_pages_message": "Publish",
}


@task
def lowercase_jpg(c):
    files = list(Path("content").rglob("*.JPG"))
    for f in files:
        old_path = str(f)
        new_path = str(f).replace(".JPG", ".jpg")
        os.rename(old_path, new_path)


@task
def remove_metadata(c):
    c.run("exiftool -r -overwrite_original -P -all= content -ext jpg -ext jpeg")


@task
def resize_images(c, pre=[lowercase_jpg, remove_metadata]):
    files = list(Path("content").rglob("*.jpg"))
    for f in files:
        filesize = f.stat().st_size
        if filesize > 300000:
            im = Image.open(f)
            width, height = im.size
            if width > 1600 or height > 1600:
                cmd = f"mogrify -verbose -resize 1600\>x1600\> {str(f)}"
                c.run(cmd)


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    c.run("hugo")
    c.run(
        "ghp-import -b {github_pages_branch} {deploy_path} -p -m {github_pages_message}".format(
            **CONFIG
        )
    )


@task
def populate_feature_image(c):
    """ Populate feature image with first image found """

    def get_first_image(text):
        pattern = r"([\(]).*([.jpg])"
        match = re.search(pattern, text)
        if match:
            return match[0][1:]
        return None

    import frontmatter

    files = list(Path("content").rglob("*.md"))
    for f in files:
        post = frontmatter.load(f)
        try:
            feature = post["featured_image"]
            print(f, "already has a featured image")
            continue
        except KeyError:
            try:
                year = post["date"][0:4]
                slug = post["slug"]
                image = get_first_image(post.content)
            except:
                print("Could not process ", f)
                continue
            if image:
                base_url = f"posts/{year}/{slug}/{image}"
                post["featured_image"] = base_url
        frontmatter.dump(post, f)
        print(f, "added", base_url)
