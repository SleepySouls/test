from cqrs.handlers import ICommandHandler
from repository.user_repo import UserRepository
from cqrs.user.command import UserCommand

class AddUserCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:UserRepository = UserRepository()
        
    async def handle(self, command:UserCommand) -> bool:
        result = await self.repo.create_user(command.details)
        return result