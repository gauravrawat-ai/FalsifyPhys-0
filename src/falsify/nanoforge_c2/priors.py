from __future__ import annotations

RAW_TRANSITIONS = [
    ("HSi100", "donate_C2_to_IR_DB", "IR_C2", {"success": 0.93, "failure_h": 0.03, "failure_si": 0.003, "failure_alt": 0.0, "other": 0.037}),
    ("IR_C2", "donate_C2_adjacent_to_IR_C2", "2IR_C2", {"success": 0.97, "failure_h": 0.01, "failure_si": 0.0, "failure_alt": 0.0, "other": 0.02}),
    ("2IR_C2", "extend_IR_C2_to_IR_C4", "IR_C2_C4", {"success": 0.92, "failure_h": 0.02, "failure_si": 0.0, "failure_alt": 0.0, "other": 0.06}),
    ("IR_C2_C4", "extend_remaining_IR_C2_to_2IR_C4", "2IR_C4", {"success": 0.84, "failure_h": 0.04, "failure_si": 0.0, "failure_alt": 0.12, "other": 0.0}),
]
