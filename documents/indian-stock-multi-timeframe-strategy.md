# Multi-Timeframe Strategy Framework for the Indian Stock Market

> **Reality check:** No strategy gives 100% accuracy. Even the best professional systems win about 40-65% of trades. What makes money is **positive expectancy**: winners bigger than losers, a strict stop loss, and filters that only let high-probability setups through.
>
> This is not financial advice. Backtest everything before using real money.

---

## Core Idea: Multi-Timeframe Alignment

Use the higher timeframe for **direction**, the middle one for the **setup**, and the lower one for the **entry**. Only trade when all three agree.

| Style | Direction (trend) | Setup | Entry trigger |
|---|---|---|---|
| Intraday | 1 hr / 15 min | 15 min / 5 min | 5 min / 1 min |
| Swing (days to weeks) | Weekly | Daily | 4 hr / 1 hr |
| Positional (weeks to months) | Monthly | Weekly | Daily |

---

## Layer 1: Universe Filter (run first, removes bad stocks)

- Index membership: Nifty 200 / Nifty 500, or F&O stocks (better liquidity)
- Average daily volume (20 days) > 5 lakh shares, or traded value > ₹20 Cr
- Price > ₹50 (avoids penny-stock manipulation)
- Not in the F&O ban list, not in ASM/GSM surveillance
- Beta: 0.8 to 1.8 for trend trades (below 0.8 is too sluggish, above 1.8 is too wild)
- ATR(14) as % of price: 1% to 4% on daily (enough movement, not chaos)

---

## Layer 2: Trend Filter (higher timeframe)

**Bullish:**

- Close > EMA 50 > EMA 200
- EMA 20 slope is rising
- ADX(14) > 20 (a trend exists; below 20 means sideways, so skip)
- Supertrend (10,3) is green
- Price > VWAP (for intraday)

**Bearish:** the exact opposite (for shorts, intraday or F&O only).

---

## Layer 3: Setup (pick one per style)

### A. Pullback in trend (best risk/reward)

- Trend filter is bullish
- Price pulls back to EMA 20 or EMA 50, or to the VWAP
- RSI(14) dips to 40-50 and turns up (it should not fall below 40 in an uptrend)
- Volume on the pullback candles is lower than average

### B. Breakout

- Close above the 20-day high (or the opening range high for intraday)
- Volume > 1.5x to 2x the 20-period average volume
- Bollinger Band width was narrow just before (a squeeze), now expanding
- RSI > 60, ADX rising

### C. Momentum / relative strength

- Stock's 1-month and 3-month performance is in the top 20% of the universe
- Stock outperforms Nifty over the same period
- Close within 5% of the 52-week high

---

## Layer 4: Entry Trigger (lower timeframe)

- A bullish candle closing above the previous candle's high
- MACD line crosses above the signal line, or the histogram turns positive
- Volume on the trigger candle > the previous 3 candles
- For intraday, avoid entries in the first 15 minutes (9:15-9:30) and after 2:45 PM

---

## Layer 5: Risk Management (matters more than the entry)

- **Stop loss:** 1.5 x ATR below entry, or below the swing low
- **Target:** at least 1:2 risk-to-reward, then trail with EMA 20 or Supertrend
- **Position size:** risk only 0.5% to 1% of capital per trade
- **Daily loss limit:** stop trading after a 2-3% loss for the day
- **Max open trades:** 3 to 5, and not all in the same sector
- **Market filter:** if Nifty is below its 50 EMA on the daily chart, take fewer or no longs
- Account for brokerage, STT, and slippage, which can eat a lot of intraday profit

---

## Example: Ready-to-Use Intraday Long Screener (15 min)

```
Universe: Nifty 200, avg volume(20) > 5L, price > 50
15m: Close > EMA(50) AND EMA(20) > EMA(50)
15m: ADX(14) > 20
15m: Close > VWAP
1h:  Close > EMA(50)
5m:  RSI(14) crosses above 50
5m:  Volume > 1.5 x SMA(Volume, 20)
Time: between 9:30 and 14:45
Stop: 1.5 x ATR(14) on 5m | Target: 2 x risk
```

---

## How to Get Closer to a "Perfect" System

1. **Backtest** on at least 3-5 years of data across both bull and sideways markets.
2. **Track the metrics that matter:** win rate, average win vs average loss, max drawdown, and profit factor (aim for above 1.5).
3. **Avoid over-fitting.** More conditions do not mean better results. Beyond 5-6 conditions you are usually fitting noise, not finding an edge.
4. **Paper trade** for 1-2 months before going live.
5. **Review monthly** and change one thing at a time.

---

## Next Steps

- List the fields your screener supports (EMA, ADX, Supertrend, VWAP, relative strength, or only basic price and volume).
- Choose which style to build first (intraday, swing, or positional).
- Convert the rules above into exact filter conditions, or into a Python backtesting script.
