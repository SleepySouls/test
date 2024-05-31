from typing import List
from model.data.gino_model import Newsfeed

class NewsfeedListQuery:

    def __init__(self): 
        self._records:List[Newsfeed] = list()
        
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records

class NewsfeedRecordQuery: 
    
    def __init__(self): 
        self._record:Newsfeed = None
        
    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record