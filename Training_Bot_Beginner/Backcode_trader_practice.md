Got you — here are **10 coding lessons** to learn **Backtrader** step-by-step, written simply but still useful for serious algorithmic trading practice.
Each lesson includes:

* 🌱 *What you learn*
* 🧠 *Why it matters*
* 💻 *Example code (runnable)*
* 📝 *Practice questions*

---

# 🚀 **10-Lesson Backtrader Coding Course (Beginner → Intermediate)**

---

# **Lesson 1 — What is Backtrader? (Like you're 5)**

### 🌱 What you learn

“Backtrader is a playground where you teach a robot how to trade.
You give it past price data → it trades → you see if it wins or loses.”

### 🧠 Why it matters

All algo traders use backtesting before touching real money.

### 💻 Example (Load Backtrader)

```python
import backtrader as bt

cerebro = bt.Cerebro()
print("Backtrader loaded!")
```

### 📝 Practice

1. Install Backtrader in a new environment.
2. Print all built-in indicators using `dir(bt.indicators)`.

---

# **Lesson 2 — Create Your First Strategy**

### 🌱 What you learn

A strategy = instructions your trading robot follows.

### 💻 Example

```python
import backtrader as bt

class TestStrategy(bt.Strategy):
    def __init__(self):
        pass

    def next(self):
        print(f"Price today: {self.data.close[0]}")

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)

data = bt.feeds.YahooFinanceCSVData(dataname='AAPL.csv')
cerebro.adddata(data)
cerebro.run()
```

### 📝 Practice

1. Print open, high, low, close each day.
2. Count how many days of data you loaded.

---

# **Lesson 3 — Indicators (Moving Average)**

### 🌱 What you learn

Indicators help the robot “see.”

### 💻 20–Day Moving Average

```python
class SmaStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data, period=20)

    def next(self):
        print(self.sma[0])
```

### 📝 Practice

1. Plot the SMA values.
2. Create SMA(50) and SMA(200).

---

# **Lesson 4 — Buy & Sell Logic**

### 🌱 What you learn

How to make your robot enter and exit trades.

### 💻 SMA Crossover Strategy

```python
class SmaCross(bt.Strategy):
    def __init__(self):
        self.sma20 = bt.indicators.SMA(self.data, period=20)
        self.sma50 = bt.indicators.SMA(self.data, period=50)

    def next(self):
        if not self.position:  # no trade open
            if self.sma20[0] > self.sma50[0]:
                self.buy()
        else:
            if self.sma20[0] < self.sma50[0]:
                self.sell()
```

### 📝 Practice

1. Modify the strategy to use SMA10 & SMA30.
2. Print when trades open and close.

---

# **Lesson 5 — Log Trades and Portfolio Value**

### 🌱 What you learn

Tracking performance.

### 💻 Example

```python
def log(self, txt):
    print(f"{self.data.datetime.date(0)}: {txt}")

def next(self):
    self.log(f"Close = {self.data.close[0]}")
```

### 📝 Practice

1. Log every buy/sell price.
2. Log portfolio value every 10 days.

---

# **Lesson 6 — Adding Cash, Commission, Slippage**

### 🌱 What you learn

Make backtests realistic.

### 💻 Example

```python
cerebro = bt.Cerebro()
cerebro.broker.setcash(10000)
cerebro.broker.setcommission(commission=0.001)
```

### 📝 Practice

1. Simulate crypto trading with 0.075% fee.
2. Test starting with $1,000, $5,000, and $20,000.

---

# **Lesson 7 — Optimization**

### 🌱 What you learn

Find the best parameters automatically.

### 💻 Example

```python
cerebro.optstrategy(
    SmaCross,
    sma1=range(10, 40),
    sma2=range(50, 100),
)
```

### 📝 Practice

1. Optimize a Bollinger Bands strategy.
2. Find the best SMA period between 5–200.

---

# **Lesson 8 — Plotting Results**

### 🌱 What you learn

Visualizing performance.

### 💻 Example

```python
cerebro.run()
cerebro.plot()
```

### 📝 Practice

1. Plot price + 3 indicators at once.
2. Plot a zoomed-in portion of the chart.

---

# **Lesson 9 — Multiple Data Feeds (Portfolio Strategy)**

### 🌱 What you learn

Trade many tickers at once.

### 💻 Example

```python
data1 = bt.feeds.YahooFinanceCSVData(dataname='AAPL.csv')
data2 = bt.feeds.YahooFinanceCSVData(dataname='MSFT.csv')

cerebro.adddata(data1, name='AAPL')
cerebro.adddata(data2, name='MSFT')
```

### 📝 Practice

1. Buy whichever ticker has the strongest SMA(20) trend.
2. Short the weaker one.

---

# **Lesson 10 — Creating Your Own Indicator**

### 🌱 What you learn

Custom tools = more powerful robot.

### 💻 Example

```python
class DiffIndicator(bt.Indicator):
    lines = ('diff',)
    def __init__(self):
        self.lines.diff = self.data.high - self.data.low
```

### 📝 Practice

1. Create an indicator that measures volatility.
2. Build an RSI(14) from scratch (bonus).

---

# 🎯 Want the 10 lessons packaged into files (.py) OR want advanced lessons?

I can generate:

* Full project folder
* All lessons in one PDF
* Advanced lessons (ML + Backtrader, crypto live trading)

Just tell me:
**“Give me the full project”** or **“Next 10 lessons”**
