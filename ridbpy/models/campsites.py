"""
Campsite Data Models
"""

import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship

from ridbpy.models._base import RidbPyModel
from ridbpy.models.equipment import PermittedEquipment
from ridbpy.models.facilities import Facilities


class Campsites(RidbPyModel, table=True):
    """
    Campsite Information
    """

    __tablename__ = "Campsites"

    CampsiteID: int = Field(primary_key=True, index=True)
    FacilityID: int = Field(foreign_key="Facilities.FacilityID", index=True)
    CampsiteName: Optional[str]
    CampsiteType: Optional[str]
    TypeOfUse: str = Field(index=True)
    Loop: Optional[str]
    CampsiteAccessible: bool
    CampsiteLongitude: float
    CampsiteLatitude: float
    CreatedDate: datetime.date
    LastUpdatedDate: datetime.date

    facility: Facilities = Relationship(back_populates="campsites")
    attributes: List["CampsiteAttributes"] = Relationship(
        back_populates="campsite",
        sa_relationship_kwargs=dict(
            primaryjoin="and_(Campsites.CampsiteID==CampsiteAttributes.EntityId, "
            "CampsiteAttributes.EntityType=='Campsite')"
        ),
    )
    permitted_equipment: List[PermittedEquipment] = Relationship(
        back_populates="campsite"
    )


class CampsiteAttributes(RidbPyModel, table=True):
    """
    Campsite Attributes
    """

    __tablename__ = "CampsiteAttributes"

    AttributeID: int = Field(primary_key=True, index=True)
    AttributeName: str = Field(index=True)
    AttributeValue: Optional[str] = Field(index=True, default="")
    EntityId: int = Field(
        primary_key=True, foreign_key="Campsites.CampsiteID", index=True
    )
    EntityType: str

    campsite: Campsites = Relationship(back_populates="attributes")
