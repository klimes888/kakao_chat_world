class WorldDto:
    def __init__(self, name, desc, bot_id, image_url):
        self.name = name
        self.desc = desc
        self.image_url = image_url
        self.bot_id = bot_id

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "bot_id": self.bot_id,
            "image_url": self.image_url,
        }
