"""
RIDB Data Models
"""

from typing import List, Type

from ridbpy.models._base import RidbPyModel
from ridbpy.models.campsites import CampsiteAttributes, Campsites
from ridbpy.models.equipment import PermittedEquipment
from ridbpy.models.facilities import Facilities, FacilityAddresses
from ridbpy.models.joins import RecAreaFacilities
from ridbpy.models.organizations import Organizations, OrgEntities
from ridbpy.models.recareas import RecAreaAddresses, RecAreas

__all__ = [
    "CampsiteAttributes",
    "Campsites",
    "PermittedEquipment",
    "Facilities",
    "FacilityAddresses",
    "RecAreaFacilities",
    "Organizations",
    "OrgEntities",
    "RecAreaAddresses",
    "RecAreas",
]

_locals_vars = locals()
ALL_TABLES: List[Type[RidbPyModel]] = [_locals_vars[name] for name in __all__]
__all__.append("ALL_TABLES")
