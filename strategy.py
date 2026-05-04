def detect_structure(data):
    highs = data["highs"]
    lows = data["lows"]

    if highs[-1] > highs[-5] and lows[-1] > lows[-5]:
        return "BULLISH"

    if highs[-1] < highs[-5] and lows[-1] < lows[-5]:
        return "BEARISH"

    return "RANGE"


def detect_liquidity(data):
    return {
        "high": max(data["highs"]),
        "low": min(data["lows"])
    }


def detect_sweep(price, liquidity):
    if price > liquidity["high"]:
        return "HIGH_SWEEP"

    if price < liquidity["low"]:
        return "LOW_SWEEP"

    return None


def confirmation(candle):
    # simple rejection logic
    return candle["rejection_wick"] > candle["body"] * 2
