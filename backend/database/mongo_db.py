from pymongo import MongoClient, errors, collection

DEFAULT_HOST = 'mongodb+srv://admin:1234@links.fc8p4.mongodb.net/PYTHON-LINK-SHORTNER?retryWrites=true&w=majority'
DEFAULT_COL = 'linkTable'
DEFAULT_DB = 'slink'
COLLECTIONS = {
    'LINKS': 'linkTable',
    'STATS': 'statTable',
    'USERS': 'userTable',
    'CONFIG': 'config'
}

class MongoDB(MongoClient):
    """MongoDB 설정해주는 클래스

    Args:
            host (str, optional): DB 호스트 명. Defaults to None.
            db (str, optional): DB 이름. Defaults to DEFAULT_DB.
            collection (str, optional): Collection 이름. Defaults to DEFAULT_COL
    """
    def __init__(self, host=None, db=DEFAULT_DB, collection=DEFAULT_COL):
        self._db = db                    # DB명
        self._col = collection           # Collection명
        self.default_host = host         # DB 호스트 명
        if not host:
            self.default_host = DEFAULT_HOST
        super().__init__(self.default_host)

    def get_collection(self, name='LINKS') -> collection.Collection:
        """데이터베이스에서 원하는 pymongo collection을 가져온다

        Args:

                name (str): COLLECTIONS 배열안에 정의된 이름만 가능합니다

        Returns:

                pymongo.collection.Collection: pymongo의 Collection 클래스 데이터가 반환됩니다

        Raises:
        
                pymongo.erros.CollectionInvalid: 잘못된 Collection 이름
        """
        name = name.upper()
        if name not in COLLECTIONS:
            print("콜렉션 이름이 잘못되었으므로 확인해주세요")
            print("콜렉션 이름은 mongo_db.py안의 COLLECTIONS에 저장되어 있습니다")
            raise errors.CollectionInvalid("콜렉션{" + name + "} 이름이 잘못되었습니다")

        return self[self._db][COLLECTIONS[name]]

db = MongoDB()