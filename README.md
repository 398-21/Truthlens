# 🧠 Objective News Aggregator — AI-Powered Web Crawling Pipeline

This project is a **custom-built AI-enhanced news aggregation pipeline** that crawls global **tech and business news**, detects **semantic similarities**, **translates** multi-language content, and synthesizes objective summaries using **GPT-based large language models**. It is designed for researchers, journalists, and data scientists seeking truth-focused, multi-source, multilingual news intelligence.

> 🛠️ Built with: Python 3.11.5 · Scrapy · GPT APIs · Custom NLP logic · Translation APIs  
> 🔍 Purpose: Reduce bias and redundancy by combining and summarizing news articles from diverse sources in a unified, objective format

---

## 🚀 Key Features

- 🔎 **Multi-source crawling**: Custom spiders scrape tech and business news across sites
- 🧠 **AI-powered similarity detection**: NLP techniques find overlapping stories from different publishers
- 🌍 **Language translation**: Auto-translates non-English articles to English for unified analysis
- 🧬 **GPT-based summarization**: Condenses multi-source input into **factual, objective summaries**
- 🧹 **Custom pipeline**: Modular, extendable processing architecture for real-time news transformation

---

## 🧠 Why It Matters to Machine Learning and AI

This project integrates multiple areas of machine learning, natural language processing (NLP), and applied AI:

| **AI Component** | **Role in Pipeline** |
|------------------|----------------------|
| ✨ GPT Model | Converts combined, multi-source data into concise, neutral news summaries |
| 🧩 NLP Similarity Engine | Matches articles on the same topic from different sites using vector embeddings |
| 🌐 Translation Model/API | Ensures non-English content is processed in the same embedding space |
| 🧠 Prompt Engineering | Guides GPT output toward objective, fact-based reporting |
| 🔁 Custom Data Pipeline | Prepares news for future fine-tuning or supervised classification models |

The project is a stepping stone toward building **bias detection models**, **stance detection**, or **source trustworthiness scoring systems** in future research.

---

## 📂 Project Structure

```
project-root/
│
├── Crawler/
│   ├── run_all_spiders.py        # Master script to run all crawlers
│   ├── market_data.json          # Output file with processed articles
│   ├── .env.example              # Template for OpenAI key and API configs
│   ├── items.py                  # Data schema for scraped articles
│   ├── middlewares.py           # Request/response interceptors
│   ├── pipelines.py             # Handles translation, similarity, GPT rewriting
│   ├── settings.py              # Core crawler settings
│   └── spiders/                 # Spider definitions for each site
│       ├── AFSpider.py
│       ├── ASTSpider.py
│       └── ...
│
├── requirements.txt             # All Python dependencies
└── README.md
```

---

## ⚙️ How It Works

1. **Scrapy Spiders**: Crawl news from predefined business and tech sources
2. **Preprocessing**: Clean text and compute vector embeddings for similarity
3. **Clustering/Matching**: Group similar articles across sources
4. **Translation**: Convert non-English stories to English using APIs
5. **GPT Summarization**: Condense and rewrite grouped articles into a neutral tone
6. **Export**: Output structured JSON for database use, apps, or dashboards

---

## 💾 Setup Instructions

Follow the instructions in [`Backend Setup Instructions`](#) to:

- Create and activate a virtual environment
- Install dependencies
- Set up your `.env` file with your OpenAI API key
- Run the spiders to crawl and generate processed news content

---

## 🧠 Potential Use Cases

- 🗞️ **Bias-free news app** for multilingual tech/business readers
- 🧑‍🔬 **Research dataset** for stance or truthfulness classification
- 🧑‍⚖️ **Source trustworthiness analysis**
- 📰 **Content moderation** and misinformation detection
- 🤖 **Autonomous news agents** for summarizing the day’s events objectively

---

## 📈 Future Enhancements

- Fine-tuned GPT model for news-specific summarization  
- Automatic stance/bias detection using supervised ML  
- Topic modeling and clustering via unsupervised learning  
- Telegram or WhatsApp bot integration for daily digest delivery  
- Frontend dashboard for visualization and article curation  

---

## 📜 License

This project is released under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**David Pan**  
AI Developer & News Integrity Enthusiast

BSc in AI and Machine Learning
First Class Honours


---

> “In an era of noise, clarity is power — this system helps you find it.”
