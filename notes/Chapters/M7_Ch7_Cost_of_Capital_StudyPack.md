# M7 Cost of Capital — Study Pack (Week 7)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構

- **資本成本的組成**：公司的資本結構（Capital Structure）由長期資金來源組成，主要包括長期債務（Long-term Debt）、優先股（Preference Shares）及普通股（Common Stock），每項資金來源都有其成本（Cost of Funds）。
- **普通股權益成本（Cost of Equity — Common Stock）**：兩大估算模型 — 股息增長模型（Dividend Growth Model, DGM）及資本資產定價模型（Capital Asset Pricing Model, CAPM）；兩模型假設不同，結果往往不一致，實務上可取兩者平均值（average the two estimates）。
- **優先股成本（Cost of Preference Shares）**：屬混合證券（Hybrid Securities），介乎債券與普通股之間；無固定到期日者視為永續年金（Perpetuity），以股息除以現價計算；附償債基金條款（Sinking Fund Clause）強制贖回者則當作有固定到期日的債券處理。
- **債務成本（Cost of Debt）**：WACC 應採用「現時」長期債務成本（Current Cost of Long-term Debt），即現時的到期收益率（Yield to Maturity, YTM），而非歷史票面利率（Coupon Rate）；利息可扣稅（Tax Deductible），故 WACC 用的是稅後債務成本（After-tax Cost of Debt）。
- **加權平均資本成本及其局限（WACC & Risk-adjusted WACC）**：WACC 是按各資金來源佔比加權的平均成本，代表投資者今日的資金機會成本（Opportunity Cost of Capital）；只有當項目的系統性風險（Systematic Risk）及融資組合（Financing Mix）與公司整體一致時，才可用公司的 WACC 折現項目現金流，否則要用風險調整後的 WACC（例如參考可比較上市公司 Comparable Companies 的 WACC）。

### 2. 必背考點清單（公式與規則）

**(a) Dividend Growth Model (DGM) — 普通股權益成本**

```
kcs = D1 / P0 + g
```
- `kcs` = Required return on common stock
- `D1` = Dividend paid in the next period (t = 1)；注意：如題目給 D0，必須先乘以 (1 + g) 推算 D1
- `P0` = Current price per share
- `g` = Expected growth rate of dividends
- 應用條件：只適用於**有派息且股息以穩定速率永遠增長**的公司（如公用事業 Electric Utility）；不適用於不派息的高增長科技公司（可用 Multistage-growth Dividend Model，以試誤法 Trial-and-error 求解）；貼現率必須大於增長率（k > g）；g 每增加 1%，cost of equity 約上升 1%，對 g 非常敏感。

**(b) Capital Asset Pricing Model (CAPM)**

```
E(Ri) = Rrf + βi × [E(Rm) − Rrf]
```
- `Rrf` = Risk-free rate of return — 必須用**現時**有效無風險資產年收益率（Current Effective Annual Yield）；因股權屬長期申索（Perpetual Claim），宜用**長期**國庫券收益率（Long-term Treasury Rate）
- `βi` = Beta coefficient — 量度個股相對大市的系統性風險/波幅（Systematic Risk）；市場組合 beta = 1；無風險資產 beta = 0；非上市公司可用同業 Comparable Company 的 beta 或行業平均 beta
- `[E(Rm) − Rrf]` = Market Risk Premium — 無法直接觀察，一般以歷史平均風險溢價估算（如美國自 1926 年起股票回報高於政府債券逾 5.5%，可用 5.71% 作估計）
- CAPM 假設：資本市場處於均衡（Equilibrium）、無交易成本（No Transaction Costs）、所有投資者可以無風險利率借貸、所有投資者預期一致（Identical Expectations）。
- 例：beta = 1.5、E(Rm) = 10%、Rrf = 4% → E(Ri) = 0.04 + 1.5 × (0.10 − 0.04) = **13%**

**(c) Cost of Preference Shares（永續年金法）**

```
kps = Dps / Pps
```
- `Dps` = Preference dividend（注意股息頻率：如季度股息，算出的是季率，需 ×4 年化为年度貼現率）
- `Pps` = Current price of preference shares
- 新發行優先股含發行成本 F（Flotation Cost）：`kps = D / [Pps × (1 − F)]`
- 優先股股息以稅後利潤支付（Paid out of After-tax Dollars），故 **kps 不作稅項調整**；CAPM 亦可用於估算優先股成本。

