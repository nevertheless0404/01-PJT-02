import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    MV_URL = 'https://api.themoviedb.org/3'   
    path1 = '/search/movie'                   
    search_URL = MV_URL + path1
    params = {
            'api_key': ''  ,     
            'language': 'ko-KR' ,
            'query' : title                        
        }
    rsp = requests.get(search_URL, params=params).json().get('results')

    if len(rsp) == 0:
        return None  #검색 결과가 없다면 none반환

    #검색한 영화는 id로 추천 목록
    MV_URL = 'https://api.themoviedb.org/3'   
    path2 ='/movie/'+str(rsp[0].get('id'))+'/recommendations'                  
    rcmd_URL = MV_URL + path2
    params = {
        'api_key': ''  ,     
        'language': 'ko-KR'                        
     }

    rcmd = []
    rsp2 = requests.get(rcmd_URL, params=params).json().get('results')

    for i in rsp2:
        rcmd.append(i.get('title'))
    return rcmd


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
