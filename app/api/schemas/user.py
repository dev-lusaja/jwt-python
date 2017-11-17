class UserSchema:

    def __init__(self):
        pass

    @staticmethod
    def get():
        schema = {
            "title": "user",
            "type": "object",
            "properties": {
                "metadata": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        "email": {"type": "string", "format": "email"}
                    },
                    "required": ["id", "name", "email"]
                }

            },
            "required": ["metadata"]
        }
        return schema
