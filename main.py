import random
a=random.randrange(1,5)
b=random.randrange(6,10)
c=random.randrange(11,15)
d=random.randrange(16,20)
e=random.randrange(21,25)
f=random.randrange(26,30)
g=random.randrange(31,35)

list_1= [a,b,c,d,e,f,g]
#if a==1:
#    a="점보베이컨김치삼각김밥"
#print(list_1)
if list_1[0]==1:
    a="RTXA스팸참치마요삼각김밥"
if list_1[0]==2:
    a="RTXA떡갈비마요삼각김밥"
if list_1[0]==3:
    a="RTXA소고기고추장&숯불갈비맛삼각김밥"
if list_1[0]==4:
    a="햄마요김볶삼각김밥"
if list_1[0]==5:
    a="점보햄치즈김볶삼각김밥"

if list_1[1]==6:
    b="듬뿍바싹불고기김밥"
if list_1[1]==7:
    b="듬뿍참치김밥"
if list_1[1]==8:
    b="듬뿍햄김밥"
if list_1[1]==9:
    b="매콤제육김밥"
if list_1[1]==10:
    b="의성마늘프랑크김밥"

if list_1[2]==11:
    c="RTXA불고기크래미불닭토핑유부초밥"
if list_1[2]==12:
    c="RTXA햄마요고추참치감자토핑유부초밥"
if list_1[2]==13:
    c="RTXA제육에그참치토핑유부초밥"
if list_1[2]==14:
    c="RTXA유부초밥"
if list_1[2]==15:
    c="명란마요제육와사비참치토핑유부초밥"

if list_1[3]==16:
    d="크린베리치킨햄샌드위치"
if list_1[3]==17:
    d="베이컨에그샌드위치"
if list_1[3]==18:
    d="케이준치킨에그샌드위치"
if list_1[3]==19:
    d="스파이시치킨샌드위치"
if list_1[3]==20:
    d="HALF,오리엔탈치킨샌드위치"

if list_1[4]==21:
    e="햄치즈포테이토샌드위치"
if list_1[4]==22:
    e="NEW베스트콤보샌드위치"
if list_1[4]==23:
    e="케이준치킨햄샌드위치"
if list_1[4]==24:
    e="BELT샌드위치"
if list_1[4]==25:
    e="닭가슴살흑임자샌드위치"

if list_1[5]==26:
    f="초코소보로패스트리빵"
if list_1[5]==27:
    f="딸기맛도너츠빵"
if list_1[5]==28:
    f="햄버거빵"
if list_1[5]==29:
    f="크림치즈데니쉬빵"
if list_1[5]==30:
    f="모카케이크빵"

if list_1[6]==31:
    g="RTXA컵과일,2MIX(파인애플/수입청포도)"
if list_1[6]==32:
    g="RTXA컵과일,배"
if list_1[6]==33:
    g="RTXA컵과일,그린키위"
if list_1[6]==34:
    g="컵과일,2MIX,사과,청포도"
if list_1[6]==35:
    g="RTXA컵과일,3MIX,오렌지,청포도,적포도"


print(a,b,c,d,e,f,g)