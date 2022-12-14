# Структура бота из статьи https://habr.com/ru/company/kts/blog/598575/

from typing import TYPE_CHECKING, Optional

from app.base.base_accessor import BaseAccessor
from app.store.bot_tg.game import CGK
from app.store.bot_tg.poller import Poller
from app.store.bot_tg.worker import Worker

if TYPE_CHECKING:
    from app.web.app import Application


class BotAccessor(BaseAccessor):
    def __init__(self, token: str, n: int, app: Optional['Application'], *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        self.poller = Poller(token=token,
                             app=self.app,)
        self.worker = Worker(token, n, app=self.app)
        self.cgk = CGK(token, app=self.app)
        self.app = app
        self.is_game = True

    async def connect(self, app: "Application"):
        await self.poller.start()
        await self.worker.start()
        if self.is_game:
            await self.cgk.start()

    async def disconnect(self, app: "Application"):
        await self.poller.stop()
        await self.worker.stop()
        if self.is_game:
            await self.cgk.stop()
