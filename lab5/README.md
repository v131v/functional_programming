## Preset

```
pip install requests
pip install aiogram
pip install dotenv
```

Create telegram bot and recieve it's token.

Create api token on http://weatherapi.com

Create file `.env` with content:
```
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
WEATHER_API_KEY=YOUR_WEATHER_API_KEY
```

## Usage 

```
python main.py
```

Go to your bot.

Commands:
* `/start` - print hello-message with list of commands
* `/exchage` - print exchange rate
* `/weather <city>` - print a weather in <city>
