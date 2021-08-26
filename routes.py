from aiohttp import web

from chat.views import CreateUser, Login, Logout, RoomChat, WebSocket

routes = [
    web.get('/', Login, name='homepage'),
    web.get('/createuser', CreateUser, name='createuser'),
    web.post('/createuser', CreateUser),
    web.post('/login', Login, name='login'),
    web.get('/logout', Logout, name='logout'),
    web.get('/room_chat', RoomChat, name='room_chat'),
    web.get('/ws', WebSocket)
]
