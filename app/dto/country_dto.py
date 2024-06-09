class CountryDto:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.desc = kwargs.get("desc", None)
        self.image_url = kwargs.get("image_url", None)
        self.world_id = kwargs.get("world_id", None)

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "image_url": self.image_url,
            "world_id": self.world_id,
        }
