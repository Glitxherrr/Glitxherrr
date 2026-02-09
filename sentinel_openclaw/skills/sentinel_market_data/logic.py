from core.config import *
from core.utils import *
from indicators import rsi, ema
from structure import detect_structure
from binance import fetch_klines


def get_market_intelligence(symbol: str, interval: str = "1h"):
    klines = fetch_klines(symbol, interval, limit=300)

    close_prices = [k["close"] for k in klines]

    rsi_value = rsi(close_prices, 14)
    ema_20 = ema(close_prices, 20)
    ema_50 = ema(close_prices, 50)

    structure = detect_structure(klines)

    htf_bias = (
        "BULLISH" if ema_50 < close_prices[-1]
        else "BEARISH"
    )

    verdict_packet = {
        "sensor_readings": {
            "htf_trend_bias": htf_bias,
            "ema_alignment": (
                "STACKED_LONG"
                if ema_20 > ema_50
                else "UNALIGNED"
            ),
            "rsi": rsi_value,
            "structure_state": structure["state"],
            "zigzag_signal": structure["zigzag_signal"]
        },
        "constraints": {
            "invalidation_point": structure["invalidation"],
            "atr": structure["atr"],
            "nearest_supply": structure["supply_zone"]
        }
    }

    return verdict_packet
