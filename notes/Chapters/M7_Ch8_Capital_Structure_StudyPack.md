# M7 Capital Structure Theories — Study Pack (Week 8)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構

- **資本結構理論 (Capital Structure Theories)**：核心是 Modigliani–Miller (M&M) 兩大命題 (Propositions) — Proposition 1 指出在六項完美市場條件下資本結構不影響公司價值 (firm value)；Proposition 2 指出普通股要求回報率 (required return on common stock, kcs) 與債務權益比 (debt-to-equity ratio) 成正比。再配合 agency theory（代理理論）、trade-off theory（權衡理論）、signalling theory（訊號理論）及 pecking order theory（融資順序理論）解釋現實世界中的最適資本結構 (optimal capital structure)。
- **風險分解 (Risk Decomposition)**：股東承受的總風險 (total equity risk) = business risk（營運風險，源自資產本身的現金流波動）+ financial risk（財務風險，源自資本結構中的債務）。營業槓桿 (operating leverage) 放大 business risk；財務槓桿 (financial leverage) 透過固定利息支出放大 financial risk。
- **稅盾與權衡 (Tax Shield & Trade-off)**：利息可扣稅 (interest payments are tax deductible) 產生 interest tax shield；永續債務的稅盾現值 = D × t。Trade-off theory 主張管理層增加債務直至邊際成本等於邊際收益 (costs and benefits are equal)，此時公司價值最大化。
- **金融產品與風險管理 (Financial Products for Risk Management)**：hedging（對沖，降低現有風險敞口）、speculating（投機，承擔高風險以博回報）、arbitraging（套利，利用價格失衡）。工具包括 forwards（遠期，可度身訂造）、futures（期貨，標準化並於交易所買賣、每日 mark-to-market）、swaps（掉期，交換現金流，如 plain vanilla interest rate swap）及 options（期權，call/put；European/American/Bermudan）。
- **集資與專家角色 (Fund Raising & Financial Experts)**：financing plan 三大組成部分為所需外部資金與來源、目標資本結構及派息政策 (payout policy)；investment banks 參與 origination（籌備發行）、underwriting（包銷，最常見為 firm commitment underwriting）及 distribution（分銷）。

### 2. 必背考點清單（公式與規則）

**M&M Proposition 1（無稅、完美市場）— 六項條件缺一不可：**
1. There are no taxes（無稅）
2. There are no costs from information or transactions（無資訊或交易成本）
3. There are no bankruptcy costs（無破產成本）
4. Companies and investors have equivalent borrowing costs（公司與投資者借貸成本相同）
5. Market information is symmetrical（市場資訊對稱）
6. Capital structure decisions do not affect the real investment policies of the company（資本結構不影響實質投資政策）
- 結論：VFirm 不隨資本結構改變；財務重組 (financial restructuring) 不改變 pie 的總大小，只改變切法；投資者可透過自製槓桿 (homemade/off-setting trades) 抵銷公司重組效果。

**企業價值恆等式：**
- **VFirm = VAssets = VDebt + VEquity**（債務市值 + 權益市值 = 資產所產生現金流的市值 = enterprise value）

**永續現金流估值（全權益公司）：**
- **VFirm = CF / i**（CF = 每年永續現金流；i = 該現金流的折現率）
- 有稅情況下之無槓桿價值：**VUnlevered = CF × (1 − t) / i**

**WACC（完整版）：**
- **WACC = xDebt × kDebt pretax × (1 − t) + xps × kps + xcs × kcs**
- 無稅且無優先股之簡化版：**WACC = xDebt × kDebt + xcs × kcs**，其中 xDebt + xcs = 1
- 權重：xDebt = VDebt / (VDebt + Vcs)；xcs = Vcs / (VDebt + Vcs)
- 在 M&M Prop 1 條件下，WACC = kAssets，不隨資本結構改變。

**M&M Proposition 2（必背）：**
- **kcs = kAssets + (VDebt / Vcs) × (kAssets − kDebt)**
- VDebt/Vcs 上升 → kcs 上升；第一項 kAssets 反映 business risk，第二項反映 financial risk。

