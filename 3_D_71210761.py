import random 
apaja = input("Masukkan tipe yang ingin anda coba : ")


r_n1 = random.randint(1,20)
e = r_n1
r_n2 = random.randint(1,20)
l = r_n2
r_n3 = random.randint(1,20)
s = r_n3
r_n4 = random.randint(1,20)
a = r_n4
options = ["<",">","=="]
random_o = random.randint(0,2)
c_pick = options[random_o]

def generateSoal():
	print("(benar/salah) jika", end=" ")

	if apaja.lower()=="pengurangan":
		print(r_n1,"-",r_n2,c_pick,r_n3,"-",r_n4, sep='')
	elif apaja.lower()=="penjumlahan":
		print(r_n1,"+",r_n2,c_pick,r_n3,"+",r_n4, sep='')
	else:
		print("hanya ada tipe pengurangan/penjumlahan")

generateSoal()
jawaban = input("Masukkan Jawaban Anda: ")


def cekHasil():
	if c_pick == "<" and apaja.lower() == "pengurangan":
		if ((e-l)<(s-a)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif c_pick == "<" and apaja.lower() == "penjumlahan":
		if ((e+l)<(s+a)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")		
	elif c_pick == ">" and apaja.lower() == "pengurangan":
		if ((e-l)>(s-a)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif c_pick == ">" and apaja.lower() == "penjumlahan":
		if ((e+l)>(s+a)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah!")	
	elif c_pick == "==" and apaja.lower() == "pengurangan":	
		if ((e-l)==(s-a)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif c_pick == "==" and apaja.lower() == "penjumlahan":
		if ((e+l)==(s+a)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")	
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

cekHasil()