# M7 Time Value of Money and Investing Basics — Model Answers（完成測驗後先好睇！）

---

## 🔄 Retest Answers（W2 錯題重測）

### Retest R1 — Answer: B

**Model Answer:** A bankers' acceptance has a maturity of 1 to 180 days (typically 90 days) — a short-term money market instrument. Options A and C are long-term: a lease running for more than one year (five or seven years) is treated as long-term financing, effectively 100% debt financing, and a seven-year term loan is plainly long-term. Option D (ordinary shares) is permanent equity capital, not money market financing.

【解題思路】分界線係**一年**：BA 45 日 → 短期；五年租約、七年 term loan → 長期；股份係永久資本。唔好再靠課文編排位置答，用規則答。

### Retest R2 — Answer: D

**Model Answer:** This is a **PIPE (private investment in public equity)**: an already-listed company sells **unregistered** shares to institutional investors, almost always **at a discount**, with an undertaking to **register the shares within a short period** (typically 60–90 days). A is wrong — an IPO is a company's FIRST public sale; StarLink has been listed for six years. B is wrong — a rights offering is made to EXISTING shareholders, not outside funds. C is wrong — a general cash offer involves REGISTERED securities open to ALL investors.

【解題思路】三步分類法：上咗市未？（上咗 → 唔係 IPO）註冊咗未？（未註冊 → 唔係 general cash offer）賣畀邊個？（外面基金，唔係現有股東 → 唔係 rights offering）→ PIPE。

### Retest R3 — Answer: 6.05%

**Model Answer / Working:**
BEY = (Face − Price) ÷ Price × 360 ÷ Days
= (20,000,000 − 19,850,000) ÷ 19,850,000 × 360 ÷ 45
= 150,000 ÷ 19,850,000 × 8
= 0.007557 × 8 = 0.060453 → **6.05%**

【解題思路】分母係**發行價 19.85m**（投資者實際付出），唔係面值；全年化用 **360 日**（360/45 = 乘 8）。常見錯：用面值做分母 → 6.00%；用 365 日 → 6.13%。

---

## Question 1 — Correct Answer: C

**Model Answer (English):**

- Ordinary annuity (payments at the end of each period):
  PV = 1,000/1.08 + 1,000/1.08² + 1,000/1.08³ + 1,000/1.08⁴ = 926 + 857 + 794 + 735 = **HK$3,312**
- Annuity due (first payment today):
  PV = 1,000 + 926 + 857 + 794 = **HK$3,577** (= HK$3,312 × 1.08)
- Statement C is correct: with the first payment today (an annuity due), PV = HK$3,577, which is larger than the ordinary annuity's PV because every cash flow is shifted forward one year and is therefore discounted less.

**【解題思路】**
- 第一步：分辨題目考嘅係 ordinary annuity（期末收付）同 annuity due（期初／即時收付）嘅分別。
- 第二步：記住來源嘅經典例子 — 4 期 HK$1,000 @ 8%：ordinary PV = HK$3,312；annuity due PV = HK$3,577。Annuity due 必然較大，因為現金流提前一期、折現較少。
- 點解 A 錯：A 將兩個數字對調咗 — 「end of year 1」係 ordinary annuity，PV 應該係 3,312 而唔係 3,577。
- 點解 B 錯：「first payment today」係 annuity due，PV 應該係較大嘅 3,577，而唔係 3,312。
- 點解 D 錯：雖然兩者未折現嘅總額一樣（都係 HK$4,000），但時間價值唔同 — 越早收到錢價值越高，所以 PV 絕對唔會相同。

## Question 2 — Correct Answer: D

**Model Answer (English):**

- EAR = (1 + i/m)^m − 1, where i = quoted APR and m = number of compounding periods per year.
- With annual compounding, m = 1: EAR = (1 + i/1)^1 − 1 = i = APR. The two rates are identical.
- For any m > 1, compounding "interest on interest" pushes the EAR above the APR — e.g., at a 24% APR: semi-monthly 26.97%, monthly 26.82%, quarterly 26.25%, but annually exactly 24.00%.
- Therefore the correct answer is D.

**【解題思路】**
- 第一步：認清 APR 係名義利率（nominal rate），唔計複利；EAR 先計埋期內利疊利。
- 第二步：當 m = 1（每年複利一次），公式 EAR = (1 + i/1)^1 − 1 = i，即係 EAR = APR。呢個係來源明確講嘅 boundary：「the only time APR and EAR are the same is when interest rate is paid only once a year」。
- 點解 A、B、C 錯：只要一年內複利多過一次（m > 1），無論 semi-monthly、monthly 定 quarterly，「利疊利」效應都會令 EAR 高過 APR；而且複利越密，EAR 越高（24% APR 下 semi-monthly 達 26.97%）。
- 考試貼士：呢類題目係典型 concept-discrimination，記住「m = 1 → APR = EAR；m > 1 → EAR > APR」就秒殺。

