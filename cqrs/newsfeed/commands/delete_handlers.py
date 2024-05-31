from cqrs.handlers import ICommandHandler
from repository.newsfeed_repo import NewsfeedRepository
from cqrs.newsfeed.command import NewsfeedCommand

class DeleteNewsfeedCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:NewsfeedRepository = NewsfeedRepository()
    
        
    async def handle(self, command:NewsfeedCommand) -> bool:
        result = await self.repo.delete_newsfeed(command.details.get("id"))
        return result
