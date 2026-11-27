# 모티도티 Google 로그인 개인정보 안내 — 2026-11-27

- Android `doti_moti`의 `0e1c7df` 실제 런타임에서 7개 언어·20개 절을 다시 추출했다.
- Google 로그인을 선택할 때 고유 계정 식별자·이메일·표시 이름을 받아 로그인/계정 연결에 사용하며 Google 비밀번호를 받거나 저장하지 않는다는 설명을 추가했다.
- 시행일은 2026-11-27이다. 계정 삭제 주소는 PostgreSQL 새 서버의 기존 주소를 유지한다.
- 회사 전용 Google 프로젝트 `motidoti-login`을 사용한다. Gmail/Drive/Health 접근 권한이나 기존 알림 프로젝트를 변경하는 작업이 아니다.
- Android Google 흐름 4개와 7언어 방침/공개 링크 검사 1개가 에뮬레이터에서 통과했다. 공개 방침은 이 런타임 결과와 일치하며, 실제 Google 인증 결과는 앱의 후속 인계에 별도로 기록한다.
- `build_moti_privacy.py --check`, `check_moti_privacy.py`, 기존 모티두잇 정책 `build_privacy.py --check` 통과. 모티두잇 정책은 변경하지 않았다.
