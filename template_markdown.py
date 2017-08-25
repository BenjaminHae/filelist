template_markdown = {
'begin':lambda title, call: title+"\n"+"="*len(title)+"\n\n\t"+call+"\n\n",
'end':'',
'headers':lambda name: name+"\n"+"-"*len(name)+"\n",

'filelist_begin':'',
'filelist_end':'',
'file':lambda name: "  * " + name + "\n",
'folder':lambda id, name, filelist:"  * **"+name+"**  \n"+''.join(map(lambda s: " "*4+s, filelist.splitlines(True)))+"\n",
}
