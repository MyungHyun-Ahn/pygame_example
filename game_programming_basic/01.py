"""
1장
라이브러리
* PyGame
* PIL
* Tkinter
NumPy
SciPy
Beautiful Soup

2장
데이터형과 데이터 구조
데이터형
int
float
string
boolean
type()

형변환
int(a)
float(a)
str(a)
bool(a)

데이터 구조
리스트
0개 이상의 요소를 갖는 나열, 추가 삭제 가능

튜플
0개 이상의 요소를 갖는 나열, 선언 후 변경 불가

딕셔너리
원하는 키에 맞는 값(value)를 저장

len()  : 리스트와 튜플에 있는 요소 수 반환
in     : 리스트나 튜플에 원소가 있는지 확인
copy() : 리스트를 복사해 반환하는 메서드, b = a는 복사가 아니라 같은 리스트를 담는 변수를 하나 더 만드는 것으로 하나를 수정할 경우 다른 것도 바뀜
sorted() : 튜플이나 리스트를 정렬한 복사본을 반환 하는 함수
sort()   : 리스트 자체를 정렬하는 메서드

.format() 메서드 : 본 교재에서 게임 제작시 자주 활용함
- 스트링에 변수의 값을 입력
- 순번을 넣을 수도 있고 이름을 넣을 수도 있음

- 순번을 넣는 예제
"1 = {1}, 2 = {0}".format("hi", "안녕")
출력 : '1 = 안녕, 2 = hi"

"1 = {1}, 2 = {1}, 3 = {0}".format("hi", "안녕")
출력 : '1 = 안녕, 2 = 안녕, 3 = hi"

- 이름을 넣는 예제
"온도 : {temp}, 습도 : {hum}".format(temp=29, hum=66.66)
출력 : '온도 : 29, 습도 : 66.66'
"""


"""
# 시험 나옴
* 람다함수
* sorted, lambda 연결
* 리스트 내포 표기
* 내포 표기 안에 내포 표기 중첩 가능
"""

"""
4장 PyGame
파이썬 게임을 만들기 위한 라이브러리
다양한 OS 지원 (윈도우, 맥, 리눅스)

* 윈도 표시

* 메인 루프 : 큐 방식으로 진행
* 타이머 : 일반적으로 메인루프를 전속력으로 진행하기 때문에 속도를 제한

* Rect 클래스
* Rect 객체 메서드
1. copy() : 복사
2. move(x, y) : 이동한 Rect를 반환 자신은 이동 X
3. move_ip(x, y) : 자신을 이동
4. inflate(x, y) : 현재 값에서 (x, y)만큼 크기를 변경한 Rect를 반환
5. inflate_ip(x, y) : 자신의 사이즈를 변경
6. union(Rect) : 자신과 인수 Rect를 포함하는 최소 Rect 반환
7. contains(Rect) : 포함 여부 체크
8. collidepoint(x, y) : 포함 여부 체크

* Rect 객체와 draw.rect는 다름

* draw 클래스
* draw.rect    : 직사각형
* draw.circle  : 원
* draw.ellipse : 타원
"""


