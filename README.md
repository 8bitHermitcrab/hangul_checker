# 한글 맞춤법 검사 프로그램

## py-hanspell 라이브러리 사용.
- 네이버 맞춤법 검사기를 이용한 파이썬용 한글 맞춤법 검사 라이브러리.
- 링크 : https://github.com/ssut/py-hanspell
- 계속 바뀌는 토큰값 추적하게끔 코드 변경
- 참고 링크 : https://github.com/ssut/py-hanspell/pull/42/files

## pyinstaller 이슈
- OS 환경에 따라 빌드 파일이 달라짐
- MacOS : ```.app```
- Windows : ```.exe```

### pyinstaller 빌드 명령어
- MacOS : ```pyinstaller -i icon.icns -w -F hangul_checker.py```
- Windows : ```pyinstaller -i icon.ico -w -F hangul_checker.py```
- ```-i``` : 아이콘 설정
- ```-w``` : 콘솔창이 보이지 않게 애플리케이션을 생성
- ```-F``` : 하나의 파일로 패키징