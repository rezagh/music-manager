import music_manager 

mm = music_manager.MusicManager()

print mm.count()

mm.fix_bad_meta(r'(?i)\(.*www.*\.com.*\)')

#print mm.apply_common_regex_list("")