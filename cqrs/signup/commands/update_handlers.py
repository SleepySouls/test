from cqrs.handlers import ICommandHandler
from repository.signup_repo import SignupRepository
from cqrs.signup.command import SignupCommand

class UpdateSignupCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:SignupRepository = SignupRepository()
        
    async def handle(self, command:SignupCommand) -> bool:
        id = command.details['id']
        details = {key: value for key, value in command.details.items() if key != 'id'}
        result = await self.repo.update_signup_user(id, details)
        return result