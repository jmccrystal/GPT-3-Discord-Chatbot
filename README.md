# GPT-3 Discord Chatbot

A Discord bot that uses OpenAI's GPT-3 model to engage in casual conversations with users. The bot maintains context by reading previous messages and responds in a casual, friendly manner.

## Features

- Integration with OpenAI's GPT model (text-davinci-002)
- Contextual responses based on conversation history
- Automatic message formatting
- Error handling for API connection issues

## Prerequisites

- Python 3.7+
- Discord Bot Token
- OpenAI API Key

## Required Python Packages

```bash
pip install nextcord
pip install openai
```

## Setup

1. Create a Discord bot and get your token from the [Discord Developer Portal](https://discord.com/developers/applications)

2. Get an OpenAI API key from the [OpenAI Platform](https://platform.openai.com/)

3. Create two files in your project directory:
   - `discord_token.txt`: Contains your Discord bot token
   - `openai_api_key.txt`: Contains your OpenAI API key

## Configuration

The bot has several configurable parameters at the top of the script:

```python
bot_id = 964775186157154344  # Your bot's Discord ID
your_id = 0  # Your Discord user ID
message_amount = 5  # Number of previous messages to include for context
```

## Usage

1. Run the bot:
```bash
python bot.py
```

2. The bot will respond to all messages in channels it has access to, except:
   - Messages from itself
   - Messages from specified ignored users

3. Commands:
   - The bot uses "." as its command prefix
   - Currently no specific commands implemented

## How It Works

1. **Message Processing**
   - Bot reads the last `message_amount` messages for context
   - Formats messages with user identifiers
   - Builds a conversation prompt for GPT

2. **GPT Integration**
   - Uses OpenAI's text-davinci-002 model
   - Temperature set to 1 for creative responses
   - Maximum response length of 20 tokens
   - Automatically retries on connection errors

3. **Response Formatting**
   - Removes empty lines
   - Maintains casual, lowercase style
   - Preserves conversation flow

## Response Format

The bot structures its prompts as follows:
```
The following is a Discord conversation with a friend. Use internet language and all lowercase.
[User1]: message1
[User2]: message2
You: [bot's response]
```

## Error Handling

The bot includes handling for:
- OpenAI API connection issues
- Empty responses
- Message formatting issues

## Customization

You can modify:
1. `message_amount`: Change how many previous messages to include
2. OpenAI parameters:
   - `temperature`: Adjust response creativity (0-1)
   - `max_tokens`: Modify response length
3. Message formatting style
4. Ignored user IDs

## Security Notes

- Keep your Discord token and OpenAI API key secure
- Don't share the token/key files
- Monitor API usage to manage costs
- Consider implementing rate limiting

## Contributing

Feel free to:
- Report issues
- Suggest features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the GPT API
- Discord for the bot platform
- nextcord development team
