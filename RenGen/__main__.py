from RenGen.Session import Session

from pick import pick

from os.path import join
from os import mkdir, getcwd

s = Session("https://htlw5.renkin.webspace.spengergasse.at/1xhif/rx-java-1xhif/aktuell/")
courses = s.get_course("Labor 2022u23")

# noinspection PyTypeChecker
option, _ = pick(list(courses.keys()), "Choose a course to autogenerate boilerplate:")
lab = courses[option]

lab.fetch_uml_diagrams()
lab.add_explanations()

path = join(getcwd(), "Results", ''.join(c for c in option.replace('\u2009', ' ') if c.isalnum() or c in (' ', '.', '_', '-')))

try: mkdir(path)
except FileExistsError:
    if input("Directory already exists. Overwrite files? y/n: ") != 'y': exit()

try: mkdir(join(path, "src"))
except FileExistsError: pass

for java_class in lab.classes.keys():
    with open(join(path, "src", f"{java_class}.java"), "w+") as f:
        f.write(lab.get_java_str(java_class))

with open(join(path, "README.md"), "w") as f:
    f.write(lab.to_markdown())

""" TODO
1. Check method/attribute by searching for () instead of ellipse/rectangle (and add color search).
2. Better support for private public protected static final const etc.
3. try to add explanations from the text as comments.
4. add a bar that indicates how good the support for a specific lab is.
5. automatically import dependencies for Scanner, Random, etc. (if needed)
6. kotlin code generation?
"""
