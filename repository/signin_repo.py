from model.data.gino_model import Signin
from typing import Dict, Any, List
from sqlalchemy import func, Sequence
from db_config.gino_connect import db

class SigninRepository:

    async def create_login_user(self, details: Dict[str, Any]) -> bool:
        try:
            async with db.acquire() as conn:
                seq = Sequence('signin_id_seq')
                id = await conn.scalar(func.next_value(seq))
                details['id'] = id
            await Signin.create(**details)
            return True
        except Exception as e:
            print(f"Error creating login user: {e}")
            return False

    async def update_login_user(self, username: str, details: Dict[str, Any]) -> bool:
        try:
            user = await Signin.query.where(Signin.username == username).gino.first()
            if user is not None:
                await user.update(**details).apply()
                return True
            else:
                print(f"No user with username '{username}' found")
                return False
        except Exception as e:
            print(f"Error updating login user: {e}")
            return False

    async def delete_login_user(self, username: str) -> bool:
        try:
            user = await Signin.query.where(Signin.username == username).gino.first()
            if user is not None:
                await user.delete()
                return True
            else:
                print(f"No user with username '{username}' found")
                return False
        except Exception as e:
            print(f"Error deleting login user: {e}")
            return False
    
    async def get_login_user_by_id(self, id: int):
        try:
            return await Signin.get(id)
        except Exception as e:
            print(f"Error retrieving login user: {e}")
            return None
        
    # async def get_all_login_users(self) -> List[Dict[str, Any]]:
    #     try:
    #         users = await Signin.query.gino.all()
    #         return [user.to_dict() for user in users]
    #     except Exception as e:
    #         print(f"Error retrieving all login users: {e}")
    #         return []
    async def get_all_login_users(self, username: str = None) -> List[Dict[str, Any]]:
        try:
            query = Signin.query.gino.all()
            if username:
                query = query.filter(Signin.username == username)
            users = await query
            return [user.to_dict() for user in users]
        except Exception as e:
            print(f"Error retrieving all login users: {e}")
            return []