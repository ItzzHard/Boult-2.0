
from core import Boult, Cog

from .events import MusicEvents
from .music import Music


async def setup(bot: Boult):
    await bot.add_cog(Music(bot))
    await bot.add_cog(MusicEvents(bot))
