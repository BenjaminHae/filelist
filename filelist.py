#!/usr/bin/python
from os import listdir
from os.path import isfile, join, basename
import argparse
import sys
from template_html import template_html
from template_markdown import template_markdown

parser = argparse.ArgumentParser(description='create a pretty html page of file-trees')
parser.add_argument('--top', '-t', action='store_true', help='use the top folders as headlines')
parser.add_argument('--ignore-subdirs', '-is', action='store_true', help='ignore all subfolders')
parser.add_argument('--title', type=str, action='store', help='title of the webpage')
parser.add_argument('--type', type=str, action='store', default='html', choices=['html','markdown'],  help='type of output')
parser.add_argument('--all', '-a', action='store_true', help='show hidden files(UNIX only)')
parser.add_argument('--output', '-o', type=str, action='store', help='output file(default STDOUT), not implemented yet')
parser.add_argument('path', nargs='*', type=str, action='store', help='folders to print')
args = parser.parse_args()

template=eval('template_'+args.type)

folderId = 0
def AddFile(file):
  return template['file'](file)
def AddDir(dir, id, top = False, showHidden = False):
  if top:
      res = lambda filelist: template['headers'](basename(dir))+filelist
  else:
      res = lambda filelist: template['folder'](str(id),basename(dir), filelist)
  return res(AddFilelist(dir, showHidden = showHidden))
  
def AddFilelist(dir, top = False, showHidden = False):
  global folderId
  if top:
    result = ""
  else:
    result = template['filelist_begin']
  oldFolderId = folderId
  content = sorted(listdir(dir))
  if not showHidden:
    content = filter( lambda f: not f.startswith('.'), content)
  for d in content:
    if not isfile(join(dir,d)):
      folderId += 1
      result += AddDir(join(dir,d),folderId, top, showHidden)
  if top and oldFolderId == folderId:
    result += template['headers'](basename(dir))
  for f in content:
    if isfile(join(dir,f)):
      result += AddFile(f)
  if top:
    return result
  return result + template['filelist_end']
  
path = args.path
printHead = True
if path == None or len(path) == 0:
  path = ['.']
if len(path)==1:
  printHead=False
  
title = args.title
if title == None or title=="":
  title = "List of files"
  if not printHead:
    title += " in "+path[0]
    
  
call = " ".join(sys.argv)
res = template['begin'](title, call)
for folder in path:
  if printHead and not args.top:
    res += template['headers'](basename(folder))
  res += AddFilelist(folder, args.top, args.all)
res += template['end'](call)
print res
