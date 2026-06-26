from sqlalchemy import select

from ViajeiAPI.models import User


def test_create_user(session):
    new_user = User("Fulaninho", "fulaninho@gmail.com", "123")

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "Fulaninho"))

    breakpoint()

    assert user.username == "Fulaninho"
