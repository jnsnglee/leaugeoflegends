import requests
from bs4 import BeautifulSoup
#import pandas as pd

champ_list=[['가렌', 'garen'], ['갈리오', 'galio'], ['갱플랭크', 'gangplank'], ['그라가스', 'gragas'], ['그레이브즈', 'graves'], ['나르', 'gnar'], ['나미', 'nami'], ['나서스', 'nasus'], ['노틸러스', 'nautilus'], ['녹턴', 'nocturne'], ['누누와윌럼프', 'nunu'], ['니달리', 'nidalee'], ['니코', 'neeko'], ['다리우스', 'darius'], ['다이애나', 'diana'], ['드레이븐', 'draven'], ['라이즈', 'ryze'], ['라칸', 'rakan'], ['람머스', 'rammus'], ['럭스', 'lux'], ['럼블', 'rumble'], ['레넥톤', 'renekton'], ['레오나', 'leona'], ['렉사이', 'reksai'], ['렝가', 'rengar'], ['루시안', 'lucian'], ['룰루', 'lulu'], ['르블랑', 'leblanc'], ['리신', 'leesin'], ['리븐', 'riven'], ['리산드라', 'lissandra'], ['마스터이', 'masteryi'], ['마오카이', 'maokai'], ['말자하', 'malzahar'], ['말파이트', 'malphite'], ['모데카이저', 'mordekaiser'], ['모르가나', 'morgana'], ['문도박사', 'drmundo'], ['미스포츈', 'missfortune'], ['바드', 'bard'], ['바루스', 'varus'], ['바이', 'vi'], ['베이가', 'veigar'], ['베인', 'vayne'], ['벨코즈', 'velkoz'], ['볼리베어', 'volibear'], ['브라움', 'braum'], ['브랜드', 'brand'], ['블라디미르', 'vladimir'], ['블리츠크랭크', 'blitzcrank'], ['빅토르', 'viktor'], ['뽀삐', 'poppy'], ['사이온', 'sion'], ['샤코', 'shaco'], ['세주아니', 'sejuani'], ['소나', 'sona'], ['소라카', 'soraka'], ['쉔', 'shen'], ['쉬바나', 'shyvana'], ['스웨인', 'swain'], ['스카너', 'skarner'], ['시비르', 'sivir'], ['신짜오', 'xinzhao'], ['신드라', 'syndra'], ['신지드', 'singed'], ['쓰레쉬', 'thresh'], ['아리', 'ahri'], ['아무무', 'amumu'], ['아우렐리온솔', 'aurelionsol'], ['아이번', 'ivern'], ['아지르', 'azir'], ['아칼리', 'akali'], ['아트록스', 'aatrox'], ['알리스타', 'alistar'], ['애니', 'annie'], ['애니비아', 'anivia'], ['애쉬', 'ashe'], ['야스오', 'yasuo'], ['에코', 'ekko'], ['엘리스', 'elise'], ['오공', 'monkeyking'], ['오른', 'ornn'], ['오리아나', 'orianna'], ['올라프', 'olaf'], ['요릭', 'yorick'], ['우디르', 'udyr'], ['우르곳', 'urgot'], ['워윅', 'warwick'], ['이렐리아', 'irelia'], ['이블린', 'evelynn'], ['이즈리얼', 'ezreal'], ['일라오이', 'illaoi'], ['자르반4세', 'jarvaniv'], ['자야', 'xayah'], ['자이라', 'zyra'], ['자크', 'zac'], ['잔나', 'janna'], ['잭스', 'jax'], ['제드', 'zed'], ['제라스', 'xerath'], ['제이스', 'jayce'], ['조이', 'zoe'], ['직스', 'ziggs'], ['진', 'jhin'], ['질리언', 'zilean'], ['징크스', 'jinx'], ['초가스', 'chogath'], ['카르마', 'karma'], ['카밀', 'camille'], ['카사딘', 'kassadin'], ['카서스', 'karthus'], ['카시오페아', 'cassiopeia'], ['카이사', 'kaisa'], ['카직스', 'khazix'], ['카타리나', 'katarina'], ['칼리스타', 'kalista'], ['케넨', 'kennen'], ['케이틀린', 'caitlyn'], ['케인', 'kayn'], ['케일', 'kayle'], ['코그모', 'kogmaw'], ['코르키', 'corki'], ['퀸', 'quinn'], ['클레드', 'kled'], ['킨드레드', 'kindred'], ['타릭', 'taric'], ['탈론', 'talon'], ['탈리야', 'taliyah'], ['탐켄치', 'tahmkench'], ['트런들', 'trundle'], ['트리스타나', 'tristana'], ['트린다미어', 'tryndamere'], ['트위스티드페이트', 'twistedfate'], ['트위치', 'twitch'], ['티모', 'teemo'], ['파이크', 'pyke'], ['판테온', 'pantheon'], ['피들스틱', 'fiddlesticks'], ['피오라', 'fiora'], ['피즈', 'fizz'], ['하이머딩거', 'heimerdinger'], ['헤카림', 'hecarim']]

def callitem(champ):
    check=0
    for i in champ_list:
        if i[0]==champ:
            champ_name=i[1]
            check=1
    if check==0:
        EY.sendMessage("챔피언명을 잘못 입력하셨습니다.")

    URL = "http://www.op.gg/champion/"+champ_name+"/statistics/top/item"
    cookies={'customLocale':'ko_KR'}
    opgg = requests.get(URL, cookies=cookies)
    html = opgg.text
    soup = BeautifulSoup(html, 'html.parser')
    item_box = soup.find("div", class_="l-champion-statistics-content__side")
    item_list = item_box.findAll("span",)
    
    return item_list
