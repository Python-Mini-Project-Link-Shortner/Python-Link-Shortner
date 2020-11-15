from backend.database.mongo_db          import db
from bson                               import ObjectId
from backend.database.util.pagination   import pagination
import pymongo

def get_link_pagination(user_id, page = 1, item_count = 10):
    """아이디가 가진 링크를 페이지대로 가져온다

    Args:

            user_id (str): 아이디
            page (int, optional): 페이지 번호. Defaults to 1.
            item_count (int, optional): 페이지 당 링크 갯수. Defaults to 10.

    Returns:

            pagination: 페이지네이션 데이터
    """
    collection = db.get_collection()

    res = collection.find({ 'userID': user_id })

    return pagination(res, [('makeDate', pymongo.DESCENDING)], page, item_count)

def get_unhide_link_pagination(user_id, page = 1, item_count = 10):
    """아이디가 가진 숨겨지지 않은 링크를 페이지대로 가져온다

    Args:

            user_id (str): 아이디
            page (int, optional): 페이지 번호. Defaults to 1.
            item_count (int, optional): 페이지 당 링크 갯수. Defaults to 10.

    Returns:

            pagination: 페이지네이션 데이터
    """
    collection = db.get_collection()

    res = collection.find({ 'userID': user_id, '$or': [ { 'hide': { '$exists': False } }, { 'hide': False } ] })

    return pagination(res, [('makeDate', pymongo.DESCENDING)], page, item_count)

def get_unhide_favorite_link_pagination(user_id, page = 1, item_count = 10):
    """아이디가 가진 즐겨찾기에 추가된 숨겨지지 않은 링크를 페이지대로 가져온다

    Args:
    
                user_id (str): 아이디
                page (int, optional): 페이지 번호. Defaults to 1.
                item_count (int, optional): 페이지 당 링크 갯수. Defaults to 10.

        Returns:

                pagination: 페이지네이션 데이터
        """
    collection = db.get_collection()

    res = collection.find({ 'userID': user_id, 'favorite': True,
        '$or': [ { 'hide': { '$exists': False } }, { 'hide': False } ] })

    return pagination(res, [('makeDate', pymongo.DESCENDING)], page, item_count)

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
            id_array (list): 삭제할 링크 아이디 배열

    Returns:
        
            bool: 정상 삭제일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.delete_many({ 'userID': user_id, '_id': { '$in': list(map(ObjectId, id_array)) }})

    if result.deleted_count == len(id_array): return True
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
            id_array (list): 태그를 변경할 링크 아이디 배열
            tag_name (str): 태그 이름

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': list(map(ObjectId, id_array)) } }, { '$set': { 'tagName': tag_name } })

    if result.modified_count == len(id_array): return True
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
            id_array (list): 링크 아이디 배열

    Returns:

            bool: 정상 삭제일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': list(map(ObjectId, id_array)) } }, { '$unset': { 'tagName': '' } })

    # 정상적으로 변경되었을경우 True 반환
    if result.modified_count == len(id_array): return True
    return False

def change_favorite(user_id, favorite_id, favorite):
    """링크의 즐겨찾기 여부를 변경한다

    Args:

            user_id (str): 아이디
            favorite_id (str): 즐겨찾기에 추가할 링크 아이디
            favorite (bool): 변경할 즐겨찾기 값

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_one({ 'userID': user_id, '_id': ObjectId(favorite_id) }, { '$set': { 'favorite': favorite } })

    if result.modified_count == 1: return True
    return False

def change_favorite_array(user_id, favorite_id_array, favorite):
    """링크들의 즐겨찾기 여부를 변경한다
    
    Args:

            user_id (str): 아이디
            favorite_id_array (list): 즐겨찾기에 추가할 링크들 아이디
            favorite (bool): 변경할 즐겨찾기 값

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': list(map(ObjectId, favorite_id_array)) } }, { '$set': { 'favorite': favorite } })

    if result.modified_count == len(favorite_id_array): return True
    return False

def get_hide_name_list(user_id):
    """숨김경로 가져오기

    Args:

            user_id (str): 아이디

    Returns:

            list: 숨김경로들을 list로 가져온다. 없을경우 None.
    """
    collection = db.get_collection()

    # distinct는 list를 반환한다
    result = collection.find({
        'userID': user_id,
        'hide': True,
        '$and': [ {'hideName': { '$ne': None } }, { 'hideName': { '$ne': "" } } ],
        })

    if result is None: return None

    # 정렬 후 반환
    result = result.distinct('hideName')
    result.sort()
    return result

def hide_link(user_id, hide_id, hide_name):
    """링크를 특정 경로에 숨긴다

    Args:

            user_id (str): 아이디
            hide_id (str): 링크 아이디
            hide_name (str): 숨김경로

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_one({ 'userID': user_id, '_id': ObjectId(hide_id) }, { '$set': { 'hide': True, 'hideName': hide_name } })

    if result.modified_count == 1: return True
    return False

def hide_link_array(user_id, hide_id_array, hide_name):
    """링크들을 특정 경로에 숨긴다

    Args:

            user_id (str): 아이디
            hide_id_array (list): 숨길 링크들 아이디
            hide_name (str): 숨김경로

    Returns:

            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': list(map(ObjectId, hide_id_array)) } }, { '$set': { 'hide': True, 'hideName': hide_name } })

    if result.modified_count == len(hide_id_array): return True
    return False

def unhide_link(user_id, unhide_id):
    """숨겨진 링크를 다시 보이게 변경한다

    Args:

            user_id (str): 아이디
            unhide_id (str): 다시 보이게 할 링크 아이디

    Returns:
        
            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_one({ 'userID': user_id, '_id': ObjectId(unhide_id) }, { '$set': { 'hide': False }, '$unset': { 'hideName': '' } })

    if result.modified_count == 1: return True
    return False

def unhide_link_array(user_id, unhide_id_array):
    """숨겨진 링크들을 다시 보이게 변경한다

    Args:

            user_id (str): 아이디
            unhide_id_array (list): 다시 보이게 할 링크들 아이디

    Returns:
    
            bool: 정상 변경일경우 True, 그 외는 False
    """
    collection = db.get_collection()

    result = collection.update_many({ 'userID': user_id, '_id': { '$in': list(map(ObjectId, unhide_id_array)) } }, { '$set': { 'hide': False }, '$unset': { 'hideName': '' } })

    if result.modified_count == len(unhide_id_array): return True
    return False

def get_tag_list(user_id):
    collection = db.get_collection()

    result = collection.find({
        'userID': user_id,
        '$and': [ {'tagName': { '$ne': None } }, { 'tagName': { '$ne': "" } } ],
        '$or': [ { 'hide': { '$exists': False } }, { 'hide': False } ] })

    if result is None: return None

    result = result.distinct('tagName')
    result.sort()
    return result

def get_tagged_link_list(user_id, tag):
    collection = db.get_collection()

    result = collection.find({
        'userID': user_id,
        'tagName': tag,
        '$or': [ { 'hide': { '$exists': False } }, { 'hide': False } ]
    })

    if result is None: return None

    return list(result)

def get_hidden_link_list(user_id, directory):
    collection = db.get_collection()

    result = collection.find({
        'userID': user_id,
        'hide': True,
        'hideName': directory
    })

    if result is None: return None

    return list(result)