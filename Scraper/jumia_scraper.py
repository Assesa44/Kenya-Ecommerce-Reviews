import sqlite3

def save_review_to_db(product_name, category, review_text, rating, review_date, verified):
    try:
        conn = sqlite3.connect('././data/reviews.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO reviews (
                product_name, category, review_text, rating, review_date, verified
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', (product_name, category, review_text, rating, review_date, verified))

        conn.commit()
        conn.close()
        print(f"Saved review for '{product_name}'")

    except Exception as e:
        print(f"Error saving review: {e}")

        # Test saving a dummy review
if __name__ == "__main__":
    save_review_to_db(
        product_name="Men's Sneakers",
        category="fashion",
        review_text="Very comfortable and stylish.",
        rating=5,
        review_date="2024-06-01",
        verified="yes"
    )

import requests
from bs4 import BeautifulSoup

# Temporary hardcoded product info
product_url = "https://www.jumia.co.ke/berrykey-mens-hawaiian-ink-print-bottom-down-beach-short-sleeve-t-shirt-casual-tops-153773493.html"
product_name = "Berrykey Hawaiian Shirt"
category = "fashion"

# Send request
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(product_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find review elements
review_elements = soup.find_all("h3", class_="-m -fs16 -pvs")

reviews_list = []
print(f"Found {len(review_elements)} reviews:")
for review in review_elements:
    review_text = review.get_text(strip=True)
    reviews_list.append(review_text)
    print("•", review_text)

# Find rating elements
rating_elements = soup.find_all("div", class_="stars _m _al -mvs")

ratings_list = []
print(f'Found {len(rating_elements)} ratings:')
for rating in rating_elements:
    rate = rating.get_text(strip= True)
    ratings_list.append(rate)
    print("•", rate)

# Find review date
review_date = soup.find_all('span', class_="-prs")

date_list = []
print(f'Found {len(review_date)} review dates:')
for date in review_date:
    date = date.get_text(strip= True)
    date_list.append(date)
    print("•", date)

# Find verified tag
verified_tag = soup.find_all('div', class_="-df -i-ctr -gn5 -fsh0")

tag_list = []
print(f'Found {len(verified_tag)} verified tags:')
for tag in verified_tag:
    tag = tag.get_text(strip= True)
    tag_list.append(tag)
    print("•", tag)

# Create dictionary.
reviews = []

for text, rating, date, tag in zip(reviews_list, ratings_list, date_list, tag_list):
    reviews.append({'text':text, 'rating':rating, 'date':date, 'verified':tag})

product_name = 'Berrykey Hawaiian Shirt'
category = 'fashion'

for r in reviews:
    save_review_to_db(
        product_name= product_name,
        category=category,
        review_text= r['text'],
        rating= r['rating'],
        review_date=r['date'],
        verified=r['verified']
    )

# Batch scraping
product_urls = [{'url': 'https://www.jumia.co.ke/fashion-mens-track-suits-2-piece-set-active-jogging-suits-sweatsuits-casual-outfits-283262160.html', 'product_name': "Men's Track Suits 2 Piece", 'category': 'fashion'},
                {'url': 'http://jumia.co.ke/ashion-fashion-casual-baseball-sweatshirt-casual-jacket-whiteblack-263227852.html', 'product_name': 'ASHION Fashion Casual Baseball Sweatshirt', 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/fashion-mens-casual-button-down-denim-jacket-classic-jean-coat-265442567.html', 'product_name': "Men's Casual Button Down Denim Jacket", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/fashion-official-trouser-pant-black-slim-fit-office-wear-men-153689713.html', 'product_name': "Official Trouser Pant", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/fashion-elastic-belt-corset-tummy-shaper-13521338.html', 'product_name': "Elastic Belt Corset", 'category': 'fashion'},
                {'url': 'http://jumia.co.ke/machislet-bodycon-dress-shift-dress-ladies-dresses-party-dress-wedding-dress-evening-dress-casual-dress-holiday-dresses-for-the-ladies-194855429.html', 'product_name': "Machislet Bodycon Dress Shift", 'category': 'fashion'},
                {'url': 'http://jumia.co.ke/fashion-high-waist-jeans-body-shape-sky-blue-33569609.html', 'product_name': "High Waist Jeans Body Shape", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/generic-seamless-shapewear-bodysuit-womens-tummy-control-body-shapers-black-comisole-208837975.html', 'product_name': "Seamless Shapewear Bodysuit", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/mateamoda-women-shoes-sandals-heels-slippers-ladies-shoes-casual-shoes-60915748.html', 'product_name': "Mateamoda Women Shoes Sandals Heels", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/alagzi-2025-mens-casual-high-top-shoes-running-sneakers-beige-48872199.html', 'product_name': "ALagzi 2025 Mens Casual High-Top Shoes", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/von-vrt-195drhs-double-door-direct-cool-195l-dark-silver-305389486.html', 'product_name': "VON VRT-195DRHS Double Door Direct Cool", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/hisense-h20moms11-20-liters-microwave-white-2yrs-wrty-315502918.html', 'product_name': "Hisense H20MOMS11 - 20 Liters Microwave ", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/von-vals-75bwy-twin-tub-washing-machine-7.5kg1yr-wrty-267725144.html', 'product_name': "VON VALS-75BWY Twin Tub Washing Machine", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/em-electromate-dry-iron-box-1000w-with-5-gear-temperature-control-1yr-wrty-279458590.html', 'product_name': "ElectroMate Dry Iron Box ", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/bruhm-bgc-5531ibk-gas-cooker-5050-black-1yr-wrty-265084252.html', 'product_name': "Bruhm BGC-5531IBK Gas Cooker,", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/rashnik-rn-2451b-hot-and-normal-stand-alone-dispenser-black-179313076.html', 'product_name': "Rashnik RN-2451B Hot And Normal Stand Alone Dispenser", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/ramtons-rm399-corded-electric-kettle-1.7-ltrs-white-1yr-wrty-177871890.html', 'product_name': "Ramtons RM/399-corded Electric Kettle", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/lyons-yt-138-blender-2-in-1-with-grinder-machines-1.5l-black-305727316.html', 'product_name': "Lyons YT-138 Blender 2 In 1 ", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/nunix-3-three-burner-low-gas-consumption-glass-top-table-infrared-cooker-183358659.html', 'product_name': "Nunix 3 Three Burner Low Gas Consumption Glass Top Table", 'category': 'appliances'},
                {'url': 'https://www.jumia.co.ke/hisense-43-inch-43a4kken-smart-tv-2yrs-wrty-312890046.html', 'product_name': "Hisense 43 Inch 43A4KKEN Smart TV", 'category': 'TV & Audios'},
                {'url': 'https://www.jumia.co.ke/ailyons-sb501-2.1ch-sound-bar-subwoofer-with-bluetooth-home-theatrer-18000w-pmpo-black-1yr-wrty-179381645.html', 'product_name': "AILYONS SB501 2.1CH Sound Bar SubWoofer", 'category': 'TV & Audios'},
                {'url': 'https://www.jumia.co.ke/amtec-55l12-55-frameless-4k-uhd-smart-android-tv-1.5gb-ram-8gb-rom-black-1yr-wrty-115584799.html', 'product_name': 'Amtec 55L12 - 55" Frameless 4K UHD Smart Android TV', 'category': 'TV & Audios'},
                {'url': 'http://jumia.co.ke/vitron-v400-2.1ch-bluetooth-speaker-system-185651933.html', 'product_name': "Vitron V400 2.1Ch Bluetooth Speaker System", 'category': 'TV & Audios'},
                {'url': 'https://www.jumia.co.ke/xiaomi-redmi-a3x-6.71-display-3gb-ram-64gb-5000mah-dual-sim-black-203838938.html', 'product_name': "XIAOMI Redmi A3x", 'category': 'phones & tablets'},
                {'url': 'https://www.jumia.co.ke/oppo-refurbished-a57-5.2-3gb-ram-32gb-rom-16mp-camera-2900mahdual-sim-gold-313705097.html', 'product_name': "Oppo Refurbished A57", 'category': 'phones & tablets'},
                {'url': 'https://www.jumia.co.ke/generic-tws-bluetooth-earphones-sports-wireless-headphones-with-mic-200430470.html', 'product_name': "TWS Bluetooth Earphones", 'category': 'phones & tablets'},
                {'url': 'https://www.jumia.co.ke/catpapa-1-6years-kids-boy-boyurn-down-collor-top-shorts-195736619.html', 'product_name': "Boy Boyurn-Down Collor Top + Shorts", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/fashion-1-6-years-kids-girl-2pcs-puff-sleeve-top-floral-dresses-192239404.html', 'product_name': "Kids Girl 2PCS Puff Sleeve Top Floral Dresses", 'category': 'fashion'},
                {'url': 'https://www.jumia.co.ke/hp-refurbished-elitebook-840-g3-6th-gen-core-i7-8gb-ram-hdd-500gb-14-silver-6-months-wrty-69597767.html', 'product_name': "HP Refurbished Elitebook 840", 'category': 'computing'},]

# Create scraping function
def scrape_reviews_for_product(product):
    print(f"Scraping: {product['product_name']}")
    url = product['url']
    name = product['product_name']
    category = product['category']

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    texts = [tag.get_text(strip=True) for tag in soup.find_all("h3", class_="-m -fs16 -pvs")]
    ratings = [int(tag["alt"][0]) for tag in soup.find_all("img", alt=True) if "star" in tag["alt"].lower()]
    dates = [date.get_text(strip= True) for date in soup.find_all('span', class_="-prs")]
    verifieds = [tag.get_text(strip= True) for tag in soup.find_all('div', class_="-df -i-ctr -gn5 -fsh0")]

    for text, rating, date, verified in zip(texts, ratings, dates, verifieds):
        save_review_to_db(name, category, text, rating, date, verified)

# loop through the product urls.
if __name__ == "__main__":
    for product in product_urls:
        scrape_reviews_for_product(product)

# END/
