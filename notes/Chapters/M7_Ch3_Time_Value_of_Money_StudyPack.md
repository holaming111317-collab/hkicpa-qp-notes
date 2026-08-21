# M7 Time Value of Money and Investing Basics — Study Pack (Week 3)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構

- 利息（Interest）分為兩大類：單利（Simple Interest）只按本金（Principal）計息；複利（Compound Interest）按「本金＋已累積利息」計息，時間越長差距越大。大多數商業情況都用複利，單利一般只用於一年或以內的短期情況。
- 金錢的時間價值（Time Value of Money, TVM）：「One dollar today is always worth more than one dollar tomorrow」。未來值（Future Value, FV）靠複利滾存（compounding）得出；現值（Present Value, PV）靠折現（discounting）得出，是估值債券、應付票據、租賃負債及資本預算的基礎。
- 等額現金流（Level Cash Flows）：年金（Annuity）為有限期等額現金流，分普通年金（Ordinary Annuity，期末收付）與期初年金（Annuity Due，期初收付）；永續年金（Perpetuity）則永遠持續（如 preference shares 固定股息、Consols）。
- 固定增長現金流（Constant Growth Cash Flows）：增長年金（Growing Annuity）有終點 n；增長永續（Growing Perpetuity）無終點，公式成立前提是 k > g。
- 年化利率（Annualised Interest Rates）：名義年利率（Annual Percentage Rate, APR）不考慮複利；實際年利率（Effective Annual Rate, EAR，又稱 annual percentage yield）考慮複利，才是做融資決策時應用的真實利率。複利頻率越高，EAR 越高。

### 2. 必背考點清單（核心公式與應用條件）

| 名稱 | 公式 | 變量定義 | 應用條件／備註 |
|---|---|---|---|
| Simple Interest | Interest = P × i × n | P = principal; i = interest rate; n = time | 只按初始本金計息；常見於 ≤1 年短期情況 |
| Compound Interest | Interest = P × (1 + i/n)^(nt) | P = principal; i = interest rate; n = 每年複利次數; t = 年數 | 利息滾入本金再計息；大多數商業情況適用 |
| Future Value (FV) | FV = P × (1 + i)^n | P = principal; i = 每期利率; n = 期數 | 單筆金額經複利滾存後的未來價值 |
| Present Value (PV) | PV = FV / (1 + i)^n | FV = 未來金額; i = 折現率; n = 期數 | 「discounting」；PV 取決於三變量：未來金額、期數、折現率 |
| PV of Ordinary Annuity (PVAn) | PVAn = CF × [1 − 1/(1+i)^n] / i | CF = 等額等距現金流; i = 折現率; n = 期數 | 現金流在**每期期末**收付 |
| FV of Ordinary Annuity (FVAn) | FVAn = CF × [(1+i)^n − 1] / i | 同上 | 同上；用於定期儲蓄／退休計劃終值 |
| Annuity Due 關係 | PV(due) = PV(ordinary) × (1+i)；FV(due) = FV(ordinary) × (1+i) | — | 現金流提前一期、折現較少 → PV 及 FV 均大於普通年金（來源例：4 期 HK$1,000 @8%：ordinary PV = HK$3,312；due PV = HK$3,577） |
| PV of Perpetuity (PVP) | PVP = CF / i | CF = 每期現金流; i = 利率 | **首期於一年後**支付；若首期即時支付（perpetuity due）：PVP = CF/i + CF |
| PV of Growing Perpetuity | PV0 = PMT1 / (k − g) | PMT1 = 一年後首期付款; k = effective annual rate; g = 增長率 | **僅當 k > g 時成立**，否則答案為負、無意義；增長率須永久維持不變 |
| PV of Growing Annuity | PV0 = [PMT1 / (k − g)] × [1 − ((1+g)/(1+k))^n] | n = 終止期 | 同上，k > g 且增長率於整段年金期內不變 |
| Effective Annual Rate (EAR) | EAR = (1 + i/m)^m − 1 | i = 名義利率 (APR); m = 每年複利期數 | APR 與 EAR 只有在**每年複利一次**時才相等；複利越頻密 EAR 越高 |
| Annual Percentage Rate (APR) | APR = 每期實際利率 × 一年內期數 | 如 1.5%/月 × 12 = 18% | 不含複利效果（nominal rate）；不能直接用於財務決策 |

**來源關鍵數字（24% APR 下不同複利頻率的 EAR）**：semi-monthly 26.97% > monthly 26.82% > bi-monthly 26.53% > quarterly 26.25% > semi-annually 25.44% > annually 24.00%。

