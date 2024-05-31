from model.data.gino_model import Signup
from typing import Dict, Any, List

class SignupRepository:

    async def create_signup_user(self, details: Dict[str, Any]) -> bool:
        try:
            await Signup.create(**details)
            return True
        except Exception as e:
            print(f"Error creating signup user: {e}")
            return False

    async def update_signup_user(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            user = await Signup.get(id)
            await user.update(**details).apply()
            return True
        except Exception as e:
            print(f"Error updating signup user: {e}")
            return False

    async def delete_signup_user(self, id: int) -> bool:
        try:
            user = await Signup.get(id)
            await user.delete()
            return True
        except Exception as e:
            print(f"Error deleting signup user: {e}")
            return False

    async def get_signup_user_by_id(self, id: int):
        try:
            return await Signup.get(id)
        except Exception as e:
            print(f"Error retrieving signup user: {e}")
            return None
        
    # async def get_all_signup_users(self) -> List[Dict[str, Any]]:
    #     try:
    #         users = await Signup.query.gino.all()
    #         return [user.to_dict() for user in users]
    #     except Exception as e:
    #         print(f"Error retrieving all signup users: {e}")
    #         return []
    async def get_all_signup_users(self, username: str = None) -> List[Dict[str, Any]]:
        try:
            query = Signup.query.gino.all()
            if username:
                query = query.filter(Signup.username == username)
            users = await query
            return [user.to_dict() for user in users]
        except Exception as e:
            print(f"Error retrieving all login users: {e}")
            return []