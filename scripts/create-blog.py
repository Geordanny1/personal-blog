#!/usr/bin/env python3

from datetime import datetime
from os import path
import string, argparse, os.path

title = input("what is gonna be the tittle for this post?\n(run this on the home directory)").replace(" ", "-")

save_path = "_posts/"

parser = argparse.ArgumentParser(description="create a template for a blog")
date = datetime.now()

data = {
    "title" : title.replace("-", " "),
    "date" : date.strftime("%Y-%m-%d"),
    "permalink" : f"posts/{date.strftime("%Y")}/{date.strftime("%m")}/{title}/"
}

# create the file

complete_name = path.join(save_path, f"{date.strftime("%Y-%m-%d")}-{title}.md")

template_string = """---
title: $title
date: $date
permalink: $permalink
tags:

---
"""

template = string.Template(template_string)
post = template.substitute(data)

# write the file
with open(complete_name, "w") as f:
    f.write(post)


