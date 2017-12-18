s=open("/etc/passwd","r")
import re
d={}

for i in s.readlines():
   j=i.split(":")
   print(j[5])
#   if "[a-z]" in j[5]:
   k=re.search(r'\bw+\b',j[5])
   if k:
      print j[5]
      #d.update({"%s":"a"})%(j[5])

