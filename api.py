from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright, expect

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is running 🫡"})

@app.route('/get_data_from_url', methods=['POST'])
def get_data_from_url():
    #Se podria modularizar esto, sin embargo al ser algo sencillo decidi dejarlo asi y no crear metodos y archivos extras🙂
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_viewport_size({'width': 1920, 'height': 1480})

            page.goto(url)

            container = page.locator('.tiendasjumboqaio-cmedia-integration-cencosud-0-x-gallery')
            expect(container).to_be_visible()
            page.wait_for_timeout(2000)
            page.mouse.wheel(0, 600)
            page.wait_for_timeout(2000)

            products = []
            divs = container.locator('> div')
            num_divs = divs.count()

            for i in range(min(15, num_divs)):
                div = divs.nth(i)
                section = div.locator('section')

                if section.is_visible():
                    name_div = section.locator('a > article > div > div:nth-child(9) > div > h3 > span')
                    price_div = section.locator('a > article > div > div:nth-child(6)')
                    promo_div = section.locator('a > article > div > div:nth-child(7) > div > div > div')

                    name = name_div.text_content() if name_div.is_visible() else None
                    price = price_div.text_content() if price_div.is_visible() else None

                    promo_price = None
                    if promo_div.count() == 3:
                        promo_price_div = promo_div.locator('div:nth-child(1) div').last
                        if promo_price_div.is_visible():
                            promo_price = promo_price_div.text_content()
                    
                    if not promo_price:
                        promo_price = "N/A"

                    products.append({
                        "name": name,
                        "price": price,
                        "promo_price": promo_price
                    })

            browser.close()
            return jsonify({"url": url, "products": products})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
