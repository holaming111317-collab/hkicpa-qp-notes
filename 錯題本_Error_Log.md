# 錯題本 (Error Log)

> 每次 Quiz 批改（Phase 4）後更新。溫習方法：遮住右欄 Model Sentence，望住「錯題」欄重新答一次，答到先算真正掌握。

## 錯因類型圖例

| 類型 | 意思 | 補救方法 |
|---|---|---|
| 概念不清 | 概念之間嘅邊界撈亂（你目前最常見）| 重温 Study Pack 嘅 Common Pitfalls 對比表 |
| 公式誤用 | 公式啱但用錯條件（例如 Gordon model 喺 g ≥ R 時用）| 背公式時連「適用條件」一齊背 |
| 條文記錯 | IRO/SDO 條文編號或內容記錯 | 用 M9 Master Section List 重背 |
| 計算粗心 | 步驟啱但計錯數 | 考試時每條 calculation 用最後 30 秒覆核單位同小數位 |
| 英文理解 | 睇錯題目要求 | 用《考試英文急救詞彙表》+ 拆題三步法 |

## M7 Financial Management

| 日期 | 章節 | 錯題 | 錯因類型 | 正確觀念 / Model Sentence |
|---|---|---|---|---|
| 8/21 | Ch1 | Q1：誤以為 profit 確認時間有分別（其實兩個項目都係 Y1 確認 HK$2.0M）| 概念不清 | "Under profit maximisation, two projects with identical accounting profits are treated as identical — the goal ignores the timing of cash flows and the time value of money." |
| 8/21 | Ch1 | Q3：EMH 三層資訊集撈亂（以為 weak form 都被推翻）| 概念不清 | "Weak ⊂ semi-strong ⊂ strong. Earning excess returns from public information contradicts the semi-strong and strong forms — but not the weak form, which only concerns past price and volume data." |
| 8/23 | Ch2 | Q1：短期 vs 長期融資分類錯（揀咗 demand line of credit；答案係 7 年租約）| 概念不清 | "The dividing line is one year: CP (1–270 days), BAs (1–180 days) and operating lines of credit are short-term; a lease running for more than one year is treated as long-term — effectively 100% debt financing." |
| 8/23 | Ch2 | Q3：PIPE 唔識（估咗 rights offering）| 概念不清 | "A PIPE is the sale of unregistered shares by an already-listed company to an institutional investor, almost always at a discount, with an undertaking to register the shares (usually within 90 days)." 分類三步：上咗市未？註冊咗未？賣畀邊個？ |
| 8/23 | Ch2 | Q4：BEY 公式背唔出，超時＋翻筆記先完成（數值 3.62% 本身啱）| 公式誤用/唔熟 | "BEY = (Face − Price) ÷ Price × 360 ÷ Days" — 分母係發行價唔係面值；貨幣市場用 360 日。閉卷下背唔出公式 = 直接失分，揭 flashcard 到反射級 |
| 9/21 | Ch3 | R3（Retest）：BEY 只計咗期內回報 0.76%，**忘記年化 ×360/45**（正確 6.05%）| 公式誤用/唔熟 | "BEY = (Face − Price) ÷ Price × 360 ÷ Days — never report the holding-period yield as the annual yield." 由 W2 到而家**第二次**跌喺同一條公式，未過關，繼續重測 |
| 9/21 | Ch3 | Q3：永續年金比較靠感覺揀「增長好過縮減」（A），冇計 PV（Grow 10,000 vs Shrink 14,285.71，答案 B）| 概念不清/唔計數 | "Rank cash flow streams by PV, never by story: PV = PMT₁ ÷ (r − g). A declining perpetuity can still be worth more if its PMT₁ is large enough." 見到兩個 choices 比較，一定要寫低兩個數先揀 |
| 9/21 | Ch3 | Q4：EAR 閉卷下**完全空白**（"FORGET THE FORMULA"）；正確 (1.015)¹² − 1 = 19.56% | 公式背誦 | "EAR = (1 + periodic rate)^n − 1. A 1.5% monthly rate is NOT 18% per year; it is (1.015)^12 − 1 = 19.56%." 處方：每日 10 分鐘公式閃卡，EAR + BEY 兩條優先 |
| 9/23 | Ch4 | R5（Retest 第 3 次）：BEY 公式完全走樣——寫成 price÷1,000,000 × 30/360 = 8.28%（正確：(F−P)÷P × 360÷30 = **7.24%**）| 公式背誦 | "BEY = (Face − Price) ÷ Price × 360 ÷ Days." 第三次錯：分子折扣額、分母發行價、最後年化。罰：將條公式寫十遍 |
| 9/23 | Ch4 | R6（Retest 第 2 次）：永續年金揀 C「計唔到」——條件係 r > g（6% > 3%，計到）；兩個 PV 都冇寫低 | 概念不清 | "A growing perpetuity is computable whenever r > g — write down both PVs before you choose." 前日先教完，今日再錯 |
| 9/23 | Ch4 | Q1：溢價債排名調轉（揀 A；premium bond 係 coupon rate > CY > YTM，答案 B）；Q2：波動性定理調轉（揀 A 3-year；最長年期 + 最低 coupon 先最波動，答案 C 10-year zero coupon）| 概念不清 | "Premium bond: coupon rate > current yield > YTM (invert for discount). Longer maturity + lower coupon = greater price volatility." 兩條定理係死背位 |
| 9/23 | Ch4 | Q4：半年複利冇換算（應係 coupon 40、r 5%、n 10；佢用咗 80、10%、10 期），annuity 公式寫成 (1 **+** 1/(1+r)ⁿ)——係**減號**唔係加號。正確 **922.78** | 公式誤用 | "Semi-annual: halve the coupon, halve the rate, double the periods. Price = C×[1−(1+r)⁻ⁿ]÷r + F×(1+r)⁻ⁿ." 常識檢查：coupon 8% < market 10% → 價格必須低過面值，你答 1,493.98 唔合理 |
| 9/23 | Ch4 | Q5：零息債方向倒轉（用 ×(1.04)¹² 得 1,602.66；應係 **÷**）。正確 1,000÷(1.04)¹² = **624.60** | 公式誤用 | "A zero-coupon bond always trades below face: Price = F ÷ (1+r)ⁿ." 答完每條計數，用 10 秒問自己：合理唔合理？ |
| 9/23 | Ch5 | R11（Retest 第 4 次）：BEY 三寶全錯——分子倒轉 (P−F)（負數都唔覺）、分母用咗面值、日數分數倒轉 ×60/360。正確 **3.02%** | 公式背誦 | "BEY = (Face − Price) ÷ Price × 360 ÷ Days." 第四次錯，而且每個組件都錯。呢條唔係理解問題，係背誦問題——今晚寫十遍、聽朝背一次 |
| 10/5 | Ch7 | Q5：三層 WACC 兩個核心錯——(1) 權重用咗**股數**（5m、10m）而唔係**市值**（股數×股價 = 75m、250m）；(2) DGM 公式走樣：寫成 2×1.04÷(25+0.04)——g 係**加喺後面**（D1÷P0 **+** g），唔係加落股價度。正確 **10.42%**（佢答 6.37%）| 公式誤用/概念不清 | "Market value of equity = shares outstanding × current price. DGM: k = D₁÷P₀ + g, where D₁ = D₀×(1+g) — g is added AFTER the division, never to the price." 口訣：weights 用市值、costs 逐層計、只有債務乘 (1−t) |
| 10/7 | Ch8 | R34（Retest 第 2 次）：WACC **三度「forgot the formula」**——答 25.01%（正確 9.03%：ke=13.25%、kd(1−t)=4.5%、市值權重 (60,90)）| 公式背誦 | "WACC = (E/V)kₑ + (D/V)k_d(1−t), using MARKET-value weights." 同一公式第三度閉卷失憶——同 BEY/EAR 一樣，處方：每日默寫 WACC＋DGM＋MM 三條公式一次，直至考試日 |
| 10/7 | Ch8 | Q1：MM Prop 1（零稅）概念錯——揀咗「平價發債提高股價」（d）；正確（c）：**公司價值不變，但剩餘股權要求回報上升** | 概念不清 | "Under MM Proposition 1 without taxes, issuing debt to repurchase shares leaves firm value unchanged, but the required return on the remaining equity rises." 記憶鉤：pizza 切法唔同，pizza 一樣大 |
| 10/7 | Ch8 | Q4：MM Prop 2「forgot the formula」——答 2,040,000（正確 **30%**：V=400,000÷20%=2,000,000；E=2,000,000−800,000=1,200,000；ke=20%+(2/3)(20%−5%)=30%）| 公式背誦 | "MM Proposition 2: kₑ = k₀ + (D/E)(k₀ − k_d)." 三步：① V = CF ÷ k₀ ② E = V − D ③ 代公式 |
| 10/7 | Ch8 | Q5：MM with tax「forgot the formula」——答 6,966,666.67（正確 **14,900,000**：V_U=2,000,000×0.7÷0.1=14,000,000；V_L=14,000,000+0.3×3,000,000）| 公式背誦 | "MM with taxes: V_L = V_U + T_c × D, where V_U = after-tax perpetual cash flow ÷ r." Perpetual debt 嘅 tax shield PV = T_c×D |
| 10/7 | Ch9 | R38（Retest 第 3 次）：**市值權重終於啱**（90m/150m、60m/150m），但之後乘嘅係**銀碼**（1.8×3m、60m×6%）唔係利率——答 4,320,000（正確 **8.58%**）| 公式背誦 | "WACC = (E/V)kₑ + (D/V)k_d(1−t) — weights multiply RATES, not dollar amounts." 進步位：權重觀念已鞏固；缺嘅係 kₑ = D₁/P₀ + g 呢一步 |
| 10/7 | Ch9 | R40（Retest 第 2 次）：當咗 WACC 計——600,000/1,600,000×0.15 + 1,000,000/1,600,000×0.04 = 8.125%（正確 **18.67%**：V=4m、E=3m、ke=15%+(1/3)(11%)）| 公式背誦 | "MM Proposition 2: kₑ = k₀ + (D/E)(k₀ − k_d)." 見到 MM 題唔好用 WACC 框架；三步：V=CF÷k₀ → E=V−D → 代公式 |
| 10/7 | Ch9 | R41（Retest 第 2 次）：亂砌 1,000,000×0.92 + 2,000,000×0.75 = 2,420,000（正確 **9,875,000**：V_U=750,000÷0.08=9,375,000；V_L=9,375,000+500,000）| 公式背誦 | "V_L = V_U + T_c × D." 稅後 CF 先折現得 V_U，再加 tax shield——兩個組件分開計 |
| 10/7 | Ch9 | Q5：CCC 公式亂砌（360÷大雜燴）答 23.23→24（正確 **45 days**：DIO=365×500,000/3,650,000=50；DSO=365×400,000/5,840,000=25；DPO=365×300,000/3,650,000=30；CCC=50+25−30=45）| 公式背誦 | "CCC = days' inventory + days' receivables − days' payables, each = 365 ÷ turnover." 三個組件逐個計，唔好一條式砌埋 |
| 10/7 | Ch10 | R42（Retest 第 4 次）：**kₑ = 1.248/25 + 4% = 8.99% 呢步啱咗** ✅，但之後崩壞——V 寫成 400,000,000（應 90m）、只得 equity 項漏咗 debt、(1−t) 乘落 equity（正確 **6.66%**）| 公式背誦 | "WACC = (E/V)kₑ + (D/V)k_d(1−t)." 兩個 components 都要齊；只有 debt 先乘 (1−t) |
| 10/7 | Ch10 | R43（Retest 第 3 次）：又係 WACC 框架——答 6.75%，自己都問「it is like wacc?」（正確 **15.94%**：V=4,166,667、E=2,666,667、ke=12%+0.5625×7%）| 公式背誦 | "MM Proposition 2: kₑ = k₀ + (D/E)(k₀ − k_d)." MM 題唔好用 WACC；見「required return on equity after repurchase」= MM Prop 2 訊號 |
| 10/7 | Ch10 | R44（Retest 第 3 次）：800,000×0.9×0.8+1,500,000 = 2,076,000 亂砌（正確 **6,700,000**：V_U=640,000÷0.10=6,400,000；+0.2×1,500,000=300,000）| 公式背誦 | "V_L = V_U + T_c × D." V_U 係**稅後 CF ÷ r**；debt 面值唔好直接加落去 |
| 10/7 | Ch10 | R45（Retest 第 2 次）：turnover 分數倒轉——寫成 365÷(600,000/4,380,000)=2664.5（正確 DIO=365×(600,000/4,380,000)=50；CCC=**38.5 days**）| 公式背誦 | "Days = 365 × (balance ÷ flow) = 365 ÷ turnover." 計出嚟過千日 = 常識檢查即刻知錯 |
| 10/7 | Ch10 | Q5：EFN 只計咗 ΔA = 500,000（正確 **84,000**：ΔA 500,000 − ΔAP 80,000 − retained 336,000；retained = 6m×20% margin... 即 NI 840,000 × (1−0.6)）| 公式背誦 | "EFN = ΔA − ΔAP − retained earnings; retained = forecast net income × (1 − payout ratio)." 三個組件缺一唔得 |
| 10/9 | Ch11 | R46（Retest 第 5 次）：**WACC 終於全對** 🎉——kₑ=8.15%、k_d(1−t)=3.2%、權重 50/50、WACC=5.675%。書寫 typo：第一項分母寫成 1,600,000,000，但計數用啱 160,000,000 | ✅ 通過 | 五度交手終於斬殺——每日默寫起效 |
| 10/9 | Ch11 | R47（Retest 第 4 次）：MM Prop 2 三步全齊——V=4m、E=3m、ke=10%+(1/3)(4%)=**11.33%** ✅ | ✅ 通過 | "kₑ = k₀ + (D/E)(k₀ − k_d)" 已入腦 |
| 10/9 | Ch11 | R48（Retest 第 4 次）：V_U=3.5m 啱，但 tax shield 用咗 **0.7**×1,000,000（應 **T_c=0.3**×1,000,000=300,000）→ 答 4,200,000（正確 **3,800,000**）| 公式背誦 | "PV of tax shield = T_c × D — use the TAX RATE itself, not (1 − T_c)." (1−t) 係計稅後數先用；shield 直接乘稅率 |
| 10/9 | Ch11 | R49（Retest 第 3 次）：CCC 三組件全對——DIO 20、DSO 20、DPO 25、CCC=**15 days** ✅ | ✅ 通過 | 第三次過關 |
| 10/9 | Ch11 | R50（Retest 第 2 次）：EFN 兩錯——(1) NI 用咗 **ΔS** 計（300,000；應用**總預測銷售** 10,000,000×0.15×0.75=1,125,000）；(2) retained 變咗**加**（+112,500；應**減** 562,500）→ 答 1,112,500（正確 **437,500**）| 公式誤用 | "EFN = ΔA − ΔAP − retained earnings, where retained = TOTAL forecast net income × (1 − payout)." NI 永遠用總銷售額計，唔係用增量 |
| 10/13 | Ch12 | R51（Retest 第 5 次）：MM with tax **全對**——V_U=7.5m、shield=0.25×2.5m=625,000、V_L=**8,125,000** ✅ | ✅ 通過 | 第五次過關 |
| 10/13 | Ch12 | R52（Retest 第 3 次）：EFN **全對**——ΔA 1.32m、ΔAP 288,000、NI 1,008,000（總銷售）、retained 604,800（正確用**減**）、EFN=**427,200** ✅ | ✅ 通過 | 第三次過關——**M7 舊公式債全部清零** 🎉 |
| 10/13 | Ch12 | Q3：relevant cost 概念錯——揀咗 C（absorbed fixed OH 要計入最低報價）；正確 D：只有 future incremental + opportunity costs 先相關，sunk 同唔變嘅 OH 唔計 | 概念不清 | "Only future incremental costs and opportunity costs that differ between options are relevant to a special-order minimum price." |
| 10/13 | Ch12 | Q4：cost-plus 漏咗 fixed **manufacturing** OH（300,000÷8,000=37.5）——total cost 應係 107.5（45+37.5+25），mark-up=200,000÷860,000=23.26% → **132.50**；佢答 118.75（仲問「mark up on the cost?」——係）| 公式誤用 | "Mark-up % = desired ROI profit ÷ TOTAL cost; total cost includes ALL fixed overheads (manufacturing + S&A)." |
| 10/13 | Ch13 | R53（Retest）：relevant cost 概念 ✅——揀 C 排除唔變嘅 absorbed fixed OH，一take過 | ✅ 通過 | 概念清 |
| 10/13 | Ch13 | R54（Retest 第 2 次）：砌出 total cost + profit = 130 **已經係答案**，但又 ×1.2 雙重計利潤 → 156（正確 **130.00**）| 公式誤用 | "Target price = total cost + desired profit — do NOT apply the mark-up again after adding profit." 利潤只加一次 |
| 10/13 | Ch13 | Q4：NPV 兩錯——(1) NWC 期初 outlay 40,000 漏咗；(2) 期末收回 40,000 折現後應**加**返，佢**減**（仲有 typo Y2 寫 10,000）。正確 **−21,262**（reject）| 公式誤用 | "Working capital: OUT at t₀, recovered (added back, discounted) at the end." NWC 兩頭都要計 |
| 10/13 | Ch13 | Q5(a)：discounted payback 亂砌 500,000×1.1÷150,000=3.67（正確 **4.26 years**：逐年折現累積——Y4 尾 cum 475,480，差額 24,520 ÷ Y5 折現流 93,138 = 0.26）| 公式背誦 | "Discounted payback: discount EACH year's cash flow, accumulate until the outlay is recovered, then interpolate the fraction." 唔可以一條式直出 |
| 10/14 | Ch14 | R55（Retest 第 3 次）：cost-plus **全對**——cost/unit 120、profit/unit 15、price **135**（120+15 一次過）✅。小疵：「120*0.125=135」寫法錯（120×0.125=15）；要寫 120×1.125 或 120+15 | ✅ 通過 | 第三次過關 |
| 10/14 | Ch14 | R56（Retest 第 2 次）：NPV **全對**——outlay 250,000、PV inflows 261,382（NWC 50,000 加入 Y3 折現）、NPV=**+11,382 accept** ✅ | ✅ 通過 | NWC 兩頭啱 |
| 10/14 | Ch14 | R57（Retest 第 2 次）：discounted payback **全對**——逐年折現累積表齊、插值 4+19,616/74,511=**4.26 years** ✅ | ✅ 通過 | 第二次過關 |
| 10/14 | Ch15 | 主卷 **5/5** 🎯（純主卷）：ROI goal congruence（拒絕 20% 項目）、BSC internal process、lagging measures、ROI 24% + RI 150,000、EVA 1,000,000 全對 | ✅ 全對 | 隊列清零後首份純主卷滿分 |
| 10/15 | Ch16 | 主卷 **5/5** 🎯（純主卷）：financial risk 分類（bond default／unlisted asset 套現唔到／foreign government freeze = (1)(2)(4)）、風險對策配對（avoidance／mitigation／transfer／acceptance）、political risk insurance + 借 xeno natural hedge、LTV = 455,000 ÷ 650,000 = **70.0%**、LTV cap 70% 回推 max borrowing = 0.70 × 900,000 = **630,000** 全對——**M7 全部 16 章完成** 🎉 | ✅ 全對 | M7 學習階段收官；下一步：總複習＋計時操卷 |

## M9 Principles of Taxation

| 日期 | 章節 | 錯題 | 錯因類型 | 正確觀念 / Model Sentence |
|---|---|---|---|---|
| 8/22 | Ch1 | Q3：揀「NOT correct」題揀咗 C（AFAL），其實錯嘅係 B——以為 interest paid to non-resident 要預扣 | 概念不清 | "There is NO withholding tax on Hong Kong source dividends and interest. Only royalties (for IP used in HK) and fees of non-resident entertainers/sportsmen are taxed on a withholding basis." 見到 "withhold + interest/dividend" 嘅組合，八成都係錯。 |
| 8/23 | Ch2 | Q5：additional assessment 條 rule 啱但**無填日期同條文編號**（題目叫 state the latest date）；超時＋英文作文諗太耐 | 答題不完整 | "Under s.60(1) IRO, an additional assessment must be raised within six years of the end of the YA. YA 2019/20 ended 31 Mar 2020 → latest 31 Mar 2026. 10-year limit = fraud/wilful evasion only." 教訓：fill-in 用電報式 `31 March 2026 — s.60(1), 6-year limit from end of YA`，唔使完整句子 |
| 9/22 | Ch3 | R1（Retest）：additional assessment **又係冇日期冇條文**——(i) 只寫咗個 rule、(iii) 直頭 "forgot"（正確：31 March 2027 — s.60(1)）| 答題不完整/條文背誦 | "Under s.60(1) IRO, an additional assessment must be raised within 6 years after the end of the YA. YA 2020/21 ended 31 Mar 2021 → latest 31 Mar 2027; a September 2026 discovery is still within time." 第三次喺同一要求跌親：見到 additional assessment 就機械式寫「日期 — s.60(1)」 |
| 9/22 | Ch3 | Q1：capital vs revenue 撈亂——揀咗 A（取消獨家分銷協議 = 整個生意框架 = capital receipt），答案係 B（貨車維修期間失去使用嘅保險賠償 = revenue，填補利潤損失）| 概念不清 | "Compensation for loss of use of an income-earning asset fills a hole in trading profits (revenue); compensation for destroying the entire framework of the business is capital." 唔係睇金額大細，係睇佢補償緊咩 |
| 9/22 | Ch3 | Q3：DIPN 21 用常理推咗 B（以為邊份合約實質賺錢），答案係 A——trading profits 只要買**或**賣其中一份合約喺香港 effected 就全數課稅，冇 50:50 | 概念不清 | "Under DIPN 21, trading profits are wholly chargeable where either the contract of purchase or the contract of sale is effected in Hong Kong; apportionment is not available for pure trading profits." 特殊規則 > 一般原則 |
| 9/22 | Ch3 | Q5：兩個遺漏——fine HK$30,000 冇 add back（違法罰款永遠唔扣得）；DA HK$200,000 擺錯步驟（要喺計 assessable profits 時扣）。正確：(i) 1,950,000 (ii) 160,875 | 概念不清/步驟 | "Fines for breach of the law are never deductible — add them back; deduct agreed depreciation allowances in arriving at assessable profits, before applying the tax rate." 固定步驟：扣非應稅收入 → 加返非扣減支出 → 扣 DA → 乘稅率 |
| 9/28 | Ch4 | R7（Retest 第 4 次）：s.60(1)——日期**終於答啱**（31 Mar 2026、out of time），但第 (iii) 問條文編號又係 "i forgot" | 條文背誦 | "Under s.60(1) IRO, an additional assessment must be raised within six years after the end of the year of assessment." 第四次：個 rule 你識，係 "s.60(1)" 四個字符背唔出 |
| 9/28 | Ch4 | R8（Retest 第 2 次）：capital vs revenue 再錯——揀咗 D（trading stock 嘅保險賠償 = revenue，存貨係流動資產），答案係 C（sole manufacturing licence = 成個生意框架）| 概念不清 | "Insurance proceeds for destroyed trading stock replace circulating capital — a revenue receipt; compensation for destroying the entire framework of the business is capital." 第二次錯：先問自己「呢筆錢補償緊咩——利潤定框架？」 |
| 9/28 | Ch4 | Q1：三種收入來源規則撈亂——揀咗 B（多咗 (IV)），答案係 A。Ms. D 香港僱傭但**全部服務境外**＋到訪 ≤60 日 → s.8(1A)(b)(ii) 豁免 | 概念不清 | "Income from a Hong Kong employment is exempt if ALL services are rendered outside Hong Kong in the year (s.8(1A)(b)(ii)). Employment looks at where services are rendered; an office looks at central management and control; government pensions are fully assessable." |
| 9/28 | Ch4 | Q2：機組人員豁免只諗咗第一關（揀 A 60 日規則），答案係 C——s.8(2)(j) 要**兩關齊過**：本年 ≤60 日 **AND** 連續兩年合計 ≤120 日（75+50=125 失敗）；transit days 都計（D11/13）| 條文記錯 | "Under s.8(2)(j), a crew member's income is exempt only if BOTH limbs are met: ≤ 60 days in the YA AND ≤ 120 days over two consecutive YAs. Transit days inside the airport count as presence (IRBRD D11/13)." |
| 9/28 | Ch4 | Q4：計薪俸稅**漏咗 rental value**——僱主提供免租住所，s.9(2) 要加返 10% × 640,000 = 64,000；NCI 應係 424,000、稅款 54,080（佢答 360,000 / 51,700，仲有 160,000 寫成 210,000 嘅計數甩漏）| 概念不清/計算粗心 | "Where an employer provides a rent-free residence (not a hotel/hostel/boarding house), add rental value = 10% of income from the employer under s.9(2), BEFORE deducting allowances." 見到「rent-free flat」五個字就要反射加 10% |
| 9/29 | Ch5 | R17（Retest 第 5 次）：s.60(1) **終於全對**——31 March 2027、within time、s.60(1) 三樣齊 ✅ 剔除 | — | 五戰功成。證明罰寫係有效嘅；記住呢個感覺，其他條文編號都要咁背 |
| 9/29 | Ch5 | R18（Retest 第 3 次）：capital vs revenue 又錯——題目問 **REVENUE** receipt，佢揀咗 C（sole distribution licence = capital），答案係 B（按失去利潤計嘅違約賠償 = revenue）| 概念不清 | "Damages calculated by reference to the profit that would have been earned fill a hole in profits — a revenue receipt; compensation for the loss of the entire business framework is capital." 三次錯晒兩個方向：答題前**先圈起題目問緊 CAPITAL 定 REVENUE** 先落筆 |
| 9/29 | Ch5 | R21（Retest）：rental value 數值啱（50,000）但**又唔記得條文**（s.9(2)）| 條文背誦 | "Rental value = 10% of income from the employer — s.9(2) IRO." 同 s.60(1) 同一個病：數會計、條文唔背。Fill-in 題見到 "state the governing section" 必須寫條文編號 |
| 9/29 | Ch5 | Q4：物業稅計算**漏咗頂手費攤分**——premium 72,000 ÷ 36 個月 × 9 個月（**包括**免租月）= 18,000 冇計（佢答 16,680；正確 18,840）| 概念不清 | "A premium is spread over the shorter of the lease term or three years (s.5B(4)) — and the spreading period INCLUDES any rent-free month." 口訣：租金（免租期唔計）+ 頂手費攤分（免租期照計）+ 租客代付未償還開支 − 業主付差餉 → ×80% → ×15% |
| 9/29 | Ch5 | Q5：暫繳稅對銷方向倒轉——已繳暫繳稅 24,000 應該**減**，佢用咗**加**（51,000；正確 30,000 = 尾數 3,000 + 新一年暫繳 27,000）| 概念不清 | "On the notice of assessment: final tax LESS provisional tax already paid, PLUS new provisional tax for the next year (based on the current year's NAV, s.63L)." 評稅通知書總額 = 舊年尾數 + 新年暫繳 |
| 9/30 | Ch6 | R23（Retest 第 2 次）：rental value **全軍覆沒**——答咗 0.8×(800,000+80,000)=704,000、條文寫 s.5。正確：10% × 800,000 = **80,000**、**s.9(2)** | 概念不清/條文背誦 | "Rental value = 10% of income from the employer, added to assessable income — s.9(2) IRO." 你把 property tax 嘅 80% NAV 邏輯搬咗嚟 salaries tax——兩個稅種嘅機械唔同：salaries tax 加 10% 租值；property tax 先係 ×80%。條文 s.5 係物業稅，rental value 係 s.9(2) |
| 9/30 | Ch6 | Q4：PA 計算兩個核心錯——(1) 租金 300,000 冇轉 **NAV**（×80% = 240,000）直接入賬；(2) 按揭利息 260,000 冇**封頂喺 NAV**（淨係扣得 240,000，超額 20,000 永久作廢）。佢答 4,050；正確 **1,250** | 概念不清 | "Under personal assessment, rental income enters as NAV (80% of rent); mortgage interest is deductible up to that NAV — any excess is permanently lost (D51/04)." PA 口訣：租金先 ×80% → 利息封頂 NAV → 扣虧損同特惠扣除 → 扣免稅額 → 累進 vs 標準取低 |
| 9/30 | Ch6 | Q5：夫婦 PA **計到一半停咗**——得 296,000 冇計稅款；而且又係冇將租金轉 NAV（正確 chargeable income 236,000、稅款 **26,620**）| 答題不完整/概念不清 | "For a jointly electing couple, aggregate the reduced total incomes, deduct the MARRIED PERSON'S allowance (not two basic allowances), then apply the lower of progressive vs standard rate." 考試鐵律：計算題唔計到最後個稅款 = 唔當答咗 |
| 10/5 | Ch7 | R26（Retest 第 3 次）：rental value——10% 概念終於有咗（1.1×660,000），但 (i) 答咗 **assessable income 726,000** 而題目問嘅係 **rental value（66,000）**；(ii) 條文寫咗 **s.14**（嗰條係利得稅！）正確係 **s.9(2)** | 答題不對題/條文背誦 | "Rental value = 10% of income from the employer — s.9(2) IRO." 三次錯法都唔同：第一次唔記得條文、第二次搬 property tax 邏輯、第三次答錯數量+寫錯條文。s.9 = salaries tax、s.5 = property tax、s.14 = profits tax——三個 charging section 即刻背 |
| 10/5 | Ch7 | R27（Retest）：NAV 題**畫蛇添足乘多咗 0.15**（稅率！）——NAV = 400,000 × 80% = **320,000**，唔係 48,000；利息封頂都係 320,000 | 概念不清 | "NAV = rent × 80% — the 15% tax rate is applied to NAV only when computing property TAX, never when computing NAV itself." 乜嘢係 NAV、乜嘢係稅款，分清楚先好乘 |
| 10/5 | Ch7 | Q2：AVD Scale 2 vs BSD 雙重標準撈亂——揀咗 A（以為 HKPR 就用得 Scale 2）；其實佢已聯名持有住宅 → 唔合資格用 Scale 2 → AVD 15%（Scale 1 Part 1）；BSD 只要係 HKPR 以本人身份就免（唔理有幾多層樓）| 概念不清 | "AVD Scale 2 requires an HKPR who owns NO other residential property at acquisition; BSD exemption looks ONLY at HKPR status acting on one's own behalf — the number of properties owned is irrelevant." 口訣：AVD Scale 2 睇首置，BSD 只睇身份 |
| 10/5 | Ch7 | Q3：股票印花稅規則——揀咗 D（外幣債券唔算 Hong Kong stock），答案係 C：contract notes 交咗從價稅後，instrument of transfer 只收 **HK$5 固定稅** | 概念不清 | "Issue of shares is NOT dutiable; a gift of HK stock IS dutiable at market value (s.27); where contract notes are duly stamped, the instrument of transfer bears a fixed duty of HK$5." |
| 10/5 | Ch7 | Q4：SSD 稅率記錯——持有 18 個月（2022/6/1 → 2023/12/1）應係 **10%**（12–36 個月檔），佢用咗 20%；仲無端 +100。正確：AVD 975,000 + SSD 650,000 + BSD 975,000 = **2,600,000**（按較高者市值 6.5M 計）| 條文記錯 | "SSD: ≤ 6 months 20%; > 6–12 months 15%; > 12–36 months 10%. AVD/BSD/SSD are all computed on the higher of consideration or market value." SSD 三檔即刻背：6 個月 20、12 個月 15、36 個月 10 |
| 10/5 | Ch7 | Q5：組件全啱（1,710 + 25,500）但**加法計錯**出 25,671；正確 **27,210** | 計算粗心 | 步驟全對、加數錯——呢種係最嘥嘅失分。考試鐵律重申：每條計數最後 30 秒覆核，尤其係最後嘅加總 |
| 10/6 | Ch8 | R29（Retest 第 4 次）：rental value 數值終於啱（70,000）——但條文寫咗 **s.9(1)**，正確係 **s.9(2)** | 條文背誦 | "Rental value = 10% of income from the employer — s.9(2) IRO (not s.9(1))." 距離過關只差一個 subsection——閉卷下 (1) 同 (2) 就係攞分同失分嘅分別 |
| 10/6 | Ch8 | R31（Retest 第 2 次）：AVD/BSD 又錯——揀咗 A，仲寫埋 "(scale 1 for non individual)" 嘅混淆理由；答案係 C（佢名下有樓 → 唔係首置 → AVD 15%；HKPR 身份 → 免 BSD）| 概念不清 | "Scale 1 Part 1 applies to ANY purchaser who already owns residential property — including an HKPR. Scale 2 is for first-home HKPRs only; BSD exemption turns solely on HKPR status acting on one's own behalf." |
| 10/6 | Ch8 | Q4：兩級制稅率揀錯——RacketStar 係**個人**（unincorporated），首 200 萬應用 **7.5%**，佢用咗公司嘅 8.25%。正確：deemed profits 2/3 × 2.4M = 1,600,000 × 7.5% = **120,000**（佢答 132,000）| 條文記錯 | "Two-tiered rates: corporations 8.25% / 16.5%; UNINCORPORATED persons (individuals) 7.5% / 15% — on the first HK$2M of assessable profits." 見到個人表演者/獨資，反射 7.5% |
| 10/6 | 保溫卷W1 | Q1：s.60(1) **回忘**——日期 31 Mar 2027 啱，但 (ii) 判斷錯（Jan 2027 早過 31 Mar 2027 → 係 **within time**，佢答 no）、(iii) 條文估咗 s.27。清除咗一星期就流失 | 條文背誦/回忘 | "Under s.60(1) IRO, an additional assessment must be raised within 6 years after the end of the YA. Discovery BEFORE that deadline = within time (yes)." 證明保溫機制係啱嘅——呢條唔可以畀佢走甩 |
| 10/7 | 保溫卷W2 | Q1：s.60(1) **第六次終於全對** 🎉——31 March 2026 + No（out of time 反向題）+ s.60(1) 三寶齊。Q5：consignment **回忘**——用咗 10%（正確 **1%**）＋條文估 s.15(5)（正確 **s.20A(3)**）；W1 本來答啱，一星期後流失。正確：15,000,000 × 1% = **150,000** | 條文背誦/回忘 | "Under s.20A(3), where actual profits cannot be readily ascertained, assessable profits are deemed to be 1% of the gross proceeds from sales to Hong Kong customers." 1% 唔係 10%；consignment 呢個數字要默到反射 |
| 10/7 | 保溫卷W3 | Q2：rental value **回忘**——揀咗 actual rent 300,000（正確 10% of income = **72,000**，s.9(2)）。Q4：capital/revenue **回忘**——sole distribution agreement 終止都答 revenue（正確 **capital**：sterilisation of entire profit-making structure）。Q5：MPF 答咗每月 1,500＋條文 s.9（正確**全年 18,000**，**s.26G**）。Q1 consignment 80,000 ✅ 清除、Q3 AVD/BSD ✅ | 概念回忘 | "Rental value under s.9(2) is 10% of income from the employer — never the actual rent paid." / "Compensation for terminating a sole agreement representing substantially the whole business is CAPITAL." / "MPF deduction cap: HK$18,000 per YEAR (s.26G)." 三條已清除項目同晚回忘——間隔重複要加密 |
| 10/9 | 保溫卷W4 | Q1 rental value 60,000 + s.9(2) ✅、Q2 五份協議之一 → revenue ✅（反向題都啱）、Q3 MPF 18,000 ✅（條文寫 s.26——下次寫全 s.26G）、Q4 s.60(1) 31 Mar 2027 + Yes ✅（第七次交手，連續第二次全對）。Q5：DIPN 21 **回忘**——誤讀 "performed entirely in Hong Kong"（以為係唔喺香港做），答咗 a no tax；正解 c：deemed 2/3 × 2.4m = 1.6m × **8.25%**（公司）= **132,000** | 審題/條文回忘 | "Under DIPN 21, fees for services performed IN Hong Kong paid to a non-resident are deemed taxable at 2/3 of the gross fee — 8.25% for corporations, 7.5% for individuals." 題目關鍵字要圈低：performed **in** Hong Kong = 課稅 |
| 10/13 | 保溫卷W5 | **5/5 全對** 🎯：DIPN 21 公司版 165,000 ✅（即晚斬殺）、SSD 20% ✅、股票印花稅 gift 市值 ✅、donations 175,000 + s.26C ✅、s.8(1A)(b)(ii) 全離港豁免 ✅ | ✅ 全對 | 首份滿分保溫卷。小疵：Q1 冇寫 governing authority（要寫 DIPN 21）；Q2 括號 (0%,15%,10%) 寫錯——三檔係 20/15/10 |
| 10/13 | 保溫卷W6 | Q1：s.60(1) **fraud 支線失守**——題目講明 wilful evasion，應用十年檔 **31 March 2032**，佢用咗六年檔 2028（(ii) yes 同 (iii) s.60(1) 啱）。Q2 96,000 啱但條文寫 s.26(G)（應 **s.9(2)**）；Q3 60,000 啱但條文寫 s.20(4) 仲話「i guess」（應 **s.20A(3)**）；Q4 ✅、Q5 ✅ | 條文背誦 | "Fraud or wilful evasion extends the s.60(1) time limit to 10 years after the end of the YA." 金額啱條文亂 = 假熟——條文編號都要默 |
| 10/14 | 保溫卷W7 | **5/5 全對** 🎯：s.60(1) fraud out-of-time 變種全對（31 Mar 2025 + No + s.60(1)）、rental value 84,000 + **s.9(2)**（條文終於寫準）、NAV 720,000/720,000、premium 攤分 30,000、office 來源 UK 全中 | ✅ 全對 | 第二份滿分保溫卷；條文默寫起效 |
| 10/14 | 保溫卷W8 | Q1 s.60(1) 邊界日全對（issue 日＝死線日 → in time）✅、Q2 AVD+BSD 3.6m ✅、Q4 capital/revenue ✅。Q3：股票印花稅用咗 0.026（離譜）→ 26,000（正確 0.1% = 1,000 + IoT 5 = **1,005**）。Q5：time apportionment **方向倒轉**——乘咗 73/365（離港日數）得 240,000（正確乘 292/365 = **960,000**），仲以為 time apportionment 係畀非香港僱員用 | 概念不清/數字亂 | "Stamp duty on a share transfer = 0.1% on the contract note + fixed HK$5 on the IoT." / "Time apportionment: assessable income = income × days in HK ÷ 365 — multiply by the HONG KONG days, not the days outside." |
| 10/15 | 保溫卷W9 | Q1：股票印花稅 **2nd strike**——上次 0.026、今次 0.01（1%）→ 5,005（正解 **505**：500,000 × 0.1% + IoT 5）。兩次錯法唔同 = 「0.1%」呢個率根本未入腦。Q2 time apportionment ✅（547,500，清除）、Q3 s.60(1) ✅（31 Mar 2027 + Yes）、Q4 education benefit ✅（b，Glynn）、Q5 SSD 剛剛 12 個月 ✅（b，15%）| 公式背誦 | "Stamp duty on a share transfer = 0.1% on the contract note plus a fixed HK$5 on the instrument of transfer — 0.1%, not 1%." 處方：默寫「0.1% + HK$5」二十次；再錯罰抄五十次 |

## 答案卡更正紀錄 (Errata)

| 日期 | 位置 | 更正 |
|---|---|---|
| 8/22 | M9 Ch1 Answers Q4 | 標準答案加總筆誤：HK$165,000 + HK$495,000 應為 **HK$660,000**（原寫 HK$742,500），已修正 |
| 10/9 | M7 Ch11 Quiz Q5 | 答案卡 ROI = 15% 係**算術錯誤**：1,000,000 ÷ 4,000,000 = 0.25 → 正確 **25%**。考生答 25% 係啱，已更正網站答案卡 |

## 🔄 Active Retest Queue（錯題重測隊列）

> 規則（你提議嘅版本，已採納）：答錯嘅題目 → 下一週 Quiz 嘅 Retest Section 出一條**新場景同理論**嘅題。**答啱 → 剔除出隊列；答錯 → 繼續帶落下週。**

| 錯題來源 | 弱點 | 狀態 |
|---|---|---|
| M7 Ch2 Q1 | 短期 vs 長期融資 1-year boundary | ✅ 已剔除（9/21 R1）|
| M7 Ch2 Q3 | PIPE vs 其他集資渠道 | ✅ 已剔除（9/21 R2）|
| M7 Ch3 Q4 | EAR 公式 | ✅ 已剔除（9/23 R4：8.24%）|
| M7 Ch3 Q3 | 永續年金比較要計 PV | ✅ 已剔除（9/23 R12：有寫低兩個 PV 先揀）|
| M7 Ch4 Q1 | 溢價/折價債券 yield 排名 | ✅ 已剔除（9/23 R13）|
| M7 Ch4 Q2 | 債券價格波動性定理 | ✅ 已剔除（9/23 R14）|
| M7 Ch4 Q4/Q5 | 半年複利債券計價 + 常識檢查 | ✅ 已剔除（9/23 R15：932.67，有做 sanity check）|
| M7 Ch2 Q4 | BEY 公式背誦 | ✅ 已剔除（9/25 R16：6.45%，第五次過關）|
| M9 Ch2 Q5 | s.60(1)：普通 6 年、**fraud/wilful evasion = 10 年**（proviso）| ✅ 已剔除（10/14 W7 Q1：fraud out-of-time 變種全對——31 March 2025 + No + s.60(1)，一日即斬）|
| M9 保溫卷 W8 Q3 | 股票轉讓印花稅：contract note **0.1%**（2023 起）＋ IoT **fixed HK$5** | 🔁 **2nd strike**（10/15 W9 Q1：又用錯率——0.01（1%）→ 5,005；正解 500,000 × 0.1% + IoT 5 = **505**）→ 帶落保溫卷 W10 |
| M9 保溫卷 W8 Q5 | Time apportionment（s.8(1A)(a)）：應課稅 = 收入 × **留港日數**/365 | ✅ 已剔除（10/15 W9 Q2：912,500 × 219/365 = **547,500** 全對，留港日數方向啱返）|
| M9 保溫卷 W2 Q5 | consignment：s.20A(3) = **1%** of HK-customer gross proceeds | ✅ 已剔除（10/7 W3 Q1：80,000 啱；條文寫 s.20(A)——下次寫全 **s.20A(3)**）|
| M9 Ch4 Q4（W3 Q2）| rental value = **10% of income**（s.9(2)），唔係實際租金 | ✅ 已剔除（10/9 W4 Q1：60,000 + s.9(2) 全對）|
| M9 Ch3 Q1（W3 Q4）| capital vs revenue：**sole** = capital；眾多中一份 = revenue | ✅ 已剔除（10/9 W4 Q2：五份協議之一 → revenue，反向題啱）|
| M9 保溫卷 W3 Q5 | MPF 全年 cap 18,000（s.26G）| ✅ 已剔除（10/9 W4 Q3：24,000 > cap → 18,000 啱；條文寫 s.26，下次寫全 **s.26G**）|
| M9 Ch3 Q3（W4 Q5）| DIPN 21：服務**喺香港** performed → deemed 2/3 課稅；公司 8.25%、個人 7.5% | ✅ 已剔除（10/13 W5 Q1：3m×2/3×8.25% = **165,000** 即晚斬殺；冇寫 governing authority，下次寫 DIPN 21）|
| M7 Ch12 Q3 | Relevant cost：sunk costs 同唔變嘅 absorbed fixed OH 一律**唔相關** | ✅ 已剔除（10/13 R53：揀 C 排除 absorbed fixed OH，一take過）|
| M7 Ch12 Q4 | Cost-plus with ROI：利潤**只加一次** | ✅ 已剔除（10/14 R55：cost/unit 120 + profit/unit 15 = **135** 全對，第三次過關）|
| M7 Ch13 Q4 | NPV：NWC 期初出、期末收回折現加返 | ✅ 已剔除（10/14 R56：+**11,382** accept 全對——NWC 兩頭啱，第二次過關）|
| M7 Ch13 Q5 | Discounted payback：逐年折現累積＋插值 | ✅ 已剔除（10/14 R57：累積表全齊，4+19,616/74,511=**4.26 years** 全對，第二次過關）|
| M9 Ch3 Q1 | capital vs revenue receipt 邊界 | ✅ 已剔除（9/30 R22：唯一零售舖 = capital，第四次過關）|
| M9 Ch3 Q3 | DIPN 21：買或賣其中一份喺香港 effected = 全數課稅 | ✅ 已剔除（9/28 R9）|
| M9 Ch3 Q5 | fine 必 add back；DA 喺 assessable profits 步驟扣 | ✅ 已剔除（9/28 R10）|
| M9 Ch4 Q1 | 收入來源三規則：employment 睇服務地 / office 睇管理控制地 / 政府退休金全課 | ✅ 已剔除（9/29 R19）|
| M9 Ch4 Q2 | s.8(2)(j) 機組人員雙重門檻 | ✅ 已剔除（9/29 R20）|
| M9 Ch4 Q4 | rent-free flat 必加 rental value 10%（條文係 **s.9(2)**，唔係 s.9(1)）| ✅ 已剔除（10/6 R35：45,000 + s.9(2)，**第五次終於全對**）|
| M9 Ch5 Q4 | 頂手費攤分 s.5B(4)：攤分期包括免租月 | ✅ 已剔除（9/30 R24：198,000）|
| M9 Ch5 Q5 | 暫繳稅對銷：final − 已繳暫繳 + 下年暫繳 | ✅ 已剔除（9/30 R25：39,000）|
| M9 Ch6 Q4 | PA 下租金必轉 NAV（×80%）；按揭利息封頂 NAV | ✅ 已剔除（10/6 R30：400,000 / 380,000 全扣）|
| M9 Ch6 Q5 | PA 計算要計到最後稅款；夫婦用 married person's allowance | ⚠️ 已剔除（10/5 R28：稅款 12,000 啱；概念跟進併入 R30 ✅）|
| M9 Ch7 Q2 | AVD Scale 2 睇首置（名下無其他住宅）；BSD 只睇 HKPR 身份 | ✅ 已剔除（10/6 R36：首置 HKPR → Scale 2 + 免 BSD，第三次過關）|
| M9 Ch7 Q3 | 股票印花稅：issue 唔課、gift 課（市值）、IoT 固定 HK$5 | ✅ 已剔除（10/6 R32）|
| M9 Ch7 Q4 | SSD 三檔：≤6m 20%、6–12m 15%、12–36m 10%；按較高者計 | ✅ 已剔除（10/6 R33：10% × 4.2M = 420,000）|
| M7 Ch7 Q5 | WACC = (E/V)kₑ + (D/V)k_d(1−t)；kₑ = D₁/P₀ + g | ✅ **已剔除（10/9 R46：5.675%，第五次終於全對**——kₑ 8.15%、k_d(1−t) 3.2%、50/50 權重全齊 🎉）|
| M7 Ch8 Q1 | MM Prop 1（零稅）：發債回購**不改變公司價值**，但推高剩餘股權要求回報 | ✅ 已剔除（10/7 R39：概念題一take過）|
| M7 Ch8 Q4 | MM Prop 2 三步：V=CF÷k₀ → E=V−D → ke=k₀+(D/E)(k₀−kd) | ✅ 已剔除（10/9 R47：11.33%，三步全齊，第四次過關）|
| M7 Ch8 Q5 | VL = VU + Tc×D；shield 用 **T_c** 唔係 (1−t) | ✅ 已剔除（10/13 R51：V_U=7.5m + 0.25×2.5m = **8,125,000** 全對，第五次過關 🎉）|
| M7 Ch9 Q5 | CCC：日數 = 365 **÷** turnover | ✅ 已剔除（10/9 R49：DIO 20 / DSO 20 / DPO 25 → 15 days 全對，第三次過關）|
| M7 Ch10 Q5 | **EFN = ΔA − ΔAP − retained**；NI 用**總預測銷售**計；retained 係**減** | ✅ 已剔除（10/13 R52：**427,200** 全對——ΔA 1.32m、ΔAP 288,000、NI 1,008,000、retained 604,800，第三次過關 🎉）|
| M9 Ch8 Q4 | 兩級制稅率：個人/unincorporated = 7.5%，公司 = 8.25% | ✅ 已剔除（10/6 R37：800,000 × 7.5% = 60,000，一take過）|

狀態圖例：🔁 隊列中（待重測）｜ ✅ 已剔除（重測答啱）

> ⚠️ **保溫機制（10/6 起，你提議嘅版本）**：**每次提交 M7 Quiz 答案 → 即刻出一份新「M9 保溫卷」**（5 題、6 分鐘閉卷，抽自已清除錯題，新場景同理論）。**保溫卷答錯 = 即刻重返上面嘅 Active Queue，並帶落下一份保溫卷**，答啱先維持剔除。

## 快問快答遺忘點 (Spaced Repetition)

| 日期 | 抽考範圍 | 得分 | 遺忘點 |
|---|---|---|---|
| 8/19 | M7 Ch1 對話微測（money market / primary vs secondary / broker vs dealer）| 2/3 | broker ≠ shareholder 混淆 → 已即場糾正並加入詞彙表 |
| 8/22 | W2 前 Retest（M7 profit maximisation timing / EMH 嵌套 / M9 no-WHT rule，全部新場景）| **3/3** ✅ | 無 — W1 三個錯點已鞏固；下次 W3 前再抽考驗證長期記憶 |
| 9/21 | M7 Ch3 Quiz（主卷 5 題 + Retest R1–R3）| 主卷 **3/5**、Retest **2/3** | EAR/BEY 公式閉卷失憶（BEY 連續第二次）；永續年金比較靠感覺唔計數 → 三項已注入 W4 R4–R6 |
| 9/22 | M9 Ch3 Quiz（主卷 5 題 + Retest R1）| 主卷 **2/5**、Retest **0/1** | s.60(1) 第三次未過關（冇日期冇條文）；capital/revenue 同 DIPN 21 兩個概念邊界失守；Q5 漏 fine add-back + DA 擺錯步驟 → 四項注入 M9 Ch4 R7–R10 |
| 9/23 | M7 Ch4 Quiz（主卷 5 題 + Retest R4–R6）| 主卷 **1/5**、Retest **1/3** | EAR 終於過關 ✅；BEY 第三次錯 + 永續年金第二次錯；債券兩條定理調轉；半年複利冇換算；零常識檢查 → 五項注入 M7 Ch5 R11–R15 |
| 9/23 | M7 Ch5 Quiz（主卷 5 題 + Retest R11–R15）| 主卷 **5/5** 🎯、Retest **4/5** | 四條舊債一日清晒（永續年金/排名/波動/計價全部答啱，有寫 PV、有做 sanity check）；唯獨 BEY 第四次錯、三寶全錯 → R16 帶落 Ch6 |
| 9/25 | M7 Ch6 CAPM Quiz（主卷 5 題 + Retest R16）| 主卷 **5/5** 🎯、Retest **1/1** | 無新增錯點——BEY 惡魔第五次嘗試終於斬殺（6.45%，三寶齊全）✅；M7 隊列全清。小疵：Q3/Q5 計數過程有冗餘步驟（見批改報告），答案啱但考試會蝕時間 |
| 9/28 | M9 Ch4 Salaries Tax Quiz（主卷 5 題 + Retest R7–R10）| 主卷 **2/5**、Retest **2/4** | DIPN 21 ✅、fine add-back ✅ 兩條舊債清；但 s.60(1) 第四次錯（日期啱條文唔記得）、capital/revenue 第二次錯；主卷新增三錯：來源規則 (IV) 誤判、s.8(2)(j) 漏咗第二關、Q4 漏 rental value → 五項注入 M9 Ch5 R17–R21 |
| 9/29 | M9 Ch5 Property Tax Quiz（主卷 5 題 + Retest R17–R21）| 主卷 **3/5**、Retest **3.5/5** | s.60(1) 第五次終於過關 ✅、來源規則 ✅、s.8(2)(j) ✅；capital/revenue 第三次錯、R21 又漏條文；主卷漏頂手費攤分 + 暫繳稅對銷方向錯 → 四項注入 M9 Ch6 R22–R25 |
| 9/30 | M9 Ch6 Personal Assessment Quiz（主卷 5 題 + Retest R22–R25）| 主卷 **3/5**、Retest **3/4** | capital/revenue 第四次終於過關 ✅、premium 攤分 ✅、暫繳稅對銷 ✅；但 rental value 第二次錯（搬咗 property tax 邏輯 + 寫錯 s.5）；主卷 Q4/Q5 兩條 PA 計算都衰喺冇將租金轉 NAV + 利息冇封頂，Q5 仲計到一半冇計稅款 → 三項注入 M9 Ch7 R26–R28 |
| 10/5 | M9 Ch7 Stamp Duty Quiz（主卷 5 題 + Retest R26–R28）| 主卷 **1/5** ⚠️、Retest **1/3** | R28 稅款計啱（12,000）✅；rental value 第三次錯（答錯數量 + 條文寫 s.14）、NAV 題乘多咗 0.15；主卷係災難：AVD/BSD 雙重標準、股票印花稅、SSD 三檔全錯，Q5 組件啱但加法計錯 → 五項注入 M9 Ch8 R29–R33 |
| 10/5 | M7 Ch7 Cost of Capital Quiz（主卷 5 題，M7 隊列清零後首份純主卷）| 主卷 **4/5** | Q1–Q4 全對（市值權重、YTM 稅盾、risk-adjusted WACC、兩層 WACC 11.38%）；Q5 三層 WACC 失手：權重用股數唔係市值 + DGM 公式走樣 → 注入 M7 Ch8 R34 |
| 10/6 | M9 Ch8 Cross-border Quiz（主卷 5 題 + Retest R29–R33）| 主卷 **4/5**、Retest **3/5** | NAV ✅、IoT HK$5 ✅、SSD 三檔 ✅ 三條清；rental value 第四次半對（s.9(1)≠s.9(2)）、AVD/BSD 第二次錯；主卷 Q4 兩級制用錯公司稅率（個人應 7.5%）→ 三項注入 M9 總複習 Quiz R35–R37。M9 全部 8 章主卷完成 ✅ |
| 10/6 | M9 總複習錯題清債卷（R35–R37）| **3/3** 🎯 | **M9 錯題隊列 100% 清零** 🎉——rental value 第五次（s.9(2) 連 subsection 都啱）、AVD/BSD 第三次（首置→Scale 2 反向題都啱）、兩級制個人 7.5% 一take過。M9 正式進入複習階段 |
| 10/6 | M9 保溫卷 W1（5 題抽自已清除錯題）| **4/5** | capital/revenue ✅、rental value + s.9(2) ✅、SSD 15% ✅、consignment 1% ✅ 全部企穩；**但 s.60(1) 回忘**——within-time 判斷錯 + 條文估 s.27 → 重返隊列，帶落 W2 |
| 10/7 | M7 Ch8 Capital Structure Quiz（主卷 5 題 + Retest R34）| 主卷 **2/5** ⚠️、Retest **0/1** | **閉卷公式災難**：R34 WACC 三度失憶（答 25.01%，正解 9.03%）；Q4/Q5 MM 公式「forgot the formula」×2；Q1 MM Prop 1 概念錯（以為平價發債提高股價）。唯二得分：Q2 MM 假設、Q3 最優資本結構概念 → 四項注入 M7 Ch9 R38–R41；處方：每日默寫三公式 |
| 10/7 | M9 保溫卷 W2 已出（觸發：M7 Ch8 提交）| **4/5** | **s.60(1) 第六次終於全對** 🎉（31 March 2026 + No + s.60(1)，反向 out-of-time 題都啱）；DIPN 21 個人 7.5% ✅、NAV 封頂 480,000 ✅、SSD 10% ✅；唯 consignment 回忘（10% + s.15(5)）→ 重返隊列帶落 W3 |
| 10/7 | M7 Ch9 Financial Analysis Quiz（主卷 5 題 + Retest R38–R41）| 主卷 **4/5**、Retest **1/4** | R39 MM Prop 1 概念 ✅ 清除；R38 市值權重終於啱但乘銀碼（第 3 次）、R40 當咗 WACC 計（第 2 次）、R41 亂砌（第 2 次）→ R42–R44 帶落 Ch10；主卷 Q1–Q4 全對（P/B、DuPont 12%、EBIT ROA、current 1.60/quick 0.80）；Q5 CCC 公式唔識（23.23 vs 45）→ R45 |
| 10/9 | M9 保溫卷 W3（觸發：M7 Ch9 提交）| **2/5** ⚠️ | consignment 80,000 ✅ 清除（條文寫 s.20(A)，下次寫全 s.20A(3)）、AVD/BSD ✅；**三條已清除項目同晚回忘**：rental value 揀 actual rent、sole agreement 補償答 revenue、MPF 答每月 1,500 + s.9 → 三條全部重返隊列帶落 W4 |
| 10/9 | M7 Ch10 Financial Forecasts Quiz（主卷 5 題 + Retest R42–R45）| 主卷 **4/5**、Retest **0/4** ⚠️ | 主卷 Q1–Q4 全對（notes payable、FCF 唔包利息、EBITDA/EBIT break-even、FCF=1,400,000）；Q5 EFN 只計 ΔA → R50。Retest 公式繼續失守：R42 kₑ 啱但組裝錯（第 4 次）、R43/R44 MM 兩條（第 3 次）、R45 CCC 分數倒轉（第 2 次）→ R46–R49 注入 Ch11 |
| 10/9 | M9 保溫卷 W4 | **4/5** | rental value ✅、capital/revenue 反向題 ✅、MPF ✅（s.26→寫全 s.26G）、s.60(1) 第七次交手連續第二次全對 ✅；DIPN 21 公司版回忘（誤讀題目）→ 帶落 W5 |
| 10/9 | M7 Ch11 SMA Quiz（主卷 5 題 + Retest R46–R50）| 主卷 **5/5** 🎯、Retest **3/5** | 主卷全對（EOQ、external failure、SMA、target cost 199.20、ROI 25%——答案卡 15% 係 errata，考生啱）；**R46 WACC 第五次終於過關** 🎉、R47 MM2 第四次過關、R49 CCC 第三次過關；R48 shield 用錯 0.7（第 4 次）、R50 EFN NI 用錯 ΔS＋retained 變加（第 2 次）→ R51/R52 注入 Ch12 |
| 10/13 | M9 保溫卷 W5 | **5/5** 🎯 | 首份滿分保溫卷——DIPN 21 公司版即晚斬殺 ✅，四條輪轉全中。**M9 錯題隊列再次清零** 🎉 |
| 10/13 | M7 Ch12 Pricing Quiz（主卷 5 題 + Retest R51–R52）| 主卷 **3/5**、Retest **2/2** 🎯 | **R51 MM-with-tax 第五次過關 ✅、R52 EFN 第三次過關 ✅——M7 舊公式債全部清零** 🎉；主卷 Q3 relevant cost 概念錯 + Q4 cost-plus 漏 manufacturing OH → R53/R54 注入 Ch13 |
| 10/13 | M9 保溫卷 W6 | **4/5** | SSD ✅、DIPN 21 個人版 ✅；**s.60(1) fraud 支線失守**（十年檔 → 帶落 W7）；rental value/consignment 金額啱但條文亂寫（s.26(G)、s.20(4)「i guess」）——條文編號列入默寫範圍 |
| 10/13 | M7 Ch13 Investment Appraisal Quiz（主卷 5 題 + Retest R53–R54）| 主卷 **3/5**、Retest **1/2** | R53 relevant cost ✅ 清除；R54 cost-plus 雙重計利潤（第 2 次）→ R55；主卷 Q1–Q3 概念全對（mutually exclusive 揀 NPV、sunk/opportunity 分類、discounted vs simple payback）；Q4 NPV NWC 兩頭錯 → R56；Q5a discounted payback 唔識逐年累積法 → R57 |
| 10/14 | M9 保溫卷 W7 | **5/5** 🎯 | 第二份滿分保溫卷——s.60(1) fraud 支線一日即斬、條文全部寫準。**M9 隊列維持清零** |
| 10/14 | M7 Ch14 Post-Appraisal Quiz（主卷 5 題 + Retest R55–R57）| 主卷 **5/5** 🎯、Retest **3/3** 🎯 | 完美之夜：R55 cost-plus ✅、R56 NPV/NWC ✅、R57 discounted payback ✅——**M7 錯題隊列再次清零**；主卷全對（post-completion audit 目的、continuous measurement、sunk cost fallacy、CPI 0.80、SPI 0.75 late）|
| 10/14 | M9 保溫卷 W8 | **3/5** | s.60(1) 邊界日 ✅、AVD/BSD ✅、capital/revenue ✅；**股票印花稅 0.026 離譜**（正解 1,005）＋ **time apportionment 方向倒轉**（乘錯離港日數，240,000 vs 960,000）→ 兩條帶落 W9 |
| 10/14 | M7 Ch15 Performance Measurement Quiz（純主卷 5 題）| 主卷 **5/5** 🎯 | ROI/RI goal congruence、BSC 四維度、lagging measures、ROI 24%+RI 150,000、EVA 1,000,000 全對；M7 隊列維持清零 |
| 10/14 | M9 保溫卷 W9 已出（觸發：M7 Ch15 提交）| 待做 | 帶落題 ×2：股票印花稅（500,000 → 505）、time apportionment（912,500 × 219/365 = 547,500）；輪轉：s.60(1)、education benefit（Glynn）、SSD 邊界 12 個月 |
| 10/15 | M9 保溫卷 W9 | **4/5** | time apportionment ✅ 清除（547,500）；**股票印花稅 2nd strike**——上次 0.026 今次 0.01 → 5,005（正解 505）→ 帶落 W10；處方：默寫「0.1% + HK$5」二十次 |
| 10/15 | M7 Ch16 Financial Risks Quiz（純主卷 5 題）| 主卷 **5/5** 🎯 | financial risk 分類、風險對策配對、political risk + natural hedge、LTV 70.0%、630,000 全對——**M7 全部 16 章主卷完成** 🎉；M7 進入總複習＋計時操卷階段 |
| 10/15 | M9 保溫卷 W10 已出（觸發：M7 Ch16 提交）| 待做 | 帶落題 ×1：股票印花稅第 3 次交手（2,000,000 → 2,005）；輪轉：s.60(1) 六年檔（YA 2018/19）、rental value s.9(2)、SSD 40 個月（0%）、MPF cap s.26G |
