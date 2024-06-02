class WorldDto:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.desc = kwargs.get("desc", None)
        self.bot_id = kwargs.get("bot_id", None)
        self.image_url = kwargs.get("image_url", None)

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "bot_id": self.bot_id,
            "image_url": self.image_url,
        }
