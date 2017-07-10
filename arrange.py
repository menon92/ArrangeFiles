#!/usr/bin/python

from argparse import ArgumentParser
from os import listdir, makedirs, getcwd
from os.path import isdir, exists, join, splitext
import shutil
import errno

__author__ = 'Md. Mehadi Hasan Menon'

# edit this config file if you need to add new type of flle.
CONFIG_DIRECTORIES = {
    "html"     : [".html5", ".html", ".htm", ".xhtml", ".css"],
    "images"   : [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"],
    "videos"   : [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", 
                  ".mpeg", ".3gp", ".mkv"],
    "documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "archives" : [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", 
                  ".rar", ".xar", ".zip", ".bz2", ".cpz", ".cpio", ".lzma", ".lz", 
                  ".xz", ".deb"],
    "audio"    : [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "plaintext": [".txt", ".in", ".out"],
    "pdf"      : [".pdf"],
    "python"   : [".py"],
    "cpp"      : [".c", ".cpp"],
    "java"     : [".java", ".jar", ".class"],
    "xml"      : [".xml"],
    "exe"      : [".exe"],
    "shell"    : [".sh"]
}
# map all the file formats with their extension.
# like,
# {'cpp' : '.c', 'cpp' : '.cpp', 'java' : '.java'}
SUPPORTED_FILE_FORMATS = { file_format : directory 
                           for directory, file_formats in CONFIG_DIRECTORIES.items() 
                           for file_format in file_formats }
ROOT_DIR = getcwd()

def junk_arranger(root_dir):

    ROOT_DIR = root_dir
    # list out all the files and directory of ROOT_DIR.
    # and iterate over them.
    for d in listdir(ROOT_DIR):
        if isdir(join(ROOT_DIR, d)):
            # this is a directory. we have nothing to do with it.
            # so just pass it.
            print "is a dir: " + d
            pass
        else:
            # get current file formate name.
            current_file_formate = splitext(d)[-1] # [-1] is for take the last one
            if SUPPORTED_FILE_FORMATS.has_key(current_file_formate):
                # we have this file formates in our dictionary
                # now 
                # if there is not any directory for this kind of file 
                # then make a directory for this file.
                # otherwise just move the current file to the destination directory.
                directory = join(ROOT_DIR, SUPPORTED_FILE_FORMATS[current_file_formate])

                if exists(directory):
                    # move the file to the destination directory.
                    source = join(ROOT_DIR, d)
                    destination = directory
                    
                    try:
                        print "moving file: " + d  
                        shutil.move(source, destination) # move the current file.
                        print "success!"
                    except Exception as e:
                        print d + " : is a duplicate file. unable to move >>" + d + "<< file."
                        # you can call shutil.copy(src, des) to copy file
                else:
                    try:
                        makedirs(directory)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise "Please buy a new machine :P"
                        else:
                          print "can not make directory: " + directory
                          print e
            else:
                # the file formet is no added in our FILE_FORMATS.
                # you can add this file formate to FILE_FORMATS or
                # this file is moved to OTHER dirSUPPORTED_ectory.
                directory = join(ROOT_DIR, "others")

                if exists(directory):
                    # do the move work
                    source = join(ROOT_DIR, d)
                    destination = directory
                    
                    try:
                        print "moving file: " + d 
                        shutil.move(source, destination)
                        print "success!"
                    except Exception as e:
                        print d + " : is a duplicate file. unable to move >>" + d + "<< file."
                        # you can call shutil.copy(src, des) to copy file
                else:
                    try:
                        makedirs(join(ROOT_DIR, "others"))
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise "Please buy a new machine :P"
                        else:
                            print "can not make directory: " + "others"
                            print e

def main():
    # process the command line argument.
    desc = "Script arrange all the files of a given directory."
    help_text = 'Give a valid path/directory location.'

    parser = ArgumentParser(description=desc)
    parser.add_argument('-p', '--path', type = str, help = help_text, required=True)
    args = parser.parse_args()
    root_dirrectory = args.path

    # arg parse finish. now just call the junk arranger function.
    junk_arranger(root_dirrectory)

if __name__ == '__main__':
    main()
