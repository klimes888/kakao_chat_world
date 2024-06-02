from typing import Optional


class UserDto:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)
        self.chat_id = kwargs.get("chat_id", None)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "chat_id": self.chat_id,
        }
