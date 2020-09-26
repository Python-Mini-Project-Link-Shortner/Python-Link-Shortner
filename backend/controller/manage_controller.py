from flask                  import Blueprint, request, jsonify
from backend.service        import link_service

manage_controller = Blueprint('manage_controller', __name__)

@app.route('linkList', methods=['POST'])
def link_list():
    req_data = request.get_json()

    user_id = req_data['userID']
    page = req_data['page']
    item_count = req_data['itemCount']

    # 링크 페이지네이션 형태로 가져오기
    res = link_service.get_link_pagination(user_id, page, item_count)

    return res

@app.route('deleteLink', methods=['POST'])
def delete_link():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['deleteID']

    res_data = jsonify({ 'flag': True })
    # TODO :
    # 나중에 res가 false이면 MongoDB가 transaction 지원 없으므로 SQL 전부 저장해서 원복시켜야 합니다
    # 기술 지원 따로 있음. 찾아보기.
    if len(item_list) == 1:
        res = link_service.delete_link(user_id, item_list[0])
        if res == False: res_data['flag'] = False
    else:
        res = link_service.delete_link_array(user_id, item_list)
        if res == False: res_data['flag'] = False

    return res

@app.route('changeTag', methods=['POST'])
def change_tag():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['changeID']
    tag_name = req_data['tagName']

    # TODO :
    # https://stackoverflow.com/questions/57140559/mongodb-query-using-where-and-in-clause
    # MongoDB의 $in을 통해 한번에 변경하는거로 바꿔보자
    change_all = True
    for change_id in item_list:
        res = Mongo.change_tag(user_id, change_id, tag_name)
        if res == False: change_all = False
        # TODO :
        # 나중에 res가 false이면 MongoDB가 transaction 지원 없으므로 SQL 전부 저장해서 원복시켜야 합니다
        # 기술 지원 따로 있음. 찾아보기.

    if change_all is True: return jsonify({ 'flag': True })
    return jsonify({ 'flag': False })

@app.route('deleteTag', methods=['POST'])
def delete_tag():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['deleteID']

    # TODO :
    # https://stackoverflow.com/questions/57140559/mongodb-query-using-where-and-in-clause
    # MongoDB의 $in을 통해 한번에 변경하는거로 바꿔보자
    delete_all = True
    for delete_id in item_list:
        res = Mongo.delete_tag(user_id, delete_id)
        if res == False: delete_all = False
        # TODO :
        # 나중에 res가 false이면 MongoDB가 transaction 지원 없으므로 SQL 전부 저장해서 원복시켜야 합니다
        # 기술 지원 따로 있음. 찾아보기.

    if delete_all is True: return jsonify({ 'flag': True })
    return jsonify({ 'flag': False })