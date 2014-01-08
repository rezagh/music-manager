import music_manager 

path = '/Users/rezaghafari/Music/test1'
mm = music_manager.MusicManager(path)

print mm.count()

#mm.show_meta()

#mm.show_meta_by_regex(r'Ebi')

#mm.fix_bad_meta(r'(?i)\(.*www.*\.com.*\)')
#mm.fix_bad_meta()

#print mm.apply_common_regex_list("")