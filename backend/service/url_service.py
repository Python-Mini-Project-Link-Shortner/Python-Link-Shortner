# Python Standard Libraries
from datetime                   import datetime
from urllib.parse               import urlparse
# Third-Party Libraries
from short_url                  import encode_url
from lxml.html                  import fromstring
import requests
# Custom modules
from backend.database.mongo_db  import db


def create_short_url(unique_id:int):
    """7자리 문자열을 생성한다.
    
    Args:
        unique_id (int): 고유 숫자
    Returns:
        str : 고유 숫자에 대응하는 7자리 문자열
    """
    return encode_url(unique_id, min_length=7)
    
def validate_url(raw_url):
    """올바른 URL 형식인지 확인한다.

    Args:
        raw_url (str): 검사할 URL
    Returns:
        bool: 올바른 URL이면 True, 아니면 False
    """
    try:
        urlparse(raw_url)
        return True
    except:
        return False

def normalize_url(raw_url):
    """URL에 생략된 부분이 있으면 붙여준다.

    Args:
        raw_url (str): 수정할 원본 URL

    Returns:
        str: 수정된 URL
    """
    # 프로토콜을 추가한다.
    # 그대로 파싱할 경우 도메인을 path로 인식한다.
    valid_protocols = ('http://', 'https://', '//')
    if not raw_url.startswith(valid_protocols):
        raw_url = '//' + raw_url

    # URL을 파싱한다. 기본 프로토콜은 http.
    parse = urlparse(raw_url, scheme='http')

    return parse.geturl()

def get_page_title(raw_url):
    """해당 URL의 제목을 추출한다.

    Args:
        url (str): 제목을 추출할 URL
    """
    r = requests.get(raw_url)
    parse_tree = fromstring(r.content)
    return parse_tree.findtext('.//title')

def get_url(url, target="short"):
    """DB에서 축약된 URL을 가져온다.

    Args:
        url (str): 원본 URL
        target (str): 검색할 URL (short | raw)

    Returns:
        str: 축약 URL
        None: DB에 없는 경우

    Raises:
        ValueError: target 인수값이 잘못된 경우
    """
    target = target.lower()
    if target not in ('short', 'raw'):
        raise ValueError('target 인수가 잘못되었습니다. short 또는 raw로 입력해주십시오.')

    collection = db.get_collection()

    if target == 'short':
        search_from = 'rawURL'
        search_for  = 'shortURL'
    elif target == 'raw':
        search_from = 'shortURL'
        search_for  = 'rawURL'

    res = collection.find_one({ search_from: url })

    if res is None: return None
    return res[search_for]

def get_unique_id():
    """URL 생성을 위한 고유 ID값을 가져온다.

    Returns:
        int: 고유 ID값
        None: 찾지 못한 경우
    """
    collection = db.get_collection('CONFIG')
    
    my_query    = {'variable': 'unique_id'}     # 검색필드
    my_result   = {'value': True}               # 결과필드

    res = collection.find_one(my_query, my_result)

    return res['value']

def increase_id():
    """URL 생성에 사용될 ID(int)를 증가시킨다.

    Returns:
        bool: 성공/실패 = True/False
    """
    collection = db.get_collection('CONFIG')

    my_query    = {'variable': 'unique_id'}   # variable 필드값이 unique_id
    new_value   = {'$inc': {'value': 1}}      # value 필드를 1 증가
    
    res = collection.update_one(my_query, new_value)

    return res.modified_count > 0        

def register_url(raw_url, user_id):
    """축약 링크를 등록한다.

    Args:
        short_url (str): 축약 URL
        user_id   (str): 유저 이메일

    Returns:
        str: DB에 등록된 축약 URL
        None: 저장에 실패한 경우
    """
    collection = db.get_collection()

    # 축약 URL 생성
    unique_id = get_unique_id()
    short_url = create_short_url(unique_id)

    # DB에 신규등록
    data = {
        'rawURL': raw_url,
        'shortURL': short_url,
        'pageTitle': get_page_title(raw_url),
        'userID': user_id,
        'makeDate': datetime.now(),
        'favorite': False
    }

    try:
        collection.insert_one(data)
    except Exception as e:
        # 저장에 실패한 경우 None 반환
        print(e)
        return None
    increase_id()

    return short_url



