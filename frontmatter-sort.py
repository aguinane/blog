import frontmatter
from glob import glob

from frontmatter.default_handlers import TOMLHandler


def reorder_frontmatter(file_path, desired_order):
    # Load the Markdown file
    toml_handler = TOMLHandler()
    with open(file_path, "r", encoding="utf-8") as file:
        post = frontmatter.load(file, handler=toml_handler)

    # Get the frontmatter data
    frontmatter_data = post.metadata

    # Reorder the keys
    reordered_data = {
        key: frontmatter_data[key] for key in desired_order if key in frontmatter_data
    }

    # Add remaining keys not in desired_order
    for key in frontmatter_data:
        if key not in reordered_data:
            reordered_data[key] = frontmatter_data[key]

    if "taxonomies" not in reordered_data:
        reordered_data["taxonomies"] = {}

    if "extra" not in reordered_data:
        reordered_data["extra"] = {}

    if "thumbnail" in reordered_data:
        image = reordered_data["thumbnail"]
        del reordered_data["thumbnail"]
        reordered_data["extra"]["image"] = image

    if "categories" in reordered_data:
        categories = reordered_data["categories"]
        del reordered_data["categories"]
        reordered_data["taxonomies"]["categories"] = categories

    if not "categories" in reordered_data["taxonomies"]:
        reordered_data["taxonomies"]["categories"] = ["Misc"]

    if "tags" in reordered_data:
        tags = reordered_data["tags"]
        del reordered_data["tags"]
        reordered_data["taxonomies"]["tags"] = tags

    if "series" in reordered_data:
        series = reordered_data["series"]
        del reordered_data["series"]
        reordered_data["taxonomies"]["series"] = series

    # Update the post metadata
    post.metadata = reordered_data

    # Write the updated file back
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(frontmatter.dumps(post, handler=toml_handler))
    print(f"Processed {file_path}")


def process_files(desired_order):
    # Find all Markdown files
    files = glob("content/posts/**/index.md", recursive=True)
    # files = list(files)[0:10]
    for file_path in files:
        print(file_path)
        reorder_frontmatter(file_path, desired_order)


# Specify the directory and the desired attribute order
desired_order = [
    "title",
    "description",
    "date",
    "updated",
    "weight",
    "slug",
    "authors",
    "template",
]

# Process the files
process_files(desired_order)
