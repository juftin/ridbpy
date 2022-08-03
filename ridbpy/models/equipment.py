"""
Equipment Data Models
"""

from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from ridbpy.models._base import RidbPyModel

if TYPE_CHECKING is True:
    from ridbpy.models import Campsites


class PermittedEquipment(RidbPyModel, table=True):
    """
    Campsite Equipment Information
    """

    __tablename__ = "PermittedEquipment"

    CampsiteID: int = Field(
        foreign_key="Campsites.CampsiteID", index=True, primary_key=True
    )
    MaxLength: int = Field(primary_key=True)
    EquipmentName: str = Field(index=True, primary_key=True)

    campsite: "Campsites" = Relationship(back_populates="permitted_equipment")
