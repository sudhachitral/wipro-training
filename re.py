import re
pattern='^S....i$'
string='Suzuki'
r=re.match(pattern,string)
if r:
    print("yess")
else:
    print("no")