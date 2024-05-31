from cqrs.handlers import ICommandHandler
from repository.donation_repo import DonationRepository
from cqrs.donation.command import DonationCommand

class DeleteDonationCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:DonationRepository = DonationRepository()
    
        
    async def handle(self, command:DonationCommand) -> bool:
        result = await self.repo.delete_donation(command.details.get("id"))
        return result
