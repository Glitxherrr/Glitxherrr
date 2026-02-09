"""Sentinel OpenClaw entrypoint."""


def audit_signal(packet, last_state):
    sensors = packet["sensor_readings"]

    # HARD FILTERS (Python, not LLM)
    if sensors["htf_trend_bias"] != "BULLISH":
        return None

    if sensors["ema_alignment"] != "STACKED_LONG":
        return None

    # Only now does the LLM wake up
    return packet


def confidence_score(packet):
    score = 0
    s = packet["sensor_readings"]

    if s["htf_trend_bias"] == "BULLISH":
        score += 3
    if s["ema_alignment"] == "STACKED_LONG":
        score += 3
    if 40 < s["rsi"] < 60:
        score += 2
    if s["structure_state"] == "BULLISH":
        score += 2

    return score