**(d) Cost of Debt（稅後債務成本）**

```
kDebt after tax = kDebt pretax × (1 − t)
```
- `kDebt pretax` = 現時債務成本：上市債券用**現時 YTM**（需按複息頻率調整，例如半年付息債券 YTM = 2 × 半年利率；並考慮有效年利率 EAR 及發行成本 Issuance Costs，以 Net Proceeds 計算）；私人/銀行債務可詢問銀行現時再融資利率（Refinancing Rate）
- `t` = Marginal tax rate（邊際稅率）
- 多筆債務：先計各筆成本，再按金額加權求平均 pre-tax cost，最後才乘 (1 − t)
- 關鍵概念：財務報表顯示的是**歷史**債務成本（如五年前發行的 7% 債券），WACC 必須用**現時**成本（如今日同類債券只售 6%），因 WACC 是投資者**今日**的機會成本；信用額度（Lines of Credit）屬臨時性質，不計入債務成本。

**(e) Weighted Average Cost of Capital (WACC)**

```
kFirm = Σ xi × ki = xDebt × kDebt pretax × (1 − t) + xps × kps + xcs × kcs
```
- `xi` = 各資金來源佔總資本的權重（Weight），應以**市值（Market Value）**計算（如例：Debt HK$300m、Preferred HK$24m、Common HK$280m → 權重 0.4967 / 0.0397 / 0.4636）
- `ki` = 各資金來源的成本；**只有債務成本需要稅項調整**，優先股及普通股成本均為稅後概念，不可再乘 (1 − t)
- 應用條件：WACC 是邊際資金成本（Marginal Cost of Funds）的最可靠指標，但前提是公司繼續投資於**標準業務風險**的項目，並按**現有資本結構比例**集資。
- 用公司 WACC 評估項目的**兩個必要條件**：(I) 項目的系統性風險與公司整體項目組合一致；(II) 項目的融資組合（Debt/Equity mix）與公司整體一致。現金流是否常規（Conventional Cash Flows）**不是**條件。
- 局限：若用單一 WACC 折現不同風險的項目 — 折現率太低會誤納負 NPV 項目（Accept Negative-NPV Projects）；太高會誤拒正 NPV 項目（Reject Positive-NPV Projects）；長遠令公司偏向高風險項目、損害股東價值。解決方法：以風險調整 WACC（Risk-adjusted WACC），參考風險特徵相近的上市公司作基準（Benchmark）。

### 3. 易混淆概念對比 (Common Pitfalls)

**Pitfall 1：Coupon Rate / Historical Cost of Debt vs Current YTM（歷史票面利率 vs 現時到期收益率）**
- 對比：債券的**票面利率（Coupon Rate）**是發行時鎖定的歷史成本，反映在財務報表上；**現時 YTM** 才是市場今日要求該債券的回報率，代表公司現時舉債的真正成本。
- 例子：ABC Entertainment Ltd 五年前以 7% 發債，其後利率下跌，同類債券今日可按面值以 6% 發行。計算 WACC 時必須用 **6%（現時成本）**，而非報表上的 7%。財務報表反映的是「過去賣出的債務成本」，WACC 要的是「今日的機會成本」。
- 考試貼士：OTQ 題目同時給 coupon rate 和債券現價/年期時，成本要用 YTM 反推；若題目直接給「current yield to maturity」或「若今日再融資的利率」，直接使用即可，切勿用票面利率。

**Pitfall 2：Pre-tax vs After-tax Cost of Debt in WACC（稅前 vs 稅後債務成本）**
- 對比：利息開支可扣稅（Interest is Tax Deductible），產生稅盾（Tax Shield），所以 WACC 公式中債務成本必須乘 (1 − t)；但**普通股股息及優先股股息均不可扣稅**（以稅後利潤支付），kcs 和 kps 在 WACC 中**不可**作稅項調整。
- 例子：債務 pre-tax cost 7.40%、t = 25% → after-tax cost = 7.40% × (1 − 0.25) = **5.55%**。若錯誤地把優先股成本 10% 也乘 (1 − t)，WACC 會被低估，可能導致誤納項目。
- 考試貼士：見到 WACC 題目，先問「邊啲成本要乘 (1−t)？」答案永遠只有 debt 一項。「考官報告指出」考生常見錯誤是漏乘稅盾、或錯誤對所有資金來源一併乘 (1 − t)。

