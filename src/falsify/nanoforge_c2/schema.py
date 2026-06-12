from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class Product(str, Enum):
    HSI = "HSi100"
    IR_DB = "IR_DB_pair"
    IR_C2 = "IR_C2"
    TWO_IR_C2 = "2IR_C2"
    IR_C2_C4 = "IR_C2_C4"
    TWO_IR_C4 = "2IR_C4"
    DEFECT = "defect"


class Outcome(str, Enum):
    SUCCESS = "success"
    H_ABSTRACTION = "nearby_H_abstraction"
    SI_ABSTRACTION = "Si_abstraction"
    UNDESIRED_C2 = "undesired_C2_product"
    OTHER = "other"


class OperationName(str, Enum):
    PATTERN_IR_DB = "pattern_IR_DB_pair"
    DONATE_C2_TO_DB = "donate_C2_to_IR_DB"
    DONATE_C2_ADJACENT = "donate_C2_adjacent_to_IR_C2"
    EXTEND_C2_TO_C4 = "extend_IR_C2_to_IR_C4"
    EXTEND_REMAINING_C2 = "extend_remaining_IR_C2_to_2IR_C4"
    IMAGE_VERIFY = "image_verify"


class ProtocolStep(BaseModel):
    name: OperationName
    target_site: str = "site_0"
    dz_pm: int | None = Field(default=50, description="Depth increment in pm for approach sampling.")
    bias_v: float | None = Field(default=0.0, description="Bias during mechanosynthetic transfer step.")
    note: str = ""


class SurfaceState(BaseModel):
    product: Product = Product.HSI
    history: list[str] = Field(default_factory=list)


class Transition(BaseModel):
    from_product: Product
    operation: OperationName
    to_product: Product
    probabilities: dict[Outcome, float]
    citation_key: str


class ProtocolResult(BaseModel):
    target: Product
    steps: list[ProtocolStep]
    estimated_success: float
    expected_steps: int
    failure_distribution: dict[str, float]
    score: float
