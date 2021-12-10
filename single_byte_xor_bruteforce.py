#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pwn


encoded = "1314190e1c1001024a0825194e145d0e251849251f4e091316032518084a11491407".decode("hex")

for i in range(255):
	decoded = pwn.xor(encoded,i)
	if ('inctf' in decoded):
		print(i)
		print(decoded)
