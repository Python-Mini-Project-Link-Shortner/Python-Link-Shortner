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

def upsert_user(email, payload):
    """유저에 대해 update와 insert를 동시에 수행한다

    Args:

            email (str): 저장할 혹은 갱신할 email
            payload (Obj): 갱신할 정보. { 'field': value } 형식으로 전달.
    """
    collection = db.get_collection("USERS")

    # 생성 시 기본값 설정
    now = datetime.now()
    defaults = {
        'banned': False,
        'lastLogin': now,
        'lastAccess': now,
        'created': now,
        'idToken': "",
        'refreshToken': ""
    }
    for key in payload:
        if key in defaults: defaults.pop(key)

    # 기본설정할 것이 있을 때만 upsert
    if not defaults:
        collection.update_one({'email': email}, {
            '$set': payload
        })
    else:
        collection.update_one({ 'email': email }, {
            '$setOnInsert': { 
                'banned': False, 
                'created': datetime.now()
                },
            '$set': payload
        }, upsert=True)