---

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): State the Dividend Growth Model (DGM) formula for the cost of common equity, and list two situations in which it is NOT appropriate.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - kcs = D1 / P0 + g
      - D1 = next period's dividend; P0 = current share price; g = constant dividend growth rate
      - Not appropriate when: (1) the company does not pay dividends (e.g. fast-growing high-tech firms); (2) dividends do not grow at a constant rate (use a multistage-growth model instead)
      - Also requires the discount rate to exceed the growth rate (k > g)
    - [中文白話解釋]: DGM 將股價視為永遠增長的股息折現值，調返轉頭就得出權益成本 = 下期股息率 + 增長率。但前提係公司有穩定派息兼增長率恒定；唔派息或者增長忽快忽慢嘅公司就用唔到，要改用多階段增長模型（multistage-growth model）以試誤法求解。

* [Flashcard 2]
  - Front (Question in English): A share has a beta of 1.6. The risk-free rate is 4% and the market risk premium is 6%. Calculate the expected return using CAPM, and state the three inputs CAPM requires.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - E(Ri) = Rrf + βi × [E(Rm) − Rrf] = 0.04 + 1.6 × 0.06 = 0.136, or 13.6%
      - Three required inputs: (1) risk-free rate; (2) beta; (3) market risk premium (or expected market return)
      - Market risk premium = E(Rm) − Rrf; it cannot be observed directly and is usually estimated from historical average premiums
    - [中文白話解釋]: CAPM 話畀你聽：要求回報 = 無風險利率 + beta × 市場風險溢價。留意題目俾嘅 6% 已經係「溢價」（即 E(Rm) − Rrf），唔使再減無風險利率；如果題目俾嘅係「市場預期回報 10%」，就要先減 4% 得出溢價先好乘 beta。呢個係最常見嘅陷阱位。

* [Flashcard 3]
  - Front (Question in English): A preference share pays an annual dividend of HK$3.50 and is currently priced at HK$38.89. Compute the cost of preference shares. If new preference shares are issued with an 8% flotation cost, how is the cost adjusted?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - kps = Dps / Pps = HK$3.50 / HK$38.89 = 0.09, or 9%
      - With flotation cost F: kps = D / [Pps × (1 − F)] — the company only receives net proceeds
      - Preference dividends are paid out of after-tax dollars → NO tax adjustment is applied to kps in WACC
      - Preference shares without fixed maturity are valued as perpetuities; those with a sinking fund clause (mandatory retirement) may be treated as bonds with fixed maturity
    - [中文白話解釋]: 優先股當係永續年金睇：成本 = 股息 ÷ 現價。如果新發行有發行成本（例如投行抽 8%），公司實收淨額少咗，分母變成 P × (1 − F)，成本自然推高。記住優先股股息唔可以扣稅，所以入 WACC 時千祈唔好乘 (1 − t)。

* [Flashcard 4]
  - Front (Question in English): A company's bonds were issued five years ago at a 7% coupon. Identical bonds could be issued at par today at 6%. The marginal tax rate is 25%. What cost of debt should be used in WACC, and why?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Use 6% (the current cost of debt), NOT the 7% historical coupon rate
      - After-tax cost of debt = kDebt pretax × (1 − t) = 6% × (1 − 0.25) = 4.5%
      - Rationale: WACC is the opportunity cost of capital for the firm's investors AS OF TODAY; financial statements only reflect the cost of debt issued in the past
      - For publicly traded bonds, the current cost of debt = current yield to maturity (YTM), adjusted for compounding frequency and issuance costs (net proceeds)
    - [中文白話解釋]: 呢題考「現時成本 vs 歷史成本」：報表上嘅 7% 係五年前發債鎖定嘅舊成本，但 WACC 代表投資者今日嘅機會成本，所以要用今日市價反映嘅 6%，再乘 (1 − 25%) 得出稅後成本 4.5%。見到 coupon rate 同 YTM 同時出現，永遠揀 YTM。

