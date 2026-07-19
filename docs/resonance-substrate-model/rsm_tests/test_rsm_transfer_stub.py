"""
test_rsm_transfer_stub.py
Minimal RSM transfer stub test.
Ensures RTO_RSM packets are well-formed and accepted by a stub receiver.
"""

from resonance_substrate_model.rsm_core.rsm_operators import RTO_RSM


# ---------------------------------------------------------------------------
# FIXTURES
# ---------------------------------------------------------------------------

class MockResonanceState:
    def __init__(self):
        self.coherence_level = 0.55
        self.gain = 0.10


class RSMTransferStub:
    """
    Minimal external-side stub that accepts an RSM transfer packet.
    """
    def __call__(self, packet):
        return {
            "received": True,
            "payload_ok": (
                "coherence_level" in packet
                and "gain" in packet
                and "stability_label" in packet
            ),
            "triad_index": packet.get("triad_index"),
            "source": packet.get("source"),
        }


# ---------------------------------------------------------------------------
# TESTS
# ---------------------------------------------------------------------------

def test_rsm_transfer_packet_structure():
    """RTO_RSM should produce a valid transfer packet."""
    rs = MockResonanceState()
    packet = RTO_RSM(
        resonance_state=rs,
        stability_label="marginal",
        triad_index=12,
    )

    assert packet["coherence_level"] == 0.55
    assert packet["gain"] == 0.10
    assert packet["stability_label"] == "marginal"
    assert packet["triad_index"] == 12
    assert packet["source"] == "RSM"


def test_rsm_transfer_stub_receives_packet():
    """Stub should acknowledge receipt of a valid RSM packet."""
    rs = MockResonanceState()
    stub = RSMTransferStub()

    packet = RTO_RSM(
        resonance_state=rs,
        stability_label="stable",
        triad_index=7,
    )

    result = stub(packet)

    assert result["received"] is True
    assert result["payload_ok"] is True
    assert result["triad_index"] == 7
    assert result["source"] == "RSM"
