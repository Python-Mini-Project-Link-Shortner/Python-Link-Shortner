import json
from datetime import datetime
from bson import ObjectId

class DataEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        
        return super().default(o)