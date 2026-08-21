# M7 Financial Management — Chapter 6: Capital Asset Pricing Model — Study Pack (Week 6)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構

- **風險與回報的取捨 (Risk–Return Trade-off)**：風險越高，投資者要求的回報越高。回報有三種量度方法：持有期回報 (Holding Period Return)、平均回報 (Average Return：Arithmetic Mean / Geometric Mean) 及預期回報 (Expected Return)；風險則以變異數 (Variance) 及標準差 (Standard Deviation) 量度。
- **分散投資與投資組合 (Diversification and Portfolio)**：將資金分散於回報「非完全正相關 (less than perfectly positively correlated)」的資產可降低組合風險，但只能消除非系統性風險 (Unsystematic Risk)，不能消除系統性風險 (Systematic Risk)；約 40–50 隻證券已可取得大部分分散效益，過度分散 (over-diversification) 反而適得其反。
- **系統性風險與 Beta**：市場只獎勵系統性風險 (Systematic Risk Principle)。Beta (β) 量度資產回報對市場回報的敏感度：β = COV(i,M) / σ²M；β = 1 與市場相同、β > 1 高於市場、β < 1 低於市場、β = 0 無系統性風險。
- **資本資產定價模型 (CAPM)**：E(Ri) = Rrf + βi[E(Rm) − Rrf]，用以計算個別證券或組合的必要/預期回報率，是估算股本成本 (cost of equity) 的核心工具。
- **證券市場線 (Security Market Line, SML)**：圖像化 CAPM，顯示不同 beta 下的必要回報。位於 SML 上方 = 被低估 (undervalued)；位於 SML 下方 = 被高估 (overvalued)；在線上 = 定價正確 (equilibrium)。

### 2. 必背考點清單（公式、變數定義及適用條件）

**(A) 回報量度 (Measures of Return)**

| 公式 | 內容 | 備註 |
|---|---|---|
| Capital appreciation | R_CA = ΔP / P₀ = (P₁ − P₀) / P₀ | P₁ = price at period 1；P₀ = price at period 0 |
| Income return | R_I = CF₁ / P₀ | CF₁ = cash flow at period 1 (e.g. dividend) |
| Total holding period return | R_T = R_CA + R_I = (ΔP + CF₁) / P₀ | 包含 capital gain 及 income 兩部分 |
| Arithmetic mean | AM = ΣRᵢ / n | 適用於約 12 個月的投資期；**永遠高估 (overstates)** 回報 |
| Geometric mean | GM = [(1+R₁)(1+R₂)…(1+Rₙ)]^(1/n) − 1 | 複利增長率，適用多期及較長投資期，結果較準確；波幅越大 AM 與 GM 差距越大 |
| Expected return | E(R_Asset) = Σ pᵢRᵢ | 各情境回報以概率加權 |
| Total return 分解 | R = E(R) + m + ε | m = systematic portion；ε = unsystematic portion |

**(B) 風險量度 (Measures of Risk)**

| 公式 | 內容 | 備註 |
|---|---|---|
| Variance | σ² = Σ pᵢ[Rᵢ − E(R)]² | 概率加權的平方偏差 |
| Standard deviation | σ = √σ² | 常態分佈下：±1σ 涵蓋 68%、±2σ 涵蓋 95%、±3σ 涵蓋 99.7% |
| Coefficient of variation | CV = σ_Asset / E(R_Asset) | 每單位回報的風險；**CV 越低越好**（風險最小化角度） |
| Modified CV | CV* = σ_Asset / [E(R_Asset) − R_rf] | 以超額回報 (excess return over risk-free) 計算 |
| VaR vs Expected Shortfall | VaR: 「99% 機會 10 日內損失不超過 HK$V」；ES = E(L \| L ≥ VaR) | ES 考慮超過 VaR 時的實際損失，永遠認可分散效益；2007–08 金融海嘯後 ES 更常用 |

**(C) 投資組合 (Portfolio)**

