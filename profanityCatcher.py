#Taking Udacity Python basics course.  Expanding on profanity tracker to grab
#source movie from IMDB, and break it into smaller quote lines, then feed
#that into the wdylike profanity checker.

#Using urllib.request due to python 3.5.2
from urllib.request import urlopen
#reg expression needed to strip spaces and replace with %20
import re

#Profanity Catcher, identifies lines in a file containing profanity
def profanityCatcher():
  #imdb page for quotes from profanity laden Glengarry Glen Ross
  url="http://www.imdb.com/title/tt0104348/quotes"
  #swapping the previous line for the next one checks suicide squad
  #A future enhancement will be to just get a movie name, then use that to
  #find the quotes page, and identify curses.
  #url="http://www.imdb.com/title/tt1386697/quotes"
  #this one's Frozen:
  #url="http://www.imdb.com/title/tt2294629/quotes"
  connection=urlopen(url)
  inp = connection.read()
  #Format the input data and check profanity on each line of quotes
  formatAndCheck(inp)
  connection.close()


def formatAndCheck(inp):
  wrapWidth=72    #line Width
  lines=inp.split(b'\n')   #break the input into individual lines
  for line in lines:       #look at each line
    line=(line).decode('utf-8')    #decode it from "bytes" to string
    #lines of actual quotes will match the following test
    if re.match('^[a-zA-Z].*</p><p>',line):   
      line=line[0:-7]      #strip the </p><p> off the end of the quote
      #the quotes are so long that urlopen can't handle some of them.
      #break them up into 72 char chunks.  End each line on a word boundary
      while (len(line) > wrapWidth):
        #find the end of the last word that can fit in the 72 char string
        for eol in range(wrapWidth,0,-1):
          #Hit some whitespace, put the rest on the next line
          if re.match('\s', line[eol]):
            nextline=line[eol+1:]
            #check it!
            check_profanity(line[0:eol])
            #proceed to handle the rest of the line
            line=nextline
            break
      #if the next line contains more than just whitespace, check it
      if re.match('\S', line):
        check_profanity(line) 
    
def check_profanity(text_to_test):
  #get the url with our text that we want to check
  url="http://www.wdylike.appspot.com/?q="+text_to_test
  #replace ' ' with '%20'
  urlNoSpace = re.compile(' ')
  url = urlNoSpace.sub('%20', url)
  #check it out
  connectwdyl=urlopen(url)
  output = connectwdyl.read()
  #did this line have profanity?
  if "true" in str(output):
      #report profane lines!!!
      print("Naughty: "+text_to_test)
  connectwdyl.close()
  #NOTE: wdylike contains a flaw.  It includes curse words that are contained
  #as parts of non-curse words. ie, it flags "asset" for containing "ass"
  
profanityCatcher()