* [Flashcard 5]
  - Front (Question in English): A firm has HK$10m secured debt at 6%, HK$7m senior unsecured debt at 7% and HK$8m subordinated unsecured debt at 9.5%. The marginal tax rate is 25%. Calculate the overall after-tax cost of debt.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Weights: 10/25 = 0.40; 7/25 = 0.28; 8/25 = 0.32
      - Weighted pre-tax cost = (0.40 × 6%) + (0.28 × 7%) + (0.32 × 9.5%) = 2.40% + 1.96% + 3.04% = 7.40%
      - After-tax cost = 7.40% × (1 − 0.25) = 5.55%
      - Method: (1) compute weights per debt issue; (2) weighted average pre-tax cost; (3) apply tax adjustment ONCE at the end
    - [中文白話解釋]: 多筆債務要三步走：先計每筆佔總債務嘅比重，再加權平均出稅前成本 7.40%，最後先至一次過乘 (1 − 稅率) 得 5.55%。次序好重要 — 係「先加權、後調稅」，唔好逐筆各自乘 (1 − t) 先再加權（雖然數學上結果一樣，但考試寫步驟要跟返教材次序）。

* [Flashcard 6]
  - Front (Question in English): A firm has debt (market value HK$300m, pre-tax YTM 4.84%), preferred shares (HK$24m, kps = 10%) and common shares (HK$280m, kcs = 16%). Marginal tax rate = 40%. Calculate the WACC.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Total capital = 300 + 24 + 280 = HK$604m
      - Weights: xDebt = 0.4967; xps = 0.0397; xcs = 0.4636
      - WACC = (0.4967 × 4.84% × (1 − 0.40)) + (0.0397 × 10%) + (0.4636 × 16%)
      - = 1.442% + 0.397% + 7.418% = 0.0926, or 9.26%
      - Only the debt component receives the (1 − t) adjustment; weights are based on MARKET values
    - [中文白話解釋]: 呢個係教材 Apply and Analyse 2 嘅完整 WACC 計算，考試必考位。三個步驟：(1) 用市值計權重；(2) 逐項計成本（債務用 YTM、優先股用 D/P、普通股用 DGM 或 CAPM）；(3) 加權求和，記住只有債務嗰格乘 (1 − t)。權重加埋必須等於 1，計完可以快速 self-check。

* [Flashcard 7]
  - Front (Question in English): Under what TWO conditions is it appropriate to use a firm's overall WACC to discount a project's cash flows? What are the consequences of using a single WACC for projects of different risk?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Condition 1: the project's systematic risk matches the systematic risk of the company's portfolio of projects
      - Condition 2: the project's financing mix (debt/equity proportions) matches that of the company as a whole
      - Consequences of misusing a single WACC: a rate too low → accept negative-NPV projects; a rate too high → reject positive-NPV projects; bias towards riskier projects, raising average firm risk and destroying shareholder value
      - Solution: use a risk-adjusted WACC, benchmarked against listed companies with similar risk profiles
    - [中文白話解釋]: 用公司 WACC 折現項目現金流要同時滿足兩個條件：風險一致 + 融資比例一致。留意「常規現金流（conventional cash flows）」唔係條件之一，呢個係 MCQ 常見干擾項。用錯折現率嘅後果係雙向嘅 — 太低會誤納蝕本項目，太高會誤拒賺錢項目，仲會令公司愈嚟愈偏向高風險投資。

* [Flashcard 8]
  - Front (Question in English): Compare the DGM and CAPM approaches to estimating the cost of equity — one advantage and one disadvantage of each — and state the practical recommendation when the two models give different answers.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - DGM: advantage — simple and easy to implement; disadvantages — only works for dividend-paying firms with constant growth; highly sensitive to g (1% higher g ≈ 1% higher kcs); ignores risk factors
      - CAPM: advantages — explicitly adjusts for systematic risk; applicable to any company whose beta can be estimated; disadvantages — market risk premium and beta both change over time and are estimated from historical data (past may not predict the future)
      - Practical recommendation: compute the cost of equity using BOTH methods and average the results (e.g. CAPM 15.52% and DGM 18.50% → average 17.01%)
    - [中文白話解釋]: 兩個模型底層假設唔同：DGM 似增長型永續年金，要求股息穩定增長；CAPM 假設回報常態分佈、無稅無交易成本。所以同一間公司計出嚟嘅答案經常唔同，實務上嘅做法係兩個都計，然後取平均值，減低單一模型假設失準嘅風險。

Phase 3 測驗題目及答案請見另外兩個檔案：*_Quiz.md / *_Answers.md
