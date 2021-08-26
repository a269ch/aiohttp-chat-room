import asyncio
import base64

import aiohttp_jinja2 as jtemplate
import jinja2
from aiohttp import web
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

import settings
from chat.model import InitDB
from routes import routes

fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
app = web.Application(
    middlewares=[
        session_middleware(EncryptedCookieStorage(secret_key)),
    ]
)
app['websockets'] = []
app.add_routes(routes)
app.router.add_static('/static', settings.STATIC_PATH, name='static')
app.router.add_static('/media', settings.MEDIA_PATH, name='media')
jtemplate.setup(app, loader=jinja2.FileSystemLoader(settings.TEMPLATE_PATH))

if __name__ == '__main__':
    initdb = InitDB()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(initdb.createdb())
    web.run_app(app)
    loop.close()
