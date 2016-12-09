import re

def lineWrap72Char():
  wrapWidth=72
  inp=open(r"C:\cfcc\Learning\udacity\python\GlenngarryGlenRoss.txt")
  out=open(r"C:\cfcc\Learning\udacity\python\GlenngarryGlenRossNew.txt",'w+')
  for line in iter(inp.readline, ''):
    while (len(line) > wrapWidth):
      for eol in range(wrapWidth,0,-1):
        if re.match('\s', line[eol]):
          nextline=line[eol+1:]
          out.write(line[0:eol]+'\n')
          line=nextline
          break          
    #if len(line) > 0:
    if re.match('\S', line):
      out.write(line+'\n')
  inp.close()
  out.close()
  ''' if line.l
    line[71] in [\w]'''

lineWrap72Char()
