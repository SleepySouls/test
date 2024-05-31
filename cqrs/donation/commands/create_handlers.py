from cqrs.handlers import ICommandHandler
from repository.donation_repo import DonationRepository
from cqrs.donation.command import DonationCommand

class AddDonationCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:DonationRepository = DonationRepository()
        
    async def handle(self, command:DonationCommand) -> bool:
        result = await self.repo.create_donation(command.details)
        return result