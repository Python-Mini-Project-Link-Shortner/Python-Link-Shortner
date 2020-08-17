from short_url import encode_url
from urllib.parse import urlparse

# 새로운 URL을 생성한다.
def create_short_url(unique_id:int):
    return encode_url(unique_id, min_length=7)
    
# 올바른 URL 형식인지 확인한다.
def validate_url(raw_url):
    try:
        urlparse(raw_url)
        return True
    except:
        return False

# 프로토콜이 생략된 url을 수정한다.
def normalize_url(raw_url):
    # URL에 프로토콜이 생략된 경우 추가한다.
    # 그대로 파싱할 경우 도메인을 path로 인식한다.
    valid_protocols = ('http://', 'https://', '//')
    if not raw_url.startswith(valid_protocols):
        raw_url = '//' + raw_url

    # URL을 파싱한다. 프로토콜이 명시되지 않은 경우 http로 파싱.
    parse = urlparse(raw_url, scheme='http')

    # 전체 url 주소를 반환한다.
    return parse.geturl()

if __name__ == "__main__":
    print(normalize_url('naver.com'))