nama = input('Nama : ')
pwd = input('Password : ')
hobby = []
other = {}
i=0
while True:
    hobby = input('Hobby Anda : ')
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi = input('Masih ada lagi [Y/T] : ')
    if lagi=='t':
        break
    i+=1
other_Sex = input('Jenis Kelamin : ')
other_TTL = input('Tempat/Tanggal lahir : ')
other_Umur = input('Umur : ')
print("=====================================Program=================================")
def guest(nama, pwd, hobby, other):
    print ("Nama Anda    :",nama)
    print ("Password Anda:",pwd)
    print ("Hobby Anda   :",hobby)
    print ("Lain-lain    :")
    print (other_Sex)
    print (other_TTL)
    print (other_Umur)
guest(nama, pwd, hobby, other)