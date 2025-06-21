import chainlit as cl


@cl.step(type="tool")
async def sleep():
    await cl.sleep(1)

    return "Response from the tool!"
