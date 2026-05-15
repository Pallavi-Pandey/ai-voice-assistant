from __future__ import annotations

from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    Agent,
    AgentSession,
    cli,
)
from livekit.plugins import openai
from dotenv import load_dotenv

from api import TOOLS
from prompts import INSTRUCTIONS, WELCOME_MESSAGE

import os

load_dotenv()


async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)

    agent = Agent(
        instructions=INSTRUCTIONS,
        llm=openai.realtime.RealtimeModel(
            voice="shimmer",
            temperature=0.7,
            modalities=["audio", "text"],
        ),
        tools=TOOLS,
    )

    session = AgentSession()
    await session.start(agent, room=ctx.room)
    await session.generate_reply(instructions=WELCOME_MESSAGE)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
