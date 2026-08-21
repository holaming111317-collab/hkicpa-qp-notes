# M7 Equities Valuation — Study Pack (Week 5)

## Phase 1: Core Concepts & Formula Cheat Sheet 重點梳理與速查表

### 1. 核心知識架構

- **股票種類 (Types of Equities)**：Ordinary shares（普通股）代表公司基本所有權，有投票權 (voting rights)、limited liability（法律責任限於原投資額）、無保證股息、無到期日（perpetuity）；Preference shares（優先股）在股息及清盤分派上優先於普通股，但一般無投票權、股息固定、以稅後盈利支付，常被視為介乎債券與股票之間的 hybrid security。
- **股息政策與種類 (Dividends)**：Dividend 是按持股比例 (pro rata) 分派現金或股票；派息三大前提為 retained earnings、adequate cash、declared dividends；形式包括 cash、property、scrip、stock；現金股息分 regular / extra / special cash dividends 三類。
- **估值三步曲 (Three-step Valuation)**：(1) Estimate expected future cash flows；(2) Determine the required rate of return (discount rate)；(3) Compute the present value。股票價值 = 未來現金流的現值，即 PV (stock) = PV (dividend) + PV (sale price)。
- **股息貼現模型家族 (Dividend Discount Models)**：由 one-period model 推展至 general dividend valuation model（P0 = 所有未來股息的 PV），再按股息增長假設簡化為 zero-growth（P0 = D/R）、constant-growth / Gordon growth（P0 = D1/(R−g)）及 mixed (supernormal) growth 模型。
- **股息時間線 (Dividend Timeline)**：Board vote → Public announcement (declaration date) → Ex-dividend date → Record date → Payable date；股價在 ex-dividend date 調整（香港個人投資者股息免稅，除息日股價理論上下跌約等於股息額，研究顯示實際跌幅略少於全部股息）。

### 2. 必背考點清單（公式速查）

| 公式名稱 | 公式 | 變數定義 | 適用條件 |
|---|---|---|---|
| Single-period valuation | P0 = (D1 + P1) / (1 + R) | P0 現價；D1 期末股息；P1 期末股價；R required return | 持有一期後賣出，現金流確定 |
| General dividend valuation model | P0 = Σ Dt / (1+R)^t（t = 1 → ∞） | Dt 第 t 期股息 | 不對股息模式或出售時間作任何假設；理論基礎 |
| Zero-growth valuation | P0 = D / R | D 每期固定股息；R required return | 股息永遠不變（g = 0）；適用於無增長公司及 perpetual preference shares |
| Constant-growth (Gordon) valuation | P0 = D1 / (R − g)；D1 = D0 × (1 + g) | D1 下一期股息；g 固定股息增長率 | **只在 R > g 時有效**；R ≤ g 時結果無意義；適用於增長穩定的成熟公司 |
| Future stock price (constant growth) | Pt = D(t+1) / (R − g) | Pt 第 t 期股價 | 股息由第 t+1 期起按 g 固定增長；股價本身亦按 g 增長（Pt = P0(1+g)^t） |
| Mixed (supernormal) growth | P0 = D1/(1+R) + D2/(1+R)² + … + Dt/(1+R)^t + Pt/(1+R)^t，其中 Pt = D(t+1)/(R−g) | 高增長期逐年股息 + 轉入固定增長時點的終值 | 兩段式增長：初期 supernormal growth，之後穩定為常數 g；須分辨固定增長由哪一年開始 |
| Preference share — fixed maturity | P0 = Σ (D/m)/(1+i/m)^t + P/(1+i/m)^(mn) | D 年度優先股息；P stated/par value；i yield to maturity；m 每年派息次數；n 到期年數 | 有強制贖回/到期條款（如 sinking fund），按債券估值模式處理 |
| Preference share — no maturity | P0 = D / R | D 固定股息；R required rate of return | 無到期日的 perpetual preference share，按永續年金估值 |

**其他必考事實：**
- 股息從 **after-tax earnings** 支付，**not tax deductible**（有別於債券利息可扣稅）。
- 股息**不會累計 (do not accrue)**，未宣派前不是負債；宣派與支付現金股息會令 equity 及 total assets 同時下降。
- Cumulative preference shares：未付的股息稱為 **dividends in arrears**，必須連同當年股息先付清，普通股股東才可收息；拖欠金額須在財務報表附註披露。
- Stock dividend（如 10%）：股數增加、每股價值下降、股東總價值不變；Scrip dividend = 股東可選擇收現金或股票。Stock split（如 2-for-1）：股數倍增、股價減半、總值不變；公司拆細股份旨在令股價回落至合適交易區間。
- 計算 D1 時的起點永遠是 **D0 × (1+g)**；計算 Pt 時用 **D(t+1)**——考試最常見陷阱就是用錯 D0 或 Dt。

### 3. 易混淆概念對比 (Common Pitfalls)

