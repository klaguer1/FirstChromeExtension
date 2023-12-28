from TikTokApi import TikTokApi
import asyncio
import os
import pprint

ms_token = ""

async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        user = api.user("keith_lee125")
        async for video in user.videos(count=60, cursor=0):
            pprint.pprint(video.as_dict['desc'])

if __name__ == "__main__":
    asyncio.run(trending_videos())