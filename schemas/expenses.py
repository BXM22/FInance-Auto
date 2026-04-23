from __future__ import annotations
from enum import Enum   

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


"""
Field(...) lets you configure a model field beyond just its type—mainly:

Validation constraints (e.g. gt=0, min_length=1)
Required vs optional (using ... means “required”)
Default values (e.g. Field("USD"))
Metadata for docs/OpenAPI (e.g. description=, example=), which shows up in /docs
"""

class ExpenseStatus(str, Enum):
    draft = "draft"
    needs_info = "needs_info"
    submitted = "submitted"
    in_review = "in_review"
    approved = "approved"
    rejected = "rejected"


class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0)
    currency: str = Field(..., min_length=3, max_length=3)  # "USD"
    merchant: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    employee_id: int = Field(..., gt=0)
    cost_center: int = Field(..., gt=0)
    occurred_at: datetime  # client provides when it happened


class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    currency: Optional[str] = Field(None, min_length=3, max_length=3)
    merchant: Optional[str] = Field(None, min_length=1)
    category: Optional[str] = Field(None, min_length=1)
    cost_center: Optional[int] = Field(None, gt=0)
    occurred_at: Optional[datetime] = None


class Expense(ExpenseCreate):
    id: int
    status: ExpenseStatus = ExpenseStatus.draft
    created_at: datetime
    updated_at: datetime


