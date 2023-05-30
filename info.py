import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'thoppimoviebot')
API_ID = int(environ.get('API_ID', '29441782'))
API_HASH = environ.get('API_HASH', 'fcd2518e068b5a42cd8fa40bdb76302a')
BOT_TOKEN = environ.get('BOT_TOKEN', '6255291464:AAErDxHIu9IZ4oymPlQOfg0Pl2DXaxo-GnY')

# Bot pics and stickers
STICKERS = (environ.get('STICKERS', '')).split()
PICS = (environ.get('PICS', 'https://i.ibb.co/k0XjRbh/images-21.jpg')).split()

# Bot Admins
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '').split()]
auth_users = [int(auth_users) if id_pattern.search(auth_users) else auth_users for auth_users in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Channels
INDEX_CHANNELS = [int(index_channels) if id_pattern.search(index_channels) else index_channels for index_channels in environ.get('-1001674948137', '-1001674948137').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001754886821')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001959250376'))

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://thoppimoviebot:thoppimoviebot@thoppimoviebot.a3lj0ir.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "thoppimoviebot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/rithikclicks')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/malluottrelease')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "False")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "True")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "✅ I Found: <code>{query}</code>\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating} / 10</a>\n☀️ Languages: {languages}\n📀 RunTime: {runtime} Minutes\n\n🗣 Requested by: {message.from_user.mention}\n©️ Powered by: <b>{message.chat.title}</b>")
FILE_CAPTION = environ.get("FILE_CAPTION", "<code>{file_name}</code>")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
WELCOME_TEXT = environ.get("WELCOME_TEXT", "ഹൈ ലൊട്ടെ {mention} 👋🏻 , Welcome to {title} group! , നിങ്ങൾക്ക് വേണ്ട മൂവി ഇവിടെ ടൈപ്പ് ചെയ്ത് അയക്കു... ഞാൻ അത് ഒപ്പിച്ച് തരാം 🤙🏻)
                           
# Log
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("AUTO_FILTER is enabled.\n" if AUTO_FILTER else "AUTO_FILTER is disabled.\n")
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += (f"FILE_CAPTION enabled with value {FILE_CAPTION}, your files will be send along with this customized caption.\n" if FILE_CAPTION else "No FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("LONG_IMDB_DESCRIPTION enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("SPELL_CHECK Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK else "SPELL_CHECK Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in IMDB_TEMPLATE, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB_TEMPLATE is {IMDB_TEMPLATE}"
