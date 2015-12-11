html = {
'begin': lambda title : '''<html>
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
'''.replace('%TITLE%',title),
'end':'</body></html>',
'headers':lambda name : '<h2>'+name+'</h2>',
'filelist_begin':'<div class="filelist">',
'filelist_end':'</div>',
'file': lambda name:'<div class="file">%NAME%</div>'.replace('%NAME%',name),
'folder':lambda id, name, filelist: '''
<div class="folder" id="%ID%"><a tag="%ID%" href="#%ID%" class="closed" onclick="clickfolder('%ID%')">%NAME%</a>
 %FILELIST%
</div>
'''.replace('%ID%',id).replace('%NAME%',name).replace('%FILELIST%',filelist),
}
