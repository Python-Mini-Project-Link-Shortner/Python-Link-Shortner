from pymongo import MongoClient

DEFAULT_HOST = 'mongodb+srv://admin:1234@links.fc8p4.mongodb.net/PYTHON-LINK-SHORTNER?retryWrites=true&w=majority'

class MongoDB(MongoClient):
    def __init__(self, host=None, db='slink', collection='link_table'):
        self._db = db                    # DB명
        self._col = collection           # Collection명
        self.default_host = host
        if not host:
            self.default_host = DEFAULT_HOST
        super().__init__(self.default_host)
        pass
    
    def save_data(self, data):
        # DB에 저장한다.
        pass

    def get_data(self, query):
        # 쿼리 구문을 통해 DB에서 데이터를 가져온다.
        pass