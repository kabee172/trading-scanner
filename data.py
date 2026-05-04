import random

def get_market_data(pair):
    """
    Simulated market data (we will replace with MT5 later)
    """

    base_price = random.uniform(1.0, 2.0)

    highs = [base_price + random.uniform(0, 0.01) for _ in range(20)]
    lows = [base_price - random.uniform(0, 0.01) for _ in range(20)]

    candles = [
        {
            "body": random.uniform(0.001, 0.005),
            "rejection_wick": random.uniform(0.002, 0.01)
        }
    ]

    return {
        "price": base_price,
        "highs": highs,
        "lows": lows,
        "candles": candles
    }
