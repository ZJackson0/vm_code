import random 
import sys
import time
import hashlib

i = int(input(">>"))

file = open("out.txt", "w+")

def hash(x):
    x = x.encode()
    m = hashlib.sha512()
    m.update(x)
    return m.hexdigest()

count = 0
s = time.time()
while True:
	p = random.randint(0, i)
	p = hash(str(p))
	print(p)
	count += 1
	if p == hash(str(i)):
		b = time.time()
		file.write("{} found in {} seconds took {} times".format(i,(b-s), count))
		print("found in {} seconds took {} times".format((b-s), count))
		break