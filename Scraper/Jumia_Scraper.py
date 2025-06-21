import requests
from bs4 import BeautifulSoup
import csv

# Define the function to scrape one product
def scrape_reviews(product_url, product_name, category):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = [tag.get_text(strip=True) for tag in soup.find_all("h3", class_="-m -fs16 -pvs")]
    texts = [tag.get_text(strip= True) for tag in soup.find_all('p', class_="-pvs")]
    ratings = [tag.get_text(strip=True).split(" ")[0] for tag in soup.find_all("div", class_="stars _m _al -mvs")]
    dates = [date.get_text(strip=True) for date in soup.find_all('span', class_="-prs")]
    verifieds = [tag.get_text(strip=True) for tag in soup.find_all('div', class_="-df -i-ctr -gn5 -fsh0")]

    reviews = []

    for title, text, rating, date, verified in zip(titles, texts, ratings, dates, verifieds):
        reviews.append({
            "product_name": product_name,
            "category": category,
            "review_title": title,
            "review_text": text,
            "rating": rating,
            "review_date": date,
            "verified": verified
        })

    return reviews

# List of products to scrape
product_urls = [
    {"url": "https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113MW2B0MUFNAFAMZ/", "product_name": "Berrykey Hawaiian Shirt", "category": "fashion"},
    {"url": "https://www.jumia.co.ke/catalog/productratingsreviews/sku/SO460HA3N497WNAFAMZ/", "product_name": "Sonar stainless steel electric kettle", "category": "appliances"},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/SH797MW3QH84SNAFAMZ/', 'product_name': 'ASHION Fashion Casual Baseball Sweatshirt', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113MW26GWH7NAFAMZ/?page=2', 'product_name': 'Official Trouser Pant', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/GE840AA1DLOCZNAFAMZ/', 'product_name': 'Elastic Belt Corset', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113MW36KZVTNAFAMZ/', 'product_name': 'Machislet Bodycon Dress Shift', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113MW1HZXW5NAFAMZ/', 'product_name': 'High Waist Jeans Body Shape', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113SL49L9X4NAFAMZ/', 'product_name': 'Seamless Shapewear Bodysuit', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113FS1EGIZMNAFAMZ/', 'product_name': 'Mateamoda Women Shoes Sandals Heels', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113FS1N0NKCNAFAMZ/', 'product_name': 'ALagzi 2025 Mens Casual High-Top Shoes', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/HO325HA63E75ANAFAMZ/', 'product_name': 'VON VRT-195DRHS Double Door Direct Cool', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/RA255HA2Q4MADNAFAMZ/', 'product_name': 'Ramtons RM/458 - Digital Glass Microwave', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/VO144HA41D1HKNAFAMZ/', 'product_name': 'VON VALS-75BWY Twin Tub Washing Machine', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/EM389HA3GS57DNAFAMZ/', 'product_name': 'ElectroMate Dry Iron Box', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/RA589HL2RG291NAFAMZ/', 'product_name': 'Rashnik RN-2451B Hot And Normal Stand Alone Dispenser', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/RA255HA1TDS0LNAFAMZ/', 'product_name': 'Ramtons RM/399-corded Electric Kettle', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/LY007HA5Z5GZYNAFAMZ/', 'product_name': 'Lyons YT-138 Blender 2 In 1', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/AI234EA2K20BHNAFAMZ/', 'product_name': 'AILYONS SB501 2.1CH Sound Bar SubWoofer', 'category': 'TVs and audios'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/VI505EA27Q9ZENAFAMZ/', 'product_name': 'Vitron V400 2.1Ch Bluetooth Speaker System', 'category': 'TVs and audios'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/IT910EA5V0VHGNAFAMZ/', 'product_name': 'Itel BudsNeo 3 ANC Wireless Bluetooth Earphone', 'category': 'phones and tablets'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113MW3640PBNAFAMZ/', 'product_name': 'Boy Boyurn-Down Collor Top + Shorts', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113MW2BN99PNAFAMZ/', 'product_name': 'Kids Girl 2PCS Puff Sleeve Top Floral Dresses', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/GA297ST0T8KSYNAFAMZ/', 'product_name': 'Garnier Even & Matte Vitamin C Booster Serum', 'category': 'health and beauty'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/GE840FC2M7W5FNAFAMZ/', 'product_name': "Women's Bag Literary Single-Shoulder Bag", 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/RA589HL2RG291NAFAMZ/', 'product_name': 'Hot And Normal Stand Alone Dispenser (Black)', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/VI505EL092BF0NAFAMZ/', 'product_name': 'Vitron V527 - 2.1 CH Multimedia Speaker', 'category': 'TVs and audios'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113FS1PMVNXNAFAMZ/', 'product_name': 'Couple Canvas Low Top Lace-up Shoes', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/TE685MP4LFB8YNAFAMZ/', 'product_name': 'Tecno CAMON 30S', 'category': 'phones and tablets'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/GE840EA1J5XPSNAFAMZ/', 'product_name': 'Fast Charging 10000mAh Power Charging Bank', 'category': 'phones and tablets'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/GE840EA1MFDBMNAFAMZ/', 'product_name': 'RichRipple 3-Cables Portable Power Bank', 'category': 'phones and tablets'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/CI320MP28TY3UNAFAMZ/', 'product_name': 'C Idea Adults Tablets, 10 Inches Android 12', 'category': 'phones and tablets'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/CI057MP4HVF7ZNAFAMZ/', 'product_name': 'C Idea CM828,8 Inch,8GB RAM 512GB ROM', 'category': 'phones and tablets'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/AM617EA1K3NOJNAFAMZ/', 'product_name': 'Amtec 43L12, 43" FHD Smart Android TV', 'category': 'TVs and audios'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/LY007EA5EV2W6NAFAMZ/', 'product_name': 'Lyons LST4304W 43”INCH Smart Android Frameless', 'category': 'TVs and audio'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/SO521EL0MRZVUNAFAMZ/', 'product_name': 'Sony PS4 PlayStation 4 Pro Console 1TB - Black', 'category': 'gaming'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/SO521EL17TVGGNAFAMZ/', 'product_name': 'Sony PS4 PlayStation 4 Slim Console 500GB - Black', 'category': 'gaming'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/FA113FC04HFCBNAFAMZ/', 'product_name': 'Pearl Earrings Hoop Earrings Set Punk Metal Drop Earrings 6 Pairs', 'category': 'fashion'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/BR053HA44Z65CNAFAMZ/', 'product_name': 'Mika Free Standing Cooker', 'category': 'appliances'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/NU344ST2Y55W1NAFAMZ/', 'product_name': 'Nunix HD02 Fashion Hair Dryer', 'category': 'health and beauty'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/GE840ST4DB6EHNAFAMZ/', 'product_name': 'Rechargeable Metal Simple Style Hair Clipper', 'category': 'health and beauty'},
    {'url': 'https://www.jumia.co.ke/catalog/productratingsreviews/sku/LE842CL21VBLBNAFAMZ/', 'product_name': 'Lenovo Refurbished Thinkpad X250 Intel Core I5', 'category': 'computing'}
]

# Scrape and collect all reviews
all_reviews = []

for product in product_urls:
    print(f"Scraping: {product['product_name']}")
    reviews = scrape_reviews(product['url'], product['product_name'], product['category'])
    all_reviews.extend(reviews)

# Save to CSV
csv_file = "././Data/Raw/jumia_reviews.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["product_name", "category", "review_title", "review_text", "rating", "review_date", "verified"])
    writer.writeheader()
    writer.writerows(all_reviews)

print(f"\n✅ Done! Scraped {len(all_reviews)} reviews and saved to {csv_file}")