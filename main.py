import openai

from nextcord.ext import commands
from openai.error import APIConnectionError


with open('openai_api_key.txt') as f:
    openai.api_key = f.read()
with open('discord_token.txt') as f:
    token = f.read()

bot_id = 964775186157154344
your_id = 0

message_amount = 5

bot = commands.Bot(command_prefix=".")


def create_message(to_send):
    while True:
        try:
            response = openai.Completion.create(engine="text-davinci-002", prompt=to_send, temperature=1, max_tokens=20).get("choices")[0].get("text")
        except APIConnectionError:
            continue
        break
    split_string = response.split("\n", 1)
    print(split_string[0])
    if split_string[0] == "":
        return split_string[1]
    return split_string[0]


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author.id == bot_id:
        return

    to_send = ""

    async for message in message.channel.history(limit=message_amount):
        if message.author.id == bot_id or your_id:
            to_send = to_send + "You: " + message.content + '\n'
        else:
            to_send = to_send + f"{message.author}: " + message.content + '\n'

    sending_message = to_send.split("\n")
    sending_message.reverse()
    sending_message.pop(0)
    to_send = ""
    for item in sending_message:
        to_send = to_send + item + "\n"

    sending_message = ""
    sending_message = f"The following is a Discord conversation with a friend. Use internet language and all lowercase.\n" + to_send + "You:"

    print(message.content)


    await message.channel.send(create_message(sending_message))

bot.run(token)
