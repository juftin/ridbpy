"""
Facility / Campground Data Models
"""

import datetime
import logging
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship

from ridbpy.models._base import RidbPyModel

if TYPE_CHECKING is True:
    from ridbpy.models import Campsites, RecAreas

logging.basicConfig(level=logging.DEBUG)


class FacilityAddresses(RidbPyModel, table=True):
    """
    Addresses for Facilities
    """

    __tablename__ = "FacilityAddresses"

    FacilityAddressID: str = Field(primary_key=True, index=True)
    FacilityID: int = Field(
        foreign_key="Facilities.FacilityID", default=None, index=True
    )
    FacilityAddressType: str
    FacilityStreetAddress1: Optional[str]
    FacilityStreetAddress2: Optional[str]
    FacilityStreetAddress3: Optional[str]
    City: Optional[str]
    AddressStateCode: Optional[str]
    PostalCode: Optional[str]
    AddressCountryCode: Optional[str]
    LastUpdatedDate: datetime.date

    facility: "Facilities" = Relationship(back_populates="addresses")


class Facilities(RidbPyModel, table=True):
    """
    Facility Information
    """

    __tablename__ = "Facilities"

    FacilityID: str = Field(primary_key=True, index=True)
    LegacyFacilityID: Optional[str]
    OrgFacilityID: int = Field(foreign_key="Organizations.OrgID")
    ParentOrgID: Optional[str]
    ParentRecAreaID: Optional[str] = Field(
        foreign_key="RecAreas.RecAreaID", default=None, index=True
    )
    FacilityName: Optional[str] = Field(index=True)
    FacilityDescription: Optional[str]
    FacilityTypeDescription: Optional[str]
    FacilityUseFeeDescription: Optional[str]
    FacilityDirections: Optional[str]
    FacilityPhone: Optional[str]
    FacilityEmail: Optional[str]
    FacilityReservationURL: Optional[str]
    FacilityMapURL: Optional[str]
    FacilityAdaAccess: Optional[str]
    FacilityLongitude: float
    FacilityLatitude: float
    Keywords: Optional[str]
    StayLimit: Optional[str]
    Reservable: bool
    Enabled: bool
    LastUpdatedDate: datetime.date

    campsites: List["Campsites"] = Relationship(back_populates="facility")
    recreation_area: "RecAreas" = Relationship(back_populates="facilities")
    addresses: List["FacilityAddresses"] = Relationship(back_populates="facility")
