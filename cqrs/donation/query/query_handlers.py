from cqrs.handlers import IQueryHandler
from repository.donation_repo import DonationRepository
from cqrs.donation.queries import DonationListQuery, DonationRecordQuery

class ListDonationQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:DonationRepository = DonationRepository()
        self.query:DonationListQuery = DonationListQuery()
        
    async def handle(self) -> DonationListQuery:
        data = await self.repo.get_all_donation()
        self.query.records = data
        return self.query
    

class RecordDonationQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:DonationRepository = DonationRepository()
        self.query:DonationRecordQuery = DonationRecordQuery()
        
    async def handle(self, id) -> DonationListQuery:
        data = await self.repo.get_donation_by_id(id)
        self.query.record = data
        return self.query