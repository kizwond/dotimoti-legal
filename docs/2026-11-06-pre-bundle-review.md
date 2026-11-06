# 401 이후 Play 제출 전 방침·언어 점검

2026-11-06 KST. 이전 Play391부터 앱401까지의 소스와 현재 광고 OFF 방침을 대조했다. 새 수집 항목·외부 전송 목적·SDK 또는 Android 권한 추가가 없으므로 방침 본문을 추가 개정하거나 시행일2026-11-02를 변경하지 않았다.

새 루틴 부모 경로와 직접/측정 출처 표시 정보는 기존2절의 수행 설정·활동 기록 범위이며 기기 내 저장이다. 카드 디자인·필드 선택·완료 제어·날짜 표시는 기존 공유/보관/삭제 범위를 바꾸지 않는다. 건강/영상/원본 ZIP/지도·지형 요청/시스템 백업에 관한 기존 고지는 유지한다.

앱의 컴파일된 `privacyPolicySections(code,false)` 출력을7개 언어×14개 절로 추출해 `policy/*.json`과 전체 구조·문자열을 대조했다. 모두 일치한다. 추가5개 언어는 앱 번역 원본 JSON도 별도로 대조했다. `build_privacy.py --check`는7개 HTML과 기본 주소의#ko/#en 호환성을 확인한다.

언어 선택 메뉴의 접근성 이름을 각 언어로 바꾸고7개 HTML을 재생성했다. 이는 탐색 표시의 변경이며 개인정보 처리 목적이나 시행일 변경이 아니다. `.worktrees/`의 기존 작업은 건드리지 않는다.

근거: https://support.google.com/googleplay/android-developer/answer/10144311?hl=en 및 https://support.google.com/googleplay/android-developer/answer/10787469?hl=en (2026-11-06 열람). Console의 기존 답변은 조회·수정하지 않았다. 실제 AAB의 최종 권한/포함 SDK/서명 대조는 사용자가 번들 제작을 요청한 뒤 수행한다.
