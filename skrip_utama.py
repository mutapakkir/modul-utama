#MUHAMMAD IBDAUL MUTAFAKKIR(20230040291)
#TI23 C


from luas.persegi import luas_persegi        
from luas.lingkaran import luas_lingkaran
from luas.segitiga import luas_segitiga
from volume.kubik import volume_kubik
from volume.bola import volume_bola
from volume.trapesium import voolume_trapesium

def main():
    while True:
        print('=====Menu Operasi=====\n')
        print('1.perhitungan luas persegi')
        print('2.perhitungan luas segitiga')
        print('3.perhitungan luas lingkaran')
        print('4.perhitungan volume bola')
        print('5.perhitungan volume kubik')
        print('6.perhitungan volume trapesium')
        print('7.Quit')

        pilihan = input('silahkann pilih menu yang tersedia!')
        if pilihan == '1':
            ('PERHITUNGAN LUAS PERSEGI\n')
            hasil = luas_persegi()
            print('hasilnya adalah ',hasil)
        elif pilihan == '2':
            'PERHITUNGAN LUAS SEGITIGA\n'
            hasil = luas_segitiga()
            print('hasilnya adalah ',hasil)
        elif pilihan == '3':
            'PERHITUNGAN LUAS LINGKARAN\n'
            hasil = luas_lingkaran()
            print('hasilnya adalah ',hasil)
        elif pilihan == '4':
            print('PERHITUNGAN VOLUME BOLA\n')
            hasil = volume_bola()
            print('hasilnya adalah ',hasil)
        elif pilihan == '5':
            print('PERHITUNGAN VOLUME KUBIK\n')
            hasil = volume_kubik()
            print('hasilnya adalah ',hasil)
        elif pilihan == '6':
            print('PERHITUNGAN VOLUME TRAPESIUM \n')
            hasil = voolume_trapesium()
            print('hasilnya adalah ',hasil)
        elif pilihan == '7':
            print('terima kasih!!!!')
        else:
            print('pilihan anda tidak valid,silahkan pilih opsi yang tersedia')
main()
