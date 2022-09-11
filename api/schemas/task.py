from lib2to3.pgen2.token import OP
from typing import Optional

from pydantic import BaseModel, Field


"""
idとdoneは作成時には不要な項目なので
titleのみだけDBに登録します。
"""
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く。")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode: True

"""
TaskBaseを引き継いでいる。
"""
class Task(TaskBase):
    id: int
    # title: Optional[str] = Field(None, example="クリーニングを取りに行く。")
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode: True


