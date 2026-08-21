# M7 Chapter 13 Investment Project Appraisal — Model Answers（完成測驗後先好睇！）

---

## Question 1 — Answer: B

**English Model Answer:**

The correct decision is to select **Project Harbour**, because it has the higher NPV (HK$210,000 vs HK$120,000). For mutually exclusive projects, the NPV method prevails: the project with the highest NPV produces the biggest increase in the company's value, which aligns with the objective of maximising shareholder value. The IRR is a relative (percentage) measure — selecting the project with the highest IRR does not necessarily maximise company value.

**Why each distractor is wrong:**

- **A is wrong:** Choosing the highest IRR is the classic error with mutually exclusive projects. IRR cannot tell you which mutually exclusive project to select — a smaller project can show a higher percentage return yet create less value.
- **C is wrong:** The projects are *mutually exclusive*, so only one can be accepted. "Accept both" would be correct only if the projects were *independent* (in which case both positive-NPV projects would be accepted).
- **D is wrong:** A higher IRR does not always imply a higher NPV. NPV and IRR rankings can conflict for mutually exclusive projects because of differences in project scale and the timing of cash flows.

【解題思路】關鍵字眼係「mutually exclusive」——互斥項目下 IRR 同 NPV 可能打架，此時以 NPV 為準，因為 NPV 直接量度公司價值增加幾多（絕對金額），而 IRR 只係百分比（相對指標）。C 選項混淆咗 independent projects 嘅規則：獨立項目先可以「全部正 NPV 都接受」。D 選項就係考官最常設嘅陷阱，記住「highest IRR ≠ highest NPV」。

---

## Question 2 — Answer: C

**English Model Answer:**

Correct classification:

- **Book value of the old machine (HK$800,000):** a sunk cost — already incurred and cannot be changed or avoided by any future decision; it must be ignored in the analysis.
- **Feasibility study cost (HK$120,000):** a sunk cost — already paid; irrelevant to the replacement decision.
- **Sale value of the old machine (HK$500,000):** an opportunity cost — if the machine is retained/used, the company forgoes the HK$500,000 it could receive by selling it; this must be included in the project analysis.

**Why each distractor is wrong:**

- **A is wrong:** It reverses every classification — a book value is never a relevant cost, a recoverable sale value is not sunk, and money already spent on a study is not an opportunity cost.
- **B is wrong:** Book value is sunk, not an opportunity cost; the sale value forgone is the opportunity cost; the study cost is already paid (sunk), not relevant.
- **D is wrong:** Not all three are sunk. The HK$500,000 sale value is a future benefit that would be forgone — a genuine opportunity cost that must be included.

【解題思路】口訣：「過去嘅錢唔理（sunk），將來放棄嘅利益要計（opportunity）」。Book value 同已付嘅研究費都係歷史成本，點決定都改變唔到，所以全部 ignore。反而部機可以賣 HK$500,000，如果留嚟用就放棄咗呢筆錢——呢個先係相關成本。呢類「relevant vs sunk cost」概念辨析係 OTQ 常客，留意題目會故意將三個金額嘅身份調亂。

---

## Question 3 — Answer: C

**English Model Answer:**

Statement C is correct:

- The discounted payback period is **equal to or longer than** the simple payback period, because future cash flows are worth less once discounted for time and risk.
- **Both** methods ignore cash flows beyond the payback/cut-off date, and in both cases the cut-off date is arbitrary (no objective criterion for a "good" payback period).

**Why each distractor is wrong:**

- **A is wrong:** Discounting *reduces* the value of future inflows, so recovery takes longer, not shorter. The discounted payback can never be shorter than the simple payback for a project with conventional cash inflows.
- **B is wrong:** Only the discounted payback considers the time value of money; the simple payback does not. And both methods ignore cash flows beyond the cut-off date.
- **D is wrong:** Neither payback method has an objective acceptance criterion — the cut-off period is set arbitrarily by management, and it is expressed in years, not compared with the cost of capital.

【解題思路】呢題考兩個 payback 方法嘅細微分別。記住兩點：(1) discounted payback 一定 ≥ simple payback，因為折現令未來現金流縮水；(2) 兩者共同缺點係「cut-off 之後嘅現金流完全唔睇」兼且 cut-off 係任意設定。如果公司識折現，其實直接計 NPV 仲好——discounted payback 只係 payback 同 NPV 之間嘅妥協。

