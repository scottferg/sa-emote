import smilies
from waveapi import events
from waveapi import model
from waveapi import robot
from waveapi import document

def OnBlipSubmitted(properties, context):
  for blip in context.GetBlips():
    UpdateBlip(blip)

def UpdateBlip(blip):
  doc = blip.GetDocument()
  doc_text = doc.GetText()
  
  updates = []
  for text, src in smilies.smilies:
    i = 0
    while doc_text.find(text, i) != -1:
      i = doc_text.find(text, i)
      updates.append((i, text,
                      "http://sa-emote.appspot.com/assets/emotes/%s" % src))
      i += len(text)
  
  updates.sort()
  updates.reverse()
  for index, text, src in updates:
    doc.DeleteRange(document.Range(index, index + len(text)))
    doc.InsertElement(index, document.Image(url=src))

if __name__ == '__main__':
  myRobot = robot.Robot('sa-emote', 
      image_url='http://sa-emote.appspot.com/assets/awesome.png',
      version='1',
      profile_url='http://sa-emote.appspot.com/')
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
