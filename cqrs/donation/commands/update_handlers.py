from cqrs.handlers import ICommandHandler
from repository.donation_repo import DonationRepository
from cqrs.donation.command import DonationCommand

class UpdateDonationCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:DonationRepository = DonationRepository()
        
    async def handle(self, command:DonationCommand) -> bool:
        id = command.details['id']
        details = {key: value for key, value in command.details.items() if key != 'id'}
        result = await self.repo.update_donation(id, details)
        return result