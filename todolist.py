# -*- coding: utf-8 -*-
"""todolist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q2FAnZXbqpcJMhbZmJyPu_NwCG7kVobT
"""

class Gorev:
    def __init__(self, gorev_adi, tamamlandi=False):
        self.gorev_adi = gorev_adi
        self.tamamlandi = tamamlandi

    def tamamla(self):
        self.tamamlandi = True

    def __str__(self):
        durum = "Tamamlandı" if self.tamamlandi else "Tamamlanmadı"
        return f"{self.gorev_adi} - {durum}"


class TaskManager:
    def __init__(self):
        self.gorevler = []
        self.gorev_dosyasi = "gorevler.txt"
        self.gorev_yukle()

    def gorev_ekle(self, gorev_adi):
        gorev = Gorev(gorev_adi)
        self.gorevler.append(gorev)
        self.gorev_kaydet()
        print(f"'{gorev_adi}' görev olarak eklendi.")

    def gorev_tamamla(self, gorev_no):
        if 0 <= gorev_no < len(self.gorevler):
            self.gorevler[gorev_no].tamamla()
            self.gorev_kaydet()
            print(f"'{self.gorevler[gorev_no].gorev_adi}' görevi tamamlandı.")
        else:
            print("Geçersiz görev numarası.")

    def gorev_sil(self, gorev_no):
        if 0 <= gorev_no < len(self.gorevler):
            silinen_gorev = self.gorevler.pop(gorev_no)
            self.gorev_kaydet()
            print(f"'{silinen_gorev.gorev_adi}' görevi silindi.")
        else:
            print("Geçersiz görev numarası.")

    def gorevleri_listele(self):
        print("Tamamlanmayan Görevler:")
        for i, gorev in enumerate(self.gorevler):
            if not gorev.tamamlandi:
                print(f"{i}. {gorev}")
        print("\nTamamlanan Görevler:")
        for i, gorev in enumerate(self.gorevler):
            if gorev.tamamlandi:
                print(f"{i}. {gorev}")

    def gorev_kaydet(self):
        with open(self.gorev_dosyasi, "w") as dosya:
            for gorev in self.gorevler:
                dosya.write(f"{gorev.gorev_adi}|{gorev.tamamlandi}\n")

    def gorev_yukle(self):
        try:
            with open(self.gorev_dosyasi, "r") as dosya:
                for satir in dosya:
                    ad, tamamlandi = satir.strip().split("|")
                    self.gorevler.append(Gorev(ad, tamamlandi == "True"))
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    yonetici = TaskManager()

    while True:
        print("\n1. Görev Ekle")
        print("2. Görevi Tamamla")
        print("3. Görev Sil")
        print("4. Görevleri Listele")
        print("5. Çıkış ve Kaydet")
        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Görev adı: ")
            yonetici.gorev_ekle(ad)
        elif secim == "2":
            yonetici.gorevleri_listele()
            sira = int(input("Tamamlanacak görev numarası: "))
            yonetici.gorev_tamamla(sira)
        elif secim == "3":
            yonetici.gorevleri_listele()
            sira = int(input("Silinecek görev numarası: "))
            yonetici.gorev_sil(sira)
        elif secim == "4":
            yonetici.gorevleri_listele()
        elif secim == "5":
            yonetici.gorev_kaydet()
            print("Görevler kaydedildi. Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")