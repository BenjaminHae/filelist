html = {
'begin':lambda title: title,
'end':'',
'headers':lambda name: name,
'filelist_begin':'',
'filelist_end':'',
'file':lambda name: name,
'folder':lambda id, name, filelist:id+name+filelist,
}