| 公式 | 內容 | 備註 |
|---|---|---|
| Portfolio expected return | E(Rp) = Σ wᵢ·E(Rᵢ) | wᵢ = 投資於資產 i 的比重；**回報永遠是加權平均** |
| Two-asset portfolio variance | σ²p = w_A²σ_A² + w_B²σ_B² + 2w_A·w_B·COV(A,B) | 組合風險 ≠ 個別風險的加權平均（除非 ρ = +1） |
| Covariance | COV_AB = Σ pᵢ[R_Ai − E(R_A)][R_Bi − E(R_B)] | 量度兩資產回報的共同變動 |
| Correlation coefficient | ρ_AB = COV_AB / (σ_A·σ_B) | 介乎 −1 至 +1；ρ = +1 完全正相關（無分散效益）；ρ = −1 完全負相關（可消除全部風險）；ρ = 0 不相關；一般股票組合 ρ ≈ 0.65 |
| Beta | βᵢ = ρ_Mi·σᵢ/σ_M = COV(i,M) / σ²_M | 量度系統性風險 |
| Portfolio beta | βp = Σ xᵢ·βᵢ | 組合 beta 是個別 beta 的加權平均 |

**(D) CAPM 與 SML**

| 公式 | 內容 | 備註 |
|---|---|---|
| CAPM | E(Rᵢ) = R_rf + βᵢ[E(R_m) − R_rf] | [E(R_m) − R_rf] = market risk premium |
| Portfolio under CAPM | E(R_Portfolio) = R_rf + β_Portfolio[E(R_m) − R_rf] | β_Portfolio = Σ xᵢβᵢ |
| SML | kᵢ = R_rf + [E(R_m) − R_rf]·βᵢ | SML 的**斜率 (slope) 是 market risk premium**，不是 beta |
| CAL / CML | E(rp) = w_r·E(r_r) + (1 − w_r)·E(r_f)；σp = w_r·σ_r | 風險資產與無風險資產的組合線；切點為 tangency portfolio |

**CAPM 假設 (Assumptions) — 必考**：
- 所有投資者可平等接觸所有投資，並使用單一時期 (one-period) 時間範圍
- 以 benchmark 的 variance 作為資產風險的唯一量度
- 無交易成本、佣金及稅項 (no transaction costs / taxes)
- 所有人均可按無風險利率借貸 (borrow/lend at the risk-free rate)
- 所有資產類別均有市場及 benchmark
- 使用歷史數據推算未來預期回報（可能不相關 — 此為限制）

**其他必記事實**：
- 香港無風險利率代理：香港金融管理局發行的外匯基金票據及債券 (Hong Kong Exchange Fund Bills and Notes)；美國則用 US Treasury securities。
- 國際分散投資 (international diversification) 理論上比單一本地市場更能減風險，但隨全球市場一體化，效益正在下降。
- 歷史數據顯示：風險（標準差）越高的證券類別（如 small stocks），平均回報越高；Treasury bills 標準差最小、回報最低。
- 考試貼士：SML 上 β = 0 時 E(R) = R_rf；β = 1 時 E(R) = E(R_m)。用這兩點可快速驗算 CAPM 答案。

### 3. 易混淆概念對比 (Common Pitfalls)

**Pitfall 1：Systematic Risk vs Unsystematic Risk**
- Systematic risk（又稱 market risk / non-diversifiable risk）：影響整個市場的外生因素，如 GDP 變化、利率、通脹 — **不能**透過分散投資消除，市場會給予風險溢價作補償。
- Unsystematic risk（又稱 unique risk / asset-specific risk / diversifiable risk）：只影響個別或少數資產，如罷工 (strikes)、零件短缺 (parts shortage)、工業意外 (accidents)、收購 (takeovers) — **可以**透過分散投資消除，市場**不會**獎勵，其預期回報為零。
- 例子：2007–08 全球金融海嘯是典型的 systematic risk — 即使持有分散組合的投資者亦無法倖免；相反，某公司管理層醜聞屬 unsystematic risk，持有 40–50 隻股票的投資者幾乎不受影響。謹記「考官報告指出」類題目常設陷阱：CAPM 補償的是 systematic risk，不是 unique risk。

