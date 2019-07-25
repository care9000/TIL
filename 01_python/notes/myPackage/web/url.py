def my_url(itemPerPage=10, **api):
  
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemPerPage={itemPerPage}&'
    print(base_url)
    if 0>=itemPerPage and 10 < itemPerPage:
        return '1~10까지의 값을 넣어주세요.'
    
    if api.get('key') =='' or api.get('targetDt') =='':
        return '필수 요청변수가 누락되었습니다.'
    for key, value in api.items():
        base_url += f'{key}={value}&'
        print(base_url)
    return base_url
