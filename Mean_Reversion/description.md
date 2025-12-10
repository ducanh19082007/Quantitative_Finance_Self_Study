Sure! We can translate your Python mean-reversion loop into a **mathematical formulation** step by step. Let’s define the variables and write the formulas clearly.

---

### **Variables**

* ( P_t ) = price at time ( t )
* ( \mu_t ) = cumulative mean up to time ( t )
* ( \sigma_t ) = cumulative standard deviation up to time ( t )
* ( Z_t ) = Z-score at time ( t )
* ( a_t ) = position at time ( t ):
  [
  a_t =
  \begin{cases}
  1 & \text{if } Z_t < -\text{buy threshold} \
  -1 & \text{if } Z_t > \text{sell threshold} \
  0 & \text{otherwise}
  \end{cases}
  ]
* ( \text{profit}_t ) = profit at time ( t )
* ( C_t ) = capital at time ( t )
* ( c ) = trading cost fraction

---

### **Step 1: Cumulative mean**

[
\mu_t = \frac{1}{t+1} \sum_{i=0}^{t} P_i
]

---

### **Step 2: Cumulative standard deviation**

[
\sigma_t = \sqrt{\frac{1}{t+1} \sum_{i=0}^{t} (P_i - \mu_t)^2}
]

---

### **Step 3: Z-score**

[
Z_t = \frac{P_t - \mu_t}{\sigma_t}, \quad \text{with } Z_0 = 0 \text{ if } \sigma_t = 0
]

---

### **Step 4: Position (decision rule)**

[
a_t =
\begin{cases}
1 & Z_t < -\text{buy threshold} \
-1 & Z_t > \text{sell threshold} \
0 & \text{otherwise}
\end{cases}
]

---

### **Step 5: Profit at time ( t )**

For ( t = 0 ):
[
\text{profit}_0 = 0
]

For ( t > 0 ):
[
\text{profit}*t = a*{t-1} \cdot (P_t - P_{t-1}) - c \cdot |a_t - a_{t-1}|
]

* The first term = PnL from holding previous position.
* The second term = trading cost if position changes.

---

### **Step 6: Capital update**

For initial capital ( C_0 = C_{\text{init}} ):

[
C_t = C_{t-1} + \text{profit}_t
]

Or, if you want **compounded return scaling** as in your original code:

[
C_t = C_{t-1} \cdot \left( 1 + \frac{\text{profit}*t}{P*{t-1}} \right)
]

---

### **Step 7: Cumulative profit**

[
\text{Cumulative Profit}*t = \sum*{i=0}^{t} \text{profit}_i
]

---

So in **compact form**:

[
\begin{aligned}
&\mu_t = \frac{1}{t+1} \sum_{i=0}^{t} P_i \
&\sigma_t = \sqrt{\frac{1}{t+1} \sum_{i=0}^{t} (P_i - \mu_t)^2} \
&Z_t =
\begin{cases} 0 & \sigma_t = 0 \ \frac{P_t - \mu_t}{\sigma_t} & \text{otherwise} \end{cases} \
&a_t =
\begin{cases} 1 & Z_t < -B \ -1 & Z_t > S \ 0 & \text{otherwise} \end{cases} \
&\text{profit}*0 = 0 \
&\text{profit}*t = a*{t-1}(P_t - P*{t-1}) - c |a_t - a_{t-1}|, \quad t>0 \
&C_0 = C_{\text{init}}, \quad C_t = C_{t-1} + \text{profit}_t \
&\text{Cumulative Profit}*t = \sum*{i=0}^{t} \text{profit}_i
\end{aligned}
]

Where ( B = ) buy threshold, ( S = ) sell threshold, ( c = ) trading cost fraction.

---

If you want, I can also **draw a flowchart of this math** so it’s easier to implement or even vectorize.

Do you want me to do that?
