# models.py

from app import app, db
from sqlalchemy import Column, Integer, String

class Campsite(db.Model):
    __tablename__ = 'campsites'
    CampsiteID = Column(Integer, primary_key=True)
    CampsiteName = Column(String(255))
    CampsiteType = Column(String(255))
    FacilityID = Column(String(255))
    FacilityName = Column(String(255))
    AddressStateCode = Column(String(255))
    FacilityLatitude = Column(Integer)
    FacilityLongitude = Column(Integer)
    OrgAbbrevName = Column(String(255))
