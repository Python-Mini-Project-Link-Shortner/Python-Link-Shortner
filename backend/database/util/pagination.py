import math

def pagination(data, sort_dict = None, page = 1, item_count = 10):
    """페이지네이션 만들어주는 함수

    Args:

            data (pymongo.cursor.Cursor): 페이지네이션 하고 싶은 MongoDB의 기본 Cursor 데이터
            sort_dict (List, optional): 정렬하기 위한 [('이름': 1 또는 -1), ('이름': 1 또는 -1)...] 형태의 값. 1일경우 Asc, -1일경우 Desc. Defaults to None.
            page (int, optional): 원하는 페이지 번호. Defaults to 1.
            item_count (int, optional): 한 페이지 당 아이템 갯수. Defaults to 10.
    """
    if data is None:
        return None

    # 최대 페이지 저장
    max_page = math.ceil(data.count() / item_count)

    # 0 ~ maxPage로 페이지 제한
    if page < 1: page = 1
    if page > max_page: page = max_page

    # sort 옵션
    if sort_dict is not None:
        data.sort(sort_dict)

    data_list = list(data.skip((page - 1) * item_count).limit(item_count))

    return { 'page': page, 'maxPage': max_page, 'list': data_list }