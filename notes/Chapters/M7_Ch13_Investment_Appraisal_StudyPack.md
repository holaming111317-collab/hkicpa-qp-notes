# M7 Chapter 13 Investment Project Appraisal — Study Pack (Week 11)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構
- 本章兩大主線：企業估值模型（Business Valuation Models：Dividend Growth Model、Free Cash Flow Model、P/E Ratio、Enterprise Value to EBITA）與資本投資評估技術（Capital Investment Appraisal：Payback、Discounted Payback、ARR、IRR、MIRR、NPV、PI）。
- 投資決策只應考慮相關及增量現金流（Relevant / Incremental Cash Flows）：Sunk costs 忽略、Opportunity costs 要計入、Financing costs 不計入（已反映在 discount rate）、Net working capital 投入並於項目完結時收回、Externalities（包括 Cannibalisation）要考慮。
- 現金流分析必須處理 Taxation、Inflation 及 Depreciation 的影響：一般用名義現金流（nominal cash flows）配以名義貼現率（nominal discount rate）；Depreciation 產生 Depreciation Tax Shield，但其金額固定，不隨通脹變動。
- NPV 是首選評估方法（primary method），因為它直接量度項目為公司價值增加多少，與股東價值最大化目標一致；IRR、MIRR、PI 各有客觀準則但均有局限（尤其 mutually exclusive projects 及 capital rationing）。
- 除財務因素外，還須考慮非財務因素（Non-financial Considerations）：CSR、Sustainability、Environmental consequences、Organisation Strategy、Legal Issues、Cultural Impacts、Operational Challenges。

### 2. 必背考點清單

**A. Business Valuation Models（13.1）**
- Dividend Growth Model：P0 = D1 ÷ (R − g)，其中 P0 = current value/price per share；D1 = dividend paid in the next period（D1 = D0 × (1+g)）；g = constant growth rate for dividends；R = required return on ordinary shares / discount rate。**適用條件：R > g**；若 R ≤ g 結果無意義。若 g = 0，P0 = D ÷ R（no-growth dividend stream）。
- Free Cash Flow Model：FCF = [(Revenue − Op Ex − D&A) × (1 − t)] + D&A − Cap Exp − Add WC；即用 NOPAT + D&A − Capital expenditures − Additions to working capital。
- Price-to-Earnings Ratio：P0 = Estimated EPS1 × Justified P/E（leading / forward P/E 用未來12個月盈利；lagging P/E 用過去12個月 EPS0）。
- Enterprise Value to EBITA：Enterprise Value = market value of an entity's capital less cash and cash equivalents（即 takeover value）；EBITA 適用於資本密集型公司（EBITDA 可能因高折舊而扭曲）。

**B. Relevant / Incremental Cash Flows（13.2）**
- Sunk costs：已發生、不會因未來決定而改變的成本，**不相關，必須忽略**（例如舊設備的 book value、已付的市場調查費）。
- Opportunity costs：因採取某行動而放棄的另一機會之利益，**相關，必須計入**（例如項目佔用設備而失去出售該設備所得的 HK$500,000）。
- Financing costs are ignored：融資現金流（利息等）不計入 FCF，因為已反映在 discount rate；NOPAT 用 **marginal tax rate** 計算。
- Net Working Capital = Current assets − Current liabilities；項目投入 WC，項目完結時全數收回（last year cash flow 要包括 recovery of working capital，否則會嚴重低估 NPV）。
- Externalities：投資對第三方產生但未反映在成本中的正/負面影響（如 carbon tax）；Cannibalisation：新產品侵蝕公司現有產品銷售（增量現金流 = 新產品收益 − 被侵蝕的收益，例如 100,000 − 40,000 = HK$60,000）。
- Discount rate：一般用 WACC；項目風險高於公司一般業務時應**調高** discount rate（discount rate = cost of capital element + risk element）。又稱 hurdle rate / required rate of return / cut-off rate。

