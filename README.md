# 🇰🇪 Kenya E-commerce Reviews: Reviews vs Reality

![mark-konig-Tl8mDaue_II-unsplash](https://github.com/user-attachments/assets/5ab2e42c-af9c-472d-8e68-b5bd9ee7d024)

### 🔍 Investigating customer sentiment to expose the gap between ratings and real experience on Jumia Kenya

## 📖 Overview

In this project, I set out to analyze customer reviews from Jumia Kenya using Natural Language Processing (NLP). My original goal was to detect possible manipulation in product ratings — such as fake reviews — and uncover whether sellers were benefiting from inflated visibility at the expense of honest vendors.

While the analysis revealed that the majority of reviews were verified and positive, the deeper insights came from mismatches between what customers rated and what they actually said. This project offers a practical way to understand product satisfaction, trustworthiness, and seller credibility on Kenyan e-commerce platforms.

---

## 🎯 Objectives

- Scrape real customer reviews from Jumia Kenya
- Clean and prepare the dataset for analysis
- Use TextBlob to perform sentiment analysis on review text
- Compare star ratings to text-based sentiment labels
- Visualize trends across product categories
- Identify mismatches between numerical ratings and review tone
- Build interactive dashboards in Tableau for deeper exploration

---

## 🛠 Tools & Technologies

- *Python*: Data collection, cleaning, sentiment analysis, and EDA  
- *BeautifulSoup & Requests*: Web scraping  
- *Pandas & Seaborn*: Data manipulation and visualization  
- *TextBlob*: Sentiment polarity scoring  
- *Tableau*: Dashboard development  
- *Jupyter Notebook*: Documentation and storytelling  

---

## 🧪 Key Insights

- ✅ Over *59% of reviews* were positive, and *only 6.8%* were negative — showing strong satisfaction across most products

![image](https://github.com/user-attachments/assets/704e5196-691d-40ef-a0eb-b517eb7c7843)

- 🤖 All reviews were from *verified purchases*, boosting credibility
- 📉 Some reviews showed mismatches — products with high ratings but negative review text, and vice versa
- 🎯 Most mismatches were subtle: e.g. “It’s okay” given a 5-star rating
- 📊 Fashion and appliance categories were the most reviewed

---

## 📁 Project Structure

```bash
Kenya-Ecommerce-Reviews/
│
├── Data/
│   └── cleanedData/ and Raw/
│
├── Notebooks/
│   └── analysis.ipynb
│
├── Scraper/
│   └── jumia_scraper.py and Scraping_setup.ipynb
│
├── Tableau/
│   └── final_dashboard.twbx
│
├── Presentation/
│   └── ecommerce_insights_deck.pptx
│
└── README.md
