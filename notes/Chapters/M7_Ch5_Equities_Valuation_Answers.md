# M7 Equities Valuation — Model Answers（完成測驗後先好睇！）

## Retest R11 — Answer: **3.02%**

BEY = (5,000,000 − 4,975,000) ÷ 4,975,000 × 360 ÷ 60 = 0.005025 × 6 = **3.02%**。
【解題思路】分子係折扣額 (F−P)、分母係發行價、最後 ×360/日數年化。三寶齊先啱。

## Retest R12 — Answer: **A**

Grow：PV = 500 ÷ (0.08 − 0.05) = HK$16,666.67。Flat：PV = 1,200 ÷ 0.08 = HK$15,000。
【解題思路】今次係增長嗰個贏——重點唔係邊個贏，係**你計咗兩個數先揀**。條件 r > g（8% > 5%）成立，一定計到。

## Retest R13 — Answer: **B**

債券折價（920 < 1,000）→ coupon rate 6% < current yield（60/920 = 6.52%）< YTM（仲有到期資本增值）。
【解題思路】口訣：溢價債「coupon > CY > YTM」；折價債反轉「YTM > CY > coupon」。

## Retest R14 — Answer: **A**

【解題思路】波動性定理：年期越短 + coupon 越高 → 價格越穩定。A（2 年 + 8% coupon）係四個入面最短年期，波動最細。B（15 年零息）係最波動嗰個。

## Retest R15 — Answer: **932.67**

半年複利：coupon = 30/期、r = 4%/期、n = 8 期。
Price = 30 × [1 − 1.04⁻⁸] ÷ 0.04 + 1,000 ÷ 1.04⁸ = 30 × 6.7327 + 730.69 = 201.98 + 730.69 = **932.67**。
【解題思路】半年複利三部曲：coupon 減半、利率減半、期數加倍。常識檢查：coupon 6% < market 8% → 價格必須低過面值 ✓。

---

## Q1 — Correct Answer: B

**Model Answer:** The constant-growth (Gordon) dividend model, P0 = D1 / (R − g), provides valid solutions only when the constant dividend growth rate g is smaller than the required rate of return R. If R is equal to or less than g (R ≤ g), the denominator is zero or negative and the results are meaningless.

