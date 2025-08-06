import re

def is_valid_email(email):
    # 아래는 이메일 주소가 맞는지 확인하는 규칙(정규식)입니다.
    # r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # ^ : 맨 앞에서부터 시작해요
    # [a-zA-Z0-9._%+-]+ : 영어 대소문자, 숫자, 점(.), 밑줄(_), %, +, - 기호가 한 번 이상 나와요 (이게 이메일의 앞부분이에요)
    # @ : 꼭 @ 기호가 들어가야 해요 (이게 이메일의 가운데에 있어요)
    # [a-zA-Z0-9.-]+ : 영어 대소문자, 숫자, 점(.), - 기호가 한 번 이상 나와요 (이게 이메일의 뒷부분이에요)
    # \. : 점(.)이 꼭 한 번 나와야 해요 (이게 이메일의 마지막 부분 앞에 있어요)
    # [a-zA-Z]{2,} : 영어 대소문자가 2개 이상 나와요 (이게 .com, .net 같은 부분이에요)
    # $ : 맨 끝에서 끝나요
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 테스트할 이메일 주소 10개
emails = [
    "test@example.com",
    "user.name@domain.co.kr",
    "invalid-email",
    "user@.com",
    "user@domain",
    "user@domain.c",
    "user@domain.com",
    "user123@sub.domain.com",
    "user+test@domain.org",
    "user_name@domain.io"
]

for email in emails:
    if is_valid_email(email):
        print(f"{email} : 유효함")
    else:
        print(f"{email} : 유효하지 않음")