**C. Inflation, Tax & Depreciation（13.3 / 13.7）**
- 通脹處理：最簡單做法是用 nominal cash flows 配 nominal discount rates（或 real cash flows 配 real rates，但 depreciation tax savings 以實際折舊額計，易造成不一致）。
- Depreciation **不隨通脹改變**（金額固定）；通脹上升會**降低** depreciation tax shield 的現值。
- After-inflation, after-tax break-even rate：B = I ÷ (100 − E)，I = inflation rate，E = effective tax rate。例：5% ÷ (100 − 16.5) = 6.0%。
- 香港兩級制利得稅（two-tiered profits tax，2018年起）：Corporations 首 HK$2 million assessable profits 稅率 8.25%，其後 16.5%；unincorporated businesses 為 7.5% / 15%。香港無 capital gains tax、股息及利息無 withholding tax；**集團不得合併報稅**（consolidated returns not allowed）。
- Depreciation tax shield：Straight-line method = 成本 ÷ estimated useful life；Diminishing-balance method = 固定百分比 × written-down value，前期折舊較高 → 前期稅務節省及稅後淨現金流較大。
- 出售資產稅項 = (Sales proceeds − remaining book value) × tax rate。

**D. Investment Appraisal Techniques（13.4 / 13.5）— 決策準則必背**
- Payback Period：收回初始投資所需年數（cumulative cash flows）；優點：簡單、可用作初步篩選及量度流動性；缺點：**忽略貨幣時間價值**、忽略 payback 後現金流、cut-off 無客觀標準。
- Discounted Payback：以折現現金流計算回本年期；**≥ simple payback**（因未來現金流被折現而縮小）；仍忽略 cut-off 後現金流、cut-off 仍屬任意。
- ARR = Average net income ÷ Average book value（或用 (Opening BV + Closing BV) ÷ 2）；用 accounting numbers 而非 cash flows；忽略 time value of money 及 risk；**易受折舊方法等會計處理操縱**。
- IRR：使 NPV = 0 的折現率（PV of inflows = PV of outflows）；準則：**IRR > cost of capital 則接受**；缺點：不適用於 mutually exclusive projects；現金流符號改變多於一次時可能無法計算/出現多解。
- MIRR：假設正現金流以 **cost of capital** 再投資（比 IRR 假設以 IRR 再投資更現實）；每個項目只有單一解；缺點：不適用於 mutually exclusive projects 及 capital rationing。
- NPV：PV of net cash flows − capital investment；準則：**NPV ≥ 0 接受，NPV < 0 拒絕**；互斥項目選最高 NPV。
- PI = PV (cash inflows) ÷ PV (cash outflows)；準則：**PI > 1 接受（即 NPV > 0）**；屬 relative measure（非絕對財富量度）；capital rationing 時可用作初步排名（類似 contribution per limiting factor），但最終應選**總 NPV 最高的項目組合**。

**E. Capital Rationing（13.6）**
- 理論上應接受所有 NPV > 0 的 independent projects；但實務上受內部預算限制或市場失效限制 → capital rationing。
- 沿 Investment Opportunity Schedule (IOS) 投資，直至 IRR = WACC 或最後項目的 NPV = 0（最佳投資額）。
- 資金受限時：用 PI 初步排名，最終以**在預算限制下總 NPV 最高的組合**作決定。

### 3. 易混淆概念對比 (Common Pitfalls)

**對比一：Sunk Costs vs Opportunity Costs（Sunk Costs 與 Opportunity Costs 之別）**
- Sunk Costs（沉沒成本）：已經支付、無論將來作任何決定都不能改變的成本，例如舊機器的 book value、已完成的可行性研究費。**在增量現金流分析中必須忽略**。
- Opportunity Costs（機會成本）：因選擇某方案而**放棄**的另一方案可帶來的利益，屬於未來相關現金流，**必須計入**項目分析。
- 例子：公司考慮一個項目，需動用一部本身擁有的舊設備。該設備 book value 為 HK$800,000，但在二手市場可賣 HK$500,000。分析時：HK$800,000 是 sunk cost，忽略；HK$500,000 是 opportunity cost，要當作項目的成本計入。常見錯誤是把兩者身份倒轉——記住「**過去的錢不理，將來放棄的利益要算**」。

**對比二：Independent Projects vs Mutually Exclusive Projects（獨立項目與互斥項目下 NPV 與 IRR 的分歧）**
- Independent projects（獨立項目）+ conventional cash flows（先流出後流入）：NPV 與 IRR 必然給出相同的接受/拒絕結論（NPV > 0 ⇔ IRR > cost of capital ⇔ PI > 1）。
- Mutually exclusive projects（互斥項目）：接受一個即要放棄另一個。此時**不能**單看哪個項目 IRR 較高——IRR 是相對量度，可能與 NPV 結論衝突；正確做法是**選 NPV 最高的項目**，因為 NPV 直接量度公司價值的增加。
- 例子：Project A IRR 18%、NPV HK$80,000；Project B IRR 15%、NPV HK$150,000。若兩者互斥，應選 B（較高 NPV），而非 A（較高 IRR）。考官常以此設陷阱：「highest IRR」是錯誤選項。

---

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): Under the Dividend Growth Model, how do you calculate the current value of a share, and when is the model valid?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - P0 = D1 ÷ (R − g), where D1 = D0 × (1 + g).
      - Valid only when R > g; if R ≤ g the result is meaningless.
      - If g = 0, the equation becomes P0 = D ÷ R (no-growth dividend stream).
      - Assumes a constant growth rate forever — an unrealistic stability assumption and a key weakness.
    - [中文白話解釋]: 股價 = 下年度股息 ÷（要求回報率 − 股息增長率）。記住條件：要求回報率必須大於增長率，否則分母變零或負數，答案無意義。若股息零增長，就退化成永續年金公式 D ÷ R。

* [Flashcard 2]
  - Front (Question in English): A company just paid a dividend of HK$0.27 per share. Dividends are expected to grow at 6% per year and the required return is 12%. Calculate the current share price.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Step 1: D1 = D0 × (1 + g) = HK$0.27 × 1.06 = HK$0.2862.
      - Step 2: P0 = D1 ÷ (R − g) = HK$0.2862 ÷ (0.12 − 0.06) = HK$0.2862 ÷ 0.06.
      - Current share price = **HK$4.77**.
    - [中文白話解釋]: 留意題目俾嘅係「剛剛派咗」嘅 D0，所以先要乘 (1+g) 轉做下年度股息 D1，先好代入公式。呢步係最常見嘅扣分位。

* [Flashcard 3]
  - Front (Question in English): Which costs are relevant in incremental cash flow analysis — sunk costs, opportunity costs, or financing costs?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Sunk costs: NOT relevant — already incurred and cannot be changed by any future decision; ignore.
      - Opportunity costs: RELEVANT — benefit forgone from an alternative use of a resource; include.
      - Financing costs (e.g. interest): NOT included in FCF — they are already captured in the discount rate.
      - Also include: incremental net working capital investment (recovered at project end) and externalities/cannibalisation.
    - [中文白話解釋]: 口訣：「沉沒唔計、機會要計、融資費用交俾 discount rate」。舊設備賬面值係 sunk cost 唔理；但設備可以賣出的價錢係 opportunity cost 要計入；利息開支唔好重複計，因為貼現率已經反映資金成本。

* [Flashcard 4]
  - Front (Question in English): What is the formula for Free Cash Flow (FCF) used in NPV analysis, and why is depreciation added back?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - FCF = [(Revenue − Op Ex − D&A) × (1 − t)] + D&A − Cap Exp − Add WC.
      - Equivalently: FCF = NOPAT + D&A − Capital expenditures − Additions to working capital.
      - D&A is deducted first to get the tax deduction (depreciation tax shield), then added back because it is a non-cash charge.
      - NOPAT uses the company's marginal tax rate.
    - [中文白話解釋]: 折舊本身唔係現金支出，但係可以扣稅，所以流程係：先扣折舊計稅（慳咗稅 = depreciation tax shield），再將折舊加返入去還原現金流。仲要扣埋買機器（Cap Ex）同投入嘅 working capital。

