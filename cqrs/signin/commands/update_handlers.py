from cqrs.handlers import ICommandHandler
from repository.signin_repo import SigninRepository
from cqrs.signin.command import SigninCommand

class UpdateSigninCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:SigninRepository = SigninRepository()
        
    async def handle(self, command:SigninCommand) -> bool:
        id = command.details['id']
        details = {key: value for key, value in command.details.items() if key != 'id'}
        result = await self.repo.update_login_user(id, details)
        return result