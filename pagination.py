import math

class Pagination:
  # data는 mongodb 기본 반환값이 cursor를 넘겨준다
  # sort_dict는 [('이름': 1 또는 -1), ('이름': 1 또는 -1)...]
  # page는 원하는 페이지 번호
  # item_count는 한 페이지 당 아이템 갯수
  @staticmethod
  def paging(data, sort_dict = None, page = 1, item_count = 10):
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