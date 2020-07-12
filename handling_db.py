from pymongo import MongoClient
from voluptuous import Schema, Required, All, Url

DEFAULT_HOST = 'mongodb+srv://admin:1234@links.fc8p4.mongodb.net/PYTHON-LINK-SHORTNER?retryWrites=true&w=majority'

class MongoDB(MongoClient):
    def __init__(self, host=None, db='slink', collection='link_table'):
        self._db = db                    # DB명
        self._col = collection           # Collection명
        self.default_host = host         # DB 호스트 명
        if not host:
            self.default_host = DEFAULT_HOST
        self.schema = Schema({           # 저장할 때의 유효성 검사 스키마
            Required('Raw_URL'): Url(),
            Required('Short_URL'): All(str)
        })
        super().__init__(self.default_host)
    
    def save_data(self, data):
        # DB에 저장한다.
        collection = self[self._db][self._col]

        try:
            # 유효성 검사 후 DB에 추가한다.
            self.schema(data)
            collection.insert_one(data)
            return True
        except Exception as e:
            # 스키마에 충족하지 않으면 False 반환
            print(e)
            return False

    def get_URL(self, query):
        # 쿼리 구문을 통해 DB에서 데이터를 가져온다.
        collection = self[self._db][self._col]
        
        return collection.find_one(query)['Raw_URL']