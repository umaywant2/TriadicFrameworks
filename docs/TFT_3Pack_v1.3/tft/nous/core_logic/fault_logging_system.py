"""
⚠️ Fault Logging System
Logs faults across validator, glyphstream, and sort benchmarking.
"""

import datetime

def log_fault(agent_id, fault_type, details, log_file):
    timestamp = datetime.datetime.now().isoformat()
    entry = f"[{timestamp}] Agent: {agent_id} | Fault: {fault_type} | Details: {details}\n"
    with open(log_file, "a") as f:
        f.write(entry)
    print(f"[FaultLogger] {entry.strip()}")
