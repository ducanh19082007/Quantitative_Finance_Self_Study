# Mean-Reversion Trading Strategy Flowchart

```mermaid
flowchart TD
    A["Start"] --> B["Initialize Variables:
    - Capital C₀ = C_init
    - Previous position a_prev = 0
    - cumulative_sum = 0
    - cumulative_sq_diff = 0
    - profits = []"]
    
    B --> C["Loop over t = 0 to n-1 (prices P_t)"]
    
    C --> D["Update cumulative mean μ_t = cumulative_sum / (t+1)"]
    D --> E["Update cumulative std σ_t = sqrt(cumulative_sq_diff / (t+1))"]
    E --> F["Calculate Z-score Z_t = (P_t - μ_t)/σ_t (0 if σ_t=0)"]
    
    F --> G{"Determine Position a_t"}
    G --> G1{"Z_t < -B?"}
    G1 -- "Yes" --> H["Set a_t = 1 (Buy)"]
    G1 -- "No" --> G2{"Z_t > S?"}
    G2 -- "Yes" --> I["Set a_t = -1 (Sell)"]
    G2 -- "No" --> J["Set a_t = 0 (Hold)"]
    
    H --> K
    I --> K
    J --> K["Compute Profit:
    if t == 0: profit = 0
    else: profit_t = a_prev*(P_t - P_{t-1}) - c*|a_t - a_prev|"]
    
    K --> L["Update Capital: C_t = C_{t-1} + profit_t"]
    L --> P["Update cumulative sum & sq diff:
    cumulative_sum += P_t
    cumulative_sq_diff += (P_t - μ_t)^2"]
    
    P --> Q["Set a_prev = a_t"]
    Q --> R["Append profit_t to profits, C_t to capital_curve"]
    R --> C
    
    C --> S["End Loop"]
    S --> T["Return profits, total_profit=sum(profits), capital_curve"]
