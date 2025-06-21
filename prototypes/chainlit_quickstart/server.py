from textwrap import dedent

import chainlit as cl
from openai import AsyncOpenAI

import tools

client = AsyncOpenAI()
# cl.instrument_openai()


##############
## Starters ##
##############


@cl.set_starters
async def set_starters(user):
    return [
        cl.Starter(
            label="What's on my todo list?",
            message=dedent(
                """
                Read my todo list and summarize the tasks I need to complete.
                """
            ),
        ),
    ]


#############
## Actions ##
#############


@cl.action_callback("action_button")
async def on_action(action: cl.Action):
    print(action.payload)


##############
## Handlers ##
##############


@cl.on_chat_start
async def start():
    await cl.context.emitter.set_commands(
        [
            {
                "id": "Memo",
                "icon": "mic",
                "description": "Record a voice note that is transcribed and saved.",
                "button": False,
                "persistent": False,
            },
            {
                "id": "Q&A",
                "icon": "book-open-text",
                "description": "Query the knowledge base.",
                "button": False,
                "persistent": False,
            },
            {
                "id": "Debug",
                "icon": "bug",
                "description": "Debug the current conversation.",
                "button": False,
                "persistent": False,
            },
        ]
    )


@cl.on_message
async def on_message(message: cl.Message):
    await tools.sleep()  # Simulate a tool call

    match message.command:
        case "Memo":
            await cl.Message(content="TODO: Save memo.").send()
        case "Q&A":
            await cl.Message(content="TODO: Query the knowledge base.").send()
        case "Debug":
            history = cl.chat_context.to_openai()
            await cl.Message(
                content=dedent(
                    f"Number of Messages: {len(history)}\n"
                    f"Received message: {message.content}\n"
                    f"Command: {message.command}"
                ),
                actions=[
                    cl.Action(
                        name="action_button",
                        icon="mouse-pointer-click",
                        payload={"value": "example_value"},
                        label="Click me!",
                    )
                ],
            ).send()
        case _:
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=cl.chat_context.to_openai(),
            )

            msg = response.choices[0].message.content
            if not msg:
                raise ValueError("The response message is empty.")

            await cl.Message(content=msg).send()


@cl.on_audio_start
async def on_audio_start():
    await cl.sleep(1)  # Simulate spooling up
    return True


@cl.on_audio_chunk
async def on_audio_chunk(chunk: cl.InputAudioChunk):
    pass


@cl.on_audio_end
async def on_audio_end():
    await cl.sleep(1)  # Simulate spooling down
