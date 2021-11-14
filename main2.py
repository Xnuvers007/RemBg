
# Using python 3.9.6
# Solo Coder
# Banten x Tangerang
# 19 Tahun
# Tested just on windows , linux will be create later

try:
    #import glob
    import os, requests, random
    from sys import platform
except ModuleNotFoundError:
    if platform=="linux" or platform=="linux2":
        os.system("apt upgrade")
        os.system("apt update")
        os.system("pip3 install requests")
        os.system("sudo su apt get install curl")
    elif platform=="win32":
        os.system("pip install requests")
    else:
        print("Cannot detect this device")
import owners

asa = os.getlogin()
print(f"Selamat datang {asa}")

try:
    os.mkdir("C:\\Users\\{}\\RemoveBG//hasil".format(asa), 755)
except FileExistsError:
    pass

jeda = input("ini adalah penjedaan, silahkan masukan file foto yang ingin diubah backgroundnya ke dalam folder C:\\Users\\(nama username laptopmu)\\RemoveBG, jika sudah silahkan enter : ")
    
# Folder Gambar Ori / Asli
filepath = 'C:\\Users\\{}\\RemoveBG'.format(asa)

# "small": 1 credit, "medium": 3 credits, "hd": 5 credits, "4k": 8 credits, "auto" = automatically use highest resolution available (based on image size and subscription plan).
img_size = 'auto'


ask = input("Masukan Warna Background (menggunakan bahasa inggris) : ")
warna = ask

#os.mkdir("C:\\ubah\\hasil")


#os.chmod("C:\\ubah\\", 755)
#os.chmod("C:\\ubah//",755)
#os.chmod("C:\\ubah\\hasil", 755)
#os.chmod("C:\\ubah//hasil", 755)
#os.chmod("C:\\ubah\\hasil//",755)
try:
    os.chmod(filepath, 755)
    os.chmod("C:\\Users\\{}\\RemoveBG//hasil".format(asa), 755)
except PermissionError:
    pass

import random
b = random.choice(owners.own)

a = "Jangan Lupa setelah diubah backgroundnya , langsung pindahkan ke folder yang aman".upper()
B = "Untuk versi Linux masih tahap pengembangan (Mungkin lama) dikarenakan saya Sedang Membuat tools Osint".upper()
c = "Kalau ingin kontribusi dan membantu saya, silahkan dan saya berterimakasih banget :) ".upper()
d = "Saya tidak terima adanya perecodean tetapi saya terima adanya kontribusi atau pengembangan yang disertai nama saya".upper()
print(a,"\n\n",B,"\n\n",c,"\n\n")
input("enter Untuk Melanjutkan")

# Your Remove.bg Api Key
removebg_key = b #

#os.mkdir("C:\\Users\\ubah")
#os.mkdir("C:\\Users\\ubah\\hasil")

for thefile in os.listdir(filepath):
	
	filename = os.fsdecode(thefile)
	filename_noext= os.path.splitext(thefile)[0]
	
	response = requests.post(
		'https://api.remove.bg/v1.0/removebg',
		files={'image_file': open('C:\\Users\\{}\\RemoveBG//{}'.format(asa,filename), 'rb')},
		data={'size': img_size,
                      'bg_color': warna},
		headers={'X-Api-Key': removebg_key},
		)
	if response.status_code == requests.codes.ok:
		with open('C:\\Users\\{}\\RemoveBG\\hasil//{}.png'.format(asa,filename_noext), 'wb') as out:
			out.write(response.content)
			print('Great, {} Berhasil Diubah !'.format(filename))
			#i += 1
	else:
		print("Error:", response.status_code, response.text)


fileOri = f"C:\\Users\\{asa}\\RemoveBG"
fileEdit = f"C:\\Users\\{asa}\hasil"
print("File Original = ",fileOri)
print("File Edit = ",fileEdit)