- Option A is incorrect: the numerator must be the dividend in the NEXT period, D1 = D0 × (1 + g). Using D0 directly understates the share value.
- Option C is incorrect: a firm growing at 35% per year is in a supernormal growth phase (and g > R would violate the model's condition). Such a firm must be valued with the mixed (supernormal) growth model, discounting each high-growth dividend individually plus a terminal price Pt = D(t+1) / (R − g).
- Option D is incorrect: constant dividends in dollar terms describe the ZERO-growth model (P0 = D / R), not the constant-growth model, in which dividends grow at rate g indefinitely.

【解題思路】呢題考你分唔分到三個模型嘅適用條件。Gordon model 嘅硬性條件係 **g < R**——只要記住「分母 R − g 唔可以係零或負數」就會揀 B。A 係最經典陷阱：分子一定係 D1（下一期股息），唔係剛派咗嘅 D0。C 講嘅 35% 高增長公司要用 mixed (supernormal) growth 模型，唔可以一條 Gordon 公式搞掂。D 描述嘅係 zero-growth model（P0 = D/R），同 constant-growth 係兩回事。考試見到 "constant-growth" 即刻諗起「D1 做分子、g < R、適合成熟穩定增長公司」三個要點。

## Q2 — Correct Answer: C

**Model Answer:** A special cash dividend is a one-time payment used to distribute an unusually large amount of cash, for example proceeds received after the sale of a major asset or to effect a change in the capital structure of a company.

- Option A is incorrect: a regular cash dividend is paid in cash on a regular basis (annually or quarterly) as the normal way of distributing profits — it does not fit a one-off distribution of asset-sale proceeds.
- Option B is incorrect: an extra cash dividend is also a one-time payment, but it is paid when earnings are higher than expected and is typically modest in size, often paid alongside regular dividends to meet a target payout ratio.
- Option D is incorrect: a scrip dividend offers shareholders an option to receive the dividend either as cash or additional stock — it is not the label for a large one-off cash distribution.

【解題思路】題目有三個關鍵詞：「one-time payment」、「unusually large」、「sale of a major asset」——三個都係 special cash dividend 嘅教科書定義。最常見錯誤係揀 B（extra dividend），因為 extra 都係一次過派，但 extra 係因為盈利高過預期、金額較細，仲可以經常性咁配合 regular dividend 達到目標 payout ratio；special 就係罕有、大額、同賣資產或資本結構變動掛鈎。A 係定期派息，D 係俾股東揀收現金定股票，都唔符合題意。

## Q3 — Correct Answer: B (HK$26.50)

**Model Answer / Working:**

This is a constant-growth (Gordon) dividend valuation, with g = 6% < R = 14% (condition satisfied).

Step 1 — Compute next period's dividend (the dividend paid yesterday is D0):
- D1 = D0 × (1 + g) = HK$2.00 × 1.06 = HK$2.12

Step 2 — Apply the constant-growth model:
- P0 = D1 / (R − g) = 2.12 / (0.14 − 0.06) = 2.12 / 0.08 = **HK$26.50**

Why the distractors are wrong:
- Option A (HK$25.00): uses D0 directly in the numerator — 2.00 / 0.08 = 25.00. The numerator must be the NEXT period's dividend D1, so D0 must first be grown by (1 + g).
- Option C (HK$15.14): forgets to subtract g from the discount rate — 2.12 / 0.14 = 15.14. A growing perpetuity is discounted at (R − g), not at R alone.
- Option D (HK$10.60): adds instead of subtracts the growth rate — 2.12 / (0.14 + 0.06) = 2.12 / 0.20 = 10.60.

【解題思路】第一步永遠問自己：「題目俾嘅股息係 D0 定 D1？」呢度寫明「paid yesterday」，所以係 D0，必須先乘 1.06 變成 D1 = HK$2.12，先至可以放入 Gordon 公式。之後檢查條件 g (6%) < R (14%) 成立，P0 = 2.12 / 0.08 = HK$26.50。三個錯誤選項分別對應三種典型失手：A 忘記將 D0 增長、C 忘記減 g、D 加減調轉。考試時養成習慣：寫低 D0 / D1 分別，再列公式 P0 = D1/(R−g)，就可以避開晒呢啲陷阱。

## Q4 — Correct Answer: HK$50.00

**Model Answer / Working:**

A perpetual preference share has no maturity and pays a constant dividend forever (g = 0), so it is valued as a perpetuity:

- P0 = D / R
- P0 = HK$6.00 / 0.12 = **HK$50.00**

Note: D is the ANNUAL dividend. If the HK$6.00 were paid quarterly instead, the correct annual dividend would be HK$6.00 × 4 = HK$24.00 and the value would be 24.00 / 0.12 = HK$200.00 — always check the payment frequency stated in the question.

【解題思路】見到 "perpetual preference shares with no maturity date" 即刻諗起永續年金公式 P0 = D/R，同 zero-growth model 係同一条公式。呢題直接：6.00 ÷ 0.12 = HK$50.00。要留意嘅陷阱係派息頻率：如果題目話「每季派 HK$1.50」之類，記住先轉換做全年股息再除 R（R 係年度回報率）。另外唔好同「有到期日的優先股」撈亂——有固定到期日就要用債券估值模式（每期股息折現 + stated value 折現），唔係一條 D/R 可以搞掂。

## Q5 — Correct Answer: 11.5%

**Model Answer / Working:**

Rearrange the constant-growth model P0 = D1 / (R − g) to solve for R:

- P0 × (R − g) = D1
- R − g = D1 / P0
- R = D1 / P0 + g

Substituting the data (note that HK$2.20 is already D1, the dividend expected in one year — do NOT multiply by (1 + g) again):

- R = 2.20 / 40.00 + 0.06
- R = 0.055 + 0.06 = 0.115 = **11.5%**

Economic interpretation: the required return equals the expected dividend yield (D1/P0 = 5.5%) plus the constant dividend growth rate (g = 6%), which under constant growth also represents the expected capital gains yield.

【解題思路】呢題考你將 Gordon 公式調轉用：R = D1/P0 + g，即係「股息率 (dividend yield) + 增長率 (capital gains yield)」。兩大陷阱：第一，題目講明 HK$2.20 係「next dividend, payable in one year」，即係已經係 D1，千祈唔好再乘 (1+6%)——再乘就會得出 12.0% 左右嘅錯誤答案；第二，記住 D1/P0 同 g 要**相加**而唔係相減。代入：2.20/40 = 5.5%，加 6% = 11.5%。驗算：P0 = 2.20/(0.115−0.06) = 2.20/0.055 = HK$40.00，同題目股價一致，答案無誤。
