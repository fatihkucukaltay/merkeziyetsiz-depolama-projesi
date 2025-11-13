import os

class ShardManager:
    """
    Bu sınıf, dosyaları parçalama (sharding) ve
    birleştirmeden (reassembly) sorumludur.
    """
    def __init__(self, upload_folder='uploads', parca_sayisi=5):
        """Ayarları (klasör, parça sayısı) yükler."""
        self.UPLOAD_FOLDER = upload_folder
        self.PARCA_SAYISI = parca_sayisi
        print("--- Parça Yöneticisi (ShardManager) başarıyla yüklendi. ---")

    def parcala_ve_kaydet(self, sifreli_veri, orijinal_dosya_adi):
        """Şifreli veriyi alır, parçalar ve diske kaydeder."""

        parca_boyutu = (len(sifreli_veri) + self.PARCA_SAYISI - 1) // self.PARCA_SAYISI

        kaydedilen_parcalar = []
        for i in range(self.PARCA_SAYISI):
            baslangic = i * parca_boyutu
            bitis = (i + 1) * parca_boyutu
            parca = sifreli_veri[baslangic:bitis]

            parca_adi = f"{orijinal_dosya_adi}.part_{i+1}_of_{self.PARCA_SAYISI}"
            parca_yolu = os.path.join(self.UPLOAD_FOLDER, parca_adi)

            with open(parca_yolu, 'wb') as p:
                p.write(parca)
            kaydedilen_parcalar.append(parca_adi)

        return kaydedilen_parcalar

    def birlestir_ve_oku(self, orijinal_dosya_adi):
        """Dosya adına göre parçaları bulur, birleştirir ve şifreli veriyi döndürür."""

        sifreli_veri_parcalari = []
        for i in range(self.PARCA_SAYISI):
            parca_adi = f"{orijinal_dosya_adi}.part_{i+1}_of_{self.PARCA_SAYISI}"
            parca_yolu = os.path.join(self.UPLOAD_FOLDER, parca_adi)

            # Hata kontrolü: Parça bulunamazsa
            if not os.path.exists(parca_yolu):
                raise FileNotFoundError(f"Eksik parça: {parca_adi}")

            with open(parca_yolu, 'rb') as p:
                sifreli_veri_parcalari.append(p.read())

        # Tüm parçaları tek bir veri bloğu halinde birleştir
        sifreli_veri = b''.join(sifreli_veri_parcalari)
        return sifreli_veri
