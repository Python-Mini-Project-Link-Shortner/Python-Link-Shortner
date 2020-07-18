from short_url import encode_url
from urllib.parse import urlparse

def create_short_url(unique_id:int):
    # 새로운 URL을 생성한다.
    return encode_url(unique_id, min_length=7)

def validate_url(raw_url):
    # 올바른 URL 형식인지 확인한다.
    try:
        urlparse(raw_url)
        return True
    except:
        return False