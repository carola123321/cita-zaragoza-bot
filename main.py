import asyncio

from monitor import comprobar_citas
from telegram_bot import enviar_aviso


async def main():

    print("Comprobando citas...")

    disponible = await comprobar_citas()

    if disponible:
        await enviar_aviso(
            "🚨🚨🚨 ¡¡HAY UNA CITA DISPONIBLE EN ZARAGOZA!! 🚨🚨🚨"
        )
    else:
        print("Todavía no hay citas.")


asyncio.run(main())
