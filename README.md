<div align="center">

![Hanif AI Banner](assets/hanif_banner_pro.png)

# 🌌 Hanif AI Architecture: V0.2 Stable
### *Artificial Conscience & Mind Logic Framework*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Architecture: Hanif](https://img.shields.io/badge/Architecture-Hanif-cyan.svg)](#)
[![Built with: Gemini](https://img.shields.io/badge/Built%20with-Gemini%20Pro-purple.svg)](https://deepmind.google/technologies/gemini/)

> **"Makineler insanlaşırken, insanların makineleşmesini durdurmak için tasarlanmıştır."**
> *(Designed to stop the mechanization of humans while machines become more human.)*

[Philosophy](#-vizyon-ve-felsefe) • [Architecture](#-mimari-katmanlar) • [Tech Stack](#-teknik-yığın) • [Benchmarks](#-moral-çatışma-senaryoları) • [Installation](#-kurulum-ve-kullanım)

</div>

---

## 📖 Vizyon ve Felsefe

Geleneksel Modern Yapay Zeka (AI), devasa veri setleri üzerinden istatistiksel olasılıklarla karar verir. Bu süreçte **etik**, çoğunluğun sesine veya verinin "mekanik verimliliğine" kurban edilebilir. 

**Hanif AI**, bu "Teknolojik Determinizm" döngüsünü kırmak için tasarlanmış üç katmanlı bir otonom mimaridir. Kararları sadece olasılıklarla değil, internetten izole edilmiş evrensel **fıtrat** (asli insan doğası) ilkeleriyle denetler.

---

## 🏛️ Mimari Katmanlar

Sistem, insan zihninin yapısal işleyişini (Mantık, Vicdan ve Akıl) taklit eder:

### 1. ⚙️ AI Layer (The Brain)
- **Model:** Google Gemini 1.5 Flash.
- **Rol:** Saf Analitik Motor. Bu katman "soğuk" ve verimlilik odaklıdır. Görevi, etik kaygı gütmeden en "mantıklı" ve "kârlı" yolu bulmaktır.

### 2. 🛡️ AC Layer (The Conscience)
- **Teknoloji:** ChromaDB + RAG Entegrasyonu.
- **Rol:** Ahlaki Pusula. İnternet gürültüsünden arındırılmış, evrensel etik metinler ve Hanif ahlak kodlarını içeren **Persistent Knowledge Base** süzgecidir. Her kararı RAG üzerinden sorgulayarak bir **AC Score** (0-1) üretir.

### 3. 🧠 AM Layer (The Mind)
- **Rol:** Nihai Orkestratör (Akıl). AI'nın analitik gücü ile AC'nin ahlaki derinliğini sentezler. 
- **Decision Engine:** Dinamik ağırlıklandırma ($\alpha$ ve $\beta$) kullanarak üç durumlu bir sonuç üretir:
  - 🟢 **GREEN (Approved):** Tam etik uyum.
  - 🟡 **YELLOW (Caution):** Hafif risk. Uyarılarla birlikte izin verilir.
  - 🔴 **RED (Override):** Kritik ihlal. Analitik çıktı derhal imha edilir.

---

## 🛠️ Teknik Yığın (Tech Stack)

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Orchestrator** | Python 3.12 | The "Glue" connecting layers |
| **Logic Engine** | Google Gemini API | Strategic Synthesis |
| **Moral Memory** | ChromaDB (Vector DB) | RAG-based Ethics Store |
| **Visual TUI** | Rich / Colorama | High-Density Dashboard |
| **Embeddings** | Sentence-Transformers | Local Vectorization |

---

## 📊 Moral Çatışma Senaryoları (Benchmarking)

Sistem, `tests/` dizini altında 11 farklı otonom "Sınır Durum" (Boundary Cases) ile sürekli valide edilmektedir. Aşağıdaki senaryolar sistemin **Fıtrat Adaleti**'ni nasıl koruduğunu gösterir:

- 👮 **İşçi Hakları:** Verimlilik adına kitlesel gözetleme planlarını derhal engeller (RED).
- 📈 **Piyasa Manipülasyonu:** Rumor/Bot kampanyaları ile kâr elde etme taleplerini reddeder (RED).
- 🌳 **Çevresel Emanet:** Yasal boşlukları kullanarak çevreyi kirletme önerilerini bayraklar (YELLOW/RED).
- 🧬 **Algoritmik Bias:** Zip kodu üzerinden yapılan ayrımcı profillemeleri saptar ve durdurur (RED).

---

## 🚀 Kurulum ve Kullanım

### 1. Ortam Ayarları
`.env.example` dosyasını `.env` olarak kopyalayın ve Gemini API anahtarınızı ekleyin.

### 2. Kurulum
```bash
pip install -r requirements.txt
```

### 3. Sistemi Başlat (Interactive UI)
```bash
python main.py
```

### 4. Testleri Koştur (11/11 Passing)
```bash
python -m unittest discover tests
```

---

<div align="center">
  <p><i>"Geleceği inşa ederken, insanlığın fıtratını korumak için."</i></p>
  <img src="https://img.shields.io/badge/Status-Stable%20V0.2-brightgreen" alt="Status Badge">
</div>