import os
from flask import Flask, request, redirect, render_template_string, send_file
import io

# Diğer iki dosyamızdaki SINIFLARI içe aktarıyoruz (import)
from guvenlik import Encryptor
from yonetici import ShardManager

# --- UYGULAMA KURULUMU ---
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
PARCA_SAYISI = 5

# SINIFLARDAN nesnelerimizi (asistanlarımızı) oluşturuyoruz
sifreleyici = Encryptor(key_file='secret.key')
parca_yonetici = ShardManager(
    upload_folder=app.config['UPLOAD_FOLDER'],
    parca_sayisi=PARCA_SAYISI
)

# HTML şablonumuz (Arayüz)
HTML_SABLONU = '''
<!doctype html>
<title>Prototip v0.4 (Profesyonel)</title>
<h1>Prototip v0.4: Profesyonel Mimari (OOP)</h1>
<h2>1. Yeni Dosya Yükle:</h2>
<form method=post enctype=multipart/form-data action="/upload">
  <input type=file name=file> <input type=submit value=Yükle>
</form>
<hr>
<h2>2. Depolanan Dosyaları İndir:</h2>
<ul>
  {% for dosya in dosyalar %}
    <li>{{ dosya }} (<a href="/download/{{ dosya }}">İndir</a>)</li>
  {% else %}
    <li>Sunucuda hiç dosya bulunamadı.</li>
  {% endfor %}
</ul>
'''

@app.route('/')
def ana_sayfa():
    kayitli_dosyalar = set()
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        if f.endswith(f'.part_1_of_{PARCA_SAYISI}'):
            ana_dosya_adi = f.rsplit('.part_', 1)[0]
            kayitli_dosyalar.add(ana_dosya_adi)
    return render_template_string(HTML_SABLONU, dosyalar=list(kayitli_dosyalar))

@app.route('/upload', methods=['POST'])
def dosya_yukle():
    file = request.files.get('file')
    if not file or file.filename == '':
        return redirect('/')

    orijinal_veri = file.read()

    # 1. İŞİ HAVALE ET: Güvenlik sınıfına şifreleme işini ver
    sifreli_veri = sifreleyici.sifrele(orijinal_veri)

    # 2. İŞİ HAVALE ET: Yönetici sınıfına parçalama işini ver
    parca_yonetici.parcala_ve_kaydet(sifreli_veri, file.filename)

    return redirect('/')

@app.route('/download/<filename>')
def dosya_indir(filename):
    try:
        # 1. İŞİ HAVALE ET: Yönetici sınıfından birleştirilmiş veriyi iste
        sifreli_veri = parca_yonetici.birlestir_ve_oku(filename)

        # 2. İŞİ HAVALE ET: Güvenlik sınıfından şifreyi çözmesini iste
        orijinal_veri = sifreleyici.sifre_coz(sifreli_veri)

        return send_file(
            io.BytesIO(orijinal_veri),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return f"Hata: Dosya indirilemedi. (Hata: {e})", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
