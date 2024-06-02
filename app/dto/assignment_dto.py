class AssignmentDto:
    def __init__(self, **kwargs):
        self.role = kwargs.get("role", None)
        self.user_id = kwargs.get("user_id", None)
        self.world_id = kwargs.get("world_id", None)

    def to_dict(self):
        return {
            "role": self.role,
            "user_id": self.user_id,
            "world_id": self.world_id,
        }