**Pitfall 2：Security Market Line (SML) vs Capital Market Line / Capital Allocation Line (CML/CAL)**
- SML：橫軸是 **beta（系統性風險）**，縱軸是 required return，公式 kᵢ = R_rf + [E(R_m) − R_rf]·βᵢ；適用於**任何**個別證券或組合（不論是否有效）；用來判斷證券被高估（SML 下方）或低估（SML 上方）。
- CAL/CML：橫軸是 **standard deviation（總風險）**，縱軸是 expected return，代表無風險資產與風險資產（market/tangency portfolio）的組合；只適用於**有效組合 (efficient portfolios)**。
- 例子：一隻 β = 1.5、σ = 40% 的股票，其 σ 含大量 unsystematic risk，在 CAL/CML 圖上會落在線的右下方（非有效），但在 SML 上只要定價正確仍會剛好落在線上。記住：SML 的斜率是 market risk premium，而**不是** beta（考試 MCQ 常見陷阱選項）。

---

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): What are the three main methods to calculate the return of an investment, and why does the arithmetic mean always overstate returns?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Three methods: (1) holding period returns, (2) average returns (arithmetic mean and geometric mean), (3) expected returns.
      - AM = ΣRᵢ/n, suitable for investment horizons of about 12 months.
      - GM = [(1+R₁)…(1+Rₙ)]^(1/n) − 1, used for compound growth over multiple periods.
      - AM simply averages returns and ignores compounding: after a loss, less capital is available to generate future returns, so AM always overstates the true return; the gap widens with higher volatility.
    - [中文白話解釋]：回報有三種計法：持有期回報（capital gain + income）、平均回報（算術平均及幾何平均）、預期回報。算術平均只係簡單將各期回報加埋再除以期數，冇考慮複利效應 — 蝕錢之後本金縮水，之後賺嘅能力都減弱，所以算術平均永遠高估真實回報，波幅越大誤差越大。

* [Flashcard 2]
  - Front (Question in English): Mr. Leung's investment in China Mobile stock has the following possible returns: Weak economy 13% (p = 0.30), OK economy 20% (p = 0.40), Strong economy 25% (p = 0.30). Calculate the expected return.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - E(R) = Σ pᵢRᵢ = (0.30 × 0.13) + (0.40 × 0.20) + (0.30 × 0.25)
      - = 0.039 + 0.080 + 0.075 = 0.194
      - Expected return = **19.4%**
    - [中文白話解釋]：預期回報就係將每個情境嘅回報乘以佢發生嘅概率再加埋。呢題三個情境：0.3×13% + 0.4×20% + 0.3×25% = 19.4%。考試見到 probability × return 嘅表格題，直接照呢條式計就得。

* [Flashcard 3]
  - Front (Question in English): Distinguish between systematic risk and unsystematic risk. Which one is rewarded by the market, and why?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Systematic risk (market risk / non-diversifiable risk): affects a large number of assets; caused by exogenous factors such as changes in GDP, interest rates and inflation; cannot be eliminated by diversification.
      - Unsystematic risk (unique / asset-specific / diversifiable risk): affects one or a small number of assets, e.g. strikes, parts shortages, accidents, takeovers; can be eliminated through effective diversification.
      - Systematic risk principle: there is reward for bearing risk, but no reward for bearing risk unnecessarily. Asset markets only reward systematic risk; the expected return on unsystematic risk is zero.
    - [中文白話解釋]：系統性風險影響成個市場（例如利率、通脹、GDP），點分散都避唔到，所以市場會用風險溢價補償你；非系統性風險只影響個別公司（例如罷工、收購），分散投資就可以消除，市場唔會因此畀多啲回報你。呢個就係點解 CAPM 淨係用 beta（系統性風險）嚟定回報。

* [Flashcard 4]
  - Front (Question in English): A portfolio has HK$800 invested in Stock O (expected return 10%) and HK$1,200 in Stock K (expected return 18%). Calculate the expected return of the portfolio.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Weight of O = 800 / (800 + 1,200) = 40%; weight of K = 60%
      - E(Rp) = Σ wᵢE(Rᵢ) = (40% × 10%) + (60% × 18%)
      - = 4% + 10.8% = **14.80%**
    - [中文白話解釋]：組合預期回報永遠係個別回報按投資金額比重嘅加權平均（注意：係金額加權，唔係簡單平均！）。先計權重 40%/60%，再乘返各自回報，加埋得 14.80%。

