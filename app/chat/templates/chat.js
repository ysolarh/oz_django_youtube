// <script>
// document.addEventListener('DOMContentLoaded', function() {
//     fetchChatRooms(); // 페이지 로드 시 채팅방 목록 로드
// });
//
// function fetchChatRooms() {
//     fetch('http://0.0.0.0:8000/api/v1/chat/room/')
//         .then(response => response.json())
//         .then(data => {
//             const roomContainer = document.getElementById('room-container');
//             roomContainer.innerHTML = ''; // 초기화
//             data.forEach(room => {
//                 const roomDiv = document.createElement('div');
//                 roomDiv.innerHTML = room.name;
//                 roomDiv.onclick = function () {
//                     enterChatRoom(room.id);
//                 };
//                 roomContainer.appendChild(roomDiv);
//             });
//         })
//         .catch(error => {
//             console.error('Error fetching chat rooms:', error);
//         });
// }
//
//     function enterChatRoom(roomId) {
//     // 채팅방 메시지 로드
//     loadChatRoom(roomId);
//
//     // WebSocket 연결
//     const chatSocket = new WebSocket(
//     'ws://' + window.location.host + '/ws/chat/' + roomId + '/'
//     );
//
//     chatSocket.onmessage = function(e) {
//     const data = JSON.parse(e.data);
//     const chatLog = document.getElementById('chat-log');
//     chatLog.innerHTML += '<div>' + data.message + '</div>';
// };
//
//     chatSocket.onclose = function(e) {
//     console.error('Chat socket closed unexpectedly');
// };
//
//     document.querySelector('#chat-message-submit').onclick = function(e) {
//     const messageInputDom = document.querySelector('#chat-message-input');
//     const message = messageInputDom.value;
//
//     chatSocket.send(JSON.stringify({
//     'message': message
// }));
//
//     messageInputDom.value = '';
// };
// }
//
//     function loadChatRoom(roomId) {
//     fetch(`/api/chatrooms/${roomId}/messages`)
//         .then(response => response.json())
//         .then(messages => {
//             const chatLog = document.getElementById('chat-log');
//             chatLog.innerHTML = ''; // 초기화
//             messages.forEach(message => {
//                 const messageDiv = document.createElement('div');
//                 messageDiv.innerHTML = message.text;
//                 chatLog.appendChild(messageDiv);
//             });
//             document.getElementById('room-name').innerText = roomId;
//         })
//         .catch(error => {
//             console.error('Error loading messages:', error);
//         });
// }
// </script>