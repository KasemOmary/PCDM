import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from pcdm.base import Base

from pcdm import (
    party,
    account,
    policy,
    claim,
    assessment,
    agreementrole,
    claimrole,
    staffing,
    partyst,
    insurable,
    money,
    event,
    product)

# Read env variables instead of hardcoding.
import os

user = os.environ['PCDM_DB_USER']
password = os.environ['PCDM_DB_PASSWORD']
host = os.environ['PCDM_DB_HOST']
protocol = os.environ['PCDM_DB_PROTOCOL']
database = os.environ['PCDM_DB_DATABASE']  

connstring = f'{protocol}://{user}:{password}@{host}/{database}'

engine = sa.create_engine(
            connstring,
            echo=True
        )
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
