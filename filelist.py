#!/usr/bin/python
from os import listdir
from os.path import isfile, join, basename
import argparse
HTML_Begin='''<html>
<head><title>%TITLE%</title>
<meta charset="utf-8" /> 
<style type="text/css"><!--
.filelist{	padding-left:12px; }
body .filelist {display:block;}
.filelist .filelist {display:none; border-width: 0 0 0 1px; border-style:solid; border-color:#000; margin-left:-4px;}
.file .folder {display:block;}
.folder a{font-weight:bold; color:inherit; text-decoration:none; cursor:default;}
.folder a.open:before{content:"-";  margin-left:-6px;}
.folder a.closed:before{content:"+";  margin-left:-10px;}
--></style>
<script type="text/javascript">
function showall()
{
	allfolders=document.getElementsByClassName('folder');
	for (var i=0; i<allfolders.length; i++)
	{
		link=allfolders[i].getElementsByTagName('a')[0];
		link.setAttribute('class','open',false);
		filelist=allfolders[i].getElementsByTagName('div')[0];
		filelist.style.display='block';
	}
}
function hideall()
{
	allfolders=document.getElementsByClassName('folder');
	for (var i=0; i<allfolders.length; i++)
	{
		link=allfolders[i].getElementsByTagName('a')[0];
		link.setAttribute('class','closed',false);
		filelist=allfolders[i].getElementsByTagName('div')[0];
		filelist.style.display='none';
	}
}
function clickfolder(name)
{
	link=document.getElementById(name).getElementsByTagName('a')[0];
	filelist=document.getElementById(name).getElementsByTagName('div')[0];
	if (filelist.style.display=='block'){
		link.setAttribute('class','closed',false);
		filelist.style.display='none';}
	else{
		filelist.style.display='block';
		link.setAttribute('class','open',false);}
}
</script>
</head>
<body>
<h1>%TITLE%</h1>
Alle <a onclick="showall()" class="closed">einblenden</a>/<a onclick="hideall()" class="open">ausblenden</a>
'''
HTML_End='</body></html>'
HTML_Headers='<h2>%NAME%</h2>'
HTML_Filelist_Begin='<div class="filelist">'
HTML_Filelist_End='</div>'
HTML_File='<div class="file">%NAME%</div>'
HTML_Folder='''
<div class="folder" id="%ID%"><a tag="%ID%" href="#%ID%" class="closed" onclick="clickfolder('%ID%')">%NAME%</a>
 %FILELIST%
</div>
'''
parser = argparse.ArgumentParser(description='create a pretty html page of file-trees')
parser.add_argument('--top', '-t', action='store_true', help='use the top folders as headlines')
parser.add_argument('--ignore-subdirs', '-is', action='store_true', help='ignore all subfolders')
parser.add_argument('--title', type=str, action='store', help='title of the webpage')
parser.add_argument('path', nargs='*', type=str, action='store', help='folders to print')
args = parser.parse_args()

folderId = 0
def AddFile(file):
  return HTML_File.replace("%NAME%",file)
def AddDir(dir, id, top = False):
  if top:
    res = HTML_Headers.replace('%NAME%',basename(dir))
    res += '%FILELIST%'
  else:
    res = HTML_Folder.replace('%NAME%',basename(dir))
    res = res.replace('%ID%',str(id))
  return res.replace('%FILELIST%',AddFilelist(dir))
  
def AddFilelist(dir, top = False):
  global folderId
  if top:
    result = ""
  else:
    result = HTML_Filelist_Begin
  oldFolderId = folderId
  for d in sorted(listdir(dir)):
    if not isfile(join(dir,d)):
      folderId += 1
      result += AddDir(join(dir,d),folderId, top)
  if top and oldFolderId == folderId:
    result += HTML_Headers.replace('%NAME%',basename(dir))
  for f in sorted(listdir(dir)):
    if isfile(join(dir,f)):
      result += AddFile(f)
  if top:
    return result
  return result + HTML_Filelist_End
  
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
    
  
res = HTML_Begin.replace('%TITLE%',title)
for folder in path:
  if printHead and not args.top:
    res += HTML_Headers.replace('%NAME%',basename(folder))
  res += AddFilelist(folder,args.top)
res += HTML_End
print res