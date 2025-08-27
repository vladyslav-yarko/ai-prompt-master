# python -m scripts.db.progress_data

import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases import db_session
from src.models import Level, Achievement, Game
from src.enums.level import LevelEnum


async def fill_level(session: AsyncSession) -> None:
    levels = [
        Level(title=LevelEnum.beginner, requiredScore=0, emoji="🐣"),
        Level(title=LevelEnum.novice, requiredScore=500, emoji="📗"),
        Level(title=LevelEnum.learner, requiredScore=1000, emoji="🧩"),
        Level(title=LevelEnum.junior, requiredScore=1500, emoji="🎯"),
        Level(title=LevelEnum.intermediate, requiredScore=2000, emoji="📘"),
        Level(title=LevelEnum.skilled, requiredScore=2500, emoji="🛠️"),
        Level(title=LevelEnum.advanced, requiredScore=3000, emoji="🚀"),
        Level(title=LevelEnum.proficient, requiredScore=3500, emoji="🧠"),
        Level(title=LevelEnum.expert, requiredScore=4000, emoji="🏆"),
        Level(title=LevelEnum.master, requiredScore=4500, emoji="👑"),
    ]
    session.add_all(levels)
    
    
async def fill_achievement(session: AsyncSession) -> None:
    # extracting games for ids
    learn_mode = (await session.execute(select(Game).where(Game.title == "🎯 Learn Mode"))).scalar()
    creative_mode = (await session.execute(select(Game).where(Game.title == "🎨 Creative Mode"))).scalar()
    code_mode = (await session.execute(select(Game).where(Game.title == "💻 Code Mode"))).scalar()
    anti_prompt_mode = (await session.execute(select(Game).where(Game.title == "🛠️ Anti-prompt Mode"))).scalar()
    puzzles_mode = (await session.execute(select(Game).where(Game.title == "🧩 Prompt Puzzle Mode"))).scalar()
    
    achievements = [
        # Learn mode
        Achievement(title="Початківець оцінки", description="Зароби 50 очок у Learn Mode", emoji="🔍", conditionKey="learnMode", conditionValue=50, gameId=learn_mode.id),
        Achievement(title="Дослідник якості", description="Зароби 200 очок у Learn Mode", emoji="🧪", conditionKey="learnMode", conditionValue=200, gameId=learn_mode.id),
        Achievement(title="Аналітик промптів", description="Зароби 500 очок у Learn Mode", emoji="📊", conditionKey="learnMode", conditionValue=500, gameId=learn_mode.id),
        Achievement(title="Профі відбору", description="Зароби 1000 очок у Learn Mode", emoji="🧠", conditionKey="learnMode", conditionValue=1000, gameId=learn_mode.id),
        Achievement(title="Майстер інтуїції", description="Зароби 2000 очок у Learn Mode", emoji="👁️‍🗨️", conditionKey="learnMode", conditionValue=2000, gameId=learn_mode.id),

        # Creative mode
        Achievement(title="Маленький творець", description="Зароби 50 очок у Creative Mode", emoji="🖌️", conditionKey="creativeMode", conditionValue=50, gameId=creative_mode.id),
        Achievement(title="Ідейний шукач", description="Зароби 200 очок у Creative Mode", emoji="🎨", conditionKey="creativeMode", conditionValue=200, gameId=creative_mode.id),
        Achievement(title="Автор промптів", description="Зароби 500 очок у Creative Mode", emoji="✍️", conditionKey="creativeMode", conditionValue=500, gameId=creative_mode.id),
        Achievement(title="Креатор промптів", description="Зароби 1000 очок у Creative Mode", emoji="🌟", conditionKey="creativeMode", conditionValue=1000, gameId=creative_mode.id),
        Achievement(title="Геній натхнення", description="Зароби 2000 очок у Creative Mode", emoji="💡", conditionKey="creativeMode", conditionValue=2000, gameId=creative_mode.id),

        # Code mode
        Achievement(title="Новачок розробник", description="Зароби 50 очок у Code Mode", emoji="💻", conditionKey="codeMode", conditionValue=50, gameId=code_mode.id),
        Achievement(title="Початківець GPT Dev", description="Зароби 200 очок у Code Mode", emoji="🧑‍💻", conditionKey="codeMode", conditionValue=200, gameId=code_mode.id),
        Achievement(title="Інженер слів", description="Зароби 500 очок у Code Mode", emoji="🛠️", conditionKey="codeMode", conditionValue=500, gameId=code_mode.id),
        Achievement(title="AI девелопер", description="Зароби 1000 очок у Code Mode", emoji="🤖", conditionKey="codeMode", conditionValue=1000, gameId=code_mode.id),
        Achievement(title="Машинний промптер", description="Зароби 2000 очок у Code Mode", emoji="📟", conditionKey="codeMode", conditionValue=2000, gameId=code_mode.id),

        # Anti-prompt mode
        Achievement(title="Початківець редактор", description="Зароби 50 очок у Anti-prompt Mode", emoji="📝", conditionKey="antiPromptMode", conditionValue=50, gameId=anti_prompt_mode.id),
        Achievement(title="Покращувач GPT", description="Зароби 200 очок у Anti-prompt Mode", emoji="🔧", conditionKey="antiPromptMode", conditionValue=200, gameId=anti_prompt_mode.id),
        Achievement(title="Редактор рівняння", description="Зароби 500 очок у Anti-prompt Mode", emoji="✂️", conditionKey="antiPromptMode", conditionValue=500, gameId=anti_prompt_mode.id),
        Achievement(title="Архітектор слів", description="Зароби 1000 очок у Anti-prompt Mode", emoji="🏗️", conditionKey="antiPromptMode", conditionValue=1000, gameId=anti_prompt_mode.id),
        Achievement(title="Реформатор ІІ", description="Зароби 2000 очок у Anti-prompt Mode", emoji="🧠✏️", conditionKey="antiPromptMode", conditionValue=2000, gameId=anti_prompt_mode.id),

        # Prompt puzzles
        Achievement(title="Збирач слів", description="Зароби 50 очок у Prompt Puzzles", emoji="🧩", conditionKey="puzzleMode", conditionValue=50, gameId=puzzles_mode.id),
        Achievement(title="Розумник GPT", description="Зароби 200 очок у Prompt Puzzles", emoji="🪄", conditionKey="puzzleMode", conditionValue=200, gameId=puzzles_mode.id),
        Achievement(title="Комбінатор промптів", description="Зароби 500 очок у Prompt Puzzles", emoji="🔀", conditionKey="puzzleMode", conditionValue=500, gameId=puzzles_mode.id),
        Achievement(title="Алхімік підказок", description="Зароби 1000 очок у Prompt Puzzles", emoji="⚗️", conditionKey="puzzleMode", conditionValue=1000, gameId=puzzles_mode.id),
        Achievement(title="Майстер синтезу", description="Зароби 2000 очок у Prompt Puzzles", emoji="🧬", conditionKey="puzzleMode", conditionValue=2000, gameId=puzzles_mode.id),
    ]
    session.add_all(achievements)


async def main() -> None:
    async for session in db_session():
        tasks = asyncio.gather(
            fill_level(session),
            fill_achievement(session)
        )
        await tasks
        await session.commit()
    
    
asyncio.run(main())
