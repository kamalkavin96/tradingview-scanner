import json
from pathlib import Path

# Regular indicator timeframes
timeframes = [
    ("1min", "1"),
    ("5min", "5"),
    ("15min", "15"),
    ("30min", "30"),
    ("1hour", "60"),
    ("2hour", "120"),
    ("4hour", "240"),
    ("1day", ""),
    ("1week", "1W"),
    ("1month", "1M")
]

# Candlestick pattern timeframes (special naming convention)
candlestick_timeframes = [
    ("1min", "1m"),
    ("5min", "5m"),
    ("15min", "15m"),
    ("30min", "30m"),
    ("1hour", "1h"),
    ("2hour", "2h"),
    ("4hour", "4h"),
    ("1day", "1D"),
    ("1week", "1W"),
    ("1month", "1M")
]

indicators = [
    # ADX
    ("adx", "ADX_Positive_DI", "ADX+DI"),
    ("adx", "ADX_Negative_DI", "ADX-DI"),
    ("adx", "ADX", "ADX"),

    # Other indicators
    ("awesome_oscillator", "AwesomeOscillator", "AO"),
    ("bollinger_band", "BollingerBandPower", "BBPower"),
    ("cci", "CCI20", "CCI20"),

    # EMA
    ("ema", "EMA_10", "EMA10"),
    ("ema", "EMA_20", "EMA20"),
    ("ema", "EMA_30", "EMA30"),
    ("ema", "EMA_50", "EMA50"),
    ("ema", "EMA_100", "EMA100"),
    ("ema", "EMA_200", "EMA200"),

    # Moving averages and trend
    ("hull_ma", "HullMA_9", "HullMA9"),
    ("ichimoku", "Ichimoku_BaseLine", "Ichimoku.BLine"),

    # MACD
    ("macd", "MACD_Line", "MACD.macd"),
    ("macd", "MACD_Signal", "MACD.signal"),

    ("momentum", "Momentum", "Mom"),

    # Pivot Camarilla
    ("pivot_camarilla", "Middle", "Pivot.M.Camarilla.Middle"),
    ("pivot_camarilla", "R1", "Pivot.M.Camarilla.R1"),
    ("pivot_camarilla", "R2", "Pivot.M.Camarilla.R2"),
    ("pivot_camarilla", "R3", "Pivot.M.Camarilla.R3"),
    ("pivot_camarilla", "S1", "Pivot.M.Camarilla.S1"),
    ("pivot_camarilla", "S2", "Pivot.M.Camarilla.S2"),
    ("pivot_camarilla", "S3", "Pivot.M.Camarilla.S3"),

    # Pivot Classic
    ("pivot_classic", "Middle", "Pivot.M.Classic.Middle"),
    ("pivot_classic", "R1", "Pivot.M.Classic.R1"),
    ("pivot_classic", "R2", "Pivot.M.Classic.R2"),
    ("pivot_classic", "R3", "Pivot.M.Classic.R3"),
    ("pivot_classic", "S1", "Pivot.M.Classic.S1"),
    ("pivot_classic", "S2", "Pivot.M.Classic.S2"),
    ("pivot_classic", "S3", "Pivot.M.Classic.S3"),

    # Pivot Demark
    ("pivot_demark", "Middle", "Pivot.M.Demark.Middle"),
    ("pivot_demark", "R1", "Pivot.M.Demark.R1"),
    ("pivot_demark", "S1", "Pivot.M.Demark.S1"),

    # Pivot Fibonacci
    ("pivot_fibonacci", "Middle", "Pivot.M.Fibonacci.Middle"),
    ("pivot_fibonacci", "R1", "Pivot.M.Fibonacci.R1"),
    ("pivot_fibonacci", "R2", "Pivot.M.Fibonacci.R2"),
    ("pivot_fibonacci", "R3", "Pivot.M.Fibonacci.R3"),
    ("pivot_fibonacci", "S1", "Pivot.M.Fibonacci.S1"),
    ("pivot_fibonacci", "S2", "Pivot.M.Fibonacci.S2"),
    ("pivot_fibonacci", "S3", "Pivot.M.Fibonacci.S3"),

    # Pivot Woodie
    ("pivot_woodie", "Middle", "Pivot.M.Woodie.Middle"),
    ("pivot_woodie", "R1", "Pivot.M.Woodie.R1"),
    ("pivot_woodie", "R2", "Pivot.M.Woodie.R2"),
    ("pivot_woodie", "R3", "Pivot.M.Woodie.R3"),
    ("pivot_woodie", "S1", "Pivot.M.Woodie.S1"),
    ("pivot_woodie", "S2", "Pivot.M.Woodie.S2"),
    ("pivot_woodie", "S3", "Pivot.M.Woodie.S3"),

    # RSI
    ("rsi", "RSI", "RSI"),

    # Recommendations
    ("recommendation", "BollingerBandPower", "Rec.BBPower"),
    ("recommendation", "HullMA9", "Rec.HullMA9"),
    ("recommendation", "Ichimoku", "Rec.Ichimoku"),
    ("recommendation", "StochasticRSI", "Rec.Stoch.RSI"),
    ("recommendation", "UltimateOscillator", "Rec.UO"),
    ("recommendation", "VWMA", "Rec.VWMA"),
    ("recommendation", "WilliamsR", "Rec.WR"),
    ("recommendation", "All", "Recommend.All"),
    ("recommendation", "MovingAverage", "Recommend.MA"),
    ("recommendation", "Other", "Recommend.Other"),

    # SMA
    ("sma", "SMA_10", "SMA10"),
    ("sma", "SMA_20", "SMA20"),
    ("sma", "SMA_30", "SMA30"),
    ("sma", "SMA_50", "SMA50"),
    ("sma", "SMA_100", "SMA100"),
    ("sma", "SMA_200", "SMA200"),

    # Stochastic
    ("stochastic", "D", "Stoch.D"),
    ("stochastic", "K", "Stoch.K"),
    ("stochastic", "RSI_K", "Stoch.RSI.K"),

    ("ultimate_oscillator", "UltimateOscillator", "UO"),
    ("vwma", "VWMA", "VWMA"),
    ("williams_r", "WilliamsR", "W.R"),

    # Price / OHLCV
    ("price", "Open", "open"),
    ("price", "High", "high"),
    ("price", "Low", "low"),
    ("price", "Close", "close"),
    ("price", "Volume", "volume"),

    # VWAP
    ("vwap", "VWAP", "VWAP"),
]

# Generate nested JSON for regular indicators
mapping = {}

for category, key_name, tv_name in indicators:

    if category not in mapping:
        mapping[category] = {}

    for tf_name, interval in timeframes:

        value = tv_name if not interval else f"{tv_name}|{interval}"

        key = f"{key_name}_{tf_name}"
        mapping[category][key] = value


# Generate candlestick patterns separately
mapping["candlestick_patterns"] = {}

for tf_name, interval in candlestick_timeframes:

    key = f"CandlestickPattern_{tf_name}"
    value = f"candlestick_patterns_{interval}"

    mapping["candlestick_patterns"][key] = value


# Save JSON
output_path = Path("tradingview_indicators_nested.json")

output_path.write_text(
    json.dumps(mapping, indent=2),
    encoding="utf-8"
)

# Statistics
total_fields = sum(len(values) for values in mapping.values())

print(f"Categories: {len(mapping)}")
print(f"Total fields: {total_fields}")
print(f"Output: {output_path.resolve()}")

# Print generated JSON
print(json.dumps(mapping, indent=2))