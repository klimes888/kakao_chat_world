class UserDto:
    def __init__(self, name, chat_id):
        self.name = name
        self.chat_id = chat_id

    def to_dict(self):
        return {
            "name": self.name,
            "chat_id": self.chat_id,
        }
