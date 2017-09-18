# CSAW17: Serial

**Category**: Misc  
**Points**: 50

## The Challenge
![Serial Challenge](https://raw.githubusercontent.com/JQuit96/CTF-Write-Ups/master/CSAW-2017/Serial/serial-challenge.png)

## The Solution
Based off the Serial Communications protocol, which is explained [here](https://learn.sparkfun.com/tutorials/serial-communication/rules-of-serial), I realized that each 11-digit number retrieved from the server would consist of 1 **start bit**, 8 **data bits**, 1 **parity bit**, and 1 **stop bit**. A "correct" transmission is one where the number of 1's found between bits 2 and 10, inclusive, is even.  
For example, transmission 00**1**00**11**00**1**1 is valid, while transmission 00**1**00**11**0001 is not.

Once I realized this, I could write a quick script (found at the bottom of the page) that returned 1 if the transmission was valid, and 0 if it wasn't. I kept track of all valid transmissions, parsed their 8-bit data into characters, and concatenated them into a string, which produced the flag.

## Code
~~~~
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
~~~~

## Flag
![Serial Flag](https://raw.githubusercontent.com/JQuit96/CTF-Write-Ups/master/CSAW-2017/Serial/serial-flag.png)
