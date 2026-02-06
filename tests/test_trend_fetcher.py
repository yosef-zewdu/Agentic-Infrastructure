import importlib
from datetime import datetime
import inspect


def _find_callable(module):
    for name in ("fetch_trends", "run", "handle", "invoke", "main"):
        fn = getattr(module, name, None)
        if callable(fn):
            return fn
    return None


def test_fetch_trends_contract():
    """Asserts that the `skills.fetch_trends` skill exists and returns
    an object matching the Fetch Trends contract in `specs/technical.md`.

    This test is expected to fail until the skill implementation exists
    and conforms to the contract.
    """
    module = importlib.import_module("skills.fetch_trends")
    fn = _find_callable(module)
    assert fn is not None, "No callable found in skills.fetch_trends (expected fetch_trends/run/handle/invoke/main)"

    sample_input = {
        "spec_id": "CHIMERA-FUNC-001",
        "agent_id": "test-agent",
        "agent_version": "0.0.1",
        "params": {"platform": "tiktok", "time_range_hours": 24, "limit": 5},
    }

    result = fn(sample_input)
    assert isinstance(result, dict), "Result must be a dict-like JSON object"

    assert result.get("ok") is True, "Expected top-level `ok: true` for success response"

    data = result.get("data")
    assert isinstance(data, dict), "`data` must be an object"

    # platform and time_range_hours echoed
    assert data.get("platform") == sample_input["params"]["platform"]
    assert data.get("time_range_hours") == sample_input["params"]["time_range_hours"]

    trends = data.get("trends")
    assert isinstance(trends, list), "`data.trends` must be a list"
    assert len(trends) <= sample_input["params"]["limit"]

    for t in trends:
        assert isinstance(t, dict), "Each trend must be an object"
        assert "topic" in t and isinstance(t["topic"], str)
        assert "volume" in t and isinstance(t["volume"], int)
        assert "trend_direction" in t and t["trend_direction"] in {"up", "down", "stable"}
        assert "source" in t and isinstance(t["source"], str)
        # fetched_at should be an ISO8601 timestamp
        fetched_at = t.get("fetched_at")
        assert isinstance(fetched_at, str)
        # simple ISO validation
        try:
            datetime.fromisoformat(fetched_at.replace("Z", "+00:00"))
        except Exception:
            assert False, f"fetched_at is not valid ISO8601: {fetched_at}"
