from typing import List
from model.data.gino_model import Donation

class DonationListQuery:

    def __init__(self): 
        self._records:List[Donation] = list()
        
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records

class DonationRecordQuery: 
    
    def __init__(self): 
        self._record:Donation = None
        
    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record