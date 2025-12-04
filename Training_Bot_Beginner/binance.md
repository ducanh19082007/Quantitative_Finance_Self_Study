Perfect — here is a **clean guide for calling the Binance API** (spot trading), followed by **10 Binance-specific practice tests for crypto trading/quant work**, exactly like you asked.

This uses the **official Binance API style**, with REST endpoints + signature rules (HMAC-SHA256).

---

# ✅ 1. Install Dependencies

```bash
pip install python-binance
```

Or if you want to implement signing manually, `requests` + `hmac` also works (I’ll show both).

---

# ✅ 2. Connect to Binance (Using python-binance)

```python
from binance.client import Client

API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

client = Client(API_KEY, SECRET_KEY)
```

---

# ✅ 3. Get Market Prices (Ticker)

```python
price = client.get_symbol_ticker(symbol="BTCUSDT")
print(price)
```

---

# ✅ 4. Get Order Book

```python
depth = client.get_order_book(symbol="ETHUSDT", limit=5)
print(depth)
```

---

# ✅ 5. Get Account Info (Balances, Positions)

```python
account = client.get_account()
for asset in account["balances"]:
    if float(asset["free"]) > 0:
        print(asset)
```

---

# ✅ 6. Place a Market Order

```python
order = client.order_market_buy(
    symbol="BTCUSDT",
    quantity=0.0005
)
print(order)
```

---

# ✅ 7. Place a Limit Order

```python
order = client.order_limit_buy(
    symbol="ETHUSDT",
    quantity=0.01,
    price="3000.00"
)
print(order)
```

---

# ✅ 8. Get Order Status

```python
order_status = client.get_order(
    symbol="BTCUSDT",
    orderId=order["orderId"]
)
print(order_status)
```

---

# ✅ 9. Cancel Order

```python
client.cancel_order(symbol="ETHUSDT", orderId=order["orderId"])
```

---

# ✅ 10. Get Historical Data (Klines / Candlesticks)

```python
import pandas as pd

klines = client.get_klines(
    symbol="BTCUSDT",
    interval=Client.KLINE_INTERVAL_1MINUTE,
    limit=10
)

df = pd.DataFrame(
    klines,
    columns=[
        "open_time","open","high","low","close","volume",
        "close_time","qav","num_trades","taker_buy_base","taker_buy_quote","ignore"
    ]
)
print(df.head())
```

---

# 🔥 11. Binance API (Manual REST Request With Signature)

Sometimes interviews expect this.

Binance requires:

```
timestamp + query_string → sign using HMAC-SHA256(secret)
```

Example:

```python
import time, hmac, hashlib, requests

API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

base = "https://api.binance.com"
endpoint = "/api/v3/account"
timestamp = int(time.time() * 1000)

query = f"timestamp={timestamp}"
signature = hmac.new(
    SECRET_KEY.encode(),
    query.encode(),
    hashlib.sha256
).hexdigest()

url = f"{base}{endpoint}?{query}&signature={signature}"
headers = {"X-MBX-APIKEY": API_KEY}

r = requests.get(url, headers=headers)
print(r.json())
```

---

# 🎯 **10 Binance API Practice Tests (Crypto-Specific)**

These match what quants actually do.

---

## **Practice Test 1 — Connect to Binance**

Write code that connects and prints:

* server time
* exchange status

---

## **Practice Test 2 — Get Latest BTC Price**

Call:

```
GET /api/v3/ticker/price?symbol=BTCUSDT
```

Print the `price`.

---

## **Practice Test 3 — Get Order Book**

Download the top 10 levels for **ETHUSDT** and print:

* best bid
* best ask

---

## **Practice Test 4 — Get Klines**

Download the latest **50 1-minute candles** for BTCUSDT and calculate:

* 20-period moving average
* 20-period volatility

---

## **Practice Test 5 — Market Order**

Place:

```
Buy 0.001 BTC at market
```

Print the returned order ID and executed price.

---

## **Practice Test 6 — Limit Order**

Place a limit buy order:

* Asset: ETHUSDT
* Qty: 0.02
* Price: **2% below the current market price**

---

## **Practice Test 7 — Check Balance**

Print free USDT and free BTC amount from your account.

---

## **Practice Test 8 — Cancel Orders**

Write code to cancel **all open orders** for:

```
ETHUSDT
```

---

## **Practice Test 9 — Trade Trigger**

Make a function:

```python
def buy_the_dip(symbol, percent_drop):
```

Behavior:

1. get last closing price
2. get current price
3. if drop ≥ percent_drop → buy 20 USD worth

---

## **Practice Test 10 — Basic Crypto Bot**

Write a loop that:

1. checks BTCUSDT price every 5 seconds
2. if RSI(14) < 30 → buy 10 USD worth
3. if RSI(14) > 70 → sell 10 USD worth

(Note: use rolling data from recent klines.)

---

If you want:

✅ **Full solutions** for all 10
✅ A **PDF formatted practice sheet**
✅ A **Binance trading bot template (with backtesting + risk management)**
Just tell me!
