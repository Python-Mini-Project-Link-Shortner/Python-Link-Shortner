from backend.database.mongo_db          import db
from bson                               import ObjectId
from backend.database.util.pagination   import pagination

def get_link_pagination(user_id, page = 1, item_count = 10):
    collection = db.get_collection()

    res = collection.find({ 'userID': user_id })
    if res is None: return None

    return pagination(res, [('makeDate', -1)], page, item_count)

def delete_link(user_id, link_id):
    collection = db.get_collection()

    result = collection.delete_one({ '_id': ObjectId(link_id), 'userID': user_id })

    # 정상적으로 삭제되었을경우 True 반환
    if result.deleted_count == 1: return True
    return False

def delete_link_array(user_id, link_array):
    collection = db.get_collection()

    result = collection.delete_many({ 'userID': user_id, '_id': map(ObjectId, link_array)})
    if result.deleted_count == len(link_array):
        return True

    return False