from os import getenv
from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    InputMediaPhoto,
    InputMediaVideo,
    BotCommand,
    BotCommandScopeDefault,
    MenuButtonCommands
)
from aiogram.types.input_file import FSInputFile
from colorama import Fore, Style
import asyncio
import logging
import text_constants.common
import text_constants.model




bot = Bot(token=str(getenv("BOT_TOKEN")), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

ADMIN_USER_ID = str(getenv("ADMIN_USER_ID"))


@dp.message(Command(commands=["start"]))
async def on_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Санкт-Петербург", callback_data="city")],
            [InlineKeyboardButton(text="Алматы", callback_data="city"), InlineKeyboardButton(text="Бишкек", callback_data="city")],
            [InlineKeyboardButton(text="Другой город", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await message.answer(text=text_constants.common.WELCOME_MESSAGE, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "start")
async def start_callback(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Санкт-Петербург", callback_data="city")],
            [InlineKeyboardButton(text="Алматы", callback_data="city"), InlineKeyboardButton(text="Бишкек", callback_data="city")],
            [InlineKeyboardButton(text="Другой город", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.common.WELCOME_MESSAGE, reply_markup=keyboard)
   

@dp.callback_query(lambda c: c.data == "city")
async def city(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Модель", callback_data="model")],
            [InlineKeyboardButton(text="Администратор", callback_data="admin")],
            [InlineKeyboardButton(text="Скаут", callback_data="scout")],
            [InlineKeyboardButton(text="Переводчик", callback_data="translator")],
            [InlineKeyboardButton(text="Секстер / Чаттер", callback_data="sexter")],
            [InlineKeyboardButton(text="Супервайзер", callback_data="supervisor")],
            [InlineKeyboardButton(text="Назад", callback_data="start")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.common.VACANCY_TEXT, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "contact")
async def contact(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Связаться", callback_data=f"contact_admin")],
        [InlineKeyboardButton(text="Главное меню", callback_data=f"start")]
    ])
    await callback_query.message.answer(text=text_constants.common.CONTACT, reply_markup=keyboard)



@dp.callback_query(lambda c: c.data == "contact_admin")
async def contact_admin(callback_query: CallbackQuery):
    username = callback_query.message.chat.username

    await callback_query.message.answer("Блоадорим за ваш интерес к сотрудничеству! Dаша заявка была отправлена админу. C вами свяжутся в ближайшее время для обсуждения деталей.")
    await bot.send_message(ADMIN_USER_ID, text=f"Запрос на сотрудничество от: @{username}.")


###########
## MODEL ##
###########
@dp.callback_query(lambda c: c.data == "model")
async def model(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Shy", callback_data="shy")],
            [InlineKeyboardButton(text="С мобильного телефона", callback_data="mobile_phone")],
            [InlineKeyboardButton(text="Fansly", callback_data="fansly")],
            [InlineKeyboardButton(text="Onlyfans", callback_data="onlyfans")],
            [InlineKeyboardButton(text="Студия", callback_data="studio")],
            [InlineKeyboardButton(text="Назад", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.model.INFO, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "shy")
async def shy(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="model")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.model.SHY, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "mobile_phone")
async def mobile_phone(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="model")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.model.MOBILE_PHONE, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "fansly")
async def fansly(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="model")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.model.FANSLY, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "onlyfans")
async def onlyfans(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="model")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.model.ONLYFANS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "studio")
async def studio(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Экскурсия по студии", callback_data="studio_excursion")],
            [InlineKeyboardButton(text="Фото комнат", callback_data="studio_room_photo")],
            [InlineKeyboardButton(text="Мероприятия", callback_data="events")],
            [InlineKeyboardButton(text="Назад", callback_data="model")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text="Выберите из вариантов: ", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "studio_excursion")
async def studio_excursion(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    media = [
        InputMediaVideo(media=FSInputFile("media/excursion.mp4")),
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="studio")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text="Проведем небольшую экскурсию в этом видео: ", reply_markup=keyboard)
    await bot.send_media_group(chat_id=chat_id, media=media)


@dp.callback_query(lambda c: c.data == "studio_room_photo")
async def studio_room_photo(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    media = [InputMediaPhoto(media=FSInputFile(f"media/rooms/{i}.jpeg")) for i in range(13)]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="studio")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text="Коллекция фотографий наших комнат: ", reply_markup=keyboard)
    await bot.send_media_group(chat_id=chat_id, media=media)


@dp.callback_query(lambda c: c.data == "events")
async def events(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    media = [InputMediaPhoto(media=FSInputFile(f"media/rooms/{i}.jpeg")) for i in range(15)]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="studio")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text="Коллекция фотографий с различных мероприятий: ", reply_markup=keyboard)
    await bot.send_media_group(chat_id=chat_id, media=media)


#####################
## OTHER VACANCIES ##
#####################
@dp.callback_query(lambda c: c.data == "admin")
async def admin(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.common.ADMIN, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "scout")
async def scout(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text=text_constants.common.SCOUT, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "translator")
async def translator(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text_constants.common.TRANSLATOR, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "supervisor")
async def supervisor(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text_constants.common.SUPERVISOR, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "sexter")
async def sexter(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await callback_query.message.answer(text_constants.common.SEXTER, reply_markup=keyboard)


@dp.message(Command(commands=["id"]))
async def get_chat_id(message: Message):
    chat_id = message.chat.id
    chat_type = message.chat.type
    await message.reply(
        f"💬 ID чата: `{chat_id}`\n📦 Тип: `{chat_type}`", parse_mode="Markdown"
    )




async def main():
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Запустить бота"),
        ],
        scope=BotCommandScopeDefault(),
    )
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=f"{Fore.GREEN}%(asctime)s{Style.RESET_ALL} | {Fore.BLUE}%(levelname)s{Style.RESET_ALL} | {Fore.YELLOW}%(name)s{Style.RESET_ALL} | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    asyncio.run(main())