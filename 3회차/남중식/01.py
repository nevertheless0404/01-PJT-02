import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_TOKEN = os.getenv('my_api_key')

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': API_KEY_TOKEN,
        'language': 'ko-KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()
    result = response.get('results')
    return len(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
