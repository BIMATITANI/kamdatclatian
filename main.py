from random import randint

alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
# skema tabel kocokan asli (awal)
# tabel_kocokan = [
#     [1,18,17,23,19,20,10,25,5,15,8,21,11,24,14,3,26,13,6,9,12,22,7,4,16,2],
#     [4,11,18,22,23,8,16,25,7,10,24,3,20,19,2,21,13,14,26,1,17,9,12,5,15,6],
#     [8,7,19,20,16,23,4,25,11,2,21,13,18,9,3,12,6,1,10,14,24,26,22,15,5,17],
#     [14,2,1,4,20,25,3,6,21,8,23,10,22,7,26,13,19,11,15,5,18,16,9,24,17,12],
#     [22,3,6,4,12,14,10,2,19,13,18,26,17,15,25,7,23,9,8,5,24,16,21,1,20,11],
#     [12,25,3,7,23,16,4,9,26,10,5,14,2,13,8,21,11,22,15,1,20,17,6,24,19,18]
# ]

# skema tabel kocokan ke-2 (ganjil = urut, genap = acak)
# tabel_kocokan = [
#     [i for i in range(26)],
#     [4,11,18,22,23,8,16,25,7,10,24,3,20,19,2,21,13,14,26,1,17,9,12,5,15,6],
#     [i for i in range(26)],
#     [14,2,1,4,20,25,3,6,21,8,23,10,22,7,26,13,19,11,15,5,18,16,9,24,17,12],
#     [i for i in range(26)],
#     [12,25,3,7,23,16,4,9,26,10,5,14,2,13,8,21,11,22,15,1,20,17,6,24,19,18]
# ]

# skema tabel kocokan ke-3 (ganjil = acak, genap = urut)
tabel_kocokan = [
    [1,18,17,23,19,20,10,25,5,15,8,21,11,24,14,3,26,13,6,9,12,22,7,4,16,2],
    [i+1 for i in range(26)],
    [8,7,19,20,16,23,4,25,11,2,21,13,18,9,3,12,6,1,10,14,24,26,22,15,5,17],
    [i+1 for i in range(26)],
    [22,3,6,4,12,14,10,2,19,13,18,26,17,15,25,7,23,9,8,5,24,16,21,1,20,11],
    [i+1 for i in range(26)]
]

def get_enkripsi(data: str) -> dict:
    data = data.lower()

    # tahap 1
    hasil_tahap_1 = []
    for i in data:
        index_huruf = alphabet.index(i)
        hasil_tahap_1.append(tabel_kocokan[0][index_huruf])
    
    # tahap 2
    hasil_tahap_2 = []
    for i in hasil_tahap_1:
        index_huruf = tabel_kocokan[1].index(i)
        hasil_tahap_2.append(index_huruf)
    
    # tahap 3
    hasil_tahap_3 = []
    for i in hasil_tahap_2:
        hasil_tahap_3.append(tabel_kocokan[2][i])
    
    # tahap 4
    hasil_tahap_4 = []
    for i in hasil_tahap_3:
        index_huruf = tabel_kocokan[3].index(i)
        hasil_tahap_4.append(index_huruf)

    # tahap 5
    hasil_tahap_5 = []
    for i in hasil_tahap_4:
        hasil_tahap_5.append(tabel_kocokan[4][i])
    
    # tahap 6
    hasil_tahap_6 = []
    for i in hasil_tahap_5:
        index_huruf = tabel_kocokan[5].index(i)
        hasil_tahap_6.append(index_huruf)
    
    hasil = [alphabet[i] for i in hasil_tahap_6]

    # Hasil Return adalah [data_asli, hasil_enkripsi, ascii_data_asli, ascii_hasil_enkripsi]
    return {
        "data_asli": [i for i in data],
        "hasil_enkripsi": hasil,
        "ascii_data_asli": [ord(i) for i in data],
        "ascii_data_enkripsi": [ord(i) for i in hasil]
    }


hasil_enkripsi = get_enkripsi("yotasikokimanja")
print(hasil_enkripsi["data_asli"])
print(hasil_enkripsi["hasil_enkripsi"])
print(hasil_enkripsi["ascii_data_asli"])
print(hasil_enkripsi["ascii_data_enkripsi"])