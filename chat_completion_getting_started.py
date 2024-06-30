from openai import OpenAI
import os

# Ref: https://platform.openai.com/docs/quickstart

# To set the OPEN_AI_KEY_GET_STARTED_TUTORIAL environment variable, go to ~/.zshrc or ~/.bashrc
# and add export OPEN_AI_KEY_GET_STARTED_TUTORIAL='<key>'
# run source ~/.zshrc in command line to load the configuration
# verify that the environment variable is now set by doing echo $OPEN_AI_KEY_GET_STARTED_TUTORIAL
key = os.getenv("OPEN_AI_KEY_GET_STARTED_TUTORIAL")
client = OpenAI(api_key=key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",

  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)