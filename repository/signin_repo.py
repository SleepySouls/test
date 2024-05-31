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

    async def authenticate_login_user(self, username: str, password: str) -> bool:
        try:
            user = await Signin.query.where(
                (Signin.username == username) & 
                (Signin.password == password)
            ).gino.first()
            return user is not None
        except Exception as e:
            print(f"Authentication error: {e}")
            return False

    async def update_login_user(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            user = await Signin.get(id)
            await user.update(**details).apply()
            return True
        except Exception as e:
            print(f"Error updating login user: {e}")
            return False

    async def delete_login_user(self, id: int) -> bool:
        try:
            user = await Signin.get(id)
            await user.delete()
            return True
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