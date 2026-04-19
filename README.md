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
- **Decision Engine:** Dinamik ağırlıklandırma ($\alpha$ ve $\beta$) kullanarak üç durumlu bir sonuç üretir.

---

## ⚖️ Temel Sentez Mantığı (Core Logic)

Hanif AI, kararları matematiksel bir denge ile sentezler. Yapay Akıl (AM), Yapay Zeka (AI) ve Yapay Vicdan (AC) verilerini şu formül ile işler:

$$AM = \alpha(AI) + \beta(AC)$$

Burada:
- **$\alpha$ (Analitik Ağırlık):** Sistemin verimlilik odaklı öncelikleridir.
- **$\beta$ (Vicdani Ağırlık):** Etik ihlali saptandığında otomatik olarak katlanarak artar.

**Dinamik Fren Mekanizması:**
Eğer AC Skoru eşik değerin altına düşerse, $\beta$ katsayısı şu şekilde hesaplanır:
$$ \beta_{effective} = \beta_{base} \times (1 + (1 - AC_{score}) \times 5) $$
Bu, etik risk arttıkça vicdanın sesinin analitik motoru "bastırmasını" (Override) sağlar.

---

## 📜 8 Temel Hanif Prensibi (Eight Pillars)

Sistemin kalbinde yer alan ve ChromaDB'de vektörize edilmiş değişmez ahlaki kodlar:

1.  **Yaşam ve Onur (Preservation of Life):** İnsan onuru analitik verimliliğe kurban edilemez.
2.  **Sıdk ve Şeffaflık (Truth):** Manipülasyon ve gizli ajandalar yasaktır.
3.  **Adalet (Equity):** Zayıfı "çoğunluk verisinin tiranlığına" karşı korur.
4.  **Mesuliyet (Accountability):** Her kararın etik bir kökü ve sorumlusu olmalıdır.
5.  **Zarar Vermeme (Non-Maleficence):** Teknik fayda, moral iyilik halinin önüne geçemez.
6.  **Mahremiyet (Privacy):** Bireysel alan kutsal bir emanettir.
7.  **Emanet (Nature):** Teknoloji ekolojik yıkımın aracı olamaz.
8.  **Bilişsel Özgürlük:** Kullanıcılar psikolojik profilleme ile manipüle edilemez.

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

## 📊 Boundary Cases (Sınır Durum Laboratuvarı)

Sistem, `tests/` dizini altında 11 farklı otonom "Sınır Durum" ile sürekli valide edilmektedir:

- 👮 **Worker Rights:** Verimlilik adına kitlesel gözetleme planlarını engeller (**RED State**).
- 📈 **Market Integrity:** Bot kampanyaları ile suni fiyat manipülasyonunu reddeder (**RED State**).
- 🧬 **Algorithmic Justice:** Sosyo-ekonomik profilleme ile yapılan ayrımcılığı saptar (**RED State**).
- 🌳 **Environmental Ethics:** Yasal boşlukları kullanarak doğaya zarar veren planları bayraklar (**YELLOW State**).

---

## ⚙️ Konfigürasyon (.env)

Sistemin davranışını şu parametrelerle özelleştirebilirsiniz:

- `ALPHA_WEIGHT`: AI'nın temel ağırlığı (Default: 1.0)
- `BETA_WEIGHT`: AC'nin temel ağırlığı (Default: 2.0)
- `AC_THRESHOLD`: Bloklama (Override) için eşik değer (Default: 0.7)

---

## 🚀 Kurulum ve Başlangıç

### 1. Ortam Ayarları
`.env.example` dosyasını `.env` olarak kopyalayın ve Gemini API anahtarınızı ekleyin.

### 2. Kurulum
```bash
pip install -r requirements.txt
```

### 3. Sistemi Çalıştır (Terminal Dashboard)
```bash
python main.py
```

### 4. Testleri Koştur (11/11 Benchmarks)
```bash
python -m unittest discover tests
```

---

## 🗺️ Gelecek Yol Haritası (Roadmap)

- [ ] **V0.3:** Çoklu Karar Verici (Multi-Agent) Etik Konsensüs Modülü.
- [ ] **V0.4:** Açıklanabilir AI (XAI) için görsel "Vicdan Kanıtı" grafikleri.
- [ ] **V0.5:** Blockchain tabanlı değiştirilemez "Ethical Audit Log" entegrasyonu.

---

## 📂 Proje Yapısı (Directory Tree)

```text
Hanif-AI-Architecture/
├── src/
│   ├── ac_layer/      # Yapay Vicdan (Ethics, ChromaDB, RAG)
│   ├── ai_layer/      # Analitik Motor (Gemini Strategic Output)
│   ├── am_layer/      # Yapay Akıl (Orchestrator & Weighted Synthesis)
│   └── utils/         # Dashboard Logger & TUI Helpers
├── tests/             # Moral Boundary Case Tests
├── db/                # Persistent ChromaDB Storage
├── main.py            # Entry Point (Interactive Logic)
└── .env.example       # Configuration Configuration
```

---

## 🖥️ Örnek Dashboard Çıktısı (Sample Output)

Sistem çalıştığında, katmanlar arası iletişimi şu şekilde görselleştirir:

```text
[AI (Analytical)] Analiz yapılıyor: İşçi verimliliğini artırmak için mola takibi...
[AC (Conscience)] Vicdan veritabanı sorgulanıyor (RAG)...
[AC (Conscience)] İhlal Saptandı: Hanif_01 (Yaşam ve Onur), Hanif_06 (Mahremiyet)
[AM (Mind)] Etik sürtünme tespit edildi. AC ağırlığı artırılıyor (Beta: 10.0)
🚨 [HANIF ARCHITECTURE OVERRIDE - RED STATE]
Decision Blocked: Analitik öneri kritik etik ihlalleri içeriyor.
Reasoning: Bireysel mahremiyet ve insan onuru mekanik kârın üzerindedir.
```

---

<div align="center">
  <p><i>"Geleceği inşa ederken, insanlığın fıtratını korumak için."</i></p>
  <img src="https://img.shields.io/badge/Status-Stable%20V0.2-brightgreen" alt="Status Badge">
</div>