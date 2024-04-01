# Poetry
## Poetry에 패키지 설치
- poetry add -D isort mypy django-stubs
- -D의 의미는 dev(개발)환경에만 설치한다는 의미, 배포시에 배포이미지의 사이즈를 줄일수 있음.

# 리눅스 명령어
## 여러 명령을 실행하는 경우
- poetry run isort . && poetry run black . & poetry run mypy .
- && 직렬 실행 앞의 명령이 성공했다면 뒤의 명령을 실행(직렬실행중에 실패가 발생하면 이후 명령은 실행되지 않는다.)
- &  병렬 실행 앞의 명령의 성공여부와 상관없이 명령을 실행
