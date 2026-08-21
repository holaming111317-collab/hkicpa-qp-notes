# M7 Financial Management — Master Formula Sheet（累積式總表）
> 每完成一章自動追加。考前第 13 週呢份就係你嘅終極複習表。

## Ch1 Financial Environment（本章以概念為主，公式較少）
- **Net working capital = Total current assets − Total current liabilities**
  - Current assets 包括：inventories、trade receivables、prepayments and deposits、cash and cash equivalents
  - Current liabilities 包括：trade payables、short-term bank loans、accruals and other payables
  - 應用：衡量短期償債能力與營運資金管理（Week 1 Quiz Q4 實戰過）
- 本章核心概念對比（詳見 Week 1 Study Pack）：money market vs capital market｜primary vs secondary market｜brokers vs dealers｜marketability vs liquidity｜EMH 三形態（weak / semi-strong / strong）


## Ch2 Sources of Finance

**1. Bond Equivalent Yield (BEY) on Commercial Paper**
- Formula: BEY = (Face Value − Issue Price) / Issue Price × 360 / Days to maturity
- Variables: Face Value = amount repaid at maturity; Issue Price = discounted price paid by investor; Days to maturity = 1–270 days (typical 30)
- When to apply: pricing/quoting money-market instruments (CP) issued at a discount; money market uses a **360-day year**. The result is the *promised yield* (maximum yield if held to maturity; expected return < promised yield when default risk exists). Yield spread = CP yield − T-bill yield (compensation for default risk).
- Text example: (HK$100m − HK$99.55m)/HK$99.55m × 360/30 = 5.424%.

**2. Borrowing-Base Credit Limit (Line of Credit)**
- Formula: Maximum credit limit = 75% × Accounts Receivable + 50% × Inventory
- Variables: AR and inventory from the statement of financial position; **cash and other current assets are excluded**
- When to apply: bank caps the maximum value of a line of credit using a standard formula; percentages as given in the chapter's Illustrative Example 1 (= HK$51,000,000 from AR 18,536,000 and inventory 74,196,000).

**3. Minimum Earnings Required by an Interest Coverage Ratio Covenant**
- Formula: Required earnings before interest = Interest expense × Minimum interest coverage ratio, where Interest expense = Principal × Annual interest rate
- When to apply: revolving lines of credit impose financial restrictions such as a minimum interest coverage ratio (coverage = earnings before interest / interest). Text example: HK$50m × 9.75% = HK$4,875,000 interest; × 1.75 = HK$8,531,250 required earnings.

**4. Net Working Capital (NWC)**
- Formula: NWC = Current Assets − Current Liabilities
- When to apply: liquidity measurement; gross working capital = current assets (the two terms are the same); most firms have positive NWC. Cash conversion cycle (time from paying for raw materials to collecting cash from sales) measures working capital *efficiency* — shorter is better.

**5. Inventory Turnover and Days in Inventory**
- Formulas: Inventory turnover = Cost of Goods Sold / Average Inventory; Days in inventory = 365 / Inventory turnover
- When to apply: assessing inventory liquidity/management; high turnover + low days-in-inventory while meeting customer needs = success. EOQ model minimises the sum of reorder (ordering) costs and carrying costs.

**Key rules / thresholds to memorise (Ch2):**
- Short-term = < 1 year (money market); long-term = > 1 year (funded debt); leases > 1 year = long-term financing, ~100% debt financing
- CP: 1–270 days (typical 30), unsecured, discount; backup line of credit commitment fee ≈ 0.125% p.a.; dealer commission ≈ 5 bp (0.05%); ABCP via SPV, 90–140 days typical; CP ratings A-1 / P-1 / F1 (highest)
- BA: 1–180 days (typical 90), discount, bank's credit supports it; stamping fee 0.50–0.75%
- Line of credit: setup fee ≈ 0.50% (also on unused balance); revolving line ≥ 364 days up to 5 years ("evergreen"); prime = floating benchmark, most borrowers "prime plus"; overdraft interest usually higher than bank loan
- Debt terminology: < 10 yrs = note/MTN; 4–10 yrs = intermediate-term bond; > 10 yrs = bond/long-term bond
- Bond ratings: highest AAA/Aaa; lowest investment grade BBB/Baa; below = junk/high-yield; stable rating philosophy + hierarchy principle
- Convertible bonds: conversion typically attractive only after share price rises 15–20%; lower coupon; dilution risk; coco bonds convert only when capital conditions trigger (favour issuer)
- Issuance costs (issue ≥ US$500m): common stock ≈ 3.63% vs non-convertible corporate bonds ≈ 0.65%; equity issues virtually always negotiated sales; vanilla bonds cheaper via competitive sales in stable markets
- VC: staged funding (3–7 stages), convertible preference stock, exit in 3–7 years (strategic buyer / financial buyer / IPO); PE: mature firms, hold 3–5 years, LBO leverage 3–4×; PIPE: unregistered shares at a discount, registration within ~90 days, damages up to 1.5%/month
- Retained earnings restrictions: legal / contractual / voluntary; internal financing = cheaper, no collateral, no dilution, but smaller amounts

## Ch3 Time Value of Money and Investing Basics

| Formula name | Formula | Variable meanings | When to apply |
|---|---|---|---|
| Simple Interest | Interest = P × i × n | P = principal; i = interest rate; n = time | Short-term situations (typically one year or less); interest on initial principal only |
| Compound Interest | Interest = P × (1 + i/n)^(nt) | P = principal; i = interest rate; n = number of compounding times per year; t = number of years | Most business situations; interest earned on principal plus previously accrued interest |
| Future Value (single sum) | FV = P × (1 + i)^n | P = principal; i = interest rate per period; n = number of periods | Value at a future date of a single amount invested, assuming compound interest (compounding) |
| Present Value (single sum) | PV = FV / (1 + i)^n | FV = future amount; i = discount rate; n = number of periods | Value now of a future amount (discounting); bond prices, notes payable, lease liabilities, capital budgeting |
| PV of Ordinary Annuity | PVAn = CF × [1 − 1/(1+i)^n] / i | CF = level, equally spaced cash flows; i = discount rate; n = number of periods | Equal cash flows received/paid at the END of each period (e.g. loan repayments) |
| FV of Ordinary Annuity | FVAn = CF × [(1+i)^n − 1] / i | Same as above | Terminal value of regular end-of-period contributions (e.g. savings/retirement plans) |
| Annuity Due adjustment | PV(due) = PV(ordinary) × (1+i); FV(due) = FV(ordinary) × (1+i) | — | Cash flows at the BEGINNING of each period (e.g. apartment rental); always larger than ordinary annuity |
| PV of Perpetuity | PVP = CF / i | CF = periodic cash flow; i = interest rate | Cash flows continuing forever, FIRST payment in one year (preference share dividends, Consols) |
| PV of Perpetuity Due | PVP = CF / i + CF | — | Perpetual cash flows with the first payment IMMEDIATELY |
| PV of Growing Perpetuity | PV0 = PMT1 / (k − g) | PMT1 = payment in one year; k = effective annual rate; g = constant growth rate | Cash flows growing at a constant rate forever; valid ONLY when k > g |
| PV of Growing Annuity | PV0 = [PMT1 / (k − g)] × [1 − ((1+g)/(1+k))^n] | n = terminal period | Cash flows growing at constant rate g ending at period n; valid only when k > g and growth constant throughout |
| Annual Percentage Rate (APR) | APR = periodic rate × number of periods per year | e.g. 1.5%/month × 12 = 18% | Nominal/quoted rate; excludes compounding; NOT for finance decisions |
| Effective Annual Rate (EAR) | EAR = (1 + i/m)^m − 1 | i = quoted (nominal) rate; m = number of compounding periods per year | True annual cost of borrowing/lending; use in finance decisions; APR = EAR only when m = 1 (annual compounding); higher m → higher EAR |