* [Flashcard 5]
  - Front (Question in English): What does the correlation coefficient (ρ) measure, and what are the diversification implications of ρ = +1, ρ = 0 and ρ = −1?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - ρ_AB = COV_AB / (σ_A·σ_B); measures how returns on two assets move together; ranges from −1 to +1.
      - ρ = +1: perfectly positively correlated — no diversification benefit.
      - ρ = 0: uncorrelated — returns not related; diversification benefit exists.
      - ρ = −1: perfectly negatively correlated — a properly weighted two-stock portfolio can eliminate all portfolio risk.
      - In practice, typical stock portfolios have ρ ≈ 0.65, so risk is lowered but not eliminated.
    - [中文白話解釋]：相關係數 = 協方差 ÷ 兩個標準差嘅乘積，數值介乎 −1 同 +1。+1 代表兩隻股票齊上齊落，分散投資冇用；−1 代表一升一跌，啱啱好配重可以完全對沖晒風險；0 代表互不相干。現實中股票之間通常約 +0.65，所以分散只能減低風險而唔係清零。

* [Flashcard 6]
  - Front (Question in English): A stock has a covariance with the market of 0.2, while the variance of the market is 0.12. Calculate the stock's beta and interpret the result.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - βᵢ = COV(i,M) / σ²_M = 0.2 / 0.12 = **1.667**
      - β > 1: the stock's systematic risk is higher than that of the market.
      - Interpretation boundaries: β = 1 → same systematic risk as the market; β < 1 → lower; β = 0 → zero systematic risk.
    - [中文白話解釋]：Beta = 股票同市場嘅協方差 ÷ 市場嘅方差 = 0.2 ÷ 0.12 = 1.667。大過 1 代表呢隻股票比大市更波動、系統性風險更高；如果市場升 1%，佢平均會升約 1.67%。記住 β=1 同市場一樣、β=0 冇系統性風險呢兩個基準。

* [Flashcard 7]
  - Front (Question in English): The beta of Tencent is 1.2, the expected market return is 10% and the rate of Hong Kong Exchange Fund Bills and Notes is 3%. Calculate the expected return using CAPM.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - E(Rᵢ) = R_rf + βᵢ[E(R_m) − R_rf]
      - = 3% + 1.2 × (10% − 3%) = 3% + 1.2 × 7% = 3% + 8.4%
      - E(R_Tencent) = **11.4%**
      - Note: in Hong Kong the risk-free proxy is HK Exchange Fund Bills and Notes issued by the HKMA.
    - [中文白話解釋]：CAPM 一條式搞掂：無風險利率 3% 加 beta 1.2 乘以市場風險溢價 (10% − 3% = 7%)，即 3% + 8.4% = 11.4%。小心唔好將「市場回報」同「市場風險溢價」撈亂 — 如果題目直接畀 market risk premium，就唔使再減無風險利率。

* [Flashcard 8]
  - Front (Question in English): On the Security Market Line (SML), how do you identify undervalued and overvalued securities? What is the slope of the SML?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - SML: kᵢ = R_rf + [E(R_m) − R_rf]·βᵢ; plots required return against beta (systematic risk).
      - Slope of the SML = market risk premium [E(R_m) − R_rf] — NOT beta.
      - In equilibrium, all accurately priced securities lie on the SML.
      - Expected return ABOVE the SML → expected return exceeds required return → undervalued (buy; price will be bid up).
      - Expected return BELOW the SML → expected return below required return → overvalued.
    - [中文白話解釋]：SML 以 beta 做橫軸、必要回報做縱軸。一隻股票如果實際預期回報高過 CAPM 算出嚟嘅必要回報，佢就會落喺 SML 上方，代表被低估、值得買；反之落喺下方就係被高估。最常見陷阱：SML 嘅斜率係市場風險溢價，唔係 beta！

---

「Phase 3 測驗題目及答案請見另外兩個檔案：M7_Ch6_CAPM_Quiz.md / M7_Ch6_CAPM_Answers.md」
