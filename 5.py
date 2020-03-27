import random 
import sys
import time
import hashlib


def hash(x):
	x = x.encode()
	m = hashlib.sha1()
	m.update(x)
	return m.hexdigest()


try:
	i = int(input(">>"))
	k = str(i)
	f = hash(k)


	count = 0
	s = time.time()
	while True:
		p = random.randint(0, i)
		p = hash(str(p))
		print(p)
		count += 1
		if p == f:
			b = time.time()
			print(" \nFound {} in {} seconds took {} times".format(f, (b-s), count))
			print("\n\toriginal: {}\n".format(i))			
			if count < int(k):
				print("Positive by {}".format(int(k) - count))
			else:
				print("Negative by {}".format(int(k) - count))
			break


except KeyboardInterrupt:
	b = time.time()	
	print("\n\t KeyboardInterrupt \n\n\tdid not find {} in {} seconds interrupted after {} times".format(f, (b-s), count))
	print("\n\toriginal: {}\n".format(i))
