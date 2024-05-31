from model.data.gino_model import Campaign
from typing import Dict, Any, List

class CampaignRepository:

    async def create_campaign(self, details: Dict[str, Any]) -> bool:
        try:
            await Campaign.create(**details)
            return True
        except Exception as e:
            print(f"Error creating campaign: {e}")
            return False

    async def update_campaign(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            campaign = await Campaign.get(id)
            await campaign.update(**details).apply()
            return True
        except Exception as e:
            print(f"Error updating campaign: {e}")
            return False

    async def delete_campaign(self, id: int) -> bool:
        try:
            campaign = await Campaign.get(id)
            await campaign.delete()
            return True
        except Exception as e:
            print(f"Error deleting campaign: {e}")
            return False

    async def get_campaign_by_id(self, id: int):
        try:
            return await Campaign.get(id)
        except Exception as e:
            print(f"Error retrieving campaign: {e}")
            return None
        
    async def get_all_campaign(self) -> List[Dict[str, Any]]:
        try:
            campaigns = await Campaign.query.gino.all()
            return [campaign.to_dict() for campaign in campaigns]
        except Exception as e:
            print(f"Error retrieving all campaign: {e}")
            return []