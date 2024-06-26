class CountryCategoryDto:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.desc = kwargs.get("desc", None)
        self.image_url = kwargs.get("image_url", None)
        self.content_id = kwargs.get("content_id", None)
        self.type = kwargs.get("type", None)
        self.value = kwargs.get("value", None)

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "image_url": self.image_url,
            "content_id": self.content_id,
            "type": self.type,
            "value": self.value,
        }
