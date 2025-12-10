# Mean-Reversion Trading Strategy Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Initialize Variables]
    B --> C[Loop over t = 0 to n-1]
    
    C --> D[Update cumulative mean μ_t = cumulative_sum / (t+1)]
    D --> E[Update cumulative std σ_t = sqrt(cumulative_sq_diff / (t+1))]
    E --> F[Calculate Z-score Z_t = (P_t - μ_t)/σ_t (0 if σ_t=0)]
    F --> G[Determine Position a_t]
    
    G --> G1{Z_t < -B?}
    G1 -- Yes --> H[Set a_t = 1 (Buy)]
    G1 -- No --> G2{Z_t > S?}
    G2 -- Yes --> I[Set a_t = -1 (Sell)]
    G2 -- No --> J[Set a_t = 0 (Hold)]
    
    H --> K[Compute Profit]
    I --> K
    J --> K
    
    K --> L{t == 0?}
    L -- Yes --> M[profit = 0]
    L -- No --> N[profit_t = a_prev*(P_t - P_{t-1}) - c*|a_t - a_prev|]
    
    M --> O[Update Capital: C_t = C_{t-1} + profit_t]
    N --> O
    
    O --> P[Update cumulative sum & sq diff]
    P --> Q[Set a_prev = a_t]
    Q --> R[Append profit_t to profits, C_t to capital_curve]
    R --> C
    
    C --> S[End Loop]
    S --> T[Return profits, total_profit=sum(profits), capital_curve]
