"""
나도코딩 파이썬 문제 1 파일입출력
"""


names = ["보겸", "유소나", "고기남자", "짤툰", "Onnivia"];

for name in names:
    with open(name + ".txt", "w", encoding= "UTF8") as emailFile:
        emailFile.write(\
"""안녕하세요? {0}님.
(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{0} 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림."""\
        .format(name));

