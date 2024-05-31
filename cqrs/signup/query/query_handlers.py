from cqrs.handlers import IQueryHandler
from repository.signup_repo import SignupRepository
from cqrs.signup.queries import SignupListQuery, SignupRecordQuery

class ListSignupQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:SignupRepository = SignupRepository()
        self.query:SignupListQuery = SignupListQuery()
        
    async def handle(self) -> SignupListQuery:
        data = await self.repo.get_all_signup_users()
        self.query.records = data
        return self.query
    

class RecordSignupQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:SignupRepository = SignupRepository()
        self.query:SignupRecordQuery = SignupRecordQuery()
        
    async def handle(self, id) -> SignupListQuery:
        data = await self.repo.get_signup_user_by_id(id)
        self.query.record = data
        return self.query