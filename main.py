from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers

from auth.database import User
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate, UserUpdate


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title="FastApi project"
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend), #requires_verification=True
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

#This router provides routes to manage users
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

#Get the current user
# current_user = fastapi_users.current_user()

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"

#Get the current active and verified user
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_verified_user)):
    return f"Hello, {user.email}"

#Get the current active superuser
# current_superuser = fastapi_users.current_user(active=True, superuser=True)

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_superuser)):
#     return f"Hello, {user.email}"