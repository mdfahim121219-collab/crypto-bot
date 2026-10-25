import requests
import time

TOKEN = "8882579503:AAH74D8r6W2mBqZzFm3dwQJECx_MiRcDcZE"
USER_ID = "5451132819"

def send_alert(text):
    url = f"https://telegram.org{TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": USER_ID, "text": text, "parse_mode": "Markdown"})
    except:
        pass

print("🚀 Server is running...")
send_alert("✅ *আপনার Whale Alert Bot এখন GitHub & Render সার্ভারে সফলভাবে সচল হয়েছে!*")

while True:
    try:
        res = requests.get("https://coingecko.com")
        if res.status_code == 200:
            for coin in res.json():
                vol = abs(coin.get("market_cap_change_24h", 0))
                if 50000 <= vol <= 5000000:
                    msg = f"🚨 *Crypto Whale Alert*\n\n🪙 *টোকেন:* {coin.get('name')} ({coin.get('symbol').upper()})\n💰 *ভ্যালু:* ${vol:,.2f} USD\n💵 *বর্তমান মূল্য:* ${coin.get('current_price')}"
                    send_alert(msg)
    except:
        pass
    time.sleep(60)
