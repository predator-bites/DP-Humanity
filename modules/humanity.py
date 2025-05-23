from playwright.async_api import async_playwright, expect, BrowserContext, Page, Locator
import asyncio
from loguru import logger
import random

from .metamask_file import Meta, MetaImp


class Humanity:
    def __init__(self, private_key):
        self.metaimp = MetaImp(private_key=private_key)
        self.meta = Meta()
        self.private_key = private_key

    
    async def go_connect_claim(self, context: BrowserContext):
        try:
            page = await context.new_page()
            await page.set_viewport_size({"width":1920, "height":1080})
            await page.goto("https://testnet.humanity.org/login")
            

            connect_button = page.get_by_test_id(test_id="connect-wallet-button")
            await expect(connect_button).to_be_enabled()
            await connect_button.click()
            
            metamask_button = page.get_by_test_id(test_id="rk-wallet-option-metaMask")
            await expect(metamask_button).to_be_enabled()
            await metamask_button.click()
            

            await self.meta.connect_to_site(context=context)
            await self.meta.approve(context=context)

            verify_button = page.get_by_test_id(test_id="rk-auth-message-button")
            await expect(verify_button).to_be_enabled()
            await verify_button.click()
            

            await self.meta.confirm(context=context)

            
            start_button = page.locator("xpath=/html/body/div[2]/div[2]/div/div/div[2]/div[3]/button")
            await expect(start_button).to_be_enabled(timeout=100000)
            await start_button.click()

            next_button_1 = page.get_by_text("Next").first
            await expect(next_button_1).to_be_enabled(timeout=100000)
            await next_button_1.click()
            

            next_button_2 = page.get_by_text("Next").first
            await expect(next_button_2).to_be_enabled(timeout=100000)
            await next_button_2.click()    
            

            next_button_3 = page.get_by_text("Next").last
            await expect(next_button_3).to_be_enabled(timeout=100000)
            await next_button_3.click()   
            
            
            next_button_4 = page.get_by_text("Next").last
            await expect(next_button_4).to_be_enabled(timeout=100000)
            await next_button_4.click()  
            

            next_button_5 = page.get_by_text("I'm ready!")
            await expect(next_button_5).to_be_enabled(timeout=100000)
            await next_button_5.click()
            

            try:
                continue_buttons = page.get_by_text("Continue")
                continue_button_last = continue_buttons.nth(1)
                continue_button_first = continue_buttons.first

                await expect(continue_button_last).to_be_enabled(timeout=100000)
                await continue_button_last.click()

                await expect(continue_button_first).to_be_enabled(timeout=100000)
                await continue_button_first.click()
                
            except Exception as err:
                logger.debug("Single continue button here")
                continue_button = page.get_by_text("Continue")
                await expect(continue_button).to_be_enabled(timeout=100000)
                await continue_button.click()
                
           

            claim_button = page.locator("xpath=/html/body/div/div/div/main/div[2]/div/div[2]/div/div[1]/button")
            inner_text =  await claim_button.inner_text()

            if inner_text == "Claim":
                await expect(claim_button).to_be_enabled(timeout=100000)
                await claim_button.click()
                logger.success("Successfully claimed daily reward")
                return True
            else:
                logger.info("Daily reward have already claimed")
                return True
        
        except Exception as err:
            logger.error(err)
            raise Exception(err)
            

