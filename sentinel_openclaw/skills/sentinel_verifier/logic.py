def verify_claim(claim: str, market_packet: dict) -> bool:
    claim = claim.lower()

    if "bullish" in claim:
        return market_packet["sensor_readings"]["htf_trend_bias"] == "BULLISH"

    if "oversold" in claim:
        return market_packet["sensor_readings"]["rsi"] < 30

    if "ema aligned" in claim:
        return market_packet["sensor_readings"]["ema_alignment"] == "STACKED_LONG"

    return False
