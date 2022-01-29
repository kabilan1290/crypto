from pwn import *
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    string =""
    length = len(s)
    length2 = len(k)
    assert(length==length2)
    for i in range(0,length):
    	a = s[i]
    	b = k[i]
    	
    	for j in range(0,length):
    		    		
    		string += (xor(int(a[j]),int(b[j])))
    print(string)





add_round_key(state, round_key)

