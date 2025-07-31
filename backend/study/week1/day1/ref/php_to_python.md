# PHP to Python 변환 가이드

## 자주 사용하는 PHP 함수의 Python 대응

### 문자열 처리

| PHP | Python | 설명 |
|-----|--------|------|
| `strlen($str)` | `len(str)` | 문자열 길이 |
| `strtolower($str)` | `str.lower()` | 소문자 변환 |
| `strtoupper($str)` | `str.upper()` | 대문자 변환 |
| `trim($str)` | `str.strip()` | 양쪽 공백 제거 |
| `explode(",", $str)` | `str.split(",")` | 문자열 분리 |
| `implode(",", $arr)` | `",".join(arr)` | 문자열 결합 |
| `str_replace("a", "b", $str)` | `str.replace("a", "b")` | 문자열 치환 |
| `strpos($str, "find")` | `str.find("find")` | 문자열 위치 찾기 |

### 배열/리스트 처리

| PHP | Python | 설명 |
|-----|--------|------|
| `count($arr)` | `len(arr)` | 배열 크기 |
| `array_push($arr, $val)` | `arr.append(val)` | 끝에 추가 |
| `array_pop($arr)` | `arr.pop()` | 끝에서 제거 |
| `array_shift($arr)` | `arr.pop(0)` | 앞에서 제거 |
| `array_unshift($arr, $val)` | `arr.insert(0, val)` | 앞에 추가 |
| `in_array($val, $arr)` | `val in arr` | 값 존재 확인 |
| `array_merge($arr1, $arr2)` | `arr1 + arr2` | 배열 합치기 |
| `array_slice($arr, 1, 3)` | `arr[1:4]` | 배열 자르기 |
| `sort($arr)` | `arr.sort()` | 정렬 |
| `array_reverse($arr)` | `arr[::-1]` 또는 `arr.reverse()` | 역순 |

### 파일 처리

| PHP | Python | 설명 |
|-----|--------|------|
| `file_get_contents($file)` | `open(file, 'r').read()` | 파일 읽기 |
| `file_put_contents($file, $data)` | `open(file, 'w').write(data)` | 파일 쓰기 |
| `file_exists($file)` | `os.path.exists(file)` | 파일 존재 확인 |
| `is_dir($path)` | `os.path.isdir(path)` | 디렉토리 확인 |
| `mkdir($dir)` | `os.mkdir(dir)` | 디렉토리 생성 |

### 타입 확인/변환

| PHP | Python | 설명 |
|-----|--------|------|
| `is_array($var)` | `isinstance(var, list)` | 배열/리스트 확인 |
| `is_string($var)` | `isinstance(var, str)` | 문자열 확인 |
| `is_int($var)` | `isinstance(var, int)` | 정수 확인 |
| `is_null($var)` | `var is None` | null/None 확인 |
| `empty($var)` | `not var` | 비어있는지 확인 |
| `isset($var)` | `var is not None` | 변수 설정 확인 |
| `(int)$var` | `int(var)` | 정수로 변환 |
| `(string)$var` | `str(var)` | 문자열로 변환 |
| `(float)$var` | `float(var)` | 실수로 변환 |

### 예제: PHP 코드를 Python으로

```php
// PHP
<?php
function processUsers($users) {
    $result = array();
    foreach ($users as $user) {
        if ($user['age'] >= 18) {
            $name = strtoupper($user['name']);
            array_push($result, $name);
        }
    }
    return $result;
}

$users = array(
    array("name" => "kim", "age" => 20),
    array("name" => "lee", "age" => 17),
    array("name" => "park", "age" => 25)
);

$adults = processUsers($users);
echo implode(", ", $adults);
?>
```

```python
# Python
def process_users(users):
    result = []
    for user in users:
        if user['age'] >= 18:
            name = user['name'].upper()
            result.append(name)
    return result

# 또는 Pythonic하게
def process_users(users):
    return [user['name'].upper() for user in users if user['age'] >= 18]

users = [
    {"name": "kim", "age": 20},
    {"name": "lee", "age": 17},
    {"name": "park", "age": 25}
]

adults = process_users(users)
print(", ".join(adults))
```

## 자주 하는 실수

1. **세미콜론**: Python에서는 세미콜론 불필요
2. **$변수**: Python에서는 $ 기호 없음
3. **중괄호**: Python은 들여쓰기로 블록 구분
4. **++ 연산자**: Python에는 없음, += 1 사용
5. **echo/print**: Python은 print() 함수 사용
6. **array()**: Python은 [] 사용
7. **null**: Python은 None (대문자 주의)
8. **true/false**: Python은 True/False (대문자 주의)
