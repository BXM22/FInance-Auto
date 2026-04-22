from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0)
    currency: str = Field(..., min_length=3, max_length=3)
    merchant: str = Field(..., min_length=1)
    description: Optional[str] = None


class Expense(ExpenseCreate):
    id: int
    created_at: datetime