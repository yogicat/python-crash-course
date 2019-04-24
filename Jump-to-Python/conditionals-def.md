### If

- 들여쓰기 중요.
- `:` 잊지 말기
- `not x`
- `x in <리스트, 튜플, 문자열>`
- 조건문에서 아무일도 하지 않게 하고 싶으면 - pass

```py
if score > 60:
	message = "success"
else:
	message = "failure"
```

**조건부 표현식 사용**
```py
message = "success" if score > 60 else "failure"
```


### while

- `:` colon!
- `continue`  while문을 빠져나가지 않고 처음으로 돌아가기.

```py
a = 0
while a < 10:
	a += 1
	if a % 2 == 0: continue
	print(a)

# 1 3 5 7 9 홀수 출력
```

```py
while True:
	# 무한 루프
```


- - - -


### for

**다양한 for**

```py
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
	print(first+last)

# 3
# 7
# 11
```

**리스트 안에 for문**

```py
a = [1,2,3,4]
result = [num * 2 for num in a]
print(result)
# [2,4,6,8]
```

```py
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 짝수에만 3을 곱한 결과 반환
```



---

### 함수

```py
def add(a, b):
	return a + b

# 매개변수가 몇개가 될지 모를때
def add_many(*args):
	result = 0
	for i in args:
		result += i
	return result
```

`*args` 에서 `*`는 입력값들을 모두 모아서 튜플로 만들어 준다.


**주의해야 할 상황들**

```py
def add_and_mul(a,b):
	return a+b, a*b
```

2개의 값을 반환하지 않는다! `(a+b , a*b)`의 튜플을 반환한다. 튜플에서 괄호는 생략가능하므로.
변수 2개에 담아서 나눠서? 받을 수 있다. (destructuring 하듯이)ㅇ
`result1 result2 = add_and_mul(3,4)`



```py
a = 1
def vartest(a):
	a = a + 1 # 여기에서 left a는 인자로 넘겨진 a

vartest(a)
print(a) 	# 여기서 출력하는 a는 글로벌 a = 1
```

변수의 스코프에 주의할것. 기본적으로 함수 스코프를 가진다.
함수 내에서 글로벌 변수를 바꿔 주고 싶다면, 반환해서 그 값을 재할당하는 방식으로 사용할것.


**람다 lambda**

람다는 함수를 한줄로 간결하게 만들 때 사용한다. (JS에서 arrow function 처럼..)

```py
add = lambda a, b: a+b
result = add(3,4)
print(result)
```
