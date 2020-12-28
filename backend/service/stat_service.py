# Python Standard Libraries
from datetime                   import datetime
from urllib.parse               import urlparse
# Third-Party Libraries
import geoip2.database          # ip -> location
# Custom modules
from backend.database.mongo_db  import db

STAT_DEFAULT = {
    'browser': {},
    'count': 0,
    'country': {},
    'entry': {},
    'index': [],
    'platform': {},
    'time': []
}

def get_stats_info(short_url):
    """DB에서 해당 링크의 통계정보를 전부 가져온다.

    Args:
        short_url (str): 축약 링크
    Returns:
        dict: 찾은 통계 정보
        None: 통계 정보가 없는 경우 (클릭수 0)
    """
    collection = db.get_collection("STATS")

    return collection.find_one({ 'shortURL': short_url })

def get_default_stats():
    """빈 통계 정보를 반환한다. 

    Returns:
        dict: 빈 통계 양식
    """
    return STAT_DEFAULT

def extract_stats(headers, environ, user_agent, stats:dict):
    """헤더에서 통계정보를 추출한다.

    Args:
        headers       : Flask request.headers
        environ (dict): Flask request.environ
        user_agent    : Flask request.user_agent
        stats   (dict): 기존 통계 정보
    Returns:
        None: stats에 바로 반영된다.
    """

    # 0. 클릭 카운트를 높인다.
    stats['count'] += 1

    # 1. 유입경로를 정리한다.
    referrer = environ.get('HTTP_REFERER')
        # 주소창에서 접근한 경우
    if referrer is None:
        referrer = 'Address Bar'
        stats['entry']['Address Bar'] = stats['entry'].get('Address Bar', 0) + 1
        # 타사이트에서 접근한 경우
    else:
        host = urlparse(referrer).hostname
        stats['entry'][host] = stats['entry'].get(host, {})
        # TODO: referrer는 긴 문자열이기에 검색이 오래 걸릴 수 있음.
        # 리디렉션이 오래 걸리는 경우 단순배열로 수정할 필요 있음.
        stats['entry'][host][referrer] = stats['entry'][host].get(referrer, 0) + 1

    # 2. 시간을 기록한다.
    stats['time'].append(datetime.now())

    # 3. 국가 정보를 기록한다.
    if headers.getlist("X-Forwarded-For"):
        # 프록시 서버가 있는 경우
        user_ip = headers.getlist("X-Forwarded-For")[0]
    else:
        user_ip = environ.get('REMOTE_ADDR')
        # ip로부터 국가명 추출
    with geoip2.database.Reader('backend/database/GeoLite2-Country.mmdb') as reader:
        try:
            response = reader.country(user_ip)
            country = response.country.name
        except:
            country = 'Not Found'

    stats['country'][country] = stats['country'].get(country, 0) + 1

    # 4. 브라우저 및 OS 정보 기록
    browser = user_agent.browser
    platform = user_agent.platform
    stats['browser'][browser] = stats['browser'].get(browser, 0) + 1
    stats['platform'][platform] = stats['platform'].get(platform, 0) + 1

    # 5. 종합기록
    overall = {
        'time': datetime.now(),
        'entry': referrer,
        'country': country,
        'browser': browser,
        'platform': platform
    }
    stats['index'].append(overall)

    # 불필요한 필드 삭제
    stats.pop('_id', None)
    stats.pop('shortURL', None)


def upsert_stats(short_url, stats):
    """통계 정보를 업데이트한다.

    Args:
        short_url (str): 저장 또는 갱신할 축약 링크
        stats (dict): 반영할 통계 딕셔너리
    """
    collection = db.get_collection("STATS")

    collection.update_one({ 'shortURL': short_url }, {
        '$set': stats
    }, upsert=True)