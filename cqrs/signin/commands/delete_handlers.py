from cqrs.handlers import ICommandHandler
from repository.signin_repo import SigninRepository
from cqrs.signin.command import SigninCommand


class DeleteSigninCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:SigninRepository = SigninRepository()
    
        
    async def handle(self, command:SigninCommand) -> bool:
        result = await self.repo.delete_login_user(command.details.get("id"))
        return result
