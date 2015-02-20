import re

print re.sub(r'(?i)[\{\[\(].*\.com.*[\}\]\)]', "" , "abc [www.AGBB.COM } abc")