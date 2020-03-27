
from Crypto.Util import number 
import random
import hashlib


#print(17835635181437510786540640217769607821935524769391490880245825820263755024410730910720769251669910263810764336054046768324152754692617814085767803608435943593614902214622615917906013008997929692560049035430705643693688924962459083022160405925189483095408000583906665074751003001078899275530109308330711439704752369530609102991155381039817787680270569659689794124191450207847305132080619465290257301833606681726327282744490833799515646124893995110178325218054748928674791944900522818081465551697807723193133168351139540256826080777999530679190655670048815590738739646902928114415937186057343236644624674244831602585013328534283139842507995279093879171480879378360384033703524354011283142728476953528547585443679807985829540507)
def find():
	while True:
		x = number.getPrime(random.randint(2048, 4096))
		print(x)
		if number.isPrime((x-1)//2):
			print("{} is a safe prime".format(x))
			break
		else:
			print("not prime \n")
			continue
