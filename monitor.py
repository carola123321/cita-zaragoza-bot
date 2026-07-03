from playwright.async_api import async_playwright

URL = "https://sede.administracionespublicas.gob.es/icpplustiej/citar?org=JUS-RC&locale=es&appVersion=V+7.44.4"

async def comprobar_citas():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(URL)

        await page.wait_for_timeout(3000)

        texto = await page.content()

        await browser.close()

        if "En este momento no hay citas disponibles" in texto:
            return False

        return True
