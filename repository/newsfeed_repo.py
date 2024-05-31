from model.data.gino_model import Newsfeed
from typing import Dict, Any, List

class NewsfeedRepository:

    async def create_newsfeed(self, details: Dict[str, Any]) -> bool:
        try:
            await Newsfeed.create(**details)
            return True
        except Exception as e:
            print(f"Error creating newsfeed: {e}")
            return False

    async def update_newsfeed(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            newsfeed = await Newsfeed.get(id)
            await newsfeed.update(**details).apply()
            return True
        except Exception as e:
            print(f"Error updating newsfeed: {e}")
            return False

    async def delete_newsfeed(self, id: int) -> bool:
        try:
            newsfeed = await Newsfeed.get(id)
            await newsfeed.delete()
            return True
        except Exception as e:
            print(f"Error deleting newsfeed: {e}")
            return False

    async def get_newsfeed_by_id(self, id: int):
        try:
            return await Newsfeed.get(id)
        except Exception as e:
            print(f"Error retrieving newsfeed: {e}")
            return None
        
    async def get_all_newsfeed(self) -> List[Dict[str, Any]]:
        try:
            newsfeeds = await Newsfeed.query.gino.all()
            return [newsfeed.to_dict() for newsfeed in newsfeeds]
        except Exception as e:
            print(f"Error retrieving all newsfeed: {e}")
            return []