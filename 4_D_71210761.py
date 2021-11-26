x = 0
def tabakangka():
	global x
	print("Apakah 4?\nApakah tebakan sudah benar ?\nlebih kecil (0)\nlebih besar (1)\nbenar (2)")
	b = int(input(": "))
	x += 1

	if b == 2:
		print("Jumlah tebakan : ", x)
		print("Program Selesai !")

	elif b == 1:
		print("Apakah 6?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		d = int(input(": "))
		x += 1

		if d == 2:
			print("Jumlah tebakan :", x)
			print("Program Selesai !")

		elif d == 0:
			print("Hasil Penjumlahannya Pasti 5 !")
			x +=1
			print("Jumlah tebakan :", x)
			print("Program Selesai !")

		elif d == 1:
			print("Hasil Penjumlahannya Pasti 7 !")
			x +=1
			print("Jumlah tebakan :", x)
			print("Program Selesai !")		

            
	elif b == 0:
		print("Apakah 2?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		c = int(input(": "))
		x += 1

		if c == 2:
			print("Jumlah tebakan :", x)
			print("Program Selesai !")

		elif c == 0:
			print("Hasil Penjumlahannya Pasti 1 !")
			x +=1
			print("Jumlah tebakan :", x)
			print("Program Selesai !")

		elif c == 1:
			print("Hasil Penjumlahannya pasti 3 !")
			x +=1
			print("Jumlah tebakan :", x)
			print("Program Selesai !")



print("Untuk memulai program masukkan (-1) untuk mulai")
a = int(input(": "))
if a == -1 : 
	tabakangka()
else : 
	print("Program tidak berhasil dijalankan")