from flask                  import Blueprint, request, jsonify
from backend.service        import link_service, url_service, stat_service

manage_controller = Blueprint('manage_controller', __name__)

@manage_controller.route('/linkList', methods=['POST'])
def link_list():
    req_data = request.get_json()

    user_id = req_data['userID']
    page = req_data['page']
    item_count = req_data['itemCount']

    # 링크 페이지네이션 형태로 가져오기
    res = link_service.get_unhide_link_pagination(user_id, page, item_count)

    return res

@manage_controller.route('/favoriteList', methods=['POST'])
def favorite_list():
    req_data = request.get_json()

    user_id = req_data['userID']
    page = req_data['page']
    item_count = req_data['itemCount']

    # 즐겨찾기 페이지네이션 형태로 가져오기
    res = link_service.get_unhide_favorite_link_pagination(user_id, page, item_count)

    return res

@manage_controller.route('/deleteLink', methods=['POST'])
def delete_link():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['deleteID']

    res_data = { 'flag': True }
    # TODO :
    # 나중에 res가 false이면 MongoDB가 transaction 지원 없으므로 SQL 전부 저장해서 원복시켜야 합니다
    # 기술 지원 따로 있음. 찾아보기.
    if len(item_list) == 1:
        res = link_service.delete_link(user_id, item_list[0])
        if res == False: res_data['flag'] = False
    else:
        res = link_service.delete_link_array(user_id, item_list)
        if res == False: res_data['flag'] = False

    return jsonify(res)

@manage_controller.route('/changeTag', methods=['POST'])
def change_tag():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['changeID']
    tag_name = req_data['tagName']

    res_data = { 'flag': True }

    if len(item_list) == 1:
        res = link_service.change_tag(user_id, item_list[0], tag_name)
        if res == False: res_data['flag'] = False
    else:
        res = link_service.change_tag_array(user_id, item_list, tag_name)
        if res == False: res_data['flag'] = False

    return jsonify(res)

@manage_controller.route('/deleteTag', methods=['POST'])
def delete_tag():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['deleteID']

    res_data = { 'flag': True }

    if len(item_list) == 1:
        res = link_service.delete_tag(user_id, item_list[0])
        if res == False: res_data['flag'] = False
    else:
        res = link_service.delete_tag_array(user_id, item_list)
        if res == False: res_data['flag'] = False

    return jsonify(res)

@manage_controller.route('/checkFavorite', methods=['POST'])
def check_favorite():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['favoriteID']

    res_data = { 'flag': True }

    if len(item_list) == 1:
        res = link_service.change_favorite(user_id, item_list[0], True)
        if res == False: res_data['flag'] = False
    else:
        res = link_service.change_favorite_array(user_id, item_list, True)
        if res == False: res_data['flag'] = False

    return jsonify(res)

@manage_controller.route('/uncheckFavorite', methods=['POST'])
def uncheck_favorite():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['favoriteID']

    res_data = { 'flag': True }

    if len(item_list) == 1:
        res = link_service.change_favorite(user_id, item_list[0], False)
        if res == False: res_data['flag'] = False
    else:
        res = link_service.change_favorite_array(user_id, item_list, False)
        if res == False: res_data['flag'] = False

    return jsonify(res)

@manage_controller.route('/hideNameList', methods=['POST'])
def hide_name_list():
    req_data = request.get_json()

    user_id = req_data['userID']

    res = link_service.get_hide_name_list(user_id)

    return jsonify(res)

@manage_controller.route('/hideLink', methods=['POST'])
def hide_link():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['hideID']
    hide_name = req_data['hideName']

    res_data = { 'flag': True }

    if len(item_list) == 1:
        res = link_service.hide_link(user_id, item_list[0], hide_name)
        if res == False: res_data['flag'] = False
    else:
        res = link_service.hide_link_array(user_id, item_list, hide_name)
        if res == False: res_data['flag'] = False

    return jsonify(res)

@manage_controller.route('/unhideLink', methods=['POST'])
def unhide_link():
    req_data = request.get_json()

    user_id = req_data['userID']
    item_list = req_data['hideID']

    res_data = { 'flag': True }

    if len(item_list) == 1:
        res = link_service.unhide_link(user_id, item_list[0])
        if res == False: res_data['flag'] = False
    else:
        res = link_service.unhide_link_array(user_id, item_list)
        if res == False: res_data['flag'] = False

    return jsonify(res_data)

@manage_controller.route('/tagList', methods=['POST'])
def tag_list():
    req_data = request.get_json()

    user_id = req_data['userID']

    tags = link_service.get_tag_list(user_id)

    res_data = { 'flag': True, 'tags': tags }
    if tags == None:
        res_data['flag'] = False

    return jsonify(res_data)

@manage_controller.route('/taggedLinkList', methods=['POST'])
def tagged_link_list():
    req_data = request.get_json()

    user_id = req_data['userID']
    tag_name = req_data['tag']

    links = link_service.get_tagged_link_list(user_id, tag_name)

    res_data = { 'flag': True, 'link': links}
    if links == None:
        res_data['flag'] = False
    
    return jsonify(res_data)

@manage_controller.route('/tempStat', methods=['POST'])
def tempStat():
    req_data = request.get_json()

    user_id = req_data['userID']
    short_url = req_data['shortURL']

    stat = stat_service.get_stats_info(short_url)

    res_data = { 'flag': True, 'stat': stat }
    if stat == None:
        res_data['flag'] = False

    return jsonify(res_data)