from konlpy.tag import Okt

okt=Okt()
text='마음에 꽂힌 칼 한자루보다 마음에 꽂힌 꽃 한송이가 더 아파서 잠이 오지 않는다'

okt_tage=okt.pos(text,norm=True,stem=True)
print(okt_tage)

okt_noun=okt.nouns(text)
print(okt_noun)