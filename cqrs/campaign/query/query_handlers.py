from cqrs.handlers import IQueryHandler
from repository.campaign_repo import CampaignRepository
from cqrs.campaign.queries import CampaignListQuery, CampaignRecordQuery

class ListCampaignQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:CampaignRepository = CampaignRepository()
        self.query:CampaignListQuery = CampaignListQuery()
        
    async def handle(self) -> CampaignListQuery:
        data = await self.repo.get_all_campaign()
        self.query.records = data
        return self.query
    

class RecordCampaignQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:CampaignRepository = CampaignRepository()
        self.query:CampaignRecordQuery = CampaignRecordQuery()
        
    async def handle(self, id) -> CampaignListQuery:
        data = await self.repo.get_campaign_by_id(id)
        self.query.record = data
        return self.query