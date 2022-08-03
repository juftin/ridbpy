from typing import List

from sqlmodel import SQLModel


class RidbPyModel(SQLModel):
    """
    Hashable SQLModel
    """

    __unhashable__: List[str] = []

    def __hash__(self) -> int:
        """
        Hash Method for Pydantic BaseModels
        """
        values_to_hash = tuple(
            getattr(self, key)
            for key in self.__fields__
            if key not in self.__unhashable__
        )
        return hash((type(self),) + values_to_hash)
