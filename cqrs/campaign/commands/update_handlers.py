from cqrs.handlers import ICommandHandler
from repository.campaign_repo import CampaignRepository
from cqrs.campaign.command import CampaignCommand

class UpdateCampaignCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:CampaignRepository = CampaignRepository()
        
    async def handle(self, command:CampaignCommand) -> bool:
        id = command.details['id']
        details = {key: value for key, value in command.details.items() if key != 'id'}
        result = await self.repo.update_campaign(id, details)
        return result