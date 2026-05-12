from dataclasses import asdict
from sqlalchemy import select, delete, update
from persistance.database import db
from persistance.models import User

def register(data: dict):
    """
    Registers a new user.
    :param data: Dictionary containing username, email, and password.
    :return: JWT token if registration is successful, otherwise None.
    """
    q = select(User).where((User.username == data["username"]) | (User.email == data["email"]))
    existing_user = db.session.execute(q).first()
    if existing_user:
        return {"status": False, "message": "Username or email already taken!"}

    user = User(
        username=data["username"],
        email=data["email"],
        password=""
    )
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()
    return {"status": True, "data": asdict(user)}


def login(username, password):
    """
    Authenticates a user.
    :param username: Username.
    :param password: Password.
    :return: Returns JWT token if authentication is successful, otherwise None.
    """
    q = select(User).where(User.username == username)
    user = db.session.execute(q).scalar_one_or_none()

    if user and user.check_password(password):
        return user
    return None


def update_account(user_id: int, data: dict):
    """
    Updates user account information.
    :param user_id: ID of the user to update.
    :param data: Dictionary of fields to update.
    :return: status & message
    """
    user = db.session.get(User, user_id)
    if not user:
        return {"status": False, "message": "User not found"}

    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.set_password(data["password"])

    db.session.commit()
    return {"status": True, "message": f"Updated account {user_id}", "data": asdict(user)}


def delete_account(user_id: int):
    """
    Deletes a user account.
    :param user_id: ID of the user to delete.
    :return: status & message
    """
    q = delete(User).where(User.id == user_id)
    result = db.session.execute(q)
    db.session.commit()
    
    if result.rowcount == 0:
        return {"status": False, "message": "User not found"}
        
    return {"status": True, "message": f"Deleted account {user_id}"}
