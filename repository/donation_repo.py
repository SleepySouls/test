from model.data.gino_model import Donation
from typing import Dict, Any, List

class DonationRepository:

    async def create_donation(self, details: Dict[str, Any]) -> bool:
        try:
            await Donation.create(**details)
            return True
        except Exception as e:
            print(f"Error creating donation: {e}")
            return False

    async def update_donation(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            donation = await Donation.get(id)
            await donation.update(**details).apply()
            return True
        except Exception as e:
            print(f"Error updating donation: {e}")
            return False

    async def delete_donation(self, id: int) -> bool:
        try:
            donation = await Donation.get(id)
            await donation.delete()
            return True
        except Exception as e:
            print(f"Error deleting donation: {e}")
            return False

    async def get_donation_by_id(self, id: int):
        try:
            return await Donation.get(id)
        except Exception as e:
            print(f"Error retrieving donation: {e}")
            return None
        
    async def get_all_donation(self) -> List[Dict[str, Any]]:
        try:
            donations = await Donation.query.gino.all()
            return [donation.to_dict() for donation in donations]
        except Exception as e:
            print(f"Error retrieving all donation: {e}")
            return []