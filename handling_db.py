from pymongo import MongoClient
from voluptuous import Schema, Required, All, Url

DEFAULT_HOST = 'mongodb+srv://admin:1234@links.fc8p4.mongodb.net/PYTHON-LINK-SHORTNER?retryWrites=true&w=majority'
DEFAULT_COL = 'link_table'
DEFAULT_DB = 'slink'
COLLECTIONS = {
    'LINKS': 'link_table',
    'CONFIG': 'config'
}
QUERIES = {
    'UNIQUE_ID': {'variable': 'unique_id'}
}

class MongoDB(MongoClient):
    def __init__(self, host=None, db=DEFAULT_DB, collection=DEFAULT_COL):
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

    def get_short_url(self, raw_url):
        # Raw_URL로 Short_URL을 검색한다
        collection = self[self._db][self._col]

        # Raw_URL로 검색
        find_item = collection.find_one({"Raw_URL" : raw_url})

        # 없을경우 None 반환
        if find_item is None:
            return None

        # 존재할경우 Short_URL 반환
        return find_item['Short_URL']

    def get_raw_url(self, short_url):
        # Short_URL로 Raw_URL을 검색한다. (방식은 short_url과 동일)
        collection = self[self._db][self._col]

        find_item = collection.find_one({"Short_URL" : short_url})

        if find_item is None:
            return None
        
        return find_item['Raw_URL']

    def get_unique_id(self):
        # URL 생성을 위한 ID 값을 가져온다.
        collection = self[self._db][COLLECTIONS['CONFIG']]

        my_query = QUERIES['UNIQUE_ID']
        my_result = { 'value': True }

        return collection.find_one(my_query, my_result)['value']

    def increase_id(self):
        # URL 생성에 사용될 ID(int)를 증가시킨다.
        collection = self[self._db][COLLECTIONS['CONFIG']]

        my_query = QUERIES['UNIQUE_ID']         # variable 필드값이 unique_id
        new_value = {'$inc': {'value': 1}}      # value 필드값을 1만큼 증가시킨다.
        
        result = collection.update_one(my_query, new_value)

        return result.modified_count > 0        # 추가되었는지 확인한다.