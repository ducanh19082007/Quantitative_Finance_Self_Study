Got it! I’ll create a **Markdown-ready version** of your mean-reversion strategy flowchart that you can directly paste into a `.md` file. I’ll use **ASCII-style boxes** and indentation for clarity.

```markdown
# Mean-Reversion Trading Strategy Flowchart

```

Start
│
▼
Initialize:

* Capital C₀ = C_init
* Previous position a_prev = 0
* cumulative_sum = 0
* cumulative_sq_diff = 0
* profits = []
  │
  ▼
  For t = 0 to n-1 (loop over prices P_t):
  │
  ▼
  Update cumulative mean:
  μ_t = cumulative_sum / (t + 1)
  Update cumulative std:
  σ_t = sqrt(cumulative_sq_diff / (t + 1))
  │
  ▼
  Calculate Z-score:
  Z_t = 0 if σ_t == 0 else (P_t - μ_t) / σ_t
  │
  ▼
  Determine position a_t:
  ┌───────────────────────────┐
  │ Z_t < -B ?                │─► Yes: a_t = 1
  │ Z_t > S  ?                │─► Yes: a_t = -1
  │ Otherwise                 │─► a_t = 0
  └───────────────────────────┘
  │
  ▼
  Compute profit:
  if t == 0: profit = 0
  else: profit_t = a_prev * (P_t - P_{t-1}) - c * |a_t - a_prev|
  │
  ▼
  Update capital:
  C_t = C_{t-1} + profit_t
  │
  ▼
  Update cumulative sum / sq diff:
  cumulative_sum += P_t
  cumulative_sq_diff += (P_t - μ_t)^2
  │
  ▼
  Set a_prev = a_t
  Append profit_t to profits
  Append C_t to capital_curve
  │
  ▼
  Next t
  │
  ▼
  End loop
  │
  ▼
  Return:
* profits
* total_profit = sum(profits)
* capital_curve

```

---

### ✅ Notes

- **B** = buy threshold  
- **S** = sell threshold  
- **c** = trading cost fraction  
- Z-score decides **whether to buy, sell, or hold**.  
- Profits are calculated using the **previous position**.  
- Capital curve reflects **real money**, starting from `C_init`.  

---

If you want, I can also create a **Markdown version using Mermaid.js** so it renders as an actual flowchart diagram when viewed on GitHub or VS Code. This looks much more professional than ASCII boxes.  

Do you want me to do that?
```
