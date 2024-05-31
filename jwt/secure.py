from fastapi import Depends, HTTPException, status

from model.request.tokens import TokenData
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, HTTPBasic
from jose import jwt, JWTError

from model.data.gino_model import Signin, Signup
from sqlalchemy.orm import Session
from db_config.gino_connect import sess_db
from repository.signin_repo import SigninRepository
from sqlalchemy.orm import Session
from cqrs.signup.query.query_handlers import ListSignupQueryHandler
from cqrs.signup.queries import SignupListQuery

from datetime import datetime, timedelta, timezone

brypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
http_basic = HTTPBasic()

SECRET_KEY = "tbWivbkVxfsuTxCP8A+Xg67LcmjXXl/sszHXwH+TX9w="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login_user/token")

def get_password_hash(password):
    return brypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return brypt_context.verify(plain_password, hashed_password)

def verify_user(username, exist_username):
    return (username == exist_username)

async def get_user_credentials():
    handler = ListSignupQueryHandler()
    query:SignupListQuery = await handler.handle() 
    records = query.records
    usernames = [record['username'] for record in records]
    passwords = [record['password'] for record in records]
    return {'usernames': usernames, 'passwords': passwords}

async def authenticate(username, password):
    try:
        account = await get_user_credentials()
        if account is None:
            return False
        usernames = account['usernames']
        passwords = account['passwords']
        if username not in usernames:
            return False
        index = usernames.index(username)
        if not verify_password(password, passwords[index]):
            return False
        return True
    except Exception as e:
        print(e)
        return False
def create_access_token(data: dict, expires_after: timedelta):
    plain_text = data.copy()
    expire = datetime.now(timezone.utc) + expires_after
    plain_text.update({"exp": expire})
    encoded_jwt = jwt.encode(plain_text, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
       
def get_current_user(token: str = Depends(oauth2_scheme), sess:Session = Depends(sess_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    loginrepo = SigninRepository(sess)
    user = loginrepo.get_all_login_users(token_data.username)
    if user is None:
        raise credentials_exception
    return user
