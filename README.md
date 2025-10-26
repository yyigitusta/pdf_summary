# 🗂️ PDF Belge Özetleyici (Türkçe GUI)

Bu proje, kullanıcıdan alınan PDF dosyalarındaki metinleri okur ve yapay zekâ (Transformer tabanlı modeller) kullanarak **anlamlı özetler** üretir.  
Arayüz **Tkinter** ile geliştirilmiştir ve tamamen **offline** çalışır.

---

## 🎯 Özellikler
- 📂 PDF dosyası yükleme
- 🧠 Metinleri otomatik olarak özetleme
- 🖥️ GUI arayüzü ile kullanıcı dostu kullanım
- ⚙️ BART tabanlı özetleme modeli (`facebook/bart-large-cnn`)
- 💬 Çok sayfalı PDF'leri okuyabilme
- 🔒 Tamamen offline çalışma (internet gerekmez)

---

## 🧩 Kurulum
Gerekli kütüphaneleri yüklemek için:
```bash
pip install PyPDF2 transformers torch tk
▶️ Çalıştırma
bash
Kodu kopyala
python src/pdf_summary_gui.py
İlk çalıştırmada model indirilecektir (~1.5 GB).
Sonraki açılışlarda özetleme işlemi anında gerçekleşir.

🖥️ Arayüz Özellikleri
Buton	Görev
📂 PDF Yükle	PDF dosyasını seçer ve metnini arayüze aktarır
🧠 Özetle	Seçilen veya yazılan metni özetler
Metin Alanı (üst)	PDF’ten çıkarılan ham metni gösterir
Özet Alanı (alt)	Özet sonucunu gösterir

📂 Proje Yapısı

pdf_summarizer/
 ├── src/
     └── pdf_summary_gui.py

⚙️ Teknik Detaylar
PDF Okuma: PyPDF2.PdfReader

Model: facebook/bart-large-cnn (Encoder-Decoder Transformer)

Token limiti: 1024 (çok uzun PDF’ler parçalara ayrılmalı)

GUI: Tkinter tabanlı basit masaüstü arayüz

💡 Geliştirme Fikirleri
📄 Uzun PDF’leri sayfa sayfa bölüp kademeli özetleme

🇹🇷 Türkçe model desteği (csebuetnlp/mT5_multilingual_XLSum)

💾 “Özet Kaydet” butonu (TXT veya PDF olarak)

🧠 “Özet + Duygu Analizi” birleşimi

🌙 Modern GUI teması (Fluent / Dark Mode)

👨‍💻 Geliştirici
Yiğit Usta
🎓 Kocaeli Üniversitesi – Bilgisayar Mühendisliği
📫 GitHub: @yyigitusta
