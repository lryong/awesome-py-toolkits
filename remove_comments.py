#/usr/bin/python
#encoding:utf-8
import re,sys
test=str(sys.argv[1])
f=open(test);b=f.readlines();f.close();f1=open('temp.txt','a');k=0;len=len(b)
while True:
	if re.search('[\s|]*<!--(.+)',b[k]) or re.search('<!--',b[k]):
		if re.search('[\s|]*<!--(.+)-->',b[k]):
			b[k]=''
			k+=1
			continue
		b[k]=''
		while not re.search('[\s|]*-->',b[k]):
			b[k]='';k+=1
		else:
			b[k]=''
			continue
	k+=1
	if k==len-1:
		break
for a in range(len):
	f1.write(b[a])
	print b[a]



	