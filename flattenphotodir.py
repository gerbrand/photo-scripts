from os import walk, path
from shutil import copyfile

sourcedir = '/home/gerbrand/Pictures/2012'
targetdir = '/home/gerbrand/upload/2012'
for root, directories, filenames in walk(sourcedir):
        for filename in filenames:
            sourcefile = path.join(root, filename)
            targetfile = path.join(targetdir, path.split(root)[-1]+"-"+filename)
            copyfile(sourcefile, targetfile)