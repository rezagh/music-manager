import re
s = 'Lamsam Kon (wWw.MyMusicBaran.Com)'
#print re.split(r'(?i)\(.*www.*\.Com.*\)',s)[1]
#print str("")

print re.sub(r'(?i)\(.*www.*\.com.*\)',"-",s)

from mutagen.easyid3 import EasyID3
#print EasyID3.valid_keys.keys()

audio = EasyID3("/Users/rezaghafari/BiaBia.mp3")
#print audio.pprint()


meta = {"a":"b","c":"d"}
#print list(meta)