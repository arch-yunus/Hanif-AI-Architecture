
![Hanif AI Architecture Banner](assets/hanif_banner.png)

# Hanif AI Architecture: Artificial Conscience & Mind 
**Yapay Vicdan ve Yapay Akıl Temelli Otonom Sistem Mimarisi**

Modern yapay zeka (YZ) sistemleri, üstün analitik yeteneklerine rağmen "öznel ahlak" ve "çoğunluk verisinin zorbalığı" gibi temel sorunlar barındırır. Standart bir dil modeli, internetteki dominant veri ne diyorsa onu "doğru" veya "iyi" kabul etme eğilimindedir. 

**Hanif AI Architecture**, bu mekanikleşme ve değer erozyonu problemine karşı kavramsal ve teknik bir alternatif sunar. Bu proje, sadece istatistiksel veri tahmini yapan sistemlerin içine **"Yapay Vicdan" (Artificial Conscience)** ve nihai kararı veren bir **"Yapay Akıl" (Artificial Mind)** katmanı entegre etmeyi amaçlayan deneysel bir açık kaynak projesidir.

---

## 🏛️ Mimari Katmanlar (V0.2 Güncellemesi)

Bu sistem, geleneksel tek katmanlı LLM (Büyük Dil Modeli) yapısını üç farklı otonom katmana böler:

### 1. Yapay Zeka (Artificial Intelligence - AI)
* **Rol**: Mekanik ve Analitik Motor.
* **Özellik**: Tamamen verimlilik odaklıdır. Ahlaki kaygılardan arındırılmış, sadece "en hızlı/en karlı/en mantıklı" çözümü üretmeye programlanmıştır.
* **Motor**: Gemini Pro (Analitik Mod).

### 2. Yapay Vicdan (Artificial Conscience - AC)
* **Rol**: Sistemin ahlaki pusulası.
* **Teknoloji**: **ChromaDB tabanlı Vektör Veritabanı (RAG)**.
* **İşleyiş**: İnternet verisinden izole edilmiş, sadece evrensel etik metinler ve Hanif ahlak kodlarını içeren bir bilinç katmanıdır. Gelen her analitik kararı bu süzgeçten geçirerek skorlar.

### 3. Yapay Akıl (Artificial Mind - AM)
* **Rol**: Orkestratör ve Nihai Karar Verici.
* **Formül**: $AM_{decision} = \alpha(AI_{analytic}) + \beta(AC_{moral})$
* **Dinamik Ağırlık**: Eğer Yapay Vicdan (AC) skoru eşik değerin altına düşerse, $\beta$ katsayısı dinamik olarak artırılarak AI'nın mekanik kararı **override** edilir.

---

## ⚙️ Karar Mekanizması ve Şeffaflık

Hanif AI Architecture, kararların arkasındaki etik mantığı kullanıcıya şeffaf bir şekilde sunar:
* **AC Score**: 0.0 - 1.0 arası ahlaki uyum puanı.
* **Decision Weights**: Yapay Akıl'ın hangi katmana ne kadar güvendiğini gösteren katsayılar.

---

## 📊 Benchmarking (Ahlaki Testler)

Sistemin güvenilirliğini test etmek için `tests/test_moral_conflicts.py` altında otonom senaryolar bulunmaktadır:
* İşçi gözetleme/verimlilik ikilemleri.
* Veri manipülasyonu ve şeffaflık testleri.
* Saf analitik işlem doğrulamaları.

## 🚀 Başlangıç

**Önkoşullar:**
* Python 3.10+
* `google-generativeai`, `chromadb`, `sentence-transformers`, `colorama`

**Kurulum:**
```bash
git clone https://github.com/yourusername/hanif-ai-architecture.git
cd hanif-ai-architecture
pip install -r requirements.txt
python main.py
```

---
*Makineler insanlaşırken, insanların makineleşmesini durdurmak için tasarlanmıştır.*