import json
from datetime import datetime
from bson import ObjectId

class DataEncoder(json.JSONEncoder):
    """JSON Encoder 확장
    필요할경우 추가적으로 확장해주면 된다
    """
    def default(self, o):
        # bson.ObjectId 형일경우 string으로 반환
        if isinstance(o, ObjectId):
            return str(o)
        # datetime 형일경우 isoformat으로 반환
        elif isinstance(o, datetime):
            return o.isoformat()
        
        return super().default(o)