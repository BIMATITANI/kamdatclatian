from random import randint
from hash_table import get_tabel

alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]

def get_enkripsi(mode: int, data: str) -> dict:
    data = data.lower()
    tabel_kocokan = get_tabel(mode)

    # tahap awal
    hasil_tahap_1 = []
    for i in data:
        index_huruf = alphabet.index(i)
        hasil_tahap_1.append(tabel_kocokan[0][index_huruf])
    
    hasil = hasil_tahap_1
    for j in range(1, 5, 2):
        hasil_tahap_2 = []
        for i in hasil:
            index_huruf = tabel_kocokan[j].index(i)
            hasil_tahap_2.append(index_huruf)
        hasil = hasil_tahap_2

        hasil_tahap_3 = []
        for i in hasil:
            hasil_tahap_3.append(tabel_kocokan[j+1][i])
        hasil = hasil_tahap_3
    
    hasil_tahap_akhir = []
    for i in hasil:
        index_huruf = tabel_kocokan[len(tabel_kocokan)-1].index(i)
        hasil_tahap_akhir.append(index_huruf)
    
    hasil = [alphabet[i] for i in hasil_tahap_akhir]

    # Hasil Return adalah [data_asli, hasil_enkripsi, ascii_data_asli, ascii_hasil_enkripsi]
    return {
        "data_asli": data,
        "hasil_enkripsi": "".join(hasil),
        "ascii_data_asli": [ord(i) for i in data],
        "ascii_data_enkripsi": [ord(i) for i in hasil]
    }


hasil_enkripsi = get_enkripsi(3, "yotasikokimanja")
print(hasil_enkripsi["data_asli"])
print(hasil_enkripsi["hasil_enkripsi"])
print(hasil_enkripsi["ascii_data_asli"])
print(hasil_enkripsi["ascii_data_enkripsi"])