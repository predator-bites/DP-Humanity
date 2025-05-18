from playwright.async_api import async_playwright, expect, BrowserContext, Page
import asyncio
from loguru import logger
import random


from modules.userangent_randomiser import Fake_User_Agent
from modules.utilits import reader, proxy_checker
from modules.metamask_file import Meta, MetaImp
from modules.humanity import Humanity
from config import DELAY
from modules.logo import show_logo


async def loop(private_key, proxy, metaimp: MetaImp, humanity: Humanity):

    async with async_playwright() as p:
        fake_useragent = Fake_User_Agent()
        useragent, browser_version, timezone, args = await fake_useragent.ultra()

        context = await p.chromium.launch_persistent_context(
            headless=False,
            channel="chromium",
            user_data_dir="",
            args=args,
            proxy={
                "server": proxy[0],
                "username": proxy[1],
                "password":proxy[2]
            },
            user_agent=useragent
        )

        await metaimp.import_metamask(context=context)
        await humanity.go_connect_claim(context=context)
        


async def main():
    data = reader()
    i = 1
    for elem in data:
        try:
            private_key = elem["private_key"]
            proxy = elem["proxy"]

            metaimp = MetaImp(private_key=private_key)
            humanity = Humanity(private_key=private_key)

            result = proxy_checker(proxy=proxy)
            if result == False:
                raise Exception(f"Proxy {proxy[0]} is not working")

            logger.info(f"Working with wallet {metaimp.address} and proxy - {proxy[0]}")
            await loop(private_key=private_key, proxy=proxy, metaimp=metaimp, humanity=humanity)
            i+=1

        except Exception as err:
            logger.error(err)
            a=1
            while a<=3:
                try:
                    logger.info(f"Trying again, attempt number {a}")
                    await loop(private_key=private_key, proxy=proxy, metaimp=metaimp, humanity=humanity)
                    break
                except Exception as err_1:
                    logger.error(err_1)
                    if a==3:
                        logger.info("Failed after 3 attempts")
                    a+=1 
            i+=1

        finally:
            print(" ")
            time_sleep = random.randint(DELAY[0], DELAY[1])
            logger.info(f"Sleeping {time_sleep} for next wallet")
            await asyncio.sleep(time_sleep)
    
        


if __name__=="__main__":
    show_logo()
    asyncio.run(main())
    logger.success("Script finished his work")


