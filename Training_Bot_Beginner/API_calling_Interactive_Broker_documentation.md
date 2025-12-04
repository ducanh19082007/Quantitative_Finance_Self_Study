Got you — here’s **exactly what you need**:

1. **How to call the Interactive Brokers (IBKR) API** (with the correct library).
2. **10 practice exercises specifically about IBKR API** (realistic trader/quant tasks).

IBKR is not a normal REST API → you must use **IBKR’s TWS API / IB Gateway API** via **`ib_insync`** (the easiest, industry-standard Python wrapper).

---

# ✅ 1. How to Call the Interactive Brokers API (Using `ib_insync`)

This is the cleanest way (all quants use this).

---

## **Step 1 — Install the library**

```bash
pip install ib_insync
```

---

## **Step 2 — Start TWS or IB Gateway**

IBKR API only works if:

✔ TWS is open
or
✔ IB Gateway is running

Then enable API access:

**TWS → Settings → API → “Enable ActiveX and Socket Client”**
Port is usually **7497** (paper trading).

---

## **Step 3 — Connect from Python**

```python
from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
```

If `connectionStatus()` prints “connected”:
→ you are inside Interactive Brokers API successfully.

---

## **Step 4 — Request Market Data**

Example: AAPL stock.

```python
stock = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(stock)

ticker = ib.reqMktData(stock)
ib.sleep(2)

print(ticker.last, ticker.bid, ticker.ask)
```

---

## **Step 5 — Place an Order**

```python
order = MarketOrder('BUY', 10)
trade = ib.placeOrder(stock, order)

ib.sleep(3)
print(trade.orderStatus.status)
```

---

## **Step 6 — Get Account Info**

```python
print(ib.accountSummary())
```

---

## **Step 7 — Historical Data**

```python
bars = ib.reqHistoricalData(
    stock,
    endDateTime='',
    durationStr='1 D',
    barSizeSetting='5 mins',
    whatToShow='MIDPOINT',
    useRTH=True
)

print(bars[:3])
```

---

# 🎯 10 Practice Tests for the **Interactive Brokers API**

These are **real quant-style training exercises.**

---

## **Practice Test 1 — Connect**

Write code that connects to TWS on port **7497** and prints:

```
"Connected:", ib.isConnected()
```

---

## **Practice Test 2 — Define a Contract**

Create an IBKR contract for:

* Symbol: **MSFT**
* Exchange: **SMART**
* Currency: **USD**

Then print the qualified contract ID.

---

## **Practice Test 3 — Get Live Price**

Request live market data for **SPY**, wait 2 seconds, and print:

* last
* bid
* ask

---

## **Practice Test 4 — Historical Price**

Download **1 day of 1-minute bars** for **AAPL** and print the closing prices of the first 5 bars.

---

## **Practice Test 5 — Account Summary**

Print:

* Net Liquidation
* Buying Power
* Excess Liquidity

from `ib.accountSummary()`.

---

## **Practice Test 6 — Market Order**

Place a paper-trade order:

```
Buy 1 share of TSLA at market
```

Then print the order status.

---

## **Practice Test 7 — Limit Order**

Submit a **limit buy** for **META** at a price **$2 below last price**, quantity = 5.

---

## **Practice Test 8 — Portfolio Scan**

Use `ib.positions()`.

Print:

* all tickers
* average cost
* current P/L

---

## **Practice Test 9 — Cancel an Order**

Submit a limit order for AMD, then cancel it after 1 second.

---

## **Practice Test 10 — Trading Bot Simulation**

Write a function:

```python
def trade_if_price_drops(symbol, threshold_percent):
```

It should:

1. Request live market data
2. If price drops more than **threshold_percent** from yesterday’s close →
   place a **market buy**

---

# If you want:

✔ I can generate **full solutions** for all 10 practice problems
✔ I can make an **assignment PDF** you can download
✔ I can build you a **starter IBKR trading bot**
✔ I can help set up **IB Gateway + Python** on Codespaces or Mac/Windows

Do you want the **solutions**, the **PDF**, or the **full trading bot template**?
