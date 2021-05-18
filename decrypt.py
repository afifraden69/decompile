# kalo gak tau cara gunain nya gak usah pake ya asw
# kalo ada yang error fix sendiri aja :v
# only marshal or zlib base64 from https://github.com/dtz-aditia/comz3

import os
import re
import sys
try: import uncompyle6
except: os.system("python -m pip install uncompyle6")

m=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115]
z=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115]
b64=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101]
b32=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 51, 50, 100, 101, 99, 111, 100, 101]
b16=[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 49, 54, 100, 101, 99, 111, 100, 101]

def kon(tol):
	return "".join([chr(x) for x in tol])

if sys.version[0]!="2":
	python="3.9" if "3.9" in sys.version[0:3] else "3.8"
else:
	exit(" ! gunakan python3")

def kode(file):
	buka=open(file).read()
	xnxx=re.search("b'(.*?)'",buka)
	if xnxx is not None:
		if str(m) in buka:
			if str(z) in buka:
				if str(b64) in buka:
					return "x={}({}({}(b'{}')))".format(kon(m),kon(z),kon(b64),xnxx.group(1))
				else:
					xnxx=re.search("b'(.+)",buka)
					return "x={}({}(b'{}'))".format(kon(m),kon(z),xnxx.group(1).replace("')))",""))
			else:
				xnxx=re.search("b'(.+)",buka)
				return "x=({}(b'{}".format(kon(m),xnxx.group(1))
		else:
			if str(z) in buka:
				xnxx=re.search("b'(.+)",buka)
				return "x={}(b'{}')".format(kon(z),xnxx.group(1).replace("',compile))",""))
			if str(b64) in buka: return "x={}(b'{}')".format(kon(b64),xnxx.group(1))
			if str(b32) in buka: return "x={}(b'{}')".format(kon(b32),xnxx.group(1))
			if str(b16) in buka: return "x={}(b'{}')".format(kon(b16),xnxx.group(1))
			else: exit()
	else: exit()
			
def decom(code):
	global python
	xode=kode(code)
	if xode is not None:
		if "('marshal').loads" in xode:
			open("cache","w").write("try:\n	{}\n	from uncompyle6.main import decompile\n	from sys import stdout\n	decompile({},x,stdout)\nexcept Exception as err: exit('error '+str(err))".format(xode,python))
			out=code[:-3]+"_.py" if len(code) > 4 else code
			os.system("python3 cache > {}".format(out))
			print(" * file save as {}".format(out))
		else:
			if ").decompress" in xode or ").b64decode" in xode or ").b32decode" in xode or ").b16decode" in xode:
				open("cache","w").write("try:\n	{}\n	print(x)\nexcept Exception as err: exit('error '+str(err))".format(xode))
				out=code[:-3]+"_.py" if len(code) > 4 else code
				os.system("python2 cache > {}".format(out))
				print(" * file save as {}".format(out))
			else: exit()
	else: exit()

if __name__=="__main__":
	if len(sys.argv) >= 2:
		if os.path.exists(sys.argv[1]):
			decom(sys.argv[1])
		else:
			exit(" ! file {} tidak ditemukan".format(sys.argv[1]))
	else:
		exit(" ! usage : python3 {} file.py".format(sys.argv[0]))
	
	
