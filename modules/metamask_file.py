from web3 import Web3
from playwright.async_api import async_playwright,expect, BrowserContext, Page
import asyncio




class Meta:
    async def find_meta_page(self, context: BrowserContext):
        await asyncio.sleep(10)
        for p in context.pages:
            if "nkbihfbeogaeaoehlefnkodbefgpgknn/notification.html" in p.url:
                metamask_page = p
                break
        return metamask_page

    async def connect_to_site(self, context: BrowserContext):
        metamask_page: Page = await self.find_meta_page(context=context)
        connect_button = metamask_page.get_by_test_id(test_id="confirm-btn")
        await expect(connect_button).to_be_enabled(timeout=15000)
        await connect_button.click()
    
    async def approve(self, context: BrowserContext):
        metamask_page: Page = await self.find_meta_page(context=context)

        approve_button = metamask_page.get_by_test_id(test_id="confirmation-submit-button")
        await expect(approve_button).to_be_enabled(timeout=15000)
        await approve_button.click()
    
    async def confirm(self, context: BrowserContext):
        metamask_page: Page = await self.find_meta_page(context=context)

        confirm_button = metamask_page.get_by_test_id(test_id="confirm-footer-button")
        await expect(confirm_button).to_be_enabled(timeout=2500)
        await confirm_button.click()


class MetaImp():
    
    def __init__(self,private_key:str):
        self.web3 = Web3(provider=Web3.HTTPProvider("https://eth.llamarpc.com"))
        self.private_key = private_key
        self.address = Web3.to_checksum_address(self.web3.eth.account.from_key(self.private_key).address)
        self.mm_pass = "u9UF92HBISNFK",     


    async def import_metamask(self, context:BrowserContext, mm_pass="F992H98HINiujhde"):
        # try:
        #     if len(context.background_pages) == 0:
        #         background = await context.wait_for_event("serviceworker")
        #     else:
        #         background = context.background_pages[0]
        #     await asyncio.sleep(5)

        # except Exception as err:
        #     return True
        await asyncio.sleep(5)
        mm_page = context.pages[-1]

        checkbox = mm_page.get_by_test_id(test_id="onboarding-terms-checkbox")
        await expect(checkbox).to_be_visible(timeout=15000)
        await checkbox.click()
        
        import_wallet_button = mm_page.get_by_test_id(test_id="onboarding-create-wallet")
        await expect(import_wallet_button).to_be_visible(timeout=15000)
        await import_wallet_button.click()

        no_thanks_button = mm_page.get_by_test_id(test_id="metametrics-no-thanks")
        await expect(no_thanks_button).to_be_visible(timeout=15000)
        await no_thanks_button.click()

        pass_field_1 = mm_page.get_by_test_id(test_id="create-password-new")
        pass_field_2 = mm_page.get_by_test_id(test_id="create-password-confirm")
        pass_checkbox = mm_page.get_by_test_id(test_id="create-password-terms")
        confirm_pass_button = mm_page.get_by_test_id(test_id="create-password-wallet")
        # await asyncio.sleep(100)
        await expect(pass_field_1).to_be_visible(timeout=15000)
        await pass_field_1.fill(mm_pass)
        await pass_field_2.fill(mm_pass)
        await pass_checkbox.click()
        await confirm_pass_button.click()

        secure_wallet_later = mm_page.get_by_test_id(test_id="secure-wallet-later")
        await expect(secure_wallet_later).to_be_visible(timeout=15000)
        await secure_wallet_later.click()
        
        confirm_secure_later = mm_page.get_by_test_id(test_id="skip-srp-backup-popover-checkbox")
        await expect(confirm_secure_later).to_be_visible(timeout=15000)
        await confirm_secure_later.click()

        skip_button = mm_page.get_by_test_id(test_id="skip-srp-backup")
        await expect(skip_button).to_be_visible(timeout=15000)
        await skip_button.click()

        onbording_done_button = mm_page.get_by_test_id(test_id="onboarding-complete-done")
        await expect(onbording_done_button).to_be_visible(timeout=15000)
        await onbording_done_button.click()

        next_button = mm_page.get_by_test_id(test_id="pin-extension-next")
        await expect(next_button).to_be_visible(timeout=15000)
        await next_button.click()

        done_button = mm_page.get_by_test_id(test_id="pin-extension-done")
        await expect(done_button).to_be_visible(timeout=15000)
        await done_button.click()
        # Importing our private key
        account1_button =mm_page.locator("""//*[@id="app-content"]/div/div[2]/div/div[2]/button""") #mm_page.get_by_test_id(test_id="account-menu-icon")
        await expect(account1_button).to_be_visible(timeout=15000)
        await account1_button.click()

        add_wallet_button = mm_page.get_by_test_id(test_id="multichain-account-menu-popover-action-button")
        await expect(add_wallet_button).to_be_enabled(timeout=15000)
        await add_wallet_button.click()

        import_new_wallet_button = mm_page.get_by_test_id(test_id="multichain-account-menu-popover-add-imported-account")
        await expect(import_new_wallet_button).to_be_visible(timeout=15000)
        await import_new_wallet_button.click()

        private_key_field = mm_page.locator("""//*[@id="private-key-box"]""")
        await expect(private_key_field).to_be_attached()
        await private_key_field.fill(self.private_key)

        confirm_import_button = mm_page.get_by_test_id(test_id="import-account-confirm-button")
        await expect(confirm_import_button).to_be_enabled(timeout=15000)
        await confirm_import_button.click()
    
        return context







