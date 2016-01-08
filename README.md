filelist
========

This simple tool generates a textfile(html or markdown) of the current or specified directory.


```
usage: filelist.py [-h] [--top] [--ignore-subdirs] [--title TITLE]
                   [--type {html,markdown}] [--all] [--output OUTPUT]
                   [path [path ...]]

create a pretty html page of file-trees

positional arguments:
  path                  folders to print

optional arguments:
  -h, --help            show this help message and exit
  --top, -t             use the top folders as headlines
  --ignore-subdirs, -is
                        ignore all subfolders
  --title TITLE         title of the webpage
  --type {html,markdown}
                        type of output
  --all, -a             show hidden files(UNIX only)
  --output OUTPUT, -o OUTPUT
                        output file(default STDOUT), not implemented yet
```
