from cqrs.handlers import IQueryHandler
from repository.user_repo import UserRepository
from cqrs.user.queries import UserListQuery, UserRecordQuery

class ListUserQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:UserRepository = UserRepository()
        self.query:UserListQuery = UserListQuery()
        
    async def handle(self) -> UserListQuery:
        data = await self.repo.get_all_user()
        self.query.records = data
        return self.query
    

class RecordUserQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:UserRepository = UserRepository()
        self.query:UserRecordQuery = UserRecordQuery()
        
    async def handle(self, id) -> UserListQuery:
        data = await self.repo.get_user_by_id(id)
        self.query.record = data
        return self.query