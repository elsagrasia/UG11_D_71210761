klmt=input("Masukan sebuah kata/kalimat: ")
krktr=input("Masukan karakter yang ingin disisipkan: ")

def sisipHuruf(klmt,krktr):
    cap=klmt.upper()
    print(krktr.join(list(cap)))
def sisipKata(klmt,krktr):
    cap=klmt.title()
    print(krktr.join(cap.split()))

sisipHuruf(klmt,krktr)
sisipKata(klmt,krktr)