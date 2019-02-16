import logging
import asyncio
from aiohttp import web

logging.basicConfig(level=logging.INFO)


# 请求处理函数
def index(request):
    return web.Response(body='hello world !')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '0.0.0.0', 9000)  # 创建服务
    logging.info('server start at http://localhost:9000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
