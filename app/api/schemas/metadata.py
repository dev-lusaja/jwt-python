# -*- coding: utf-8 -*-
class MetadataSchema:
    def __init__(self):
        pass

    @staticmethod
    def get():
        schema = {
            "title": "user",
            "type": "object",
            "properties": {
                "metadata": {"type": "object"}
            },
            "required": ["metadata"]
        }
        return schema
