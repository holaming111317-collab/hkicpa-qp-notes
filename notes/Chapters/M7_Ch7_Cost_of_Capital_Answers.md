# M7 Cost of Capital — Model Answers（完成測驗後先好睇！）

---

**Question 1 — Correct answer: B**

**Model answer:** The weights in a WACC calculation should be based on the **market values** of the financing sources: debt = 350 / (350 + 1,050) = 25%; equity = 1,050 / 1,050 + 350 = 75%. WACC is the opportunity cost of capital for the firm's investors **as of today**, and opportunity costs are measured at current market values, not at the historical amounts recorded when the capital was raised.

【解題思路】呢題考 book value vs market value 權重嘅概念分辨。WACC 本質上係投資者「今日」嘅機會成本，所以每個資金來源嘅比重，應該反映佢哋今日喺市場值幾多錢（market value），而唔係當年集資時記落簿嘅歷史金額（book value）。選項 A 同 C 都主張用 book value，前者話 book value 反映「實際籌到嘅資本」——但嗰個係歷史成本，同今日機會成本無關；後者話 market value 波動大唔穩定——波動並唔係放棄機會成本原則嘅理由。選項 D 話兩者結果一樣——只有喺市值剛好等於賬面值嘅極罕有情況下先成立，呢度明顯唔同（股權市值 1,050m 遠高於賬面 600m）。「考官報告指出」考生經常喺 OTQ 誤用賬面值權重，令 WACC 嚴重失真，呢個係高頻失分位。

---

**Question 2 — Correct answer: B**

**Model answer:** The cost of debt entering the WACC is the **current yield to maturity (YTM) of 5.5% pre-tax**, not the 7% historical coupon rate. The current cost of long-term debt is the appropriate cost for WACC because WACC is the opportunity cost of capital for the firm's investors as of today; financial statements merely reflect the cost of debt issued in the past. Interest is tax deductible, so the after-tax cost of debt = 5.5% × (1 − 0.25) = **4.125%**. Only the debt component receives the (1 − t) adjustment; preference dividends and common dividends are paid out of after-tax dollars, so kps = 9% and kcs = 13% enter the formula unadjusted.

【解題思路】呢題一次過考兩個最易混淆概念：(1) 歷史票面利率 vs 現時 YTM；(2) 邊啲資金來源要稅項調整。第一步：見到 coupon 7% 同 YTM 5.5% 同時出現，永遠揀 **YTM**，因為票面利率係五年前發行時鎖死嘅舊成本，而 WACC 要嘅係今日嘅機會成本——所以 A 錯。第二步：利息可扣稅，產生稅盾，債務成本要乘 (1 − t)，即 5.5% × 0.75 = 4.125%——C 話「稅項提高債務成本」方向完全調轉，錯。第三步：優先股同普通股股息都係用稅後利潤派，**唔可以**扣稅，所以 D 將 kps 都乘 (1 − t) 係經典錯誤。「考官報告指出」考生最常犯嘅就係「所有成本一率乘 (1−t)」或者「漏乘稅盾」兩個極端，記住：**只有 debt 一格有 (1 − t)**。

---

**Question 3 — Correct answer: B**

**Model answer:** A company's WACC may be used to evaluate a project's cash flows only when **both** conditions hold: (I) the systematic risk of the project's cash flows matches the systematic risk of the company's portfolio of projects, and (II) the project's financing mix matches the debt/equity proportions of the company as a whole. Project Alpha satisfies both conditions, so the 12% firm-wide WACC is appropriate. Project Beta has substantially higher systematic risk; discounting it at 12% (too low a rate) could make a negative-NPV project appear positive. Its WACC should be **risk-adjusted**, e.g. by identifying listed companies with similar risk profiles and using their WACC as a benchmark.

【解題思路】呢題考 Section 7.5 風險調整 WACC 嘅兩個必要條件，係教科書 Knowledge Check Q14 嘅變奏。選項 A 話 WACC「永遠啱用」——明顯違反兩條件原則，錯。選項 C 話高風險項目反而要用平均折現率——邏輯相反：風險愈高，要求回報（折現率）應該愈高，用 12% 折現高風險項目會低估風險、誤納負 NPV 項目，錯。選項 D 係精心設計嘅干擾項：「conventional cash flows」聽落好專業，但教科書明確指出現金流是否常規**唔係**使用 WACC 嘅條件（Knowledge Check Q14 答案 C 只有 I 同 II 成立），錯。記住口訣：**Same risk + Same financing mix → 先用得公司 WACC**。

---

**Question 4 — Correct answer: 11.38% (11.375% before rounding)**

**Model answer / Working:**

Step 1 — Weights at market value:
- Total capital = HK$90m + HK$210m = HK$300m
- xDebt = 90 / 300 = 0.30
- xEquity = 210 / 300 = 0.70

Step 2 — After-tax cost of debt:
- kDebt after tax = 7.5% × (1 − 0.30) = 5.25%

Step 3 — WACC:
- WACC = xDebt × kDebt pretax × (1 − t) + xEquity × kEquity
- WACC = (0.30 × 7.5% × 0.70) + (0.70 × 14%)
- WACC = 1.575% + 9.800% = 11.375% ≈ **11.38%**

【解題思路】典型兩層資本結構 WACC 計算題，照公式三步走。第一步用**市值**計權重（題目已說明係 market values，直接 90/300 同 210/300，兩個權重加埋要等於 1，可以 self-check）。第二步處理稅盾：YTM 7.5% 係**稅前**成本，必須乘 (1 − 0.30) 得 5.25%；最常見錯誤係直接將 7.5% 擺入公式（會得出 12.05%），或者調轉乘 (1 + t)。第三步加權：0.30 × 5.25% = 1.575%，0.70 × 14% = 9.8%，相加得 11.375%，按題目要求 round 到兩個小數位 = 11.38%。考試貼士：OTQ 計算題記得睇清楚要求嘅小數位同埋「percentage vs decimal」格式，寫 0.1138 定 11.38% 要配合題目指示。

---

**Question 5 — Correct answer: 10.42% (10.4235% before rounding)**

**Model answer / Working:**

Step 1 — Market values and weights:
- Debt = HK$100m (given)
- Preference equity = 5,000,000 × HK$15 = HK$75m
- Common equity = 10,000,000 × HK$25 = HK$250m
- Total capital = 100 + 75 + 250 = HK$425m
- xDebt = 100 / 425 = 0.23529; xps = 75 / 425 = 0.17647; xcs = 250 / 425 = 0.58824

Step 2 — Component costs:
- Cost of debt (pre-tax) = 8% (current YTM, given)
- Cost of preference shares: kps = Dps / Pps = HK$1.50 / HK$15.00 = 10.00%
- Cost of common equity (DGM): D1 = D0 × (1 + g) = HK$2.00 × 1.04 = HK$2.08
  kcs = D1 / P0 + g = (HK$2.08 / HK$25.00) + 0.04 = 0.0832 + 0.04 = 0.1232 = 12.32%

Step 3 — WACC:
- WACC = xDebt × kDebt pretax × (1 − t) + xps × kps + xcs × kcs
- WACC = (0.23529 × 8% × 0.75) + (0.17647 × 10.00%) + (0.58824 × 12.32%)
- WACC = 1.4118% + 1.7647% + 7.2471% = 10.4235% ≈ **10.42%**

【解題思路】呢題係三層資本結構嘅完整 WACC（對標教科書 Apply and Analyse 2），難度喺每層成本要用唔同方法計。第一步市值：債務直接俾咗 100m；優先股同普通股要用「股數 × 現價」自己計——唔好以為題目已經俾晒市值。第二步成本：債務用現時 YTM 8%（稅前）；優先股係永續年金 D/P = 1.5/15 = 10%；普通股用 DGM——**最大陷阱**係題目俾嘅 HK$2.00 係「剛剛派咗」嘅 D0，公式要嘅係 D1，必須先乘 (1 + g) 得 2.08；如果直接用 2.00/25 + 4% 會得出 12%，令 WACC 變成約 10.23%，錯。第三步組裝：再次提醒——只有債務乘 (1 − 0.25)，優先股同普通股**唔乘**稅盾。三個權重加埋 = 1（0.23529 + 0.17647 + 0.58824），計完做個 quick check。考試貼士：呢類題喺閉卷 OTQ 下約 2.5 分鐘要完成，建議練熟「weights → costs → assemble」嘅固定套路，先寫低公式再代入數字，避免按錯 calculator。
