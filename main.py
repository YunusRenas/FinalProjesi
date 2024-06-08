from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd


def main():
    try:
        # Gelecekteki davranış değişikliğine opt-in yapma
        pd.set_option('future.no_silent_downcasting', True)

        # Personel nesneleri
        personel1 = Personel(1, "Ali", "Atay", "Muhasebe", 5000)
        personel2 = Personel(2, "Yusuf", "Kayacı", "IT", 6000)

        # Doktor nesneleri
        doktor1 = Doktor(3, "Dara", "Taş", "Kardiyoloji", 10000, "Kalp Cerrahisi", 10, "İnönü Hastanesi")
        doktor2 = Doktor(4, "İlhan", "Kılıç", "Nöroloji", 12000, "Beyin Cerrahisi", 8, "Şehir Hastanesi")
        doktor3 = Doktor(5, "Hasan", "Uçar", "Psikatri", 9500, "Psikoloji", 5, "Meram Tıp")

        # Hemşire nesneleri
        hemsire1 = Hemsire(6, "Eda", "Karakoç", "Acil Servis", 7000, 40, "İlk Yardım", "İnönü Hastanesi")
        hemsire2 = Hemsire(7, "İrem", "Aksoy", "Cerrahi", 7500, 45, "Ameliyathane Hemşireliği", "Şehir Hastanesi")
        hemsire3 = Hemsire(8, "Seçil", "Taş", "Yoğun Bakım", 7200, 50, "Yoğun Bakım Hemşireliği", "Meram Tıp")

        # Hasta nesneleri
        hasta1 = Hasta(1, "Renas", "Taş", "1980-01-01", "Grip", "İlaç Tedavisi")
        hasta2 = Hasta(2, "Mehdi", "Dursun", "1990-03-05", "Covid-19", "Karantina ve İlaç Tedavisi")
        hasta3 = Hasta(3, "Afra", "Ordulu", "1975-07-15", "Kırık", "Ameliyat ve Fizik Tedavi")

        # DataFrame oluşturma
        data = {
            "Personel No": [personel1.get_personel_no(), personel2.get_personel_no(),
                            doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(),
                            hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no(),
                            0, 0, 0],
            "Ad": [personel1.get_ad(), personel2.get_ad(),
                   doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(),
                   hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(),
                   hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
            "Soyad": [personel1.get_soyad(), personel2.get_soyad(),
                      doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(),
                      hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(),
                      hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
            "Departman": [personel1.get_departman(), personel2.get_departman(),
                          doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(),
                          hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(),
                          0, 0, 0],
            "Maas": [personel1.get_maas(), personel2.get_maas(),
                     doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(),
                     hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(),
                     0, 0, 0],
            "Uzmanlik": [0, 0,
                         doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(),
                         0, 0, 0, 0, 0, 0],
            "Deneyim Yili": [0, 0,
                             doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(),
                             0, 0, 0, 0, 0, 0],
            "Hastane": [0, 0,
                        doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(),
                        hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(),
                        0, 0, 0],
            "Calisma Saati": [0, 0,
                              0, 0, 0,
                              hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(),
                              0, 0, 0],
            "Sertifika": [0, 0,
                          0, 0, 0,
                          hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(),
                          0, 0, 0],
            "Hasta No": [0, 0,
                         0, 0, 0,
                         0, 0, 0,
                         hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
            "Dogum Tarihi": [0, 0,
                             0, 0, 0,
                             0, 0, 0,
                             hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
            "Hastalik": [0, 0,
                         0, 0, 0,
                         0, 0, 0,
                         hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
            "Tedavi": [0, 0,
                       0, 0, 0,
                       0, 0, 0,
                       hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
        }

        df = pd.DataFrame(data)

        # Boş olan değişken değerleri için 0 atama ve dtype çıkarımı yapma
        df.fillna(0, inplace=True)
        df = df.infer_objects(copy=False)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
        doktor_df = df[df['Uzmanlik'] != 0]
        uzmanlik_grup = doktor_df.groupby('Uzmanlik').size()
        print("Uzmanlık alanlarına göre doktor sayısı:")
        print(uzmanlik_grup)

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
        deneyimli_doktorlar = doktor_df[doktor_df['Deneyim Yili'] > 5]
        toplam_deneyimli_doktor = deneyimli_doktorlar.shape[0]
        print(f"5 yıldan fazla deneyime sahip doktorların toplam sayısı: {toplam_deneyimli_doktor}")

        # Hasta adına göre DataFrame’i alfabetik olarak sıralama
        df_hasta_sirali = df[df['Hasta No'] != 0].sort_values(by='Ad')
        print("Hasta adına göre alfabetik olarak sıralanmış DataFrame:")
        print(df_hasta_sirali)

        # Maaşı 7000 TL üzerinde olan personelleri bulma
        yuksek_maas_personel = df[df['Maas'] > 7000]
        print("Maaşı 7000 TL üzerinde olan personeller:")
        print(yuksek_maas_personel)

        # Doğum tarihi 1990 ve sonrası olan hastaları gösterme
        df['Dogum Tarihi'] = pd.to_datetime(df['Dogum Tarihi'], errors='coerce')
        yeni_hastalar = df[(df['Dogum Tarihi'] >= '1990-01-01') & (df['Dogum Tarihi'].notna())]
        print("Doğum tarihi 1990 ve sonrası olan hastalar:")
        print(yeni_hastalar)

        # Yeni DataFrame oluşturma
        yeni_data = df[['Ad', 'Soyad', 'Departman', 'Maas', 'Uzmanlik', 'Deneyim Yili', 'Hastalik', 'Tedavi']].copy()
        print("Yeni DataFrame:")
        print(yeni_data.to_string())

    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if __name__ == "__main__":
    main()