**折現率選擇**：評估「平均風險」項目可用 WACC（weighted average cost of capital，公司額外長期融資的稅後成本）；若項目風險異於公司一般項目，須調整折現率（風險較高 → 用較高折現率），否則會作出錯誤的投資決定。

「考試貼士」：多重現金流 FV/PV 題，記住三步曲 — ① 畫 timeline；② 逐筆計 FV（或 PV）；③ 加總。見到「beginning of each period / first payment immediately」即屬 annuity due / perpetuity due，要乘 (1+i) 或加 CF。

### 3. 易混淆概念對比 (Common Pitfalls)

**Pitfall 1 — Ordinary Annuity vs Annuity Due（期末 vs 期初收付）**
- 對比：Ordinary Annuity 的等額現金流在每期**期末**（end of each period）收付；Annuity Due 在每期**期初**（beginning of each period）收付，首期即時發生（如租金，入住即付第一期）。
- 澄清例子：同樣 4 期、每期 HK$1,000、8% 折現率 — Ordinary Annuity 的 PV = HK$3,312；Annuity Due 的 PV = HK$3,577。因為 Annuity Due 的現金流整體提前一期、折現較少，所以 PV（及 FV）必然較大。考試見題目講「first payment today / immediately」就要用 due 版本，否則會選錯 ordinary annuity 的答案。

**Pitfall 2 — APR (Nominal Rate) vs EAR（名義利率 vs 實際年利率）**
- 對比：APR 是把每期利率簡單乘以期數（例如每月 1.5% × 12 = 18%），**完全不含複利效果**；EAR = (1 + i/m)^m − 1，把期內「利疊利」計算在內，代表真實借貸成本（true cost of borrowing），財務決策必須用 EAR。
- 澄清例子：信用卡報價 APR 24%，若每月複利（2%/月），EAR = (1.02)^12 − 1 = 26.82%；若 semi-monthly 複利（1% × 24），EAR = 26.97%。只有每年複利一次時 APR = EAR。同一 APR 下複利越頻密，借款人實際付出越多 — 這正是信用卡公司的賺錢伎倆。

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): What is the difference between simple interest and compound interest, and when is each typically used?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Simple interest = P × i × n; calculated only on the initial principal; the same amount of interest every period.
      - Compound interest = P × (1 + i/n)^(nt); calculated on principal plus previously accrued interest; unpaid interest converts into new principal.
      - Simple interest: typically short-term situations of one year or less. Compound interest: most business situations.
    - [中文白話解釋]: 單利每期利息固定，因為永遠只按最初本金計；複利每期把未提取的利息滾入本金再計息，所以利息會越滾越大，年期越長兩者差距越誇張（來源例：HK$100 million @10%、20 年，單利終值 HK$300m，複利終值 HK$672.6m）。記住：現實商業世界幾乎全用複利，單利只見於一年內的短期安排。

* [Flashcard 2]
  - Front (Question in English): You deposit HK$100 in a bank account paying 10% per year, compounded annually. What is the future value at the end of year 3?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - FV = P × (1 + i)^n = 100 × (1.10)^3
      - = 100 × 1.331 = HK$133.10
      - (1.10)^3 can also be read from the future value table: factor 1.33100 for n = 3, i = 10%.
    - [中文白話解釋]: 計 FV 就是將本金乘 (1+i) 的 n 次方。呢度 10% 複利滾 3 年，100 蚊變 133.10 蚊。考試可以用公式直接計，或者用 FV table 搵 factor（3 期、10% = 1.33100）再乘本金，兩個方法答案一樣。

* [Flashcard 3]
  - Front (Question in English): A bond pays HK$100 million in five years and the funding cost (discount rate) is 10%. What is its present value, and what decision rule applies when comparing PV with the asking price?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - PV = FV / (1 + i)^n = 100 / (1.10)^5 ≈ HK$62 million.
      - Decision rule: never pay more than what a financial product is worth today — buy only if PV > price; the PV represents what the bond is worth to the company given its funding cost.
    - [中文白話解釋]: PV 即係將未來收到的錢「折返」今日值幾多。100m 五年後先收、折現率 10%，即係今日只值約 62m。決策原則好簡單：絕對唔好畀多過佢今日嘅價值 — 如果賣家開價 64m 就唔買；相反若 PV 高過售價（如來源中 4 年期債券 PV 66m > 64m），就值得買。

