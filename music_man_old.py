import os
from os import listdir
from os.path import isfile, join
import collections

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2
from mutagen.easyid3 import EasyID3
import re

path = '/Users/rezaghafari/Music/music'

def do_regex_www(title,file):
	print 'old:' + title
	new_title = re.split(r'[{*\(\[].*[wW][wW][Ww].*',title)[0]
	print 'new:' + new_title
	set_title(file,new_title)
	print

def do_regex_http(title,file):
	if 'http' in title:
		print file
		print 'old:' + title
		new_title = re.split(r'http.*',title)[0]
		print 'new:' + new_title
		set_title(file,new_title)
		print

def replace_titles():
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			if '.mp3' in f or '.MP3' in f:
				title = get_mp3_title2(dirpath + '/' + f)	
				#do_regex_www(title, dirpath + '/' + f)
				do_regex_http(title, dirpath + '/' + f)
				#print f

def find_in_title(text):
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			if '.mp3' in f or '.MP3' in f:
				title = get_mp3_title2(dirpath + '/' + f)	
				if text in title:
					print title
	
#######################

def check_empty_title():
	for t,f in get_titles_with_path():
		if t.isspace() or t is None or t is "":
			print f
			print '-'
			

#def get_mp3_title(mp3_file):
#	if '.mp3' not in mp3_file or '.MP3' not in mp3_file:
#		return None
#	audio = MP3(mp3_file)
#	
#	try:
#		return audio["TIT2"]
#	except KeyError:
#		print 'no tit2 fro ' + mp3_file
#		return None

def get_mp3_title2(file):
	audio = EasyID3(file)
	#the following returns a list 
	try:
		title = audio["title"] [0]
		return title
	except Exception:
		return ""
	
def print_duplicate_files():
	files = os.walk(path)

	allfiles = []
	for f in files:
		allfiles.extend(f[2])
	
	#count and print the duplicates
	print "\n".join( [x for x, y in collections.Counter(allfiles).items() if y > 1])

def set_title(file, title):
	audio = EasyID3(file)
	audio["title"] = title
	#audio.add(TIT2(encoding=3, text=title))
	audio.save()

def get_titles_with_path():
	titles_path_tuples = []
	for dirpath, dirnames, files in os.walk(path):
		for f in files:
			if '.mp3' in f or '.MP3' in f:
				#print f
				title = get_mp3_title2(dirpath + '/' +  f)
				titles_path_tuples.append((str(title),dirpath + '/' + f))
	return titles_path_tuples



def get_files_by_title(title,title_file_tuples):
	return [f for t,f in  title_file_tuples if t == title]
	
	
def find_duplicate_titles():
	title_file_tuples = get_titles_with_path()
	titles = [t for t,f in  title_file_tuples]
	bucket = [] # not to print duplicate
	for title,file in title_file_tuples:
		if(titles.count(title) > 1 and title not in bucket):
			bucket.append(title)
			print title
			print get_files_by_title(title, title_file_tuples)
			print '-'


	

#count and print the duplicates in a list
#print "\n".join( [x for x, y in collections.Counter(titles).items() if y > 1])
	
#replace_titles()
#get_titles_with_path()
#check_empty_title()
#set_title('/Users/rezaghafari/Music/music/Selection/mo sharabi/Shahin S2 & Danesh - Lamsam Kon [128].mp3','Lamsam Kon')
#print get_mp3_title2('/Users/rezaghafari/Music/music/Selection/mo sharabi/Shahin S2 & Danesh - Lamsam Kon [128].mp3')

#print get_title2('/Users/rezaghafari/Music/music/25 Band/Bia Bia.mp3');	
#print get_title('/Users/rezaghafari/Music/music/.DS_Store')
