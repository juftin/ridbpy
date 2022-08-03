"""
Querying Examples
"""

import rich.traceback
from sqlmodel import select

from ridbpy.application import session
from ridbpy.models import Campsites, Facilities, RecAreas

rich.traceback.install(show_locals=True)

campsites = []
rec_area = session.exec(
    select(RecAreas).where(RecAreas.RecAreaName == "Glacier National Park")
).first()
assert isinstance(rec_area, RecAreas)
org = rec_area.organization
facilities = rec_area.facilities
facility: Facilities
for facility in facilities:
    campsites += facility.campsites

example_campsite: Campsites = campsites[5]
attributes = example_campsite.attributes
equipment = example_campsite.permitted_equipment