**利息稅盾（有稅、永續債務按面值交易）：**
- **PV of tax savings = D × t**（D = 債務額；t = 邊際公司稅率）
- 有稅時槓桿公司價值：**VLevered = VUnlevered + PV of tax shield**（債務越多、公司價值越高——與無稅 M&M 結論相反）

**其他理論要點：**
- Trade-off theory：add debt until marginal cost = marginal benefit → target capital structure maximises firm value。
- Signalling theory：發債公告一般被視為正面（公司有能力付息）；減債公告被視為負面。
- Pecking order theory：internal funds (retained earnings) → new debt → new equity（new common stock 最後、最貴，因發行成本高及市場反應差）。
- Agency theory：principal–agent conflict；asset substitution problem（股東以高風險資產取代低風險資產，損害 lenders）；underinvestment problem（財困公司股東拒絕正 NPV 項目，因利益歸 lenders）；debt 可減少管理層浪費（alignment 好處），亦可令管理層過份保守。

**對沖 / 投機計算：**
- **Profit (loss) from naked short position = (F − ST) × n**（F = forward price；ST = spot price；n = number of contracts）
- Long 外幣敞口（如出口商將收外幣）→ sell forward 對沖；short 敞口（如進口商將付外幣）→ buy forward。
- Basis risk：被對沖資產與對沖工具不完全相同所產生的剩餘風險；forwards 因可訂造，可減低 basis risk。

**Interest rate swap（plain vanilla, fixed-for-floating）：**
- 利用 comparative advantage：各自在具比較優勢的市場借貸再交換付款；總節省 = 固定息差 − 浮動息差；節省分配取決於談判。
- 公司 A 淨成本 = 本身固定利率 + 付給 B 的 HIBOR − 從 B 收取的固定利率（類推 B）。

**Arbitrage Pricing Theory (APT)：**
- **ERi = a0 + bi1F1 + bi2F2 + … + binFn**（a0 = 零系統風險證券的預期回報；bi = 對風險因子的敏感度；F = 風險溢價）
- 基於 no-arbitrage principle；因子須實證識別（常見 3–5 個：預期通脹變動、未預期通脹、未預期工業生產變動、違約風險溢價變動、利率期限結構變動）；若只有一個因子（市場回報）則退化為 CAPM。

**Financing plan 三部分：**(1) amount of external funding needed and sources of funds；(2) desired capital structure；(3) payout policy。投資與融資決策不能獨立作出。

### 3. 易混淆概念對比 (Common Pitfalls)

**Pitfall 1：Business risk vs Financial risk**
- Business risk（營運風險）：源自資產與營運本身 — unit sales、unit prices、生產銷售成本、degree of operating leverage；即使零負債 (all-equity) 亦存在，反映在 kAssets 上。
- Financial risk（財務風險）：源自資本結構中的債務 — 固定的 interest and principal payments 令股東現金流更波動；反映在 M&M Prop 2 的第二項 (VDebt/Vcs)(kAssets − kDebt)。
- 例子：兩間同行公司 operating leverage 相同（business risk 相同），一間無債、一間 50% 債務 — 兩者 EBIT 對銷售變動的敏感度**相同**（營運層面無分別），但有債公司的 net income 對 EBIT 變動**更敏感**（financial risk 更高）。記住：營業槓桿放大的是 EBIT；財務槓桿放大的是 EBIT 到 net income 之間的波動。

**Pitfall 2：M&M 無稅世界 vs 有稅世界（對資本結構的結論完全相反）**
- 無稅（Prop 1 六條件全成立）：capital structure is irrelevant — VFirm 不變，發債回購股票只改變現金流在 debt holders 與 shareholders 之間的分配。
- 有稅（其他條件不變）：利息可扣稅，VLevered = VUnlevered + D × t — 債務**提升**公司價值，理論上越多債越好（直至 trade-off theory 的 distress/agency costs 抵銷）。
- 例子：公司無槓桿價值 HK$5,417（按稅後現金流折現），發行 HK$1,500 永續債、稅率 35% → 稅盾 = 1,500 × 0.35 = HK$525 → VLevered = HK$5,942。常見錯誤：考生在有稅題目中忘記用稅後現金流折現 VU，或忘記加回稅盾。

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): State the six conditions under which M&M Proposition 1 holds, and its conclusion on capital structure.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - (1) No taxes; (2) no information or transaction costs; (3) no bankruptcy costs; (4) companies and investors have equivalent borrowing costs; (5) market information is symmetrical; (6) capital structure decisions do not affect the firm's real investment policies.
      - Conclusion: capital structure decisions do NOT affect the value of the firm (VFirm = VDebt + VEquity stays constant); the pie is only sliced differently.
    - [中文白話解釋]: M&M 第一命題話：喺一個冇稅、冇交易成本、冇破產成本、人人借錢成本一樣、資訊完全對稱、而且融資決策唔影響實質投資嘅完美市場入面，公司點樣混合債同股都唔會改變公司總價值——個餅大細不變，只係切法唔同。考試常要求背出六個條件。

* [Flashcard 2]
  - Front (Question in English): A firm generates perpetual annual cash flows of HK$300,000, is all-equity financed, and its cost of equity is 25%. It borrows HK$600,000 at 8% (perpetual) to repurchase equity. Assuming M&M Proposition 1 holds, calculate the new cost of equity.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - VFirm = CF / i = 300,000 / 0.25 = HK$1,200,000 (unchanged by restructuring).
      - VEquity after repurchase = 1,200,000 − 600,000 = HK$600,000.
      - Annual interest = 600,000 × 8% = HK$48,000; cash flow to shareholders = 300,000 − 48,000 = HK$252,000.
      - New kcs = 252,000 / 600,000 = 42%.
    - [中文白話解釋]: 先用永續年金公式 (CF ÷ i) 計出全權益公司價值，M&M 話重組後公司價值不變；扣返債務市值就係新股權價值，再將扣除利息後剩返俾股東嘅現金流除以新股權價值，就得出新嘅權益成本。債務越多，股東要求回報越高，呢個就係 Proposition 2 嘅精華。

* [Flashcard 3]
  - Front (Question in English): Distinguish business risk from financial risk, and identify the components of business risk.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Business risk: risk of the cash flows generated by the firm's assets/operations (captured in kAssets); exists even with zero debt.
      - Its components: systematic variation in (1) unit sales, (2) unit prices, (3) costs of producing and selling products, and (4) the degree of operating leverage.
      - Financial risk: additional risk to shareholders arising from the capital structure — fixed interest and principal payments to debt holders; increases with more debt financing (second term of M&M Proposition 2).
      - Total equity risk = business risk + financial risk.
    - [中文白話解釋]: Business risk 係生意本身嘅風險——銷量、售價、成本同營業槓桿嘅波動，就算零負債都有；financial risk 係因為借咗錢要固定還息還本，令股東剩低嘅現金流更加波動。債越多 financial risk 越大，兩者加埋先係股東承受嘅總風險。

* [Flashcard 4]
  - Front (Question in English): A company has pre-tax perpetual cash flows of HK$1,000, a tax rate of 35% and a discount rate of 12%. It issues a HK$1,500 perpetual bond and pays the proceeds out as a special dividend. Calculate the value of the firm after the debt issuance.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - VUnlevered = CF(1 − t) / i = 1,000 × (1 − 0.35) / 0.12 = HK$5,417.
      - PV of tax shield = D × t = 1,500 × 0.35 = HK$525.
      - VLevered = 5,417 + 525 = HK$5,942.
    - [中文白話解釋]: 有稅嘅世界，先將稅後現金流 CF×(1−t) 用永續公式折現出無槓桿價值；永續債務嘅稅盾現值好簡單就係債務額乘稅率 (D×t)；兩者相加就係發債後嘅公司價值。記住：有稅時發債會提升公司價值，同無稅 M&M 結論相反。

* [Flashcard 5]
  - Front (Question in English): A company issues HK$1 million of perpetual debt at a YTM of 9%, trading at par. The marginal corporate tax rate is 35%. Calculate the present value of the tax savings.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Annual interest = 1,000,000 × 9% = HK$90,000; annual tax saving = 90,000 × 35% = HK$31,500.
      - Discounted in perpetuity at 9%: 31,500 / 0.09 = HK$350,000.
      - Shortcut for permanent debt at par: PV of tax savings = D × t = 1,000,000 × 0.35 = HK$350,000.
    - [中文白話解釋]: 每年利息乘稅率就係每年稅務慳返嘅錢，再用債息率做永續折現；因為兩個 9% 會約走，所以永續、按面值發行嘅債券，稅盾現值永遠等於 D×t。考試見到「perpetual debt at par」直接用捷徑就得。

* [Flashcard 6]
  - Front (Question in English): Explain the asset substitution problem and the underinvestment problem as agency costs of debt.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Asset substitution problem: after receiving a loan, shareholders have an incentive to substitute riskier assets for less risky ones; the upside accrues to shareholders while lenders bear the downside — a wealth transfer from lenders to shareholders (can even make negative NPV risky projects attractive to shareholders).
      - Underinvestment problem: shareholders of a financially distressed firm turn down positive NPV projects because the value created would go to the lenders rather than to them.
      - Lenders respond by charging higher interest rates and adding protective contract clauses (e.g. dividend limits).
    - [中文白話解釋]: Asset substitution 係股東借到錢之後偷龍轉鳳買高風險資產——贏咗股東袋、輸咗債權人墊底；underinvestment 係財困公司嘅股東連正 NPV 項目都唔做，因為做好咗啲利益全部歸債權人。兩者都係債務帶嚟嘅代理成本，債權人會用更高利率同合約條款自保。

* [Flashcard 7]
  - Front (Question in English): Two companies enter a plain vanilla interest rate swap. Company A pays fixed 10.8% on its own borrowing, pays HIBOR to Company B, and receives fixed 10.9% from Company B. What is Company A's net borrowing cost, and what principle makes the swap beneficial?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Net cost to A = 10.8% (own fixed) + HIBOR (paid to B) − 10.9% (received from B) = HIBOR − 0.1%.
      - Compared with A's direct floating quote of HIBOR + 0.25%, A saves 0.35%.
      - Principle: comparative advantage — each firm borrows where it has a comparative advantage (A in fixed, B in floating) and swaps payments; the total gain equals the difference between the fixed-rate spread and the floating-rate spread, split by negotiation.
    - [中文白話解釋]: 掉期計淨成本就係「自己俾嘅 + 付俾對方嘅 − 收對方嘅」三項加減。背後原理係比較優勢：A 喺定息市場優勢大啲、B 喺浮息市場蝕得少啲，各自去自己有優勢嘅市場借，再交換付款，大家齊齊慳息。總慳幅 = 定息息差 − 浮息息差，點分由談判決定。

* [Flashcard 8]
  - Front (Question in English): Lantau Ltd will receive GBP135,000 in 60 days. The 60-day forward rate is US$1.7864/GBP. If it does NOT hedge and the spot rate in 60 days is US$1.7635/GBP, how much does the company lose by not hedging?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Hedged receipt = 135,000 × 1.7864 = US$241,164.
      - Unhedged receipt = 135,000 × 1.7635 = US$238,072.50.
      - Loss from not hedging = 241,164 − 238,072.50 = US$3,091.50.
      - Alternatively: (F − ST) × n = (1.7864 − 1.7635) × 135,000 = US$3,091.50.
    - [中文白話解釋]: 出口商將來會收外幣，即係 long 外幣，對沖方法係賣出遠期 (sell forward) 鎖定匯率。冇對沖嘅話就要用到期即期價兌換；兩個匯率嘅差額乘外幣金額，就係唔對沖嘅損失（或者慳返嘅錢）。呢條公式 Profit/(loss) = (F − ST) × n 係對沖計算嘅萬用式。

Phase 3 測驗題目及答案請見另外兩個檔案：*_Quiz.md / *_Answers.md
