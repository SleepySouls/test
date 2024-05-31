from typing import List
from model.data.gino_model import Signin

class SigninListQuery:

    def __init__(self): 
        self._records:List[Signin] = list()
        
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records

class SigninRecordQuery: 
    
    def __init__(self): 
        self._record:Signin = None
        
    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record