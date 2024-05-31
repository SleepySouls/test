from cqrs.handlers import ICommandHandler
from repository.signup_repo import SignupRepository
from cqrs.signup.command import SignupCommand


class DeleteSignupCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:SignupRepository = SignupRepository()
    
        
    async def handle(self, command:SignupCommand) -> bool:
        result = await self.repo.delete_signup_user(command.details.get("id"))
        return result