**Pitfall 1：D0 vs D1 —— Gordon growth model 的分子**
- 對比：P0 = D1/(R−g) 中的 D1 是**下一期（未來）**股息；題目若給「剛派發的股息 D0」，必須先乘 (1+g)。若直接將 D0 除以 (R−g)，會低估股價。
- 例子：公司昨天派息 HK$2.15（D0），g = 5%，R = 15%。正確：P0 = 2.15 × 1.05 / (0.15 − 0.05) = HK$22.58；錯誤做法 2.15/0.10 = HK$21.50。相反，若題目直接說「next year's dividend will be HK$2.26」，那就是 D1，不可再乘 (1+g)。

**Pitfall 2：Constant-growth model 的適用條件（R > g）vs Supernormal growth**
- 對比：Gordon growth model 假設股息**由現在起**永遠按單一固定比率 g 增長，且 **g 必須小於 R**，否則分母為零或負數、結果無意義；公司若處於高速增長期（g > R 或增長率逐年不同），必須改用 mixed (supernormal) growth 模型：逐年折現高增長期股息，再在穩定增長起點用 Pt = D(t+1)/(R−g) 求終值，一併折現回 t=0。
- 例子：D1 = HK$1、D2 = HK$2、D3 = HK$3，之後 g = 6%，R = 15%。不能直接用 P0 = D1/(R−g)；正確做法是先算 P3 = D4/(R−g) = 3.18/0.09 = HK$35.33，再 P0 = 1/1.15 + 2/1.15² + (3 + 35.33)/1.15³ = HK$27.58。

---

## Phase 2: Bilingual Flashcards 雙語記憶閃卡

* [Flashcard 1]
  - Front (Question in English): What are the three conditions a company must meet before it can pay a cash dividend?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Retained earnings — dividends may legally be paid from retained earnings, not from legal capital (payments from paid-in capital are liquidating dividends).
      - Adequate cash — the board must consider current and future demands on the company's resources.
      - Declared dividends — dividends do not accrue and are not a liability until the board of directors formally declares them.
    - [中文白話解釋]：派息要過三關：首先要有 retained earnings（累積盈利）先可以合法派息，用股本 (legal capital) 派息屬於 liquidating dividend；其次公司要有足夠現金應付派息後的營運需要；最後必須經董事會正式宣派 (declare)，未宣派前股息不是負債，亦不會像利息般累計。

* [Flashcard 2]
  - Front (Question in English): State the zero-growth dividend valuation formula and identify the type of security for which it is most typically used.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Formula: P0 = D / R, where D = constant cash dividend per period and R = required return.
      - The dividend stream is a perpetuity with a constant cash flow (g = 0).
      - Most typical application: preference shares with no maturity, and common stock of companies that are not growing (e.g. the preference shares of a utility company).
    - [中文白話解釋]：零增長模型其實就是永續年金 (perpetuity) 公式：固定股息 D 除以要求回報率 R。最典型用嚟計無到期日的優先股 (perpetual preference shares)，因為優先股息固定唔會增長；亦適用於完全無增長的普通股公司。

* [Flashcard 3]
  - Front (Question in English): A company just paid a dividend (D0) of HK$2.50. Dividends are expected to grow at a constant rate of 5% and the required return is 15%. Calculate P0 and P5 (the share price five years from now).
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - D1 = D0 × (1 + g) = 2.50 × 1.05 = HK$2.625.
      - P0 = D1 / (R − g) = 2.625 / (0.15 − 0.05) = HK$26.25.
      - P5 = D6 / (R − g); D6 = 2.50 × (1.05)^6 = HK$3.35; P5 = 3.35 / 0.10 = HK$33.50.
      - Check: P5 / (1.05)^5 = 33.50 / 1.2763 ≈ HK$26.25 = P0 — under constant growth, the share price itself also grows at rate g.
    - [中文白話解釋]：記住 Gordon model 的分子一定係「下一期」股息，所以 D0 要先乘 (1+g) 變成 D1。計 P5 時要用 D6（即第 6 年股息），因為 P5 係第 5 年尾企住睇將來的價值。有個好好用的檢查方法：固定增長下股價本身都按 g 增長，所以 P5 = P0 × (1+g)^5，兩條路計出嚟答案一樣就啱。

* [Flashcard 4]
  - Front (Question in English): Under what condition is the constant-growth (Gordon) dividend model valid, and what should an analyst do if a firm's growth rate exceeds the required return during its early years?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Valid only if g < R. Results are meaningless if R ≤ g (the denominator becomes zero or negative).
      - If the firm has supernormal growth early on (growth rates varying year by year or g > R), use the mixed (supernormal) growth model instead.
      - Steps: discount each dividend in the high-growth phase individually; at the point constant growth begins, compute the terminal price Pt = D(t+1) / (R − g); discount Pt back to t = 0; sum all present values.
    - [中文白話解釋]：Gordon model 有一個硬性條件：g 一定要細過 R，否則條數計出嚟無意義。遇到公司頭幾年高速增長（增長率逐年唔同，或者 g 仲大過 R），就要用兩段式 mixed growth 模型：高增長期的股息逐年折現，穩定增長開始嗰一刻用 Pt = D(t+1)/(R−g) 計終值，再折返今日，加埋就係 P0。

* [Flashcard 5]
  - Front (Question in English): A perpetual preference share pays an annual dividend of HK$5.00 and investors require an 8% rate of return. Calculate the value of the preference share. How would the valuation change if the share instead had a fixed maturity?
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - No maturity: value as a perpetuity, P0 = D / R = 5.00 / 0.08 = HK$62.50.
      - Fixed maturity (e.g. mandatory retirement / sinking fund): treat it like a bond — P0 = PV of dividend payments + PV of stated (par) value at maturity, discounting at the yield to maturity with the appropriate payment frequency (D/m, i/m, m × n periods).
    - [中文白話解釋]：無到期日的優先股當永續年金計，D 除 R 就搞掂，呢題答案係 HK$62.50。但如果合約寫明到期要贖回（例如有 sinking fund 條款），就要改用債券估值模式：每期股息折現加埋到期時 stated value 的折現，仲要按派息頻率調整（每季派息就 m = 4，利率同期數都要轉換）。

* [Flashcard 6]
  - Front (Question in English): An investor owns 1,000 shares priced at HK$24 each. The company announces (a) a 10% stock dividend and (b) a 3-for-1 stock split. For each event, state the number of shares held and the total value of the holding afterwards.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - (a) 10% stock dividend: shares rise to 1,000 × 1.10 = 1,100; total value unchanged at HK$24,000 (per-share value falls to HK$24,000 / 1,100 ≈ HK$21.82).
      - (b) 3-for-1 stock split: shares rise to 1,000 × 3 = 3,000; price falls to HK$24 / 3 = HK$8; total value unchanged at HK$24,000.
      - Neither event distributes value; proportional ownership is unchanged. Stock dividends are generally scheduled events; stock splits are infrequent and are used to bring the share price down to an appropriate trading range.
    - [中文白話解釋]：無論係 stock dividend 定 stock split，都係「股數變多、每股價值變細、總值不變」——公司無真係派咗價值出嚟。紅股 (stock dividend) 係按比例送新股；拆細 (stock split) 係將一股拆成幾股。考試見到呢類題，第一步就係計總值（股數 × 股價）係咪前後一致，唔一致的選項即刻刪。

* [Flashcard 7]
  - Front (Question in English): List the five steps in the dividend payment timeline for a publicly traded company, and state on which date the share price adjusts for the dividend.
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Timeline: (1) Board vote → (2) Public announcement (declaration date) → (3) Ex-dividend date → (4) Record date → (5) Payable date.
      - The share price adjusts on the ex-dividend date — the first date the stock trades without rights to the dividend. Buying before this date entitles the investor to the dividend (cum dividend); buying on or after it does not (ex dividend).
      - With no taxes, the price should drop by the amount of the dividend; research shows prices actually drop by slightly less than the full dividend. The record date is usually about two business days after the ex-dividend date; the three key dates are the declaration, record and payment dates.
    - [中文白話解釋]：股息流程五部曲：董事會表決 → 對外宣佈 (declaration date) → 除息日 (ex-dividend date) → 股東名冊截止日 (record date) → 派息日 (payable date)。最考得起嘅係：股價喺除息日調整（唔係 record date 或 payable date），因為除息日之後買入嘅投資者收唔到今次股息；無稅情況下股價理論上會跌足成個股息額。

* [Flashcard 8]
  - Front (Question in English): Distinguish between regular cash dividends, extra cash dividends and special cash dividends, and explain why preference share dividends are sometimes said to make preference shares "debt-like".
  - Back (Answer & Explanation):
    - [English Point-form Answer]:
      - Regular cash dividends: paid in cash on a regular basis (annually or quarterly); the most common way to distribute profits.
      - Extra cash dividends: paid when earnings are higher than expected, often alongside regular dividends, e.g. to hit a target payout ratio.
      - Special cash dividends: one-time payments, generally much larger, e.g. distributing proceeds from selling a major asset or effecting a capital-structure change.
      - Preference shares are debt-like because: fixed dividend regardless of earnings; no voting rights (for regular non-convertible preference shares); stated (not residual) value on liquidation; credit ratings similar to bonds; often have call/retirement dates so they are not true perpetuities.
    - [中文白話解釋]：三種現金股息分別在於規律同規模：regular 係定期派、最常見；extra 係業績好過預期時加碼；special 係一次過嘅大額分派（例如賣資產套現）。至於優先股似債券，係因為股息固定、無投票權、清盤時只攞 stated value、有信貸評級、通常有贖回日期——但記住佢法律上仍係 equity，股息唔可以扣稅，唔派息亦唔構成 default。

Phase 3 測驗題目及答案請見另外兩個檔案：*_Quiz.md / *_Answers.md
