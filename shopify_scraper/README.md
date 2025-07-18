# 🛍 Shopify Brand Scraper (Flask Project)

This is a simple Flask-based API that scrapes a Shopify store and extracts brand-related information *without using the Shopify API*.

---

## ✅ Features

- 📦 Scrapes product catalog (/products.json)
- 🖼 Detects hero images from homepage
- 🔐 Finds Privacy Policy & Return/Refund links
- ❓ Extracts FAQ page links
- 🔗 Grabs social media & contact info
- 🧠 Gives a clean, structured JSON response

---

## 📁 Folder Structure

shopify_scraper/ ├── app/ │   └── main.py              # Flask app and scraper logic ├── requirements.txt         # Package requirements ├── README.md                # This file ├── test_body.json           # Sample JSON request for testing └── .gitignore

## 🚀 How to Run Locally

### 1. Open project folder in VS Code

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask server

```bash
python app/main.py 
```

## 🧾 Sample Output (Shortened)

```json
{
  "product_catalog": [{ "title": "Printed T-Shirt", "handle": "printed-tee" }],
  "hero_products": ["Hero Banner T-Shirt"],
  "privacy_policy": "/pages/privacy-policy",
  "return_policy": "/pages/refund-policy",
  "faqs": ["/pages/faqs"],
  "social_links": {
    "instagram": "https://instagram.com/...",
    "facebook": "https://facebook.com/..."
  },
  "contact_details": {
    "email": "support@brand.com",
    "phone": "‪+91-9999999999‬"
  },
  "about_brand": "/pages/about-us",
  "important_links": [{ "Track Order": "/pages/track-order" }]
}
```
---

## 👨‍💻 Author

Built by Yukti Nadhe for a GenAI Developer Internship Assignment 🚀