* [Flashcard 4]
  - Front (Question in English): A financial contract pays HK$2,000 at the end of each of the next three years. The discount rate is 8%. Calculate the present value of this ordinary annuity.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - PVAn = CF × [1 − 1/(1+i)^n] / i
      - = 2,000 × [1 − 1/(1.08)^3] / 0.08
      - = 2,000 × (1 − 0.7938) / 0.08 = 2,000 × 2.5771
      - = HK$5,154.19
    - [中文白話解釋]: 普通年金（end of each period 收付）用年金 PV 公式一 take 過計，唔使逐期折現。呢條題 CF=2,000、n=3、i=8%，年金 factor 係 2.5771，答案 HK$5,154.19。注意「end of each year」= ordinary annuity；如果題目改做「beginning of each year」，就要將答案乘返 1.08 變 annuity due。

* [Flashcard 5]
  - Front (Question in English): Four annual cash flows of HK$1,000 each are discounted at 8%. Compare the PV if the cash flows occur (a) at the end of each year, and (b) at the beginning of each year. Explain why they differ.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - (a) Ordinary annuity: PV = 926 + 857 + 794 + 735 = HK$3,312.
      - (b) Annuity due: PV = 1,000 + 926 + 857 + 794 = HK$3,577 (= 3,312 × 1.08).
      - The annuity due's cash flows are shifted forward one year and discounted less, so both its PV and FV are always larger than those of an otherwise identical ordinary annuity.
    - [中文白話解釋]: 兩組現金流金額一樣，唯一分別係時間：annuity due 首期今日就收，之後每期都早一年，折現少咗，所以 PV 一定大過 ordinary annuity。記捷徑：PV(due) = PV(ordinary) × (1+i)。考試最常考嘅陷阱就係 timeline 畫錯 — 3 年 annuity due 嘅現金流落喺第 0、1、2 年，而唔係第 1、2、3 年。

* [Flashcard 6]
  - Front (Question in English): Sheung Wan Financial Services offers a perpetuity of HK$5,000 per year at an opportunity cost of 8%. What is the PV if (a) the first payment is in one year, and (b) the first payment is immediate?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - (a) Standard perpetuity: PVP = CF / i = 5,000 / 0.08 = HK$62,500.
      - (b) Perpetuity due: PVP = CF / i + CF = 62,500 + 5,000 = HK$67,500.
      - Preference shares (fixed dividends paid forever) and Consols (perpetual government bonds) are the classic real-world perpetuities.
    - [中文白話解釋]: 永續年金公式 CF/i 假設首期一年後先收；如果題目講明「first payment immediately」，就要額外加返今日嗰筆 CF，變成 CF/i + CF。呢個 boundary case 係考試常客：同一條題只差一個字（in one year vs immediately），答案就由 62,500 變 67,500。

* [Flashcard 7]
  - Front (Question in English): ABC Investment Ltd wants to endow a professorship paying HK$1.6 million per year forever, with a 3% annual pay rise. The university can earn 8% annually in perpetuity. How much must be donated today? State the condition for the formula to hold.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Growing perpetuity: PV0 = PMT1 / (k − g) = 1.6m / (8% − 3%) = HK$32 million.
      - (Without growth: PV = 1.6m / 8% = HK$20 million.)
      - Conditions: (1) k > g, otherwise the answer is negative and uninformative; (2) only future estimated cash flows and their growth are relevant; (3) the growth rate must continue at the same rate indefinitely.
    - [中文白話解釋]: 增長永續公式 PV = 首期付款 / (k − g)。呢度教授人工每年加 3%，投資回報 8%，所以需要捐 1.6m ÷ 5% = 32m（如果人工唔加就只需 20m）。最緊要記住前提：k 必須大過 g，否則分母變零或負數，公式完全無意義 — 呢點 MCQ 好鍾意考。

* [Flashcard 8]
  - Front (Question in English): A credit card quotes an APR of 24%. (a) Which compounding frequency maximises the EAR, and (b) when are APR and EAR identical?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - EAR = (1 + i/m)^m − 1; the more frequent the compounding, the higher the EAR.
      - At 24% APR: semi-monthly 26.97% > monthly 26.82% > bi-monthly 26.53% > quarterly 26.25% > semi-annually 25.44% > annually 24.00%.
      - APR = EAR only when interest is compounded once a year.
      - EAR (the annual percentage yield) is the true cost of borrowing and is the rate that should be used in finance decisions.
    - [中文白話解釋]: APR 係名義利率，唔計複利；EAR 先係真實年利率。同一個 APR 之下，複利越密 EAR 越高，所以信用卡公司最想用 semi-monthly compounding 嚟「合法地」收多啲息。牢記一個 boundary：只有每年複利一次（annually）嗰陣 APR 先會等於 EAR，其他情況 EAR 一定高過 APR。

「Phase 3 測驗題目及答案請見另外兩個檔案：M7_Ch3_Time_Value_of_Money_Quiz.md / M7_Ch3_Time_Value_of_Money_Answers.md」
