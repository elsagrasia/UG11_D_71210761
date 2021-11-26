ex=input("Masukkan string : ")

def cekString(ex):
	if ex.replace(".","").isnumeric() == True:
		if float(ex)%2 == 0:
			print(format(float(ex)/2, ".0f"))
		else :
			print(format((round(float(ex))+5)/2, ".0f"))
	else:
		print(ex[::-1])

cekString(ex)