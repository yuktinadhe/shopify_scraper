from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(_name_)

def scrape_shopify(url):
    data = {
        "product_catalog": [],
        "hero_products": [],
        "privacy_policy": "",
        "return_policy": "",
        "faqs": [],
        "social_links": {},
        "contact_details": {},
        "about_brand": "",
        "important_links": []
    }

    # Product catalog
    try:
        r = requests.get(url.rstrip("/") + "/products.json", timeout=10)
        if r.status_code == 200:
            prods = r.json().get("products", [])
            data["product_catalog"] = [{"title": x.get("title"), "handle": x.get("handle")} for x in prods]
    except:
        pass

    # Homepage scrape
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    # Hero images
    imgs = soup.find_all("img", alt=True)
    data["hero_products"] = [img['alt'] for img in imgs if "hero" in img['alt'].lower()][:5]

    # Links extraction
    for a in soup.find_all("a", href=True):
        href = a['href']
        text = a.get_text(strip=True)
        low = href.lower()
        if "privacy" in low:
            data["privacy_policy"] = href
        if "refund" in low or "return" in low:
            data["return_policy"] = href
        if "faq" in low:
            data["faqs"].append(href)
        if "about" in low:
            data["about_brand"] = href
        if any(x in text.lower() for x in ["track", "blog", "contact"]):
            data["important_links"].append({text: href})
        if "instagram.com" in href:
            data["social_links"]["instagram"] = href
        if "facebook.com" in href:
            data["social_links"]["facebook"] = href
        if href.startswith("mailto:"):
            data["contact_details"]["email"] = href.replace("mailto:", "")
        if href.startswith("tel:"):
            data["contact_details"]["phone"] = href.replace("tel:", "")

    return data

@app.route("/get_brand_data", methods=["POST"])
def get_brand_data():
    req = request.get_json()
    url = req.get("url", "")
    if not url.startswith("http"):
        return jsonify({"error": "Invalid URL"}), 401
    try:
        result = scrape_shopify(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Server error", "detail": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Shopify Scraper running 🚀"})

if _name_ == "_main_":
    app.run(debug=True)

