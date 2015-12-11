template_markdown = {
'begin':lambda title: title+"\r\n"+"="*len(title)+"\r\n",
'end':'',
'headers':lambda name: name+"\r\n"+"-"*len(name)+"\r\n",

'filelist_begin':'',
'filelist_end':'',
'file':lambda name: "  * "+name+"  \r\n",
'folder':lambda id, name, filelist:"  * **"+name+"**  \r\n"+''.join(map(lambda s: " "*4+s, filelist.splitlines(True)))+"\r\n",
}
