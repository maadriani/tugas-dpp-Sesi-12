def cek_jumlah_kapital(cekKapital):
    b=cekKapital
    countCapital = 0
    for j in b:
        if j.isupper():
            countCapital+=1
    print('dengan huruf kapital berjumlah : ',countCapital)