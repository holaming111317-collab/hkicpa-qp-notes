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

## 答案卡更正紀錄 (Errata)

| 日期 | 位置 | 更正 |
|---|---|---|
| 8/22 | M9 Ch1 Answers Q4 | 標準答案加總筆誤：HK$165,000 + HK$495,000 應為 **HK$660,000**（原寫 HK$742,500），已修正 |

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
| M7 Ch2 Q4 | BEY 公式背誦 | 🔁 未過關（9/23 R11 **第四次**錯：三寶全錯）→ 帶落 M7 Ch6 R16 |
| M9 Ch2 Q5 | additional assessment 要答日期 + 條文編號 | ✅ 已剔除（9/29 R17：31 March 2027 + s.60(1) 齊，第五次過關）|
| M9 Ch3 Q1 | capital vs revenue receipt 邊界 | 🔁 未過關（9/29 R18 **第三次**錯：問 REVENUE 揀咗 capital）→ 帶落 M9 Ch6 R22 |
| M9 Ch3 Q3 | DIPN 21：買或賣其中一份喺香港 effected = 全數課稅 | ✅ 已剔除（9/28 R9：sale contract effected in HK → fully chargeable）|
| M9 Ch3 Q5 | fine 必 add back；DA 喺 assessable profits 步驟扣 | ✅ 已剔除（9/28 R10：fine not deductible 答啱）|
| M9 Ch4 Q1 | 收入來源三規則：employment 睇服務地 / office 睇管理控制地 / 政府退休金全課 | ✅ 已剔除（9/29 R19）|
| M9 Ch4 Q2 | s.8(2)(j) 機組人員雙重門檻：≤60 日本年 + ≤120 日兩年合計 | ✅ 已剔除（9/29 R20）|
| M9 Ch4 Q4 | rent-free flat 必加 rental value 10%（s.9(2)）| 🔁 半對（9/29 R21：10% 計啱但條文唔記得）→ 帶落 M9 Ch6 R23 |
| M9 Ch5 Q4 | 頂手費攤分 s.5B(4)：攤分期包括免租月 | 🔁 新增 → 已放入 M9 Ch6 Quiz R24 |
| M9 Ch5 Q5 | 暫繳稅對銷：final − 已繳暫繳 + 下年暫繳 | 🔁 新增 → 已放入 M9 Ch6 Quiz R25 |

狀態圖例：🔁 隊列中（待重測）｜ ✅ 已剔除（重測答啱）

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
