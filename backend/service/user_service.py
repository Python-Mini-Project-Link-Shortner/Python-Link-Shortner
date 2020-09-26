from datetime                   import datetime
from backend.database.mongo_db  import db

def get_user_info(email):
    """사용자 정보를 전부 가져온다.

    Args:

            email (str): 이메일.

    Returns:

            pymongo.cursor.Cursor: 반환값과 연결된 cursor.
    """
    collection = db.get_collection("USERS")

    return collection.find_one({ 'email': email })

def is_normal_user(email):
    """유저가 정상적인 상태인지 확인한다.

    Args:

            email (str): 유저 이메일 정보.

    Returns:

        bool: 유저가 존재하거나 정지되지 않았을경우 True, 그 외는 False.
    """
    user_info = get_user_info(email)

    if user_info is None:
        return False

    if user_info['banned']:
        return False

    return True

def upsert_user(email, id_token = '', banned = False, last_login = datetime.now()):
    """유저에 대해 update와 insert를 동시에 수행한다

    Args:

            email (str): 저장할 혹은 갱신할 email
            id_token (str, optional): Google OAUTH의 id_token. Defaults to ''.
            banned (bool, optional): 정지상태. Defaults to False.
            last_login ([type], optional): 마지막 로그인 시간. 자동으로 현재 시간으로 갱신한다. Defaults to datetime.now().
    """
    collection = db.get_collection("USERS")

    collection.update_one({ 'email': email }, {
        '$setOnInsert': { 'banned': False },
        '$set': { 'lastLogin': last_login, 'idToken': id_token }
    }, upsert=True)

