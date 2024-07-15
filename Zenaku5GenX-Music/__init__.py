from Zenaku5GenX-Music.core.bot import Dil
from Zenaku5GenX-Music.core.dir import dirr
from Zenaku5GenX-Music.core.git import git
from Zenaku5GenX-Music.core.userbot import Userbot
from Zenaku5GenX-Music.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Dil()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
