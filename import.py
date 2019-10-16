import Rumus

def main():

	#keliling segitiga
	a = 4
	b = 3
	c = 5
	
	kel = Rumus.kelilingSegitiga(a, b, c)
	print("KELILING SEGITIGA")
	print("sisi satu\t: ", a)
	print("sisi dua\t: ", b)
	print("sisi tiga\t: ", c)
	print("keliling (a + b + c)\t: ", kel)
	
	#luas segitiga
	a = 4
	t = 3
	
	luas = Rumus.luasSegitiga(a, t)
	print("LUAS SEGITIGA")
	print("alas\t: ", a)
	print("tinggi\t: ", t)
	print("luas (1/2 x a x t)\t: ", luas)
	
	#tinggi segitiga
	L = 6
	a = 4
	
	ting = Rumus.tinggiSegitiga(L, a)
	print("TINGGI SEGITIGA")
	print("luas\t: ", L)
	print("alas\t: ", a)
	print("tinggi ((2 x Luas):a)\t: ", ting)
	
if __name__ == "__main__":
	main()
