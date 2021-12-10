#!/usr/bin/python
# loopbase64 solver
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
			print("The end")
			break

except:
	print("")
       

