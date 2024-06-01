class WorldDto:
    def __init__(self, name, desc, chat_id, image_url, user_id):
        self.name = name
        self.desc = desc
        self.image_url = image_url
        self.chat_id = chat_id
        self.user_id = user_id

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.name,
            "chat_id": self.chat_id,
            "image_url": self.image_url,
            "user_id": self.user_id,
        }
