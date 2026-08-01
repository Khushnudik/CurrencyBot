from database.models import History
from database.database import SessionLocal


def get_history(user_id):
    session = SessionLocal()

    try:
        history = (
            session.query(History)
            .filter(History.user_id == user_id)
            .order_by(History.created_at.desc())
            .all()
        )

        return history

    finally:
        session.close()


def save_history(user_id, amount, from_currency, to_currency, result):
    session = SessionLocal()

    try:
        history = History(
            user_id=user_id,
            amount=amount,
            from_currency=from_currency,
            to_currency=to_currency,
            result=result
        )

        session.add(history)
        session.commit()

    finally:
        session.close()