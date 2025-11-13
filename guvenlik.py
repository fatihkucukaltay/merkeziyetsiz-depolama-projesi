import os
from cryptography.fernet import Fernet

class Encryptor:
    """
    Bu sınıf, şifreleme ve anahtar yönetiminden sorumludur.
    """
    def __init__(self, key_file='secret.key'):
        """Sınıf başladığında anahtarı yükler veya oluşturur."""
        self.KEY_FILE = key_file
        self.key = self._anahtar_yukle()
        self.f = Fernet(self.key)
        print("--- Güvenlik Motoru (Encryptor) başarıyla yüklendi. ---")

    def _anahtar_olustur(self):
        """Yeni bir anahtar oluşturur ve 'secret.key' dosyasına kaydeder."""
        key = Fernet.generate_key()
        with open(self.KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        return key

    def _anahtar_yukle(self):
        """Anahtarı dosyadan okur. Yoksa yenisini oluşturur."""
        if not os.path.exists(self.KEY_FILE):
            return self._anahtar_olustur()

        with open(self.KEY_FILE, 'rb') as key_file:
            key = key_file.read()
        return key

    def sifrele(self, veri):
        """Verilen ham veriyi şifreler."""
        return self.f.encrypt(veri)

    def sifre_coz(self, sifreli_veri):
        """Verilen şifreli veriyi çözer."""
        return self.f.decrypt(sifreli_veri)
