import random,sys

dump =[]

def clone():

	nama = input('masukan nama : ')
	jumlah = int(input('masukan jumlah : '))
	for x in range(jumlah):

		angka = str(random.randint(00000,99999))
		mail = f'{nama}{angka}@gmail.com|'+nama
		if mail in dump:pass
		else:dump.append(mail)
		sys.stdout.write(f'\rTotal Dump : {len(dump)}')
		sys.stdout.flush()
	print()
clone()
