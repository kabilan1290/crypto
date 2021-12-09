#!/usr/bin/python
# loopbase64
import sys

args = sys.argv[1]

i =0
try:
	while True:
		div = len(args) % 4
		if(div == 0):
			args = args.decode("base64")
			print(args)
		#if ( == True):
		#	continue
		#else:
		#	break
		
		else:
			print(args)
			break

except:
	print("")
       

