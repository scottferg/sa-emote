import urllib

def GetSmilies():
  f = urllib.urlopen(
      "http://forums.somethingawful.com/misc.php?s=&action=showsmilies")
  smilies = []
  for line in f:
    if line.strip() == '<li class="smilie">':
      raw_text, raw_src = f.readline(), f.readline()
      smilies.append((
            raw_text[20:raw_text.index('</div>',20)],
            raw_src[raw_src.index('src="')+5:raw_src.index('" title')].split('/')[-1]
          ))
  return smilies

smilies = GetSmilies()
print "smilies = ["
for smilie in smilies[:-1]:
  print "('%s', '%s'), " % smilie
print "('%s', '%s')]" % smilies[-1]
