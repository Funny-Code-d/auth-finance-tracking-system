from .hubs import hub_token
from .settelites import sat_token

from .base import metadata, engine



metadata.create_all(bind=engine)
# metadata.drop_all(bind=engine)
# 

