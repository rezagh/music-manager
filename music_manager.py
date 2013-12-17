import re
import os
from mutagen.easyid3 import EasyID3

class MusicManager():
	
	metas = []
	replace_www_url= r'(?i)\(.*www.*\.com.*\)'
	replace_http_url=''
	common_regex_list=[replace_www_url]
	
	def __init__(self):
		self.metas = create_metadata()

	def f__init__(self,library_path):
		self.metas = create_metadata(library_path)
		
	def count(self):
		return len(self.metas)
	
	def apply_common_regex_list(self,value):
		''' apply all common regex to this value string '''
		for regex in self.common_regex_list:
			value = re.sub(regex,"",value)
		
		print 'final value:' + value	
		return value;
	
	#apply a regex 				
	def apply_regex(self,value,regex):
		value =  re.sub(regex,"",value)
		print 'final value:' + value	
		return value
	
	def set_audio_meta(self,audio, key, value):
		audio[key] = value
		audio.save()
		
		
	def fix_bad_meta(self,*regex_list):
		"""apply a list of regex to all meta values. if no regex provided will use common ones"""
		for meta in self.metas:
			meta_keys = list(meta)
			for key in meta_keys:
				value = meta[key]
				if regex_list is None or len(regex_list) == 0:
					value = self.apply_common_regex_list(value)
					# set the value back
				else:
					value = self.apply_regex(value,regex_list[0])
					# set the value back
				
				#set_audio_meta(meta["audio"],key,value)





path = '/Users/rezaghafari/Music/music'


def create_metadata():
    metas = []
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if '.mp3' in f or '.MP3' in f:
                file_path = dirpath + '/' + f
                #do_regex_www(title, dirpath + '/' + f)
                #do_regex_http(title, dirpath + '/' + f)
                meta = {}
                audio = EasyID3(file_path)
                meta["audio"] = audio
                meta["path"] = file_path
                meta["title"] = get_audio_meta(audio,'title')
                meta["artist"]=get_audio_meta(audio,'artist')
                meta["album"]=get_audio_meta(audio,'album')
                meta["performer"] = get_audio_meta(audio,'performer')
                meta["composer"]=get_audio_meta(audio,'composer')
                meta["genre"]=get_audio_meta(audio,'genre')
                
                #print meta
                metas.append(meta)
    return metas

def get_audio_meta(audio,meta_name):
    #the following returns a list 
    try:
        value = audio[meta_name] [0]
        return str(value)
    except Exception:
        return ""
