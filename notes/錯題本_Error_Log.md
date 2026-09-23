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
| M9 Ch2 Q5 | additional assessment 要答日期 + 條文編號 | 🔁 未過關（9/22 R1 第三次錯）→ 帶落 M9 Ch4 R7 |
| M9 Ch3 Q1 | capital vs revenue receipt 邊界 | 🔁 新增 → 已放入 M9 Ch4 Quiz R8 |
| M9 Ch3 Q3 | DIPN 21：買或賣其中一份喺香港 effected = 全數課稅 | 🔁 新增 → 已放入 M9 Ch4 Quiz R9 |
| M9 Ch3 Q5 | fine 必 add back；DA 喺 assessable profits 步驟扣 | 🔁 新增 → 已放入 M9 Ch4 Quiz R10 |

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
