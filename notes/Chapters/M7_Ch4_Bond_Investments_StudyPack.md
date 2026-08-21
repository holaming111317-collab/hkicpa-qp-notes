# M7 Introduction to Bond Investments — Study Pack (Week 4)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構

- **債券本質與種類**：債券是長期債務工具 (long-term debt instrument)，發行人承諾定期支付利息 (coupon payments) 並於到期日 (maturity date) 償還全部本金 (par value / face value)。公司債分為 fixed-income/coupon bonds、floating-rate bonds（利率與 HIBOR / HONIA 等基準掛鈎）、zero coupon bonds（折價發行、到期收回面值）及 convertible bonds（可轉換為發行公司股份，票息通常較低）。政府債按年期分為 Treasury bills（<1 年）、Treasury notes（2–10 年）及 Treasury bonds（>10 年）。
- **估值核心 (Bond Valuation)**：債券價格 = 未來所有 coupon 及本金按市場利率 (market rate of interest, 即 YTM) 折現的現值 (present value)。市場利率 > coupon rate → 折價 (discount)；市場利率 < coupon rate → 溢價 (premium)；兩者相等 → 平價 (par value)。
- **收益率體系 (Bond Yields)**：Current yield（年利息 ÷ 市價）、Yield to maturity (YTM，使未來現金流現值等於債券價格的折現率）、Effective annual yield (EAY，考慮複利的年化收益率） 及 Realised yield（按實際收取現金流計算的已實現回報，適用於到期前出售）。
- **價格波動因素 (Factors Affecting Bond Price)**：利率與債券價格呈反向關係 (negatively related)；年期越長、票息越低，價格波動 (volatility) 越大 —— zero coupon bonds 波動最大。
- **契約與評級 (Indenture & Rating)**：bond indenture 為法律文件，載明付款規定、抵押 (security/collateral) 及保護性條款 (protective covenants)；call provision 賦予發行人提前贖回權。評級機構 (Moody's / S&P / Fitch) 將 Baa3/BBB− 或以上列為 investment-grade，以下為 junk / high-yield bonds。

### 2. 必背考點清單（公式與規則）

**A. Current Yield (CY)**
- CY = Annual interest ÷ B（B = market price）
- 注意：CY 只考慮下一年的利息收入，**不考慮**資本增值/虧損，並非真正的回報衡量（source 稱之為 cash yield / flat yield）。

**B. Yield to Maturity (YTM)**
- B = (i/kb) × [1 − 1/(1+kb)ⁿ] + F/(1+kb)ⁿ
- B = market price；kb = discount rate / YTM；n = number of periods to maturity；F = amount paid at maturity；i = interest (coupon per period)
- YTM 是使 coupon 及本金現值**剛好等於**債券價格的折現率；投資者以現價買入、持有至到期、所有款項準時收取且以 YTM 再投資時所實現的收益率。

**C. Bond Valuation Formula（年度付息）**
- PB = C/i × [1 − 1/(1+i)ⁿ] + Fn/(1+i)ⁿ
- PB = price of the bond；C = coupon payment per period；Fn = par value at maturity；i = market interest rate；n = periods to maturity
- 債券本質是 annuity（coupon 部分）加上到期一次過償還的 face value。

**D. Semi-annual Compounding Formula（每半年付息）**
- PB = C/i × [1 − 1/(1+i/m)^(mn)] + Fmn/(1+i/m)^(mn)
- C = annual coupon payment；m = number of coupon payments per year（半年付息 m = 2）；n = years to maturity；i = annual market interest rate
- 考試操作：coupon ÷ m、利率 ÷ m、年期 × m，三者必須一致調整。

**E. Zero Coupon Bond Pricing**
- PB = Fmn / (1 + i/m)^(mn)
- 所有 coupon 為 0 的特例；發行時以 deep discount 出售，到期收回 full face value；價格波動大於 coupon bonds。

**F. Effective Annual Yield (EAY)**
- EAY = (1 + Quoted interest rate / m)^m − 1
- Quoted interest rate = simple annual yield（semi-annual yield × 2，即 Wall Street convention）；m = 每年複利次數
- 直接將每期收益率乘以期數（×2）**沒有考慮複利**，比較不同複利頻率的債券（如歐洲年度 vs 美國半年度）時必須用 EAY。

**G. Realised Yield**
- 債券於到期前出售時，使**實際收到**的現金流（已收 coupons + 出售價）現值等於買入價的利率。計算方法與 YTM 相同，只是將到期值換成售價、年期換成持有期。

**H. Par / Discount / Premium 判斷規則**
- i > coupon rate → bond sells at a **discount**
- i < coupon rate → bond sells at a **premium**
- i = coupon rate → bond sells at **par**

**I. 價格波動規則（Bond Theorems）**
- 利率上升 → 債券價格下跌；利率下降 → 價格上升（負相關）。
- 其他條件相同：**maturity 越長** → volatility 越大；**coupon rate 越低** → volatility 越大（source 實例：同為 10 年期、折現率同升 1%，Landmade zero coupon bond 跌 9.1%，而 8% coupon bond 只跌 6.5%）。

**J. Indenture 主要條款**
- **Callable bonds**：發行人可在指定時間以預定價格（一般高於面值）贖回；觸發條件是市場利率**下降**（發行人可以更低成本再融資）。
- **Retractable (putable) bonds**：持有人可在到期前按預定價格賣回給發行人；行使條件是利率**上升**。
- **Extendible bonds**：持有人可延長到期日。
- **Sinking fund provisions**：發行人每年撥出資金以備到期還款（可每年回購部分債務或支付入 sinking fund）。
- **Purchase fund provisions**：僅當可按指定價格或以下回購時方須回購，對持有人有利（提供流動性及價格支持）。
- **Negative covenants** 禁止某些行為（如限制派息）；**positive covenants** 要求承諾行為（如提交季度報表、維持營運資金水平）。

**K. Bond Rating**
- 三大機構：Moody's、Standard & Poor's、Fitch。
- Investment-grade = Baa3 / BBB− 或以上；Ba1 / BB+ 或以下 = junk bonds / high-yield bonds（風險較高但預期回報較高）。
- 評級越低 → 投資者要求的 yield 越高（risk–expected return trade-off）；評級下調 → 債券價格下跌。
- Issue rating vs issuer rating：同一公司不同債券可因抵押條款不同而有不同評級（junior/unsecured claims 評級較低）。

### 3. 易混淆概念對比 (Common Pitfalls)

**Pitfall 1：Coupon Rate vs Current Yield vs YTM**
- **對比**：Coupon rate = annual coupon ÷ **face value**（發行時固定，永不改變）；Current yield = annual interest ÷ **current market price**（只看利息，忽略資本增值）；YTM = 令未來所有現金流現值等於現價的折現率（同時考慮利息、資本增值/虧損及再投資）。
- **例子**：面值 HK$1,000、coupon rate 8%（年息 HK$80）的債券以 HK$1,100 溢價買賣。Coupon rate 仍是 8%（不變）；CY = 80 ÷ 1,100 = 7.27%；YTM 只有 6.62%（source Exhibit 4.2 的 Hopefully Inc 實例）。溢價債必然 coupon rate > CY > YTM；折價債則相反。切記 coupon 高不代表 YTM 高——source 明確指出 Candy Floss coupon 7.25% 但 YTM 10.75%，高過 coupon 8% 但 YTM 僅 6.62% 的 Hopefully Inc。

**Pitfall 2：Callable（贖回權）vs Retractable / Putable（回售權）**
- **對比**：Call provision 是**發行人 (issuer)** 的權利——市場利率**下跌**時按預定 call price（一般高於面值）提前贖回，對投資者構成風險（上限被封頂）；Retractable/putable 是**持有人 (bondholder)** 的權利——利率**上升**時把債券賣回給發行人，對投資者有利。
- **例子**：公司發行 8% 債券後市場利率跌至 5%，發行人會行使 call provision 以較低成本發新債取代舊債；相反，若利率升至 10%，手持 8% 債券的投資者會行使 putable 權利把債券按預定價格賣回發行人，轉投更高收益的新債。記憶口訣：「息跌 issuer call；息升 holder put」。

**考試貼士**：OTQ 常見陷阱是把「premium/discount 條件」與「利率變動方向」混合出題。記住兩條鐵律：(1) i 與 coupon rate 比較決定 premium/discount；(2) i 上升 → 所有債券價格下跌，長年期、低票息跌得最多。做計算題時，半年付息必須三項同步調整：coupon ÷ 2、i ÷ 2、n × 2。

---

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): Define coupon rate, current yield and yield to maturity, and state how they rank for a bond trading at a premium.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Coupon rate = annual coupon payment ÷ face value (fixed for the life of the bond)
      - Current yield (CY) = annual interest ÷ current market price (B); ignores capital gain/loss
      - Yield to maturity (YTM) = the discount rate (kb) that makes the PV of all coupon and principal payments equal to the bond price; assumes the bond is held to maturity, all payments are made on time and cash flows are reinvested at the YTM
      - For a premium bond: coupon rate > current yield > YTM (for a discount bond the ranking reverses)
    - [中文白話解釋]: 三個「率」的分母不同：coupon rate 除以面值、永遠不變；current yield 除以市價、只計利息；YTM 是整體回報，連資本增值/虧損都計算在內。溢價債因為買貴了，實際回報被攤薄，所以 coupon rate > CY > YTM。

* [Flashcard 2]
  - Front (Question in English): A bond has a face value of HK$1,000, an annual coupon of HK$60 and a current market price of HK$920. Calculate its current yield.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - CY = Annual interest ÷ B
      - CY = HK$60 ÷ HK$920 = 0.0652 = 6.52%
      - Note: CY ignores the capital gain from buying below par, so it understates the true return (YTM would be higher)
    - [中文白話解釋]: Current yield 只需將年利息除以現時市價：60 ÷ 920 = 6.52%。因為這隻是折價債（920 < 1,000），到期還有資本增值，所以真正回報 YTM 一定高過 6.52%，而 coupon rate（6%）則一定低過 CY。

* [Flashcard 3]
  - Front (Question in English): Write down the bond valuation formula for annual coupon payments and define each variable. When does the bond sell at par, at a discount and at a premium?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - PB = (C/i) × [1 − 1/(1+i)ⁿ] + Fn/(1+i)ⁿ
      - PB = price of the bond; C = coupon payment per period; i = market interest rate; n = periods to maturity; Fn = par value at maturity
      - i > coupon rate → discount; i < coupon rate → premium; i = coupon rate → par
      - The coupon stream is valued as an annuity; the face value is added as a single repayment at maturity
    - [中文白話解釋]: 債券價格 = coupon 年金現值 + 到期面值現值。判斷平/折/溢價只需比較市場利率 i 與 coupon rate：i 高於 coupon rate 時債券息率「跑輸大市」，唯有減價（折價）先有人買；i 低於 coupon rate 時債券息率吸引，價格被搶高（溢價）。

* [Flashcard 4]
  - Front (Question in English): A 4-year bond has a face value of HK$1,000 and a coupon rate of 6% paid semi-annually. The market rate of interest is 8% with semi-annual compounding. Calculate the bond price.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Adjust for semi-annual payments: coupon per period C/m = 60/2 = HK$30; periods = m × n = 2 × 4 = 8; rate per period = i/m = 8%/2 = 4%
      - PV of coupons = 30 × [1 − (1.04)⁻⁸]/0.04 = 30 × 6.7327 = HK$201.98
      - PV of face value = 1,000 × (1.04)⁻⁸ = 1,000 × 0.7307 = HK$730.69
      - PB = 201.98 + 730.69 = HK$932.67 (a discount bond, since i 8% > coupon 6%)
    - [中文白話解釋]: 半年付息要做三個調整：票息除 2（30）、利率除 2（4%）、年期乘 2（8 期）。然後用年金公式計 coupon 現值，再加面值現值。市場利率 8% 高於 coupon rate 6%，所以結果一定是折價（低於 1,000），可用來檢查答案是否合理。

* [Flashcard 5]
  - Front (Question in English): How is a zero coupon bond priced, and why is its market price more volatile than a similar coupon-paying bond?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - PB = Fmn / (1 + i/m)^(mn) — the special case of the semi-annual compounding formula with all coupon payments equal to zero
      - Issued at a deep discount; investor profit = face value received at maturity minus purchase price
      - Because the only cash flow occurs at maturity, the market price tends to fluctuate more than that of coupon bonds
      - Lower coupon rate → higher price volatility for a given change in interest rates (bond theorem); zero coupon is the extreme case
    - [中文白話解釋]: Zero coupon bond 沒有中期利息，成個回報靠「低買高收」——以 deep discount 買入、到期收回十足面值。正因為所有現金流集中在最遲的到期日，利率一郁，折現影響最大，價格波動自然大過有定期 coupon 的債券。

* [Flashcard 6]
  - Front (Question in English): A bond earns a semi-annual yield of 5%. Calculate (a) the quoted (simple) annual yield and (b) the effective annual yield (EAY).
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - (a) Quoted interest rate = semi-annual yield × 2 = 5% × 2 = 10%
      - (b) EAY = (1 + Quoted rate / m)^m − 1 = (1 + 0.10/2)² − 1 = (1.05)² − 1 = 0.1025 = 10.25%
      - Multiplying the per-period yield by the number of periods ignores compounding and understates the true annual return; only compare yields of bonds with the same compounding frequency directly
    - [中文白話解釋]: 市面慣例（Wall Street convention）直接將半年收益率乘 2 得 10%，但這樣忽略了複利。正確做法是 EAY = (1.05)² − 1 = 10.25%。比較歐洲債（年度複利）與美國債（半年複利）時必須統一用 EAY，否則會作出錯誤決定。

* [Flashcard 7]
  - Front (Question in English): State how interest rate changes, maturity and coupon rate affect bond prices and price volatility.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Interest rate: negatively related to bond prices — as interest rates decline, bond prices rise, and vice versa (the coupon is fixed at issue)
      - Maturity: bonds with longer maturities are more volatile than shorter-maturity bonds of similar risk for a given interest rate change
      - Coupon rate: bonds with lower coupon rates are more volatile than those with higher coupon rates
      - Source evidence: with a 1% rise in discount rate, the 3-year Lord Inc bond lost only 2.7% while the 15-year Sociability bond lost 7.8%; the Landmade zero coupon bond lost 9.1% vs 6.5% for the identical-maturity 8% coupon bond
    - [中文白話解釋]: 記住三句：利率同價格「鬥相反」；年期越長越「敏感」；票息越低越「波動」。原因係 coupon 係發行時鎖死，利率升時舊債唔吸引，價格就要跌；年期長代表受折現影響嘅期數多；票息低代表大部分回報押後到後期先收，對利率變化更敏感。

* [Flashcard 8]
  - Front (Question in English): Distinguish callable, retractable (putable) and extendible bonds, and state the interest-rate condition under which each option is exercised. What separates investment-grade from junk bonds?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Callable bonds: issuer's option to repurchase outstanding bonds at predetermined prices (call price generally exceeds par) at specified times; exercised when market interest rates decline
      - Retractable/putable bonds: bondholder's option to sell the bonds back to the issuer at predetermined prices before maturity; exercised when interest rates have gone up
      - Extendible bonds: bondholder's option to extend the maturity date
      - Investment-grade: ratings of Baa3 / BBB− or better (Moody's / S&P); Ba1 / BB+ or lower = junk (high-yield) bonds — more risk but higher expected returns
    - [中文白話解釋]: Call 係發行人嘅權利，息跌時贖回舊債再平價發新債；putable 係投資者嘅權利，息升時將舊債賣返俾發行人；extendible 就係持有人可以延長到期日。評級分界線記 Baa3/BBB−：以上係 investment-grade（穩陣），以下係 junk/high-yield（高風險高回報）。評級越低，投資者要求嘅 yield 越高，債券價格越低。

---

「Phase 3 測驗題目及答案請見另外兩個檔案：M7_Ch4_Bond_Investments_Quiz.md / M7_Ch4_Bond_Investments_Answers.md」
