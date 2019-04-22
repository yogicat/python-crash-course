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

