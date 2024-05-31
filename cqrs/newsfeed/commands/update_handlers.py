from cqrs.handlers import ICommandHandler
from repository.newsfeed_repo import NewsfeedRepository
from cqrs.newsfeed.command import NewsfeedCommand

class UpdateNewsfeedCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:NewsfeedRepository = NewsfeedRepository()
        
    async def handle(self, command:NewsfeedCommand) -> bool:
        id = command.details['id']
        details = {key: value for key, value in command.details.items() if key != 'id'}
        result = await self.repo.update_newsfeed(id, details)
        return result