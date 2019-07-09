import webbrowser

#webbrowser.open('https://google.com')
#webbrowser.open_new_tab('https://google.com')
#webbrowser.open_new('https://google.com')
idols = ['bts', 'red velvet', 'iu', 'winner']

for idol in idols:
    print(type(idol))
    webbrowser.open('https://search.naver.com/search.naver?query={}'.format(idol))
