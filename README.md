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


3. Likes/Dislike
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