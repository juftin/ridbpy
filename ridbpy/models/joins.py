"""
One to Many Data Models
"""

from sqlmodel import Field

from ridbpy.models._base import RidbPyModel


class RecAreaFacilities(RidbPyModel):
    """
    Join Table Between Recreation Areas and Facilities
    """

    __tablename__ = "RecAreaFacilities"

    RecAreaID: str = Field(
        foreign_key="RecAreas.RecAreaID", primary_key=True, index=True
    )
    FacilityID: str = Field(
        foreign_key="Facilities.FacilityID", primary_key=True, index=True
    )
