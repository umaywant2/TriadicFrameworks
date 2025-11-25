import datetime

class ObserverState:
    def __init__(self, name="Remixer"):
        self.name = name
        self.state_log = []

    def log_state(self, timestamp=None, resonance_level=0.0, symbolic_trigger=None):
        """
        Log observer state at a given moment.
        timestamp: datetime object or auto-generated
        resonance_level: float between 0.0 and 1.0
        symbolic_trigger: optional string (e.g., 'spiral', 'echo', 'glyph')
        """
        if timestamp is None:
            timestamp = datetime.datetime.now()
        entry = {
            "timestamp": timestamp.isoformat(),
            "resonance_level": resonance_level,
            "symbolic_trigger": symbolic_trigger
        }
        self.state_log.append(entry)

    def export_log(self):
        return self.state_log

if __name__ == "__main__":
    observer = ObserverState(name="Nawder")
    observer.log_state(resonance_level=0.7, symbolic_trigger="spiral")
    observer.log_state(resonance_level=0.9, symbolic_trigger="glyph")
    for entry in observer.export_log():
        print(entry)
