from os import walk, path
from shutil import copyfile
import sys

if len(sys.argv) < 3:
    print """
    Flatten a photo directory. Copies all files recursively. Direct parent directory is prepended to the filename, seperated by a -.
    So \"John/2013/Uploaded/My Birthday\DSC01.jpg\" becomes \"My Birthday-DSC01.jpg\"

    Usage:
    flattenphotodir.py <sourcedir> <targetdir>"""
    sys.exit(1)

sourcedir = sys.argv[1]
targetdir = sys.argv[2]
print "Flatting pictures from", sourcedir, "into", targetdir
for root, directories, filenames in walk(sourcedir):
    for filename in filenames:
        sourcefile = path.join(root, filename)
        newname = path.split(root)[-1] + "-" + filename
        targetfile = path.join(targetdir, newname)
        if not path.isfile(targetfile):
            copyfile(sourcefile, targetfile)
            print 'Copied:', newname
        else:
            print 'Already exists in', targetdir, ':', newname
