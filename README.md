# CatCordModerator

CatCordModerator is a Python-based Discord bot that uses GPT-J to generate responses in the style of an anime cat. The bot also includes moderation commands and functionality in the style of an anime cat.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/catsanzsh/CatCordModerator-.git
   cd CatCordModerator-
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - `DISCORD_TOKEN`: Your Discord bot token.
   - `OPENAI_API_KEY`: Your OpenAI API key.

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

### Commands

- `!meow`: The bot will respond with a cute and playful message in the style of an anime cat.
- `!ban <user> [reason]`: Bans a user from the server. The bot will explain the ban in the style of an anime cat.
- `!kick <user> [reason]`: Kicks a user from the server. The bot will explain the kick in the style of an anime cat.
- `!mute <user> [reason]`: Mutes a user in the server. The bot will explain the mute in the style of an anime cat.
- `!unmute <user> [reason]`: Unmutes a user in the server. The bot will explain the unmute in the style of an anime cat.

### Examples

- `!meow`
  - Bot: "Nyaa~! How can I help you today, nya?"

- `!ban @user Spamming`
  - Bot: "Nyaa~! @user has been banned for spamming, nya!"

- `!kick @user Being rude`
  - Bot: "Nyaa~! @user has been kicked for being rude, nya!"

- `!mute @user Using inappropriate language`
  - Bot: "Nyaa~! @user has been muted for using inappropriate language, nya!"

- `!unmute @user Apologized`
  - Bot: "Nyaa~! @user has been unmuted after apologizing, nya!"