Key reference values (24% APR, from source): semi-monthly EAR 26.97% > monthly 26.82% > bi-monthly 26.53% > quarterly 26.25% > semi-annually 25.44% > annually 24.00%.
Discount rate selection: use WACC for average-risk projects; adjust the discount rate upward (downward) for projects with higher (lower) risk than the firm's typical projects.

## Ch4 Introduction to Bond Investments

**1. Current Yield (CY)**
- CY = Annual interest ÷ B
- CY = current yield; B = market price
- When to apply: quick yield measure ignoring capital gain/loss; also called cash yield / flat yield. Not a true return measure.

**2. Yield to Maturity (YTM)**
- B = (i/kb) × [1 − 1/(1+kb)ⁿ] + F/(1+kb)ⁿ
- B = market price; kb = discount rate / YTM; n = number of periods to maturity; F = amount paid at maturity; i = interest per period
- When to apply: find the discount rate that makes PV of coupon + principal payments equal to the bond price (solve by financial calculator/trial). Assumes held to maturity, all payments on time, cash flows reinvested at YTM.

**3. Bond Valuation Formula (annual coupons)**
- PB = (C/i) × [1 − 1/(1+i)ⁿ] + Fn/(1+i)ⁿ
- PB = price of the bond; C = coupon payment per period; i = market interest rate; n = periods to maturity; Fn = par value at maturity
- When to apply: coupon annuity PV + face value PV. Pricing rules: i > coupon rate → discount; i < coupon rate → premium; i = coupon rate → par.

**4. Semi-annual Compounding Formula**
- PB = (C/i) × [1 − 1/(1+i/m)^(mn)] + Fmn/(1+i/m)^(mn)
- C = annual coupon payment; m = coupon payments per year (semi-annual: m = 2); n = years to maturity; i = annual market interest rate; Fmn = face value at maturity
- When to apply: coupons paid more than once a year — divide coupon and rate by m, multiply years by m (all three must be adjusted consistently).

**5. Zero Coupon Bond Pricing**
- PB = Fmn / (1 + i/m)^(mn)
- PB = price of the bond; Fmn = payment at maturity; i = annual market rate; m = compounding periods per year; n = years to maturity
- When to apply: bonds with no periodic coupons (deep discount bonds); special case of the compounding formula with all coupons = 0. Most price-volatile bond type.

**6. Effective Annual Yield (EAY)**
- EAY = (1 + Quoted interest rate / m)^m − 1
- Quoted interest rate = simple annual yield (semi-annual yield × 2); m = number of compounding periods per year
- When to apply: to annualise a per-period yield correctly (captures compounding); essential when comparing bonds with different compounding frequencies (e.g. European annual vs US semi-annual bonds).

**7. Realised Yield**
- Mechanics identical to YTM, but equates the PV of **actual** cash flows (coupons received + sale price) to the original purchase price
- When to apply: bond sold before maturity — measures the return actually earned over the holding period.

**Related price-volatility rules (bond theorems):**
- Bond prices are negatively related to interest rate movements (rates ↓ → prices ↑).
- Longer maturity → greater price volatility.
- Lower coupon rate → greater price volatility.

## Ch5 Equities Valuation

| Formula | Formula expression | Variable meanings | When to apply |
|---|---|---|---|
| Present value of a stock | PV (stock) = PV (dividend) + PV (sale price) | — | Foundation of all equity valuation; value of any asset = PV of its future cash flows |
| Single-period valuation | P0 = (D1 + P1) / (1 + R) | P0 = current price; D1 = dividend paid at end of period; P1 = stock price at end of period; R = required return for the risk class | Stock bought now and sold after one period with known dividend and sale price |
| General dividend valuation model | P0 = Σ (t=1→∞) Dt / (1+R)^t | Dt = dividend in period t; R = required return | Theoretical basis for all dividend models; makes no assumption about dividend pattern or sale date; requires forecasting infinite dividends |
| Zero-growth valuation | P0 = D / R | D = constant cash dividend each period; R = required return | Dividends constant forever (g = 0); non-growing companies and perpetual preference shares |
| Future dividend under constant growth | Dt = D0 × (1 + g)^t; D1 = D0 × (1 + g) | D0 = dividend paid in current period; g = constant growth rate | Compute any future dividend as input to the models below |
| Constant-growth (Gordon) valuation | P0 = D1 / (R − g) | P0 = current price; D1 = dividend in next period (t = 1); g = constant dividend growth rate; R = required return | Mature companies with stable constant dividend growth; **valid only if g < R — meaningless if R ≤ g** |
| Future stock price (constant growth) | Pt = D(t+1) / (R − g) | Pt = price at time t; D(t+1) = dividend one period after t | Price at any point in time once dividends grow at constant g; implies share price itself grows at rate g |
| Mixed (supernormal) growth valuation | P0 = D1/(1+R) + D2/(1+R)² + … + Dt/(1+R)^t + Pt/(1+R)^t, where Pt = D(t+1)/(R − g) | Dt = dividends in the non-constant growth phase; Pt = terminal price when constant growth begins | Firms with two growth stages: supernormal/variable growth early, then stable constant growth g; identify when constant growth starts |
| Preference share with fixed maturity | P0 = Σ (D/m)/(1+i/m)^t + P/(1+i/m)^(mn) | D = annual preference dividend; P = stated (par) value; i = yield to maturity; m = dividend payments per year; n = years to maturity | Preference shares with mandatory retirement / sinking fund / call date — valued like a bond |
| Preference share with no maturity | P0 = D / R | D = constant cash dividend; R = required rate of return | Perpetual preference shares (no maturity) — valued as a perpetuity |
| Implied required return (rearranged Gordon) | R = D1 / P0 + g | D1/P0 = expected dividend yield; g = growth rate (= capital gains yield under constant growth) | Inferring the market's required return from an observed share price |

## Ch6 Capital Asset Pricing Model

| Name | Formula | Variable meanings | When to apply |
|---|---|---|---|
| Capital appreciation return | R_CA = (P₁ − P₀) / P₀ = ΔP / P₀ | P₁ = price at period 1; P₀ = price at period 0; ΔP = change in price | Price-change component of holding period return |
| Income return | R_I = CF₁ / P₀ | CF₁ = cash flow at period 1 (dividend/coupon) | Income component of holding period return |
| Total holding period return | R_T = R_CA + R_I = (ΔP + CF₁) / P₀ | As above | Total return over a specific holding period |
| Arithmetic mean | AM = ΣRᵢ / n | Rᵢ = return in period i; n = number of periods | ~12-month horizons; always overstates returns |
| Geometric mean | GM = [(1+R₁)(1+R₂)…(1+Rₙ)]^(1/n) − 1 | Rᵢ = return of i-th period; n = number of periods | Compound growth over multiple/longer periods |
| Expected return (probabilities differ) | E(R_Asset) = Σᵢ pᵢ·Rᵢ | pᵢ = probability of situation i; Rᵢ = return in situation i | Probability-weighted expected return of an asset |
| Expected return (equal probabilities) | E(R_Asset) = ΣRᵢ / n | As above | When p₁ = p₂ = … = 1/n |
| Total return decomposition | R = E(R) + m + ε | E(R) = expected return; m = systematic portion; ε = unsystematic portion | Splitting actual/realised return into expected + unexpected components |
| Variance (probabilities differ) | σ² = Σᵢ pᵢ·[Rᵢ − E(R)]² | pᵢ, Rᵢ, E(R) as above | Risk (total) of an asset with probability data |
| Standard deviation | σ = √σ² | — | Total risk; normal distribution: ±1σ ≈ 68%, ±2σ ≈ 95%, ±3σ ≈ 99.7% |
| Coefficient of variation | CV = σ_Asset / E(R_Asset) | σ = standard deviation; E(R) = expected return | Risk per unit of return; lower CV preferred (risk minimisation) |
| Modified coefficient of variation | CV* = σ_Asset / [E(R_Asset) − R_rf] | R_rf = risk-free rate | Risk per unit of excess return over the risk-free rate |
| Portfolio expected return | E(R_p) = Σᵢ wᵢ·E(Rᵢ) | wᵢ = proportion invested in asset i; E(Rᵢ) = expected return on asset i; m = number of assets | Weighted-average return of a multi-asset portfolio |
| Two-asset portfolio variance | σ²_p = w_A²σ_A² + w_B²σ_B² + 2w_A·w_B·COV(A,B) | w_A, w_B = weights; σ_A, σ_B = standard deviations; COV(A,B) = covariance | Total risk of a two-asset portfolio |
| Covariance | COV_AB = Σᵢ pᵢ·[R_Ai − E(R_A)][R_Bi − E(R_B)] | R_Ai, R_Bi = returns of A and B under event i | How returns of two assets move together |
| Correlation coefficient | ρ_AB = COV_AB / (σ_A·σ_B) | COV_AB = covariance; σ_A, σ_B = standard deviations | −1 ≤ ρ ≤ +1; ρ = +1: no diversification benefit; ρ = −1: can eliminate all risk; typical stocks ρ ≈ 0.65 |
| Beta of an asset | βᵢ = ρ_Mi·σᵢ / σ_M = COV(i,M) / σ²_M | ρ_Mi = correlation of asset i with market; σᵢ, σ_M = standard deviations of asset i and market; COV(i,M) = covariance with market; σ²_M = market variance | Measuring systematic risk; β=1 same as market; β>1 higher; β<1 lower; β=0 zero systematic risk |
| CAPM | E(Rᵢ) = R_rf + βᵢ[E(R_m) − R_rf] | E(Rᵢ) = expected return of asset i; R_rf = risk-free rate (HK: Exchange Fund Bills and Notes); E(R_m) = expected market return; [E(R_m) − R_rf] = market risk premium | Required/expected return of a security; economic feasibility test; cost of equity |
| Portfolio beta / Portfolio CAPM | β_p = Σᵢ xᵢ·βᵢ ; E(R_p) = R_rf + β_p[E(R_m) − R_rf] | xᵢ = weighting of asset i; βᵢ = beta of asset i | Expected return of a portfolio under CAPM |
| Security Market Line (SML) | kᵢ = R_rf + [E(R_m) − R_rf]·βᵢ | kᵢ = required return of asset i; slope = market risk premium | Plot of required return vs beta; above SML = undervalued; below SML = overvalued; on SML = correctly priced |
| Capital Allocation Line (CAL/CML) | E(r_p) = w_r·E(r_r) + (1 − w_r)·E(r_f) ; σ_p = w_r·σ_r | w_r = weight in risky (market/tangency) portfolio; r_f = risk-free asset; σ_r = SD of risky portfolio | Combining a risk-free asset with a risky portfolio; leveraged positions (w_r > 1 means borrowing at risk-free rate) |

## Ch7 Cost of Capital

### 1. Dividend Growth Model (DGM) — Cost of Common Equity
- **Formula:** kcs = D1 / P0 + g
- **Variables:** kcs = required return on common stock; D1 = dividend in next period (t = 1; if D0 is given, D1 = D0 × (1 + g)); P0 = current price per share; g = expected constant dividend growth rate
- **When to apply:** Only for dividend-paying firms with dividends growing at a constant rate forever (e.g. electric utilities); discount rate must exceed growth rate (k > g). Not suitable for non-dividend-paying fast-growth firms (use multistage-growth DGM, solved by trial and error). Highly sensitive to g (+1% in g ≈ +1% in kcs).

### 2. Capital Asset Pricing Model (CAPM)
- **Formula:** E(Ri) = Rrf + βi × [E(Rm) − Rrf]
- **Variables:** Rrf = risk-free rate (use the CURRENT effective annual yield; long-term treasury rate preferred as equity is a perpetual claim); βi = beta coefficient (systematic risk; market β = 1, risk-free asset β = 0; unlisted firms: use comparable company beta or industry average); [E(Rm) − Rrf] = market risk premium (not directly observable; estimated from historical averages, e.g. US premium > 5.5% since 1926, ~5.71%)
- **When to apply:** Any company whose beta can be estimated; explicitly adjusts for systematic risk. Disadvantages: market risk premium and beta change over time and rely on historical data.

### 3. Cost of Preference Shares
- **Formula:** kps = Dps / Pps
- **Variables:** Dps = preference dividend (mind payment frequency — a quarterly dividend gives a quarterly rate; annualise by × 4); Pps = current price of preference shares
- **With flotation cost F (new issues):** kps = D / [Pps × (1 − F)]
- **When to apply:** Preference shares without fixed maturity are treated as perpetuities; those with a sinking fund clause (mandatory retirement) may be treated as bonds with fixed maturity. Preference dividends are paid out of after-tax dollars → NO (1 − t) adjustment. CAPM may also be used.

### 4. Cost of Debt
- **Formula:** kDebt after tax = kDebt pretax × (1 − t)
- **Variables:** kDebt pretax = CURRENT cost of long-term debt — for traded bonds the current YTM (adjust for compounding frequency, e.g. semi-annual bond: YTM = 2 × semi-annual yield; use net proceeds to reflect issuance costs; consider EAR); for bank/private debt, the rate the bank would charge to refinance today; t = marginal tax rate
- **When to apply:** WACC always uses the current (marginal) cost, NOT the historical coupon rate shown in financial statements, because WACC is today's opportunity cost of capital. Lines of credit are temporary and excluded. For multiple debt issues: weight each issue by its amount → weighted average pre-tax cost → apply (1 − t) once.

### 5. Weighted Average Cost of Capital (WACC)
- **Formula:** kFirm = Σ xi × ki = xDebt × kDebt pretax × (1 − t) + xps × kps + xcs × kcs
- **Variables:** xi = weight of each source in total capital, based on MARKET values; ki = cost of each source; ONLY debt is tax-adjusted
- **When to apply:** WACC is the most reliable guide to the marginal cost of capital provided the firm keeps investing in projects of standard business risk and raises funds in the same proportions as its existing capital structure. Use firm-wide WACC to discount project cash flows ONLY IF (I) project systematic risk = company portfolio systematic risk AND (II) project financing mix = company financing mix (conventional cash flows are NOT a condition). Otherwise use a risk-adjusted WACC benchmarked on comparable listed companies.

### 6. Benchmark worked WACC (Apply and Analyse 2)
- Debt HK$300m (pre-tax YTM 4.84%), preferred HK$24m (kps = 1.20/12.00 = 10%), common HK$280m (kcs = 2.20/20.00 + 5% = 16%), t = 40%
- Weights: 0.4967 / 0.0397 / 0.4636
- WACC = (0.4967 × 4.84% × 0.60) + (0.0397 × 10%) + (0.4636 × 16%) = 9.26%

## Ch8 Capital Structure Theories

| Formula name | Formula | Variable meanings | When to apply |
|---|---|---|---|
| Firm's enterprise value | VFirm = VAssets = VDebt + VEquity | VDebt = market value of debt; VEquity = market value of equity; VAssets = market value of cash flows generated by assets | Always — the identity linking capital structure claims to asset value; under M&M Proposition 1 (no taxes, perfect markets) VFirm is unchanged by restructuring |
| Value of firm with perpetual cash flows (no growth) | VFirm = CF / i | CF = perpetual annual cash flow; i = discount rate appropriate for the cash flows | Valuing an all-equity firm with constant perpetual cash flows |
| Unlevered firm value (with taxes) | VUnlevered = CF × (1 − t) / i | t = marginal corporate tax rate | When taxes exist: discount AFTER-TAX perpetual cash flows |
| PV of interest tax shield (perpetual debt at par) | PV of tax savings = D × t | D = amount of perpetual debt; t = marginal corporate tax rate | Permanent debt trading at par; annual tax saving (interest × t) discounted at the debt rate, which cancels out |
| Levered firm value (with taxes) | VLevered = VUnlevered + PV of tax shield | — | M&M with corporate taxes: debt increases firm value |
| Weighted average cost of capital (full) | WACC = xDebt × kDebt pretax × (1 − t) + xps × kps + xcs × kcs | x = market-value weight; k = required return; ps = preference shares; cs = common stock; t = tax rate | General WACC with debt, preference shares and common stock |
| WACC (simplified, no taxes, no preference shares) | WACC = xDebt × kDebt + xcs × kcs = kAssets | xDebt + xcs = 1 | Under M&M Proposition 1 conditions: WACC is constant regardless of capital structure and equals the required return on assets |
| Capital structure weights | xDebt = VDebt / (VDebt + Vcs); xcs = Vcs / (VDebt + Vcs) | VDebt = dollar value of debt; Vcs = dollar value of common stock | Computing WACC weights from market values |
| M&M Proposition 2 — required return on common stock | kcs = kAssets + (VDebt / Vcs) × (kAssets − kDebt) | kAssets = required return on assets (business risk); (VDebt/Vcs)(kAssets − kDebt) = financial risk premium | Finding the new cost of equity after a change in leverage; shows kcs rises linearly with the debt-to-equity ratio |
| Gains/losses from a naked short (forward) position | Profit (loss) = (F − ST) × n | F = forward price; ST = spot price at settlement; n = number of contracts (or units) | Pricing hedge/speculation payoffs on forward contracts; reverse the sign for a long forward position |
| Arbitrage pricing theory (APT) | ERi = a0 + bi1F1 + bi2F2 + … + binFn | ERi = expected return on security i; a0 = expected return on a zero-systematic-risk security; bi = sensitivity of security i to risk factors 1…n; F = risk premium for each factor | Multifactor expected-return model based on the no-arbitrage principle; collapses to CAPM with a single (market) factor |

**Key rules / facts (non-formula):**
- M&M Proposition 1 conditions: (1) no taxes; (2) no information or transaction costs; (3) no bankruptcy costs; (4) companies and investors have equivalent borrowing costs; (5) symmetrical market information; (6) capital structure does not affect real investment policies.
- Business risk components: variation in unit sales, unit prices, production/selling costs, and the degree of operating leverage. Financial risk: fixed interest/principal payments to lenders — grows with leverage. Total equity risk = business + financial risk.
- Trade-off theory: add debt until marginal cost = marginal benefit → target capital structure that maximises firm value (tax shield vs agency/financial distress costs).
- Signalling theory: debt-increase announcements viewed positively; debt-reduction announcements viewed negatively.
- Pecking order: internal funds (retained earnings) → new debt → new common equity (most expensive).
- Agency costs of debt: asset substitution problem (shareholders swap safer assets for riskier ones at lenders' expense); underinvestment problem (distressed shareholders reject positive NPV projects because gains accrue to lenders).
- Hedging lowers existing risk exposure; speculating trades high risk for expected returns; arbitraging exploits price imbalances across markets/forms.
- Forwards: customised, OTC, can eliminate basis risk. Futures: standardised, exchange-traded, marked to market daily. Plain vanilla swap = fixed-for-floating interest rate swap in one currency; gains arise from comparative advantage (total saving = fixed spread − floating spread). Options: call (right to buy) / put (right to sell); European (exercise at expiry only) vs American (any time before expiry) vs Bermudan (specific dates).
- Four motives for holding cash: transactions, precautionary, finance, speculative.
- Financing plan components: (1) external funding needed and sources; (2) desired capital structure; (3) payout policy. Investment banks perform origination, underwriting (most common: firm commitment) and distribution.

## Ch9 Financial Analysis and Profitability

**Stock Exchange Indicators / Market-Based Ratios**
- Price-to-book ratio (P/B) = Market value of equity per share ÷ Book value of equity per share. When: assess whether market value exceeds accumulated equity investment; P/B < 1 = no reasonable value created for shareholders.
- Earnings per share (EPS) = Net income ÷ Shares outstanding. When: per-share profitability for shareholders/investors.
- Price–earnings ratio (P/E) = Price per share ÷ EPS. When: market value placed on each HK$1 of earnings; meaningless when EPS negative/very low. Forward P/E = Price ÷ Estimated EPS (EEPS).
- Book value per share (BVPS) = Shareholders' equity ÷ Number of shares.
- Dividend yield = DPS ÷ Current share price (P). Dividend payout = DPS ÷ EPS.
- EBITDA multiple = Total enterprise value (TEV) ÷ EBITDA; TEV = equity market value + market value of debt. When: takeover/whole-firm valuation.

**Short-term Solvency / Liquidity Ratios**
- Current ratio = Current assets ÷ Current liabilities. When: ability to pay current liabilities; < 1 is a warning sign.
- Quick ratio (acid test) = (Cash + Marketable securities + Accounts receivable) ÷ Current liabilities. When: stricter liquidity test; excludes inventory (least liquid current asset).

**Financial Leverage / Long-term Solvency Ratios**
- Total debt ratio = Total liabilities ÷ Total assets.
- Debt-to-equity ratio = Total debt ÷ Total equity.
- Equity multiplier = Total assets ÷ Total equity = 1 + Debt-to-equity. All three linked by TA = TL + SE — knowing one gives the other two.
- Times-interest-earned (TIE) = EBIT ÷ Interest.
- Cash coverage ratio = (EBIT + Depreciation/Amortisation) ÷ Interest. When: cash-based ability to pay interest.

**Asset Management Efficiency (Activity) Ratios**
- Receivables turnover = Sales ÷ Accounts receivable (avg/ending); Days' receivables = 365 ÷ Receivables turnover.
- Payables turnover = Net credit purchases ÷ Accounts payable (alt: COGS ÷ AP); Days' payables = 365 ÷ Payables turnover.
- Inventory turnover = COGS ÷ Inventory (avg/ending); Days' inventory = 365 ÷ Inventory turnover.
- Fixed asset turnover = Sales ÷ Net fixed assets.
- Total asset turnover = Sales ÷ Total assets.

**Profitability Ratios**
- Gross profit margin = (Net sales − COGS) ÷ Net sales.
- Operating profit margin = EBIT ÷ Net sales (EBITDA margin uses EBITDA).
- Net profit margin = Net income ÷ Net sales = (EBIT/Sales) × (EBT/EBIT) × (Net income/EBT).
- EBIT return on assets (EROA) = EBIT ÷ Total assets. When: pre-tax operating efficiency; numerator (earnings to both debtholders & shareholders) matches denominator (investment by both).
- Return on assets (ROA) = Net income ÷ Total assets.
- Return on equity (ROE) = Net income ÷ Total equity.
- Average asset/equity value = (Beginning + Ending) ÷ 2 — preferred for ROA/ROE.

**DuPont System**
- ROA = Net profit margin × Total asset turnover.
- ROE = ROA × Equity multiplier.
- DuPont equation: ROE = Net profit margin × Total asset turnover × Equity multiplier = (NI/Sales) × (Sales/TA) × (TA/TE). Three levers: margin, asset efficiency, leverage.

**Short-term Financial Planning**
- Operating cycle = Days' inventory + Days' receivables.
- Cash conversion cycle (CCC) = Days' inventory + Days' receivables − Days' payables. Negative CCC = excess cash to invest; lower CCC = higher liquidity.

**Cash Flow / Growth / Leverage Measures**
- Free cash flow = Net cash from operating activities − Capital expenditures − Dividends.
- Profitability index (PI) = PV of future cash flows ÷ Initial cost. Accept if PI > 1 (positive NPV).
- Internal growth rate (IGR, no external funding): opening assets → ROA × b; closing assets → (ROA × b) ÷ (1 − ROA × b). b = retention rate = 1 − dividend payout.
- Sustainable growth rate (SGR, constant capital structure): opening equity → ROE × b; closing equity → (ROE × b) ÷ (1 − ROE × b).
- DOL = %ΔEBIT ÷ %ΔSales; DFL = %ΔEPS ÷ %ΔEBIT; DCL = %ΔEPS ÷ %ΔSales = DOL × DFL.

## Ch10 Financial Forecasts and Business Planning

| Name | Formula | Variable meanings | When to apply |
|---|---|---|---|
| Incremental after-tax free cash flow (FCF) | FCF = [(Revenue − Op Ex − D&A) × (1 − t)] + D&A − Cap Exp − Add WC | Revenue = incremental net sales; Op Ex = incremental cash operating expenses; D&A = incremental depreciation & amortisation; t = company's marginal tax rate; Cap Exp = incremental capital expenditures; Add WC = incremental additions to working capital | Capital budgeting / NPV analysis of a project (stand-alone principle); excludes interest & financing cash flows (in discount rate); unchanged fixed costs excluded |
| FCF derivation chain | EBITDA → EBIT = EBITDA − D&A → NOPAT = EBIT × (1 − t) → CF Opns = NOPAT + D&A → FCF = CF Opns − Cap Exp − Add WC | NOPAT = net operating profit after tax (excl. interest) | Step-by-step FCF build-up in OTQ calculations |
| Operating cash flow (indirect method) | OCF = Net income + Depreciation − Increases in assets + Decreases in assets + Increases in liabilities − Decreases in liabilities | Adjust accrual net income for working-capital movements and non-cash items | Converting accrual net income to cash-basis operating cash flow |
| Percent change in sales | %ΔS = (S_{t+1} − S_t) / S_t | S_t = net sales in period t; S_{t+1} = net sales in period t+1 | Sales growth forecast — key driver of financial planning models |
| Dividend payout ratio | Payout ratio = Cash dividends / Net income | — | Pro forma profit forecasts; payout + retention = 1 |
| Retention (plowback) ratio | Retention ratio = Addition to retained earnings / Net income = 1 − Payout ratio | — | Computing addition to retained earnings for pro forma SOFP and EFN |
| Capital intensity ratio | Capital intensity ratio = Total assets / Net sales | Inverse of total asset turnover | Measures assets needed per HK$1 of sales; higher = more capital intensive = riskier |
| External funding needed (EFN / plug value) | EFN = (Assets/Sales × ΔS) − (Spontaneous liabilities/Sales × ΔS) − Addition to retained earnings | ΔS = forecast sales increase; spontaneous liabilities vary with sales (e.g. accounts payable); notes payable, long-term debt, common stock do NOT vary with sales ('n/a') | Preliminary pro forma statement of financial position (percent-of-sales method); balancing figure |
| Pre-tax operating cash flow (EBITDA) break-even | EBITDA break-even = FC / (Unit Price − Unit VC) | FC = fixed costs; Unit Price − Unit VC = contribution margin per unit (CM) | Cash-required analysis for a business/product line; round units UP |
| Accounting operating profit (EBIT) break-even | EBIT break-even = (FC + D&A) / (Unit Price − Unit VC) | D&A included in numerator | Accounting-profit break-even; always higher than EBITDA break-even |
| Contribution margin ratio | CM ratio = CM / Unit Price | CM = Unit Price − Unit VC | Needed for break-even in sales dollars |
| Break-even sales dollars | Break-even sales $ = FC / CM ratio | — | When break-even is required in revenue terms |

Note: The chapter does NOT present internal growth rate or sustainable growth rate formulas — do not import them from other texts; growth funding is handled via the EFN/plug-value approach above.

## Ch11 Strategic Management Accounting Framework

**SMA Core Concepts**
- Strategic management accounting (SMA) = brings together strategic business objectives with management accounting information → forward-looking projections and models. When: distinguishing SMA (external focus: cost trends, prices, market share, competitors, suppliers, technologies; sequence of decisions) from traditional management accounting (internal, introspective, single issue/period; originated as an expansion of cost accounting).
- SMA triangular structure — three considerations: Technical analysis / Behavioural considerations / Cultural considerations. Examined in light of QCT factors: Quality, Cost, Time.
- Current issues: globalisation of supply/value chains; coordination between SMA (formulates forward-looking strategies) and traditional management accounting (implements them); value beyond financial measures (ESG, brand loyalty, consumer opinion — not quantifiable in monetary terms).
- Strategy cascade: Board of directors sets mission, vision, long-term goals (5–10+ years) → senior management formulates strategic plans → implemented via tactics → quantified by annual budgets (planning, control, performance measurement).

**Business Planning Process — Five Steps (Exhibit 11.1, in order)**
1. Develop a strategy; 2. Estimate revenues, expenses and other financial variables; 3. Create an operating budget; 4. Analyse any potential risks and deviations (worst-case to best-case); 5. Monitor and review performance and results. Planning is ongoing; strategic plans forecast 1–5+ years.

**Inventory Management Approaches (11.4.1)**
- EOQ model: optimal inventory level minimising shortage + carrying costs (point where carrying costs = shortage costs); assumes constant sales rate → unsuitable for seasonal products.
- MRP (Materials Requirement Planning): computerised system aligning inventory with production schedules; computes raw materials/in-process inventory needed for a given order volume.
- JIT: goods manufactured/purchased/delivered exactly when needed; near-zero inventory; needs close supplier relationships and finely tuned logistics; ideal = delivery straight to shelf.

**TQM (11.4.2)**
- Goal: zero defects. Four-step cycle PDCA (Plan, Do, Check, Act): (1) Identify and plan (find root cause); (2) Take action (implement fix + measurement system); (3) Check the results (before/after testing); (4) Disseminate the information. Repeated continually.

**Product Life Cycle Costing (11.4.3)**
- Four phases in order: Introduction → Growth → Maturity → Decline. (Maturity: defend market share, downward price pressure → target costing introduced; cash flows may be positive.)
- Life cycle costing (LCC): tracks/accumulates actual costs and revenues from invention until termination = total cost of ownership; long-term view vs traditional cost accounting's focus on immediate accounting periods.

**Target Costing (11.4.4) — FORMULA**
- Target cost = Market price − Desired profit (Exhibit 11.2). When: prices set by supply and demand → profitability pursued through cost control; target cost must cover ALL production costs over the product's entire life cycle; reverses the traditional design→cost→price procedure.

**Quality Costing (11.4.5) — Four COQ Categories**
- Total cost of quality = Prevention + Appraisal + Internal failure + External failure costs.
- Prevention: prevent problems (specifications, QA system/department, TQM training). Appraisal: monitor conformance (supplier pre-approvals, audits, verification). Internal failure: defects found BEFORE delivery (rework, defect-cause investigation, unusable stock losses). External failure: defects found AFTER delivery (complaints, warranty repairs, return/recall transport).
- In COQ theory "quality cost" = cost of POOR quality; quality costs may be 10%–30% of sales and 25%–40% of operating expenses; ABC is a proven tool to identify/quantify the four categories.

**Theory of Constraints (11.4.6)**
- TOC (Goldratt, "The Goal", 1984): identify and manage constraints/bottlenecks → profit rises; fixing constraints beats chasing full capacity. Tools: Five focusing steps (Identify → Exploit → Subordinate → Elevate → Repeat), Thinking processes (What needs changing? What to? What actions?), Throughput accounting.
- Constraints: internal (demand > capacity: equipment, skills, policies) vs external (output > market demand → create more demand). Throughput accounting treats inventory as a LIABILITY (vs traditional accounting's ASSET).

**Throughput Analysis (11.4.7) — FORMULAS**
- Throughput = Revenue − Totally variable expenses.
- Net profit = Throughput − Operating expenses.
- ROI = Net profit ÷ Investment (investment = cash invested to increase production capacity).
- Decision priority: increase throughput (no theoretical upper limit) > reduce operating expenses (floor of zero); evaluates investment decisions by impact on the WHOLE company.

## Ch12 Pricing Strategies and Decisions

### Formulas & Calculation Rules

| Name | Formula | Variable meanings | When to apply |
|---|---|---|---|
| Cost-plus formula | Cost + (Mark-up % × Cost) = Target selling price | Mark-up % = profit expressed as % of cost; Mark-up = Selling price − Cost | Total cost-plus pricing when cost base and desired mark-up are known (List of Formulas, Exhibit 12.5) |
| Margin-based price | Price = Cost ÷ (1 − Profit margin %) | Profit margin % = profit as % of SELLING PRICE | When the required profit is stated as a margin on sales, e.g. 25% net profit margin: 780 ÷ 0.75 = HK$1,040 |
| Mark-up-based price | Price = Cost × (1 + Mark-up %) | Mark-up % = profit as % of COST | When profit is stated as a mark-up on cost, e.g. 30% gross profit mark-up: 780 × 1.30 = HK$1,014 |
| ROI-based mark-up per unit | Mark-up = (Desired ROI % × Amount invested) ÷ Units produced | ROI % = target return on investment; Units = planned production volume | Setting mark-up to achieve a target ROI, e.g. (20% × 1,000,000) ÷ 10,000 = HK$20 → price = VC 60 + FC 52 + 20 = HK$132 |
| Total cost-plus selling price | Price = VC per unit + FC per unit + ROI mark-up per unit | FC per unit = total fixed costs ÷ expected units | Full build-up of target selling price (Illustrative Example 5) |
| Gross profit margin | GPM = (Sales − Variable cost) ÷ Sales | Rate (not amount) monitors pricing policy effectiveness | Comparing pricing policies over time / across competitors (Illustrative Example 1) |
| Break-even price | Total operating cost ÷ average attendance (volume) | | Non-profit / single-price setting: 510,000 ÷ 1,200 = HK$425 |
| Break-even volume | Total operating cost ÷ unit ticket price | | 510,000 ÷ 400 = 1,275 attendees |
| Relevant cost minimum price | Sum of future incremental costs + opportunity costs (exclude sunk costs and absorbed/unchanged fixed overheads) | Incremental (differential) costs = extra costs from a short-term change in activity | Special orders / one-off deals: e.g. refurbishment 500 + transport 200 = HK$700/unit minimum; any quote above this is profitable |

### Key Rules & Concepts

- Demand-based optimum: for each price, profit = (Price − Variable cost) × Quantity demanded − Fixed costs; pick the price with the highest profit.
- Cost behaviour: variable (proportional to activity), fixed (unchanged), mixed. Traceability: direct vs indirect (common) costs — NOT the same split as variable/fixed; both direct and indirect costs can be fixed or variable.
- Price taker vs price setter: takers accept market price (petrol, commodities); setters have unique/patented/differentiated products (Intel chips, Starbucks).
- Psychological pricing: price just below a round number (HK$149,999); customers read left to right; advantages include lower price-band perception, easy discounting (ending digit), inventory control.
- Government policy: price ceilings (maximum) / floors (minimum), taxes, tariffs; predatory pricing may be prohibited — HK Competition Ordinance (Cap. 619), enacted 13 Jan 2013.
- Skimming = initial price HIGHER than competitors → early adopters → lower price later (iPhone, patented drugs). Penetration = price LOWER than competitors → rapid volume, market share, economies of scale (FMCG 'No Frill', Xiaomi). Opposite directions.
- Complementary product: one product priced low for volume to boost a high-margin complement (razor & blades). Product line: related products priced in combination; captive pricing (KFC side dishes); loss leaders (supermarkets).
- Volume discounting: lower unit price for large volumes; reasons = attract new customers, competitiveness, lower distribution costs; drawbacks = thinner margins, product devaluation, hard to raise prices later.
- Price discrimination: same product, different prices. 1st degree = max price per unit; 2nd degree = by quantity consumed; 3rd degree = by customer group. More INELASTIC demand → charge MORE (funeral services). Customer groups must not overlap.
- Relevant costing: sunk costs irrelevant; opportunity costs included; materials in continuous use → replacement cost; materials not otherwise used → net realisable value; labour at full capacity → lower of overtime premium vs basic pay + contribution forgone; labour below capacity → hourly rate only; absorbed fixed overheads irrelevant.
- Cost of quality (cost of POOR quality): Preventive, Appraisal, Internal failure, External failure costs. Quality of design (meets customer expectations) vs quality of conformance (matches design specifications). Cheaper to fix internally than after delivery.
- Environmental costs: Conventional, Hidden (in overheads), Contingent (future clean-up), Image and relationship. Oil industry: up to 20% of operating costs. ISO 14001 standard.
- External market factors: Demand, Competition, Government regulation (+ user group, location, time/perishability). Internal: fixed vs variable cost mix; cost-based pricing.
- ABC four steps: (1) form cost pools by activity; (2) allocate only controllable capacity costs; (3) cost drivers with strongest causal relation; (4) denominator volume = practical capacity → reveals unused capacity. Activity hierarchy: unit-level, batch-level, product/customer-level, facility-level.
- Non-profit pricing: Voluntary pricing / PWYW (pay from zero up; German experiment — most paid ~19% below list but volume rose); Ability to pay (banking = "capacity"); Versioning = quality discrimination (suits high fixed / low variable cost, e.g. software); Bundling/memberships capture consumer surplus (= willingness to pay − price paid).

## Ch13 Investment Project Appraisal

| Technique / Concept | Formula | Variable meanings | When to apply / decision rule |
|---|---|---|---|
| Dividend Growth Model | P0 = D1 ÷ (R − g) | P0 = current value/price per share; D1 = dividend in next period = D0 × (1+g); g = constant dividend growth rate; R = required return on ordinary shares / discount rate | Share valuation; valid only when R > g. If g = 0: P0 = D ÷ R |
| Free Cash Flow | FCF = [(Revenue − Op Ex − D&A) × (1 − t)] + D&A − Cap Exp − Add WC | t = marginal tax rate; D&A = depreciation & amortisation; Cap Exp = capital expenditure; Add WC = additions to working capital | Incremental after-tax cash flows for NPV analysis; financing costs excluded (captured in discount rate); WC recovered at project end |
| Valuation under P/E Ratio | P0 = Estimated EPS1 × Justified P/E | EPS1 = next 12 months' estimated earnings per share (leading/forward P/E); lagging P/E uses EPS0 | Relative valuation vs comparable companies |
| Enterprise Value multiples | EV ÷ EBIT / EBITA / EBITDA | EV = market value of entity's capital less cash & cash equivalents (takeover value) | Use EBITA for capital-intensive firms where EBITDA is distorted by high depreciation |
| Accounting Rate of Return (ARR) | ARR = Average net income ÷ Average book value | Average NI = (NI1+…+NIn)/n; Average BV = (BV1+…+BVn)/n or (Opening BV + Closing BV)/2 | Uses accounting numbers, ignores time value of money; accept if ARR > required return; can be manipulated via depreciation method |
| Internal Rate of Return (IRR) | NPV = Σ NCFt ÷ (1 + IRR)^t = 0 (t = 0…n) | NCFt = net cash flow at time t; IRR = discount rate where PV inflows = PV outflows | Accept if IRR > cost of capital; not for mutually exclusive projects; multiple/no solutions if cash-flow signs change more than once |
| Modified IRR (MIRR) | MIRR = [FV(Positive cash flows × Cost of capital) ÷ PV(Initial outlays × Financing cost)]^(1/n) − 1 | FV = future value of positive CFs reinvested at cost of capital; PV = present value of outlays at financing cost | Accept if MIRR > cost of capital; single solution only; not for mutually exclusive projects or capital rationing |
| Net Present Value (NPV) | NPV = PV of net cash flows − Capital investment | Discount at cost of capital / required rate of return (hurdle rate); use nominal CFs with nominal rate | Accept if NPV ≥ 0; reject if NPV < 0; mutually exclusive → pick highest NPV; primary method (maximises shareholder value) |
| Profitability Index (PI) | PI = PV(cash inflows) ÷ PV(cash outflows) | Outflows usually the initial after-tax outlay | Accept if PI > 1 (⇔ NPV > 0); relative measure; useful starting point for ranking under capital rationing — final choice = highest total NPV combination |
| Payback Period | Years to recover initial outlay from cumulative (undiscounted) cash flows | Cash flows assumed even within a year for fractional years | Shorter is better; ignores time value of money and post-cut-off cash flows; cut-off arbitrary |
| Discounted Payback | Years to recover initial outlay from cumulative discounted cash flows | Discount at project discount rate | ≥ simple payback; still ignores post-cut-off cash flows; no objective criterion |
| After-inflation, after-tax break-even rate | B = I ÷ (100 − E) | I = inflation rate; E = effective tax rate | Minimum net return needed just to break even after inflation and taxes (e.g. 5% ÷ 83.5 = 6.0%) |
| Depreciation tax shield | Tax saving = Annual depreciation × tax rate | Straight-line: cost ÷ useful life; Diminishing-balance: fixed % × written-down value | Deduct D&A before tax, add back to NOPAT (non-cash); diminishing-balance gives larger early tax savings |
| Tax on disposal of asset | (Sales proceeds − Remaining book value) × tax rate | Remaining book value = cost − accumulated depreciation | Terminal cash flow adjustment |

## Ch14 Post-Appraisal Audit of Projects

*Note: conceptual chapter — no exam formulas beyond the scorecard indices below.*

**Five stages of a capital investment project**
1. Identification → 2. Analysis → 3. Selection → 4. Implementation → 5. Follow-up or post-audit (post-completion audit; also called the control phase)

**Aim of post-completion audit:** to determine if projects have met expectations (exceed / meet / fall short of goals). Actual results vs expected results (expenses, revenues, cash flows, initial assumptions); differences must be explained.

**Six reasons a post-completion audit is necessary (§14.1.1)**
1. Monitor quality/accuracy of forecasts, predictions, analyses and underlying assumptions
2. Identify systematic errors (e.g. overly optimistic forecasts) and why not corrected earlier
3. Track business operations associated with the project
4. Decide whether sales or costs are out of line, and why
5. Generate new ideas for future projects
6. Provide a benchmark for analysis of future projects

**Three main benefits / lessons learned (§14.1.2)**
1. Lessons for future projects (improve planning, execution, strategic planning process)
2. Identify problems and find solutions (improve cash flows/revenues; abandon failing projects and limit losses)
3. Insert structure into investment planning and control (managers more careful when review is expected; interim audits enable early correction/abandonment)

**Abandonment rule:** capital already invested does NOT justify continuing a failing project; cut costs immediately if future revenues/profits are unlikely to meet expectations.
Typical failure reasons: poor preparation, inadequate marketing, non-competitive pricing, overly optimistic assumptions.

**Team evaluation — 10 criteria (§14.2.1):** understand goals; team agrees on goals; leadership effective; conflicts dealt with; leadership identifies problems & makes decisions; overall process effective; procedures expressed & enforced; communication effective; resources used well; trust among members.
Success factors for a post-completion audit: team evaluations with the right people; timing of the audit; quality of documentation.

**Three evaluation methods (§14.2.2)**
- Yes/no question list: end-of-project; may be weighted; starting point only, not conclusive
- Continuous measurement: limited, clearly expressed criteria on a scale (e.g. 1–10); performed at the end of EACH phase; spots emerging problems before critical — preferred over end-of-project methods
- Baseline performance system: minimally acceptable results set per area; compared to baseline at junctures/phases (e.g. 2-year project in six segments)

**Success criteria – three areas (KCQ4):** deliverable success; process success; stakeholder success.

**Project Scorecard — Pennypacker (2005) ten performance measures (§14.2.3)**
1. ROI = percentage return per dollar invested
2. Productivity = outputs per unit of input
3. Cost of Quality — 4 categories: prevention, appraisal, internal failure, external failure
4. Cost Performance Index (CPI) = Earned Value ÷ Actual Costs (<1 = cost overrun)
5. Schedule Performance Index (SPI) = total authorised project duration ÷ total final project duration (<1 = late)
6. Customer Satisfaction (hard + soft measures)
7. Cycle Time (project life cycle length)
8. Requirement Performance
9. Employee Satisfaction Index (weighted soft + hard measures)
10. Alignment to Strategic Business Goals ("doing the right projects")

**Management neutrality ('neutrality' until done, §14.3)**
- Stay neutral on implementation criteria during implementation and audit; pinpoint responsibility WITHOUT pre-assigning blame
- Minimises the key negative impact of audits: staff withholding proposals for fear of criticism
- Reduces project 'padding'/overestimates and intra-firm agency problems
- Five steps: know the goals; positive environment; let team members work (minimum interference); emphasise the right matters; protect team members with safety standards
- Skills: self-confidence, focus, self-control, consistency, conflict resolution

**Regular times & processes (§14.4)**
- Regular formal reviews avoid delays/extra costs from too many review cycles; streamline decision authority; minimise number of decision makers
- Six common challenges: unrealistic assumptions; lack of reference to life cycle costs and management costs; unsustainable debt; lack of management capacity; lack of funding; abuses or conflicts
- Improvement avenues: prioritise projects; institutional memory; clear investment objectives (avoid pet projects failing NPV targets); regular reviews; track ROI; streamline approvals; frequent forecasts; avoid management silos; continuous improvement

## Ch15 Effective Performance Measurement

**Return on Investment (ROI)**
- Formula: `ROI = Net profit / Average operating assets` (investment centre: `Controllable margin / Average operating assets`)
- Variables: Operating assets = assets used in production of goods/services (cash, AR, inventory, plant & equipment); exclude non-operating assets. Use the AVERAGE of opening and closing operating assets (captures the whole period; prevents manipulation by temporarily cutting investment at measurement date). Only include assets under the evaluated manager's control.
- When to apply: Evaluating investment centres / sub-units; comparable across sub-units, across entities in an industry, and over time. Beware: managers may reject projects with ROI below the division's current ROI even if above the company's required rate; ROI ignores risk and can be overstated when assets are understated (historical cost / depreciation / unrecognised intangibles).

**DuPont model (ROI decomposition)**
- Formula: `ROI = (Net profit / Sales) × (Sales / Average operating assets) = Net profit margin × Asset turnover`
- When to apply: To diagnose WHY ROI is above/below benchmark — profit margin problem vs asset turnover problem (e.g. 3.8% × 1.5 = 5.7%).

**Residual Income (RI)**
- Formula: `RI = Operating income − (Required rate of return × Average operating assets)`
- Variables: Required rate of return = capital charge; average operating assets as above.
- When to apply: Absolute-dollar performance measure. Goal-congruent: managers accept any project with return ≥ required rate of return regardless of the division's current ROI. Limitation: not comparable across divisions of different sizes; managers may set the required rate too low or cut R&D/maintenance/training.

**Economic Value Added (EVA)**
- Formula: `EVA = Adjusted after-tax operating income − [WACC × (Adjusted total assets − Current liabilities)]`
- Variables: Adjusted after-tax operating income replaces EBIT (consistent with after-tax WACC; incentivises tax reduction); (Adjusted total assets − Current liabilities) = invested capital.
- Key adjustments: R&D capitalised (not expensed); long-term operating leases treated as capital leases. Internal measures need not follow HKFRS/GAAP.
- When to apply: Measuring value created above the cost of capital; best at higher organisational levels. Limitations: cost of capital and adjustments involve judgement; complex, expensive, lengthy.

**Weighted Average Cost of Capital (WACC)**
- Formula: `WACC = (E/V × Re) + (D/V × Rd × (1 − Tc))`
- Variables: Re = cost of equity; Rd = pre-tax cost of debt; E, D = MARKET values of equity and debt; V = E + D; Tc = corporate tax rate. Use market values, never book values.
- When to apply: Minimum return needed to satisfy creditors and investors; used in EVA and as a project discount rate ONLY when (1) the project's systematic risk matches the company's, and (2) the project uses the same debt/equity financing mix. Otherwise (SML–WACC analysis): risky projects with negative true NPV get wrongly accepted; low-risk positive-NPV projects get wrongly rejected.

**Segment reporting thresholds (rules, not formulas)**
- Required for publicly held entities only; report separately any segment ≥10% of revenues, profit/loss or assets; reported segments must cover ≥75% of total company revenue (else add segments); combine if more than 10 segments; similar segments may be aggregated.

## Ch16 Financial Risks and Their Management

> Note: Ch16 is concept-heavy. Its ONLY numeric formula is the loan-to-value ratio. Hedging instruments (forwards / futures / options / swaps) appear in this chapter only as **risk-transfer/hedging tools and glossary definitions** — no pricing or payoff formulas are given in this chapter's source text.

### Formula

| Name | Formula | Variable meanings | When to apply |
|---|---|---|---|
| Loan-to-value ratio (LTV) | LTV = Amount borrowed ÷ Total value of the asset | Amount borrowed = loan principal granted by the lender; Total value of the asset = value of the asset being financed | Used by lenders in **risk-based pricing** of credit risk: the lower the LTV, the lower the risk; higher LTV → higher interest rate charged. Source example: HK$310,000 ÷ HK$400,000 = 77.5%. Can be asked three ways: compute LTV; max borrowing = LTV cap × asset value; compare two borrowers (lower LTV = safer). |

### Key rules & instrument definitions (as per source)

**Risk classification**
- Financial risks (4 types): **Credit risk, Foreign investment risk, Liquidity risk, Market risk**. Separate categories: Business risk, Operating risk (Basel II: 'risk of loss resulting from inadequate or failed internal processes, people and systems or from external events'), Sales risk.
- Credit risk subtypes: **Default risk** (borrower fails timely payment, partial or full); **Country risk** (assets frozen in a foreign country that defaults/freezes assets); **Concentration risk** (exposure to a single company or industry); **Sovereign risk** (government unable/unwilling to repay or honour guarantees); **Counterparty risk** (a form of default risk — counterparty fails obligations on loans, bonds, derivatives or insurance policies).
- Liquidity risk: **Asset liquidity** (no ready market; too-wide bid–ask spread) vs **Funding liquidity** (cannot pay liabilities when due — too little cash).
- Market risk subtypes: **Equity risk, Commodity risk, Interest rate risk** (unfavourable changes in rates), **Currency risk** (investment in currency exchange products, e.g. FOREX), **Margin risk** (cannot satisfy a margin call on short positions).

**Credit risk mitigation (6 ways)**: Risk-based pricing (uses credit history, credit rating, LTV); Credit insurance (premium → insurer assumes the risk); Credit derivatives — **Credit default swap (CDS): the seller pays the buyer if a debt default occurs**; Covenants (periodic reports; restrictions on dividends/share repurchases/further borrowing); Diversification (offset concentration risk); Tightening (limit maximum credit; shorten repayment terms, e.g. 30 → 15 days).

**Hedging & derivatives (as covered in Ch16)**
- **Hedging**: entering into a contract with the goal of lowering existing exposure to risk, such as price fluctuations (also called 'covering' — removing a naked position).
- **Derivatives**: options and other contracts used to hedge against financial risk — a form of risk **transfer**; options offset/reduce market risk; other derivatives hedge currency exchange rate risks.
- **Forward**: a contract similar to a futures contract, between two parties, to buy or sell a particular asset in the future (glossary definition).
- **Futures contract**: a legal agreement to buy or sell an asset (typically stocks, commodities or foreign currency) at a predetermined price at some point in the future.
- **Call option**: right, but not the obligation, to BUY an underlying asset at a specified price within a specific period. **Put option**: right, but not the obligation, to SELL an underlying asset at a specific price within a specific time frame.
- **Interest rate swap**: an agreement between two counterparties to exchange streams of future interest payments.
- **Basis risk**: risk in a hedged position because the asset to be hedged is not identical to the asset used as the hedge.
- **Naked position**: a financial position (e.g. security or foreign currency) with NO hedging associated with it.

**FX / foreign investment risk mitigation**
- Foreign investment risk: host-country tax changes, rapid inflation, expropriation/nationalisation of assets, volatile political climate; milder forms: differences in regulation, accounting standards, reporting and audit rules.
- Mitigation: **political risk insurance** (transfer — covers political violence, confiscation, business disruption); **derivatives** to hedge foreign currency depreciation; **natural hedge — borrow in the local currency of the host country to finance local assets** (asset and liability fall together when the currency depreciates).

**Risk management approaches (4)**
- **Avoidance** (remove exposure to a known hazard altogether); **Mitigation** (reduce threat level, not eliminate; steps: identification → impact assessment → analysis → mitigation; follow-up options: acceptance/avoidance/control/transfer/monitoring); **Transfer** (insurance is the most common form; also derivatives, outsourcing by contract); **Acceptance** (conscious assumption of a known risk when management cost > potential loss).
- **Risk avoidance ≠ risk ignorance**: avoidance is a conscious decision after evaluation; ignorance = unaware/unconcerned (no risk assessment performed).

**KRI**
- **KRI**: assigns degrees of risk to activities/threats; estimates probability and potential cost of future losses; monitors KNOWN risks only. **KPI** measures performance of internal routines — not future risk events.
- Risk appetite profiles: **Averse / Minimal / Cautious / Open**.
- KRI development cycle: identify major risks → list underlying causes → analyse metrics → define thresholds and gaps → describe data/frequency/reporting → backtest → loop.
- Risk matrix focus: high impact × high likelihood first.
