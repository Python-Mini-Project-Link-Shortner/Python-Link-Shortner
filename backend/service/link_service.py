from backend.database.mongo_db          import db
from bson                               import ObjectId
from backend.database.util.pagination   import pagination

def get_link_pagination(user_id, page = 1, item_count = 10):
    """아이디가 가진 축약된 링크를 페이지대로 가져온다

    Args:

            user_id (str): 아이디
            page (int, optional): 페이지 번호. Defaults to 1.
            item_count (int, optional): 페이지 당 링크 갯수. Defaults to 10.

    Returns:

            pagination: 페이지네이션 데이터
    """
    collection = db.get_collection()

    res = collection.find({ 'userID': user_id })

    return pagination(res, [('makeDate', -1)], page, item_count)

def delete_link(user_id, link_id):
    """링크를 삭제한다

    Args:

            user_id (str): 아이디
            link_id (str): 삭제할 링크 아이디

    Returns:

            bool: 정상 삭제일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.delete_one({ '_id': ObjectId(link_id), 'userID': user_id })

    # 정상적으로 삭제되었을경우 True 반환
    if result.deleted_count == 1: return True
    return False

def delete_link_array(user_id, id_array):
    """링크들을 삭제한다

    Args:

            user_id (str): 아이디
            id_array (array): 삭제할 링크 아이디 배열

    Returns:
        
            bool: 정상 삭제일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.delete_many({ 'userID': user_id, '_id': { '$in': map(ObjectId, id_array) }})
    if result.deleted_count == len(id_array):
        return True

    return False

def change_tag(user_id, change_id, tag_name):
    """링크의 태그를 변경한다

    Args:

            user_id (str): 아이디
            change_id (str): 태그를 변경할 링크 아이디
            tag_name (str): 태그 이름

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_one({ 'userID': user_id, '_id': ObjectId(change_id) }, { '$set': { 'tagName': tag_name } })

    # 정상적으로 변경되었을경우 True 반환
    if result.matched_count == result.modified_count: return True
    return False

def change_tag_array(user_id, id_array, tag_name):
    """링크들의 태그를 변경한다

    Args:

            user_id (str): 아이디
            id_array (array): 태그를 변경할 링크 아이디 배열
            tag_name (str): 태그 이름

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': map(ObjectId, id_array) } }, { '$set': { 'tagName': tag_name } })

    if result.modified_count == len(id_array):
        return True
    return False

def delete_tag(user_id, delete_id):
    """태그를 지운다

    Args:

            user_id (str): 아이디
            delete_id (str): 태그를 지울 링크 아이디

    Returns:

            bool: 정상 삭제일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_one({ 'userID': user_id, '_id': ObjectId(delete_id) }, { '$unset': { 'tagName': '' } })

    # 정상적으로 변경되었을경우 True 반환
    if result.modified_count == 1: return True
    return False

def delete_tag_array(user_id, id_array):
    """태그들을 지운다

    Args:

            user_id (str): 아이디
            id_array (array): 링크 아이디 배열

    Returns:

            bool: 정상 삭제일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': map(ObjectId, id_array) } }, { '$unset': { 'tagName': '' } })

    # 정상적으로 변경되었을경우 True 반환
    if result.modified_count == 1: return True
    return False