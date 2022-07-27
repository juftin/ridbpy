"""
Recreation Area Data Models
"""

import datetime
import logging
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship

from ridbpy.models._base import RidbPyModel
from ridbpy.models.organizations import Organizations

if TYPE_CHECKING is True:
    from ridbpy.models import Facilities

logging.basicConfig(level=logging.DEBUG)


class RecAreas(RidbPyModel, table=True):
    """
    Recreation Area Data
    """

    __tablename__ = "RecAreas"

    RecAreaID: str = Field(primary_key=True)
    OrgRecAreaID: Optional[int]
    ParentOrgID: int = Field(foreign_key=Organizations.OrgID)
    RecAreaName: Optional[str] = Field(index=True)
    RecAreaDescription: Optional[str]
    RecAreaUseFeeDescription: Optional[str]
    RecAreaDirections: Optional[str]
    RecAreaPhone: Optional[str]
    RecAreaEmail: Optional[str]
    RecAreaReservationURL: Optional[str]
    RecAreaMapURL: Optional[str]
    RecAreaLongitude: Optional[float]
    RecAreaLatitude: Optional[float]
    StayLimit: Optional[str]
    Keywords: Optional[str]
    Reservable: bool
    Enabled: bool
    LastUpdatedDate: datetime.date

    addresses: List["RecAreaAddresses"] = Relationship(back_populates="recreation_area")
    facilities: List["Facilities"] = Relationship(back_populates="recreation_area")
    organization: Organizations = Relationship(back_populates="recreation_areas")


class RecAreaAddresses(RidbPyModel, table=True):
    """
    Recreation Area Addresses
    """

    __tablename__ = "RecAreaAddresses"

    RecAreaAddressID: int = Field(primary_key=True)
    RecAreaID: int = Field(foreign_key="RecAreas.RecAreaID")
    RecAreaAddressType: str
    RecAreaStreetAddress1: Optional[str]
    RecAreaStreetAddress2: Optional[str]
    RecAreaStreetAddress3: Optional[str]
    City: Optional[str]
    PostalCode: Optional[str]
    AddressStateCode: Optional[str]
    AddressCountryCode: Optional[str]
    LastUpdatedDate: datetime.date

    recreation_area: RecAreas = Relationship(back_populates="addresses")
