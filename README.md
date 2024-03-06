# 유튜브 백엔드 구현

## 1. REST API
### (1) 모델 구조

1. User (Custom)
    - email
    - password
    - nickname
    - is_business(boolean): personal, business


2. Video
    - title
    - link
    - description
    - category
    - views_count
    - thumbnail
    - video_uploaded_url(S3)
    - video_file(FileField)
    - User: FK


3. Likes/Dislike (Reaction)
    - User: FK
    - Video: FK
    Video : Like/Dislike (1 : N)


4. Comment
    - USER: FK
    - Video: FK
    - like
    - dislike
    - content


5. Subscription (채널 구독)
    - User: FK => subscriber -> 내가 구독한 사람
    - User: FK => subscribed_to -> 나를 구독한 사람


6. Notification
   - User: FK
   - message
   - is_read


7. Common
    - created_at
    - updated_at


8. Chatting
   - User: FK (nickname)


## 수업 진행

- 1일차: Project Settings (Docker => Django, Github => Github Actions(CI))
- 2일차: 
  - Project Settings (PostgreSQL)
  - CustomUser Model
    - 왜 커스텀 유저 모델을 사용하는가?
      - 장고의 유저 모델을 상속받아서 기존에 구현된 기능을 내가 직접 구현하지 않아도 되기 때문
      - 장고의 공식 문서에서 강력히 추천함
- 3일차: Custom User Model
  - (1) User Model 생성
    - docker-compose run --rm app sh -c 'django-admin startapp users'
  - (2) Teest Code를 작성
  - (3) AbstractUserModel을 상속
  - (4) Admin 세팅
- 4일차: REST API -> Video 관련 API  
  (1)
  - Common
  - Videos
  - Comments
  - Reactions (like/dislike)
  - Subscriptions
  - Notifications  
  (2)
  - 
  (3) settings.py의 INSTALLED_APPS에 등록  
  (4) DB migration
  
  (5) Video API create
  - VideoList
  - api/v1/videios
    - GET: 전체 비디오 목록 조회 => Video.objects.all() => 클라이언트에 전달
    - POST: 새로운 비디오 생성
    - DELETE, PUT: X
  - VideoDetail
  - api/v1/videos/{video_id}
    - GET: 특정 비디오 상세 조회
    - POST: X
    - PUT: 특정 비디오 정보 업데이트(수정)
    - DELETE: 특정 비디오 삭제
  (6) Subscription API
    - 특정 유저를 구독한 유저 리스트
    - 유저가 구독한 구독 리스트
    - post: 구독하기
    - get: 구독리스트
    - delete: 구독삭제
    - 내가 나를 구독 -> X
    - 이미 구독했는데 다시 구독 -> X
    - 구독 여부 확인
    - api/v1/subscriptions
        - [POST]: 구독하기 버튼 클릭
    - api/v1/subscriptions/{user_id}
        - [DELETE]: 구독취소
  (7) Reaction API
  - 영상에 좋아요, 싫어요 추가하는 기능
  - api/v1/video/{video_id}/reaction
  - like/dislike count 두가지 방법
    - Reaction Model
    - Video Model

  (8) Chatting - SocketIO
  - api/v1/chat/msg
    - [POST] - 채팅 메시지 생성
  - api/v1/chat/room
    - [POST]: 채팅방 생성
    - [GET]: 채팅방 조회
  - api/v1/chat/room/{room_id}
    - [GET]: 채팅방 조회
  - wss: 127.0.0.1:8000/ws/chat/{room_id}
    Django SocketIO - Channels Library (pip install channels)
  (9) Deployment
  - IAM 유저 생성
  - EC2 instance 생성 (Amazon Linux)
  - EC2 SSH 접속 -> Finger Print
  - AWS -> 배포
