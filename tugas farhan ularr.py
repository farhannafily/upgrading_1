laporan_minuman = [
    {
        'nama': 'kopi',
        'harga': '11000',
        'terjual': '10',
        'modal_satuan': 6000,
    },
    {
        'nama': 'teh_ES',
        'harga': '6000',
        'terjual': '12',
        'modal_satuan': '3500',
    },
    {
        'nama': 'jus',
        'harga': '10000',
        'terjual': '7',
        'modal_satuan': '6000',
    },
] # tidak ada yg perlu dibuah dsn

# isi list makanan dan untuk nama, harga, terjual, modal satuan bebas tetapi diinput melalui terminal (cukup 2 makanan)
laporan_makanan = [] # format makanan samad dengan minuman
"""
format makanan
{
        'nama': '',
        'harga': '',
        'terjual': '',
        'modal_satuan': ,
}
"""

penjualan = {
    'minuman': laporan_minuman,
    'makanan': laporan_makanan,
    'summary': {
        'total_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':''
        },
        'keuntungan_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':'',
        },
        'special_case':'total_semua_penjualan+total_semua_keuntungan_penjualan+special_value+10000' # juga tidak ada yg perlu diubah dsn
    }
}

# lakukan programn didalam fungsi ini
def main():
    global laporan_makanan, laporan_minuman, penjualan
    special_value = 19042020 # ex: special_value = 2011512010
    laporan_makanan_dict = dict()

    for x in range (2):
        nama = input("Menu : ")
        harga = int(input("Harga Makanan : "))
        jumlah = int(input("Jumlah Pesanan : "))
        modal = int(input("Modal Awal : "))
        laporan_makanan_dict = {'nama' : nama,'harga' : harga,'jumlah' : jumlah,'modal' :modal}
        laporan_makanan.append(laporan_makanan_dict)

    penjualan['summary']['total_penjualan']['makanan'] = penjualan['makanan'][0]['jumlah'] + penjualan['makanan'][1]['jumlah']
    penjualan['summary']['keuntungan_penjualan']['makanan'] = int((penjualan['makanan'][0]['harga'] * penjualan['makanan'][0]['jumlah']-penjualan['makanan'][0]['modal'])+(penjualan['makanan'][1]['jumlah'] * penjualan['makanan'][1]['jumlah']-penjualan['makanan'][0]['modal']))
    print('laporan_makanan')
    print(penjualan['makanan'])
    print("Total terjual :")
    print(penjualan['summary']['total_penjualan']['makanan'])
    print("total keuntungan :")
    print(penjualan['summary']['keuntungan_penjualan']['makanan'])







if __name__ == "__main__":
    main()