---

## Question 4 — Answer: NPV = −HK$21,262 (approximately); the project should be **rejected**.

**English Model Answer / Full Working:**

Step 1 — Identify all relevant cash flows:

- Year 0: initial outlay = equipment HK$260,000 + net working capital HK$40,000 = **HK$300,000 outflow**.
- Years 1–3: after-tax operating cash inflows of **HK$100,000** each year.
- Year 3: **recovery of net working capital HK$40,000** (must be included — excluding it would underestimate the NPV).

Step 2 — Discount at 10%:

| Year | Cash flow (HK$) | Discount factor @10% | Present value (HK$) |
|------|----------------:|---------------------:|--------------------:|
| 0 | (300,000) | 1.00000 | (300,000.00) |
| 1 | 100,000 | 0.90909 | 90,909.09 |
| 2 | 100,000 | 0.82645 | 82,644.63 |
| 3 | 100,000 + 40,000 = 140,000 | 0.75131 | 105,183.80 |

(Equivalently: PV of operating inflows = 100,000 × 2.48685 = 248,685.20; PV of working capital recovery = 40,000 × 0.75131 = 30,052.59.)

Step 3 — NPV:

NPV = −300,000 + 90,909.09 + 82,644.63 + 105,183.80 = **−HK$21,262** (accepting rounding in the range −HK$21,200 to −HK$21,300)

Step 4 — Decision rule: NPV < 0 → **reject the project**.

【解題思路】第一步要將所有 relevant cash flows 搵齊：Year 0 唔好淨係計部機，working capital HK$40,000 都係即時投入；到 Year 3 完結時 working capital 會全數收回，呢筆 HK$40,000 一定要加返落去，否則會低估 NPV（呢個係考官常考位）。逐步折現之後加埋，得出負 NPV，按決策規則「NPV < 0 → reject」。常見錯誤：(1) 漏計 working capital recovery，會得出更負嘅答案（−HK$51,315）；(2) 將 working capital 當成每年收回；(3) 忘記 Year 3 係營運現金流加 WC 收回一齊折現。

---

## Question 5 — Answer: (a) Discounted payback ≈ **4.26 years**; (b) Simple payback ≈ **3.33 years**.

**English Model Answer / Full Working:**

(a) Discounted payback period (discount rate 10%):

| Year | Cash flow (HK$) | Discount factor @10% | Discounted CF (HK$) | Cumulative discounted CF (HK$) |
|------|----------------:|---------------------:|--------------------:|-------------------------------:|
| 1 | 150,000 | 0.90909 | 136,364 | 136,364 |
| 2 | 150,000 | 0.82645 | 123,967 | 260,331 |
| 3 | 150,000 | 0.75131 | 112,697 | 373,028 |
| 4 | 150,000 | 0.68301 | 102,452 | 475,480 |
| 5 | 150,000 | 0.62092 | 93,138 | 568,618 |

The HK$500,000 outlay is recovered during Year 5:

Discounted payback = 4 + (500,000 − 475,480) ÷ 93,138 = 4 + 24,520 ÷ 93,138 = **4.26 years**

(b) Simple payback = 500,000 ÷ 150,000 = **3.33 years**.

Reason for the difference: the discounted payback is longer because future cash flows have less value once discounted for the time value of money (and risk). Discounting shrinks each year's inflow, so it takes longer to recover the initial outlay.

【解題思路】先計每年嘅折現現金流，再做累計（cumulative）。第四年尾累計得 HK$475,480，仲差 HK$24,520 先回本，而第五年嘅折現流入係 HK$93,138，所以用比例計 24,520 ÷ 93,138 ≈ 0.26 年，加返 4 年即 4.26 年。至於 simple payback 就淨係 500,000 ÷ 150,000 = 3.33 年，完全唔使折現。留意 discounted payback 一定長過（或等於）simple payback，因為折現令未來現金流縮水——呢個正好呼應 Question 3 嘅概念。常見錯誤：用未折現嘅 150,000 去計最後一年嘅比例（會錯得 4.16 年），或者忘記累計應該用折現後數字。

---

*來源：以上答案內容全部建基於 Learning Pack Module 7 Chapter 13（Investment Project Appraisal and Evaluation）之內容，包括 13.4–13.5 各評估技術之決策規則、13.2.1 相關成本原則及 13.4.7 PI 公式。*
