from fastapi import APIRouter
from db.models.user import User
from .schemas import APIKey, Signup, SignupResponse, Login, LoginResponse

router = APIRouter()


@router.get("/my_details/")
def get_current_user(current_user: User):
    return current_user


router = APIRouter()


@router.post("/signup", response_model=SignupResponse)
async def create_user(signup: Signup):
    return signup


@router.post("/login", response_model=LoginResponse)
async def login(login: Login):
    return login


@router.get("/key")
async def get_user_api_key():
    # Check Database if User id exist
    # Depends on session user id

    # If user exist get user APIkey
    userAPIKey = APIKey(
        key="3fa85f64-5740-2262-b3fc-2c963f36afa1",
        user="3fa85f64-5740-2262-b3fc-2c963f36afa1",
    )

    # Send key string
    return userAPIKey
