def splitblocks(c):
	order = len(c)/16
	chunks, chunk_size = len(c), len(c)/order
	a = [ c[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
	raw_blocks = a
	blocks = []
	for i in range(0,order):
		blocks.append(a[i].encode("hex"))
	return blocks
