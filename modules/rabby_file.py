from web3 import Web3
from playwright.async_api import async_playwright,expect, BrowserContext, Locator, Page
import asyncio
from loguru import logger


class Rabby:

    async def find_rabby_page(self, context: BrowserContext):
        await asyncio.sleep(10)
        for p in context.pages:
            if "chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/notification.html" in p.url:
                rabby_page: Page = p
                break
        return rabby_page
    

    async def connect(self, context: BrowserContext):
        rabby_page: Page = await self.find_rabby_page(context=context)
    
        ignore_all_button = rabby_page.get_by_text('Ignore all')
        await expect(ignore_all_button).to_be_enabled()
        await ignore_all_button.click()

        confirm_button = rabby_page.locator('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/button[1]')
        await expect(confirm_button).to_be_enabled()
        await confirm_button.click()


    async def add_network(self, context: BrowserContext):
        rabby_page: Page = await self.find_rabby_page(context=context)

        add_button = rabby_page.locator('//*[@id="root"]/div/div/div[3]/button[2]')
        await expect(add_button).to_be_enabled()
        await add_button.click()


    async def confirm(self, context: BrowserContext):
        rabby_page: Page = await self.find_rabby_page(context=context)

        sign_button = rabby_page.locator('//*[@id="root"]/div/footer/div/section/div[2]/div/button')
        await expect(sign_button).to_be_enabled()
        await sign_button.click()

        confirm_button = rabby_page.locator('//*[@id="root"]/div/footer/div/section/div[2]/div/button[1]')
        await expect(confirm_button).to_be_enabled()
        await confirm_button.click()


        

class RabbyImp():

    def __init__(self,private_key:str):
        self.web3 = Web3(provider=Web3.HTTPProvider("https://eth.llamarpc.com"))
        self.private_key = private_key
        self.address = Web3.to_checksum_address(self.web3.eth.account.from_key(self.private_key).address)
        self.rabby_pass = "u9UF92HBISNFK", 

    async def import_rabby(self, context: BrowserContext):
        await asyncio.sleep(5)

        rabby_page = context.pages[-1]
        
        import_wallet_button: Locator =  rabby_page.locator('//*[@id="root"]/div/div/div[2]/button[2]')
        await expect(import_wallet_button).to_be_visible()
        await import_wallet_button.click()
        logger
        private_key_button: Locator =  rabby_page.locator('//*[@id="root"]/div/div/div[2]/div[2]')
        await expect(private_key_button).to_be_visible()
        await private_key_button.click()
        
        # Pasting private key in field
        private_key_input: Locator =  rabby_page.get_by_placeholder('Input private key')
        await expect(private_key_input).to_be_visible()
        await private_key_input.fill(self.private_key)
        
        confirm_button: Locator =  rabby_page.locator('//*[@id="root"]/div/div/div/button')
        await expect(confirm_button).to_be_enabled()
        await confirm_button.click()
        

        # Creating password
        password_field_1:Locator =  rabby_page.get_by_placeholder('8 characters min')
        await expect(password_field_1).to_be_visible()
        await password_field_1.fill(str(self.rabby_pass))
        

        password_field_2: Locator =  rabby_page.locator('//*[@id="confirmPassword"]')
        await expect(password_field_2).to_be_visible()
        await password_field_2.fill(str(self.rabby_pass))

        # await asyncio.sleep(1000)
        # Confirm import 
        confirm_import: Locator = rabby_page.locator('//*[@id="root"]/div/div/div/form/footer/button')
        await expect(confirm_import).to_be_enabled()
        await confirm_import.click()
        await asyncio.sleep(0.1)
        # Get started
        finish_import: Locator =  rabby_page.locator('//*[@id="root"]/div/div/button')
        await expect(finish_import).to_be_visible()
        await finish_import.click()
        
        logger.success(f'Wallet {self.address} successfully imported')

