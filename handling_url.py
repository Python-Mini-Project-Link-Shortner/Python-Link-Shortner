from short_url import encode_url

def create_short_url(unique_id:int):
    # 새로운 URL을 생성한다.
    return encode_url(unique_id, min_length=7)