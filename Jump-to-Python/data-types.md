# python
#python



# Python Basics

## Python 기본 자료형

### 숫자형

* Int : 정수
* Float : 실수

#### 연산자

* 사칙연산
* `**` 제곱
* `%` 나머지 연산자
* `//`  나눗셈 몫을 반환하는 연산자

- - - -

### 문자열

* `str` 문자들의 집합
* `"some str"`
* `'single quotes'`
* `"""this is also str"""`
* `'''this too'''`
* `\` 백슬래쉬로 quote 포함시킬 수 있다.
* `\n`  줄바꿈

#### 문자열 연산

**문자열 인덱싱**

```py
a = 'hello'
a[0] # h
a[1] # e
```

**문자열 슬라이싱**

```py
a[0,2]	# he
a[:3] 	# 시작 번호 생략시 처음부터
a[2:] 	# 끝 번호 생략시 끝까지
```

*문자열의 요소값은 바꿀 수 있는 값이 아님 - immutable*

**문자열 포매팅**

```py
"I have %d dollars." % 3
"I have %s dollars." % "three"

# %d 숫자
# %s 문자
```

**문자열 포맷 코드**

```py
%s		# 문자열 (자동으로 뒤에 있는 값을 문자열로 바꾼다.)
%c		# character
%d		# int
%f		# float
%o		# 8진수
%x		# 16진수
%%		# 문자 %
```

```py
number = 10
'I have {number} dollar.'.format(number)

'I ate {number2} apples and {number3} bananas.'.format(number2=5, number3=2)
```


**f 포매팅**

*python 3.6 +*

```py
number = 10
name = 'Dahye'
x = 3.21773921

f'I am {name} and I have {number} dollars.'
f'{x:0.2f}'		# 소수점 2자리까지 표현
```


#### 문자열 관련 함수

```py
a = 'hello world'
a.count('l')	# 문자의 갯수를 센다
a.find('w')	# 문자 위치 - 없으면 -1
a.index('t')	# 위치 반환 - 없으면 오류
a.upper()		# HELLO WORLD
a.lower()
a.lstrip()	# 왼쪽 공백 지우기 (l은 left의미)
a.rstrip()	# 오른쪽 공백 지우기
a.strip()		# 양쪽 공백
a.replace('hello', 'hi')
a.split()		# ['hello', 'world']
```


- - - -

### 리스트

```py
a = [1,2,3]
a[0]	# 1

a = [1, 2, 3, ['a', 'b', 'c']]
a[-1]		# ['a', 'b', 'c']
a[0:2]	# [1, 2]

a = [1, 2, 3]
b = [4, 5, 6]
a + b 	# [1,2,3,4,5,6]
a * 2		# [1,2,3,1,2,3]

len(a)	# 3
a[2] = 100	# 값 수정
del a[1]		# 요소 삭제
```


**리스트 관련 함수들**

```py
a = [6, 9, 3]
a.append(4)
a.sort()
a.reverse()
a.index(6)		# 0
a.insert(0, 4)	# 0번째에 4를 삽입
a.remove(9)		# 첫번째로 나오는 9를 삭제
a.pop()			# 맨 마지막 요소를 삭제 (삭제된 요소 반환)
a.pop(1)			# 1번째 요소를 삭제 (삭제된 요소 반환)
a.count(6)		# 6갯수 카운트
a.extend([1,2])	# 리스트 a에 [1,2]를 더한다
```


연습문제
```py
a = ['life', 'is', 'too', 'short']
print(" ".join(a))

b = [1, 3, 5, 4, 2]
b.sort()
b.reverse()
print(b)
```


- - - -

### Tuple 튜플

- 리스트는 `[]`, 튜플은 `()`
- 리스트는 값의 생성, 삭제, 수정이 가능(mutable)하지만 튜플은 값을 바꿀 수 없다. (Immutable)
- `,` 콤마가 필요

```py
t1 = (1, 2, 3, 4)
t2 = ('a', 'b', 5)

t1[0]		# 1
t1[1:]	# (2, 3, 4)
t2 * 2	# ('a', 'b', 5, 'a', 'b', 5)
len(t2)	# 3
```


- - - -

### Dict 딕셔너리

- 딕셔너리는 Key, Value Pair
- Key에는 변하지 않는 값을 사용한다.
- Value에는 모두 사용 가능
- 순서가 없기 때문에 인덱싱 x

```py
d1 = {'name': 'Brad', 'phone': '1234567'}
d1.values()
d1.keys()
d1.get('name', 'who')		# 'Brad' 'who'- 디폴트값
'name' in d1 		# True
'email' in d1 	# False
```


- - - -

### Set 집합 자료형

- 중복을 허용하지 않고, 순서가 없다.
- list, tuple은 순서가 있기 때문에 인덱싱을 통해 값을 얻지만, Set는 순서가 없어 인덱싱 불가능
- 자료형의 중복을 제거하기 위한 필터 역할로 사용되기도 한다.

```py
s1 = set([1,2,3])		# {1, 2, 3}
s2 = set('hello')		# {'e', 'h', 'l', 'o'}
```


**교집합**

```py
s1 = set([1,2,3])
s2 = set([2,3,4])

s1 & s2	# {2,3}
s1.intersection(s2)	# {2,3}
```

**합집합**

```py
s1 | s2	# {1, 2, 3, 4}
s1.union(s2)
```

**차집합**

```py
s1 - s2	$ {1}
s1.difference(s2)
```

**값 추가, 삭제**

```py
s1.add(9)

# 여러개 추가
s1.update([4,5,6])

# 제거하기
s1.remove(1)
```

- - - -

### Bool


#### True

```py
bool("python") 	# True
[1,2,3]
1
1 == 1
```


#### False

```py
bool(2 < 1) 	# False
""
[]
()
{}
0
None
```

- - - -


### 변수

변수는 객체를 *가르키는 것*
변수에 값을 할당하게되면, 값을 가지는 객체가 메모리에 생성되고 변수는 값이 저장된 메모리의 주소를 가르키게 된다.


```py
a = [1,2,3]
id(a)   # 변수 a가 저장된 메모리의 주소를 알 수 있다.
```

**리스트 복사**

```py
a = [1,2,3]
b = a   # a와 b가 가르키는 대상이 동일하다. (주소가 동일)
```

**카피해서 복사**

다양한 방법으로 동일한 곳을 가르키지 않도록 카피 복사 할 수 있다.

```py
b = a[:]
```

```py
# copy 모듈 사용
from copy import copy
b = copy(a)
```


#### 변수 만들기

```py
a, b = ('hello', 'world')
(a, b) = 'hello', 'world'
[a, b] = ['hello', 'world']

# 같은 값 대입
a = b = 'python'

# 두개의 변수 값 바꾸기
a, b = b, a
```
