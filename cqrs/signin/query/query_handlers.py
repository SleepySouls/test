from cqrs.handlers import IQueryHandler
from repository.signin_repo import SigninRepository
from cqrs.signin.queries import SigninListQuery, SigninRecordQuery

class ListSigninQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:SigninRepository = SigninRepository()
        self.query:SigninListQuery = SigninListQuery()
        
    async def handle(self) -> SigninListQuery:
        data = await self.repo.get_all_login_users()
        self.query.records = data
        return self.query
    

class RecordSigninQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:SigninRepository = SigninRepository()
        self.query:SigninRecordQuery = SigninRecordQuery()
        
    async def handle(self, id) -> SigninListQuery:
        data = await self.repo.get_login_user_by_id(id)
        self.query.record = data
        return self.query