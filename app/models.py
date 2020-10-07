from datetime import datetime
from app import db


########################################
#  You do not need to touch this file  #
########################################


class Sandwich(db.Model):
    """
    DEMO CODE
    """
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), index=True)
    bread = db.Column(db.String(120), index=True)
    filling = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<Sandwich {}>'.format(self.name)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bread": self.bread,
            "filling": self.filling
        }


class SandwichManager:

    @staticmethod
    def get_all_sandwiches():
        return Sandwich.query.all()

    @staticmethod
    def get_sandwich_by_id(sandwich_id):
        return Sandwich.query.get(sandwich_id)

    @staticmethod
    def create_sandwich(sandwich_dict):
        sandwich_name = sandwich_dict.get('name', "")
        sandwich_bread = sandwich_dict.get('bread', "")
        sandwich_filling = sandwich_dict.get('filling', "")
        sandwich = Sandwich(
            name=sandwich_name,
            bread=sandwich_bread,
            filling=sandwich_filling
        )
        db.session.add(sandwich)
        db.session.commit()
        return sandwich

    @staticmethod
    def delete_sandwich(sandwich_id):
        sandwich = Sandwich.query.get(sandwich_id)
        if sandwich:
            db.session.delete(sandwich)
            db.session.commit()
        else:
            raise ValueError(
                "Could not find Sandwich with ID: " + str(sandwich_id)
            )
        return True


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(10), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.String(64), index=True)
    content = db.Column(db.String(120))

    def __repr__(self):
        return '<Message {} from {}'.format(self.id, self.chat_id)

    def to_dict(self):
        return {
            "id": self.id,
            "chat_id": self.chat_id,
            "timestamp": str(self.timestamp),
            "username": self.username,
            "content": self.content
        }


class MessageManager:

    @staticmethod
    def get_all_messages():
        return Message.query.all()

    @staticmethod
    def get_message_by_id(message_id):
        return Message.query.get(message_id)

    @staticmethod
    def filter_messages_by_chat_id(chat_id):
        return Message.query.filter(Message.chat_id == chat_id)

    @staticmethod
    def get_last_messages(num_messages):
        return Message.query.order_by(Message.timestamp.desc()).limit(num_messages)

    @staticmethod
    def create_message(message_dict):
        message_username = message_dict.get('username', "")
        message_content = message_dict.get('content', "")
        message_chat_id = message_dict.get('chat_id', "")
        message = Message(
            username=message_username,
            content=message_content,
            chat_id=message_chat_id
        )
        db.session.add(message)
        db.session.commit()
        return message

    @staticmethod
    def delete_message(message_id):
        message = Message.query.get(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
        else:
            raise ValueError(
                "Could not find Message with ID: " + str(message_id)
            )
        return True
