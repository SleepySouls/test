from model.data.gino_model import User
from typing import Dict, Any, List

class UserRepository:

    async def create_user(self, details: Dict[str, Any]) -> bool:
        try:
            await User.create(**details)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    async def update_user(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            user = await User.get(id)
            await user.update(**details).apply()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    async def delete_user(self, id: int) -> bool:
        try:
            user = await User.get(id)
            await user.delete()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    async def get_user_by_id(self, id: int):
        try:
            return await User.get(id)
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None
        
    async def get_all_user(self) -> List[Dict[str, Any]]:
        try:
            users = await User.query.gino.all()
            return [user.to_dict() for user in users]
        except Exception as e:
            print(f"Error retrieving all user: {e}")
            return []