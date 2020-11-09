# Third Party Libraries
from flask              import Blueprint, request, jsonify
# Custom Modules
from backend.service    import stat_service

stat_controller = Blueprint('stat_controller', __name__)

@stat_controller.route('/getStats', methods=['POST'])
def get_stats():
    req_data = request.get_json()

    user_id = req_data['userID']
    short_url = req_data['shortURL']

    stat = stat_service.get_stats_info(short_url)

    res_data = { 'flag': True, 'stat': stat }
    if stat == None:
        res_data['flag'] = False
        res_data['stat'] = {}

    return jsonify(res_data)