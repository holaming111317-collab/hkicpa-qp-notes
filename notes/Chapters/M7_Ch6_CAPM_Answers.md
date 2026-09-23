# M7 Financial Management — Chapter 6: Capital Asset Pricing Model — Model Answers（完成測驗後先好睇！）

---

## Retest R16 — Answer: **6.45%**

BEY = (1,000,000 − 992,000) ÷ 992,000 × 360 ÷ 45 = 0.008065 × 8 = **6.45%**。
【解題思路】三寶：分子折扣額 (F−P) = 8,000；分母發行價 992,000（唔係面值）；最後 ×360÷45 年化。

---

**Question 1 — Answer: B**

**Model Answer:**
Systematic risk (market risk / non-diversifiable risk) is the risk of being in the market rather than in any specific investment. It is caused by exogenous factors such as changes in gross domestic product (GDP), interest rates and inflation, which affect a large number of assets. An unexpected increase in market interest rates is therefore systematic risk. Strikes, parts shortages, accidents and takeovers affect only one or a small number of assets — they are classic examples of unsystematic (unique / asset-specific / diversifiable) risk.

【解題思路】
- 第一步：回想定義 — systematic risk 係市場層面嘅風險（利率、通脹、GDP），影響大量資產；unsystematic risk 只影響個別或少數公司。
- 第二步：逐個選項分類。B 嘅利率變動影響成個市場，係 systematic risk，所以係正解。
- 錯誤選項分析：
  - A（airline strike）：source 明確將 strikes 列為 unsystematic risk 嘅例子。
  - C（parts shortage）：source 同樣將 parts shortage 列為 unsystematic risk。
  - D（takeover）：source 將 takeovers 列為 unsystematic risk。
- 考試貼士：呢類「概念分類」題係 OTQ 常客，背熟 source 入面四個 unsystematic risk 例子（strikes, parts shortage, accidents, takeovers）就可以秒殺。

---

**Question 2 — Answer: C**

**Model Answer:**
Statement C is NOT correct. The slope of the security market line is the market risk premium [E(R_m) − R_rf], not beta. Beta is the horizontal-axis variable of the SML (systematic risk), whereas the slope represents the compensation per unit of systematic risk. Statements A, B and D are all correct: beta measures market/systematic risk, measures the risk of an individual stock or portfolio relative to the market portfolio, and changes over time as the risk of the underlying security or portfolio changes.

【解題思路】
- 第一步：認清 SML 嘅結構 — kᵢ = R_rf + [E(R_m) − R_rf]·βᵢ。橫軸係 beta，斜率係 market risk premium。
- 第二步：題目問邊句「NOT correct」，要特別小心呢種反向提問。
- 錯誤選項分析：
  - A：正確描述 — beta 量度 market risk（systematic risk）。
  - B：正確描述 — beta 係相對於市場組合嘅風險量度。
  - D：正確描述 — beta 會隨相關證券或組合嘅風險改變而改變。
- C 係混淆概念陷阱：beta 係 SML 嘅橫軸變數（x 軸），唔係斜率。呢個正係考官愛考嘅 SML 概念陷阱。

---

**Question 3 — Answer: B**

**Model Answer:**
Required return from CAPM / SML:
k_X = R_rf + β_X[E(R_m) − R_rf] = 2% + 1.5 × (10% − 2%) = 2% + 1.5 × 8% = 2% + 12% = 14%.
The actual expected return (16%) exceeds the required return (14%). Securities with expected returns that exceed their required returns lie above the SML and are considered undervalued. Rational investors would bid up the share price until the expected return falls back to the 14% level predicted by the SML at equilibrium.

【解題思路】
- 第一步：用 CAPM 計必要回報 = 2% + 1.5 × (10% − 2%) = 14%。
- 第二步：比較實際預期回報（16%）同必要回報（14%）。16% > 14%，即股票喺圖上落喺 SML 上方。
- 第三步：記住口訣 —「上 = 低估（undervalued），下 = 高估（overvalued）」。SML 上方代表畀緊你多過應得嘅回報，即價格太平，值得買。
- 錯誤選項分析：
  - A：16% ≠ 14%，唔係 correctly priced。
  - C：位置啱（above SML）但結論反轉咗 — above SML 係 undervalued，唔係 overvalued。
  - D：位置錯（應係 above），結論亦配錯。
- 考試貼士：呢類題目兩步搞掂 — 先 CAPM，後比較。方向記唔住時諗返「回報高 → 抵買 → 低估」。

---

**Question 4 — Answer: 12.5%**

**Model Answer / Working:**
E(R_G) = R_rf + β_G × (market risk premium)
E(R_G) = 2% + 1.5 × 7%
E(R_G) = 2% + 10.5%
E(R_G) = **12.5%**

【解題思路】
- 第一步：認清題目畀嘅係「market risk premium」（7%），即 [E(R_m) − R_rf] 已經計好，**唔使再減無風險利率**。
- 第二步：直接代入：2% + 1.5 × 7% = 12.5%。
- 常見錯誤：
  - 再減一次無風險利率：2% + 1.5 × (7% − 2%) = 9.5%（錯 — 雙重扣減）。
  - 將 7% 當成市場回報：2% + 1.5 × 7% 咁啱數字一樣，但如果改用市場回報 E(R_m) = 7% 解讀，式子應為 2% + 1.5 × (7% − 2%) = 9.5%。呢度題目字眼係 "market risk premium"，所以 12.5% 先啱。
  - 忘記加返無風險利率：1.5 × 7% = 10.5%（錯 — 漏咗 R_rf）。
- 考試貼士：見到 "market risk premium" 就唔使再減 R_rf；見到 "expected return on the market" 就一定要減。呢個係 CAPM OTQ 最常見嘅陷阱。

---

**Question 5 — Answer: 11.32%**

**Model Answer / Working:**
Step 1 — Portfolio beta:
β_p = Σ xᵢβᵢ = (0.60 × 1.2) + (0.40 × 0.8) = 0.72 + 0.32 = 1.04
Step 2 — Market risk premium:
E(R_m) − R_rf = 11% − 3% = 8%
Step 3 — CAPM for the portfolio:
E(R_p) = R_rf + β_p[E(R_m) − R_rf] = 3% + 1.04 × 8% = 3% + 8.32% = **11.32%**

【解題思路】
- 第一步：組合 beta 係個別 beta 嘅金額加權平均：0.6×1.2 + 0.4×0.8 = 1.04。
- 第二步：市場風險溢價 = 11% − 3% = 8%。
- 第三步：代入 CAPM：3% + 1.04 × 8% = 11.32%。
- 常見錯誤：
  - 用簡單平均 beta：(1.2 + 0.8)/2 = 1.0，得出 3% + 1.0 × 8% = 11%（錯 — 權重唔係 50/50）。
  - 唔減無風險利率：3% + 1.04 × 11% = 14.44%（錯 — 混淆咗市場回報同市場風險溢價）。
  - 倒轉權重：0.4×1.2 + 0.6×0.8 = 0.96 → 3% + 0.96×8% = 10.68%（錯 — 對錯股票配權重）。
- 考試貼士：組合 CAPM 題目永遠行同一路線：先計 β_p（加權），再一條 CAPM 式。唔好分開幫每隻股票計 CAPM 再加權（雖然數學上答案一樣，但容易出錯兼慢）。
