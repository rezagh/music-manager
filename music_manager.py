import re
import os
from mutagen.easyid3 import EasyID3


class MusicManager(object):

    metas = []
    #(?i) starts case-insensitive mode
    #(?-i) turns off case-insensitive mode
    www_url_inside_parans= r'(?i)\(.*www.*\.com.*\)'
    replace_http_url=''
    common_regex_list=[www_url_inside_parans]

    # 	def __init__(self):
    # 		self.metas = create_metadata()

    def __init__(self,library_path):
        self.metas = create_metadata(library_path)

    def count(self):
        return len(self.metas)

    def __apply_regexes(self,value,regexes):
        """ apply a bunch of regexes """

        for regex in regexes:
            value = re.sub(regex,"",value)

        print 'final value:' + value
        return value

    def set_audio_meta(self,audio, key, value):
        audio[key] = value
        audio.save()

    def __get_keys_for_print(self,meta):
        meta_keys = list(meta)
        return [key for key in meta_keys if key != "audio" and key != "path"]

    def __print_meta_all(self):
        for meta in self.metas:
            print meta["path"]
            for key in self.__get_keys_for_print(meta):
                print " " + key + ": " + meta[key]

    def print_meta(self, regex = None, show_other_non_matching_fields= True):
        """ shows all meta data or by a regex. if a regex is provided then there is an option whether to show other non-matching fields
        when the regex finds a match  """
        #TODO check for blank regex
        if regex is None:
            self.__print_meta_all()
        else:
            matching={}
            non_matching={}
            for meta in self.metas:
                for key in self.__get_keys_for_print(meta):
                    value = meta[key]
                    if re.search(regex, value) is not None:
                        matching[key] = value;
                    else:
                        non_matching[key] = value

            if len(matching) > 0:
                print meta["path"]
                for key in matching.keys():
                    print "  " + key + " : " + matching[key]
                if show_other_non_matching_fields == True:
                    for key in non_matching.keys():
                        print "  " + key + ": " + non_matching[key]


    def fix_bad_meta(self,*regex_tuple):
        """apply a list of regexes to all meta values. if no regex provided will use common regexes"""
        for meta in self.metas:
            meta_keys = list(meta)
            valid_keys = [key for key in meta_keys if key != "audio"]
            for key in valid_keys:
                value = meta[key]
                if regex_tuple is None or len(regex_tuple) == 0:
                    value = self.__apply_regexes(value, self.common_regex_list)
                else:
                    value = self.__apply_regexes(value,regex_tuple)
                self.set_audio_meta(meta['audio'], key, value)


def __get_originla_keys():
    return ["title","artist","album","performer","composer","genre"]

def __get_all_keys():
    return __get_originla_keys() + ["audio","path","filename"]

def __get_audio_meta(audio,meta_name):
    #the following returns a list 
    try:
        value = audio[meta_name] [0]
        return str(value)
    except Exception as e:
        return " error fetching key: " + meta_name + " - " + str(e)


def create_metadata(path):
    """ path is either a single file path or a dir """
    def get_meta(file_path):
        local_meta = {}
        audio = EasyID3(file_path)
        for key in __get_all_keys():
            if key == 'audio': local_meta[key] = audio
            elif key == 'path': local_meta[key] = file_path
            elif key == 'filename': local_meta[key]= os.path.split(file_path)[1]

            elif key == 'title': local_meta[key] = __get_audio_meta(audio,key)
            elif key == 'artist': local_meta[key]=__get_audio_meta(audio,key)
            elif key == 'album': local_meta[key]=__get_audio_meta(audio,key)
            elif key == 'performer': local_meta[key] = __get_audio_meta(audio,key)
            elif key == 'composer': local_meta[key]=__get_audio_meta(audio,key)
            elif key == 'genre': local_meta[key]=__get_audio_meta(audio,key)
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


#keep this handy outside of the class
def set_meta(file_path, key, value):
    audio = EasyID3(file_path)
    audio[key] = value
    audio.save()

#keep this handy outside of the class
def print_meta(file_path):
    audio = EasyID3(file_path)
    for key in __get_originla_keys():
        print key + ": " + __get_audio_meta(audio, key)
	
