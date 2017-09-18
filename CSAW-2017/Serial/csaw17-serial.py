from pwn import *
import binascii

r = remote('misc.chal.csaw.io', 4239)

print "> " + r.recvline()

counter = 0
flag=''
while(1):
	data = r.recvline()
	
	for x in range (1, 10):
		if data[x] == '1':
			counter = counter + 1	

	if counter % 2 == 0:
		flag = flag + data[1:-3]
		n = int(flag, 2)
		final = binascii.unhexlify('%x' % n)
		print final
		
		r.send('1')
		print data[1:-2]
	else:
		r.send('0')

	counter = 0

print r.recvuntil("END\n")