## Question 3 — Correct Answer: B

**Model Answer (English):**

- Growing perpetuity formula: PV0 = PMT1 / (k − g), valid only when k > g and growth continues at a constant rate forever.
- Grow: PV = 100 / (0.05 − 0.04) = 100 / 0.01 = **HK$10,000**.
- Shrink: the decline of 2% means g = −2%, so PV = 1,000 / (0.05 − (−0.02)) = 1,000 / 0.07 = **HK$14,285.71**.
- Shrink is preferred because its present value (HK$14,285.71) exceeds Grow's (HK$10,000). Hence B.

**【解題思路】**
- 第一步：兩個都係 growing perpetuity（無終點、固定增長率），用 PV0 = PMT1 / (k − g)。
- 第二步：最關鍵嘅一步係處理「shrink」— 下降 2% 即係 g = −2%，分母變成 k − g = 5% − (−2%) = 7%，唔係 3%。呢個正負號係最常見嘅計算陷阱。
- 第三步：Grow = 10,000；Shrink = 14,285.71 → Shrink 現值較高，應選 Shrink。
- 點解 A 錯：「增長」唔代表價值高 — Grow 首期只有 HK$100，基數太細，即使年年加 4%，PV 仍低過首期 HK$1,000 但每年縮 2% 嘅 Shrink。
- 點解 C 錯：公式適用條件係 k > g（5% > 4%，成立），同「growth rate vs first payment」完全無關；PV 可以正常計出。
- 點解 D 錯：兩者 CF 同 g 都唔同，PV 自然唔同 — 同樣係 perpetuity 唔代表同價值。

## Question 4 — Correct Answer: 19.56%

**Model Answer (English):**

- Monthly rate = 1.5%, so m = 12 compounding periods per year.
- EAR = (1 + i/m)^m − 1 = (1 + 0.015)^12 − 1
- (1.015)^12 = 1.195618
- EAR = 1.195618 − 1 = 0.195618 ≈ **19.56%**
- (The APR would be 1.5% × 12 = 18% — the EAR exceeds the APR because of monthly compounding.)

**【解題思路】**
- 第一步：認清「1.5% per month」係每期利率，EAR 要用複利公式 (1 + i/m)^m − 1，而唔係簡單乘 12。
- 第二步：(1.015)^12 = 1.195618，減 1 得 19.56%。
- 常見錯誤 1：直接計 1.5% × 12 = 18% — 呢個係 APR（nominal rate），唔係 EAR；題目問 EAR 就必須計複利。
- 常見錯誤 2：計 (1.18)^12 − 1 之類將期數同利率調亂 — 記住 m = 12（每月一次，一年 12 次），每期利率 1.5%。
- 檢查方向：EAR 一定要大過 APR（18%），19.56% > 18% 合理；如果你計出嚟細過 18%，即係計錯。

## Question 5 — Correct Answer: HK$17,325.53

**Model Answer (English):**

- This is an ordinary annuity: level cash flows of CF = HK$5,000, paid at the end of each period, n = 4, i = 6%.
- PVAn = CF × [1 − 1/(1+i)^n] / i
- (1.06)^4 = 1.26247696; 1 / (1.06)^4 = 0.792094
- Annuity factor = (1 − 0.792094) / 0.06 = 0.207906 / 0.06 = 3.465106
- PVAn = 5,000 × 3.465106 = **HK$17,325.53**

**【解題思路】**
- 第一步：辨認題型 — 「at the end of each of the next four years」= ordinary annuity，直接用年金現值公式，唔使逐期折現再相加（當然逐期計都會得到同一答案）。
- 第二步：計 (1.06)^4 = 1.26247696，倒數 = 0.792094；1 − 0.792094 = 0.207906；再除以 0.06 得年金 factor 3.465106。
- 第三步：5,000 × 3.465106 = 17,325.53。
- 常見錯誤 1：乘多咗 1.06（變成 18,365.06）— 嗰個係 annuity due（期初收付）嘅做法，但題目講明 end of each period，唔可以乘。
- 常見錯誤 2：直接 5,000 × 4 = 20,000 — 完全忽略折現；年金 PV 一定細過未折現總額。
- 常見錯誤 3：用錯 FVA 公式 [(1+i)^n − 1]/i — 嗰個係計未來值（終值），題目問嘅係 present value。
- 合理性檢查：PV（17,325.53）應介乎「未折現總額 20,000」之下，合理。

---
*全部內容根據 Module 7 Chapter 3 (Time Value of Money and Investing Basics) Learning Pack 編寫。*