* [Flashcard 5]
  - Front (Question in English): State the accept/reject decision rules for NPV, IRR, PI and MIRR.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - NPV: accept if NPV ≥ 0 (zero or positive); reject if NPV < 0.
      - IRR: accept if IRR > cost of capital (required rate of return).
      - PI: accept if PI > 1 (equivalent to NPV > 0); reject if PI < 1.
      - MIRR: accept if MIRR > cost of capital.
      - For independent projects with conventional cash flows, all four give the same accept/reject decision.
    - [中文白話解釋]: 四條準則背到滾瓜爛熟：NPV 唔可以負、IRR 同 MIRR 要高過資金成本、PI 要大過 1。獨立項目加正常現金流之下，四把尺結論一致；一出現互斥項目或非傳統現金流，就得以 NPV 為準。

* [Flashcard 6]
  - Front (Question in English): A project has an initial outlay of HK$12 million and PV of cash inflows of HK$13.38867 million at a 15% discount rate. Calculate the PI and state the decision. What is the NPV?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - PI = PV (cash inflows) ÷ PV (cash outflows) = HK$13.38867m ÷ HK$12m = **1.12** (or 112%).
      - PI > 1 → accept the project.
      - NPV = PV inflows − initial outlay = 13.38867 − 12 = **HK$1.38867 million** (positive, consistent with PI > 1).
      - Relationship: NPV > 0 ⇔ PI > 1; NPV < 0 ⇔ PI < 1.
    - [中文白話解釋]: PI 就係「流入現值 ÷ 流出現值」。PI 大過 1 即代表流入現值大過投資額，NPV 必定為正，兩者結論一致。考試常問「俾咗 NPV 同投資額，PI 係幾多」——記住 PI = (投資額 + NPV) ÷ 投資額。

* [Flashcard 7]
  - Front (Question in English): Why can NPV and IRR give conflicting rankings, and which method should prevail for mutually exclusive projects?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Conflicts arise with mutually exclusive projects or unconventional cash flows (more than one sign change).
      - IRR is a relative measure — the highest IRR does not guarantee the highest value creation.
      - NPV is an absolute measure of the increase in company value → select the project with the highest NPV.
      - NPV should be the primary method because it aligns with maximising shareholder value.
      - Unconventional cash flows may produce multiple IRRs or no IRR at all.
    - [中文白話解釋]: 互斥項目下唔可以淨係睇邊個 IRR 高。IRR 係百分比（相對指標），細項目可以有高 IRR 但增值少；NPV 係金額（絕對指標），直接話你知公司值錢多咗幾多。所以互斥項目揀最高 NPV。

* [Flashcard 8]
  - Front (Question in English): A project's equipment costs HK$100,000, depreciated straight-line over 8 years. Tax rate is 30% and the required rate of return is 10%. If the fixed capital outlay increases by HK$100,000, what is the effect on the project's NPV?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Additional annual depreciation = HK$100,000 ÷ 8 = HK$12,500.
      - Depreciation tax saving = HK$12,500 × 30% = HK$3,750 per year for 8 years.
      - Change in NPV = −100,000 + Σ [3,750 ÷ (1.10)^t] for t = 1 to 8.
      - PV of annuity (8 years, 10%) = 5.3349 → 3,750 × 5.3349 = HK$20,006.
      - Effect on NPV = −100,000 + 20,006 = **decrease of HK$79,994** (not the full HK$100,000).
    - [中文白話解釋]: 額外投資額雖然係 HK$100,000，但多咗嘅折舊會帶來稅務節省（tax shield），抵銷一部分成本，所以 NPV 跌幅細過 HK$100,000。呢類題目考你識唔識將 depreciation tax shield 折現後扣返落額外投資額度。

---

Phase 3 測驗題目及答案請見另外兩個檔案：*_Quiz.md / *_Answers.md
