import urllib

def DownloadSmilie(base_dir, url):
  webFile = urllib.urlopen(url)
  localFile = open("%s%s" % (base_dir, url.split('/')[-1].replace('~','')), 'wb')
  localFile.write(webFile.read())
  webFile.close()
  localFile.close()

def GetSmilies():
  f = urllib.urlopen(
      "http://forums.somethingawful.com/misc.php?s=&action=showsmilies")
  smilies = []
  for line in f:
    if line.strip() == '<li class="smilie">':
      raw_text, raw_src = f.readline(), f.readline()
      #This is a hack to get the data from the forums.
      #I hope they dont change the html format or I'll have to rewrite it
      #to use the DOM. Sorry for all the huge single lines!
      text = raw_text[20:raw_text.index('</div>',20)]
      url = raw_src[raw_src.index('src="')+5:raw_src.index('" title')]
      img_name = raw_src[raw_src.index('src="')+5:raw_src.index('" title')].split('/')[-1].replace('~','')
      
      print 'Downloading %s' % img_name
      DownloadSmilie("assets/emotes/", url)            
      smilies.append((text,img_name))
  return "smilies = [%s]" % '\n\t'.join(["('%s', '%s')," % (text, img) for (text, img) in smilies])

def UpdateSmilies():
  f = open('smilies.py', 'w')
  f.write(GetSmilies())
  f.close()


if __name__ == '__main__':
  import sys, os, subprocess
  print 'Updating smilies..'
  path = os.path.abspath(os.path.dirname(sys.argv[0]))
  UpdateSmilies()
  print '\n############################\n'
  if len(sys.argv) == 2 and sys.argv[1] == "-send":
    
    p = subprocess.Popen(['appcfg.py','update',path])
    p.wait()
  else:
    print 'Smilies updated. Run:\n\n\tappcfg.py update %s\n' % path
    print 'or run python update-smilies.py with the -send flag\n'  