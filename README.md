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
