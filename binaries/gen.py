#!/usr/bin/python
import time
import sys
import os

mypath=os.path.dirname(os.path.abspath(__file__))
os.listdir(mypath)
fp=open("index.html","w")
fp.write( """<html><head><title>Windows Partio/SeExpr Binaries</title></head>
<style>
body {font-family:Arial;}x
p {font-family:Arial;}
h1 {font-family:Arial;}
h2 {font-family:Arial;}
table {background: #000000; }
th {background: #dddddd; text-align:left; font-family:Arial; font-weight: bold; padding: 5px; }
td {background: #eeeeee; font-family:Arial; padding: 5px;}
</style>
<body>
<h1>SeExpr and Partio Windows Binaries</h1>
<p>
Windows build tends to be more difficult to do than Linux. The following
builds are built with Qt 4.8.4 and Visual Studio 10.  Since SeExpr and Partio 
use cmake. If you wish to build yourself, usually, you can do:


<h2>SeExpr</h2>

<table>
<tr><th>Filename</th><th>Size</th><th>Date</th>
""")
for i in os.listdir(mypath):
    if i.endswith(".zip"):
        full=os.path.join(mypath,i)
        size=os.stat(full).st_size
        datetime=time.ctime(os.stat(full).st_mtime)
        mb=size/float(1<<20)
        fp.write( "<tr><td><a href=\"%s\">%s</a></td><td>%.1f MB</td><td>%s</td></tr>\n"%(i,i,mb,datetime))
fp.write("""
</table>

<h3>Doing your own Windows builds</h3>

<ol>
<li>Clone the git repo
<li>On Windows, the parser and scanner generators are not usually available.
You can either download bison/flex, or you can build seexpr on Linux or
Mac OS and copy the generated .cpp and .h for the parser/scanner into the
SeExpr source. To do the latter, build as usual on Linux, and then copy
src/SeExpr/generated/* from your Linux source tree to your windows source
tree.
<li>Open a visual studio command prompt
<li>cd into the source directory and make a build directory and cd into it
<ol>
<li>cd c:\\builds\\seexpr
<li>md build
<li>cd build
</ol>
<li>Run CMake c:\\program files\\cmake 2.8\\bin\\cmake-gui ..\\</li>
<li>Choose a NMake makefile
<li>Click configure and then generate
<li>make install</li>
</ol>
</p>


</body>
</html>
""")

