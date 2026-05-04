from data import get_market_data
from strategy import detect_structure, detect_liquidity, detect_sweep, confirmation
from scoring import score_trade
from config import PAIRS, MIN_SCORE


def scan():
    signals = []

    for pair in PAIRS:

        data = get_market_data(pair)

        structure = detect_structure(data)
        liquidity = detect_liquidity(data)
        sweep = detect_sweep(data["price"], liquidity)
        confirm = confirmation(data["candles"][0])

        score = score_trade(structure, sweep, confirm)

        if score >= MIN_SCORE:
            signals.append({
                "pair": pair,
                "direction": "BUY" if sweep == "LOW_SWEEP" else "SELL",
                "score": score,
                "entry": data["price"],
                "sl": liquidity["low"],
                "tp": liquidity["high"]
            })

    return {"signals": signals}
