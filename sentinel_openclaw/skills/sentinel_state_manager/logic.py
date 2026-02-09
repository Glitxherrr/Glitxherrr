import json
from pathlib import Path

STATE_FILE = Path("state/market_state.json")


def load_market_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_market_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2))
