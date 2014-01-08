import re
import os
from mutagen.easyid3 import EasyID3

class MusicManager(object):
	
	metas = []
	replace_www_url= r'(?i)\(.*www.*\.com.*\)'
	replace_http_url=''
	common_regex_list=[replace_www_url]
	
# 	def __init__(self):
# 		self.metas = create_metadata()

	def __init__(self,library_path):
		self.metas = create_metadata(library_path)
		
	def count(self):
		return len(self.metas)

	def apply_regexes(self,value,regexes):
		''' apply a bunch of regexes '''

		for regex in regexes:
			value = re.sub(regex,"",value)

		print 'final value:' + value	
		return value
	
	def set_audio_meta(self,audio, key, value):
		audio[key] = value
		audio.save()

# 	def set_meta(self,file_path,meta_name,meta_value):
# 		if meta_name == 'audio' or meta_name == 'path' or meta_name == 'filename' :
# 			return
# 		audio = EasyID3(file_path)
# 		audio[meta_name] = meta_value
# 		audio.save()
		
# 	def show_meta(self):
# 		for meta in self.metas:
# 			meta_keys = list(meta)
# 			valid_keys = [key for key in meta_keys if key != "audio"]
# 			print meta["path"]
# 			for key in valid_keys:
# 				value = meta[key]
# 				print "  " + key + " : " + value
			

	def show_meta(self, *regex):
		def print_it():
			
		for meta in self.metas:
			meta_keys = list(meta)
			valid_keys = [key for key in meta_keys if key != "audio"]
			for key in valid_keys:
				value = meta[key]
				if regex is None or len(regex) == 0:

				if re.search(regex, value) is not None:
					print meta["path"]
					print "  " + key + " : " + value

				
	def fix_bad_meta(self,*regex_tuple):
		"""apply a list of regexes to all meta values. if no regex provided will use common regexes"""
		for meta in self.metas:
			meta_keys = list(meta)
			valid_keys = [key for key in meta_keys if key != "audio"]
			for key in valid_keys:
				value = meta[key]
				if regex_tuple is None or len(regex_tuple) == 0:
					value = self.apply_regexes(value, self.common_regex_list)
				else:
					value = self.apply_regexes(value,regex_tuple)




def create_metadata(path):
	''' path is either a single file path or a dir'''

	def get_audio_meta(audio,meta_name):
	    #the following returns a list 
	    try:
	        value = audio[meta_name] [0]
	        return str(value)
	    except Exception:
	        return ""
	
	def get_meta(file_path):
		local_meta = {}
		audio = EasyID3(file_path)
		local_meta["audio"] = audio
		local_meta["path"] = file_path
		local_meta["filename"]= os.path.split(file_path)[1]
		local_meta["title"] = get_audio_meta(audio,'title')
		local_meta["artist"]=get_audio_meta(audio,'artist')
		local_meta["album"]=get_audio_meta(audio,'album')
		local_meta["performer"] = get_audio_meta(audio,'performer')
		local_meta["composer"]=get_audio_meta(audio,'composer')
		local_meta["genre"]=get_audio_meta(audio,'genre')
		return local_meta

	metas = []

	if os.path.isfile(path):
		metas.append(get_meta(path))
		
	if os.path.isdir(path):
	    for dirpath, dirnames, filenames in os.walk(path):
	        for f in filenames:
	            if '.mp3' in f or '.MP3' in f:
	                file_path = dirpath + '/' + f
	                metas.append(get_meta(file_path))
	return metas
    	



