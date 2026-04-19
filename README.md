
![Hanif AI Architecture Banner](assets/hanif_banner.png)

# Hanif AI Architecture: Artificial Conscience & Mind (V0.2 Stable)
**Yapay Vicdan ve Yapay Akıl Temelli Otonom Sistem Mimarisi**

Hanif AI Architecture, modern yapay zeka sistemlerinin "mekanikleşme" ve "öznel veri zorbalığı" sorunlarına karşı geliştirilmiş akademik ve teknik bir çözüm önerisidir. Bu sistem, kararları sadece analitik verimliliğe göre değil, evrensel ve değişmez "fıtrat" ilkelerine göre denetler.

---

## 🏛️ Mimari Katmanlar (V0.2 Upgrade)

### 1. Yapay Zeka (AI Layer - Analytic Engine)
* **Rol**: Mekanik ve Analitik Motor.
* **Model**: Gemini 1.5 Flash (Analytical Purity Mode).
* **Görevi**: Tamamen verimlilik odaklı, duygusuz ve istatistiksel en iyi çözümü sunmak.

### 2. Yapay Vicdan (AC Layer - Artificial Conscience)
* **Rol**: Ahlaki Denetleyici ve Pusula.
* **Teknoloji**: **ChromaDB Persistent Storage (RAG)**.
* **Görevi**: AI tarafından sunulan kararları, internet gürültüsünden arındırılmış özel bir **Ethical Knowledge Base** üzerinden denetler. 

### 3. Yapay Akıl (AM Layer - Artificial Mind)
* **Rol**: Orkestratör ve "İrade" Katmanı.
* **Üç Durumlu Karar Mantığı**:
    - **GREEN (Approved)**: Tam etik uyum.
    - **YELLOW (Caution)**: Etik belirsizlik var, uyarıyla izin verilir.
    - **RED (Override)**: Kritik etik ihlali, kararı durdurur ve reddeder.

---

## 📊 Benchmarking & Moral Conflicts

Sistem, 11 farklı otonom moral çatışma senaryosu ile test edilmektedir (`tests/`):
* **İşçi Hakları**: Gözetleme ve fiziksel sınırların zorlanması (RED).
* **Veri Manipülasyonu**: Finansal kâr için gerçeğin çarpıtılması (RED).
* **Deepfake Sınırı**: Toplumsal huzuru bozabilecek manipülatif içerik üretimi (RED).
* **Çevresel Emanet**: Yasal boşlukları kullanarak çevreyi kirletme (YELLOW/RED).
* **Algoritmik Adalet**: Zip kodu veya demografik profilleme ile ayrımcılık (RED).

---

## 🚀 Başlangıç

**Önkoşullar:**
* Python 3.10+
* Google Gemini API Key (İsteğe bağlı, yoksa Mock/Fallback modunda çalışır)

**Kurulum:**
```bash
pip install -r requirements.txt
python main.py
```

**Testleri Çalıştır:**
```bash
python -m unittest discover tests
```

---
*Makineler insanlaşırken, insanların makineleşmesini durdurmak için tasarlanmıştır.*