"""
Organizations Data Models
"""

import datetime
import logging
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship

from ridbpy.models._base import RidbPyModel

if TYPE_CHECKING is True:
    from ridbpy.models import RecAreas

logging.basicConfig(level=logging.DEBUG)


class Organizations(RidbPyModel, table=True):
    """
    Organization Information
    """

    __tablename__ = "Organizations"

    OrgID: str = Field(primary_key=True, index=True)
    OrgType: str
    OrgName: str = Field(index=True)
    OrgImageURL: Optional[str]
    OrgURLText: Optional[str]
    OrgURLAddress: Optional[str]
    OrgAbbrevName: Optional[str]
    OrgJurisdictionType: Optional[str]
    OrgParentID: int
    LastUpdatedDate: datetime.date

    recreation_areas: List["RecAreas"] = Relationship(back_populates="organization")


class OrgEntities(RidbPyModel, table=True):
    """
    Organization Entity Information
    """

    __tablename__ = "OrgEntities"

    EntityId: str = Field(primary_key=True, index=True)
    OrgID: str = Field(foreign_key="Organizations.OrgID", index=True)
    EntityType: str
