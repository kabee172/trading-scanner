def score_trade(structure, sweep, confirm):
    score = 0

    # 1. Structure quality
    if structure in ["BULLISH", "BEARISH"]:
        score += 30
    elif structure == "RANGE":
        score += 10

    # 2. Liquidity sweep (very important)
    if sweep:
        score += 40

    # 3. Confirmation (rejection candle)
    if confirm:
        score += 30

    return score
