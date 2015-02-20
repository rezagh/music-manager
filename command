Name:
	Music ?

Description:
	
Usage:   
  
  mmd <command> -[options]

Commands:
  show                        show music files and their meta data
  set						  set meta data value
  append					  Append to the end of a meta data value
  help                        Show help for commands
  test_run					  Shows you how it will look if the meta data value is removed 
  							  but it does not remove it actually.
  

Options:
  -lib <file>     			Music library folder or a single file                
  -regex <regex>  			Regular expression which applies to meta values.
  -meta <meta data>			A particular meta data key to work with. Others will be ignored. If not provided then
  							will be applied to all meta keys.
  							Available keys are: "title","artist","album","performer","composer","genre"
  -value <value>			The value to replace

  -show_non_matching		In the output shows other meta data that do not match the regex 

Examples:

  
