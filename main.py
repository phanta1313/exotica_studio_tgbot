from operator import call
from os import getenv
from dotenv import load_dotenv
from httpx import get

import text_constants.administrator
import text_constants.agent
import text_constants.common
import text_constants.model
import text_constants.operator
import text_constants.vacancies
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
    BotCommand,
    BotCommandScopeDefault,
    MenuButtonCommands
)
from aiogram.types.input_file import FSInputFile
from colorama import Fore, Style
import asyncio
import logging
import text_constants




bot = Bot(token=str(getenv("BOT_TOKEN")), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

CITIES = ["moscow", "peter", "ekaterinburg", "novosibirsk", "krasnoyarsk", "tumen", "tomsk", "ufa", "other_city"]
ADMIN_USER_ID = getenv("ADMIN_USER_ID")


@dp.message(Command(commands=["start"]))
async def on_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Москва", callback_data="moscow"), InlineKeyboardButton(text="Санкт-Петербург", callback_data="peter")],
            [InlineKeyboardButton(text="Екатеринбург", callback_data="ekaterinburg"), InlineKeyboardButton(text="Новосибирск", callback_data="novosibirsk")],
            [InlineKeyboardButton(text="Челябинск", callback_data="chelabinsk"), InlineKeyboardButton(text="Красноярск", callback_data="krasnoyarsk")],
            [InlineKeyboardButton(text="Краснодар", callback_data="krasnodar"), InlineKeyboardButton(text="Тюмень", callback_data="tumen")],
            [InlineKeyboardButton(text="Томск", callback_data="tomsk"), InlineKeyboardButton(text="Уфа", callback_data="ufa")],
            [InlineKeyboardButton(text="Другой город", callback_data="other_city")],
            [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data="contact")]
        ])
    await message.answer(text_constants.common.WELCOME_MESSAGE, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data in CITIES or c.data == "vacancies")
async def city_callback(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Модель", callback_data=f"model")],
        [InlineKeyboardButton(text="Оператор", callback_data=f"operator")],
        [InlineKeyboardButton(text="Агент", callback_data=f"agent")],
        [InlineKeyboardButton(text="Администратор", callback_data=f"administrator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.common.VACANCY_INFO, reply_markup=keyboard)
    

###########   
## MODEL ##
###########
@dp.callback_query(lambda c: c.data == "model")
async def model(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Работа из дома", callback_data=f"model_home")],
        [InlineKeyboardButton(text="Работа на студии", callback_data=f"model_studio")],
        [InlineKeyboardButton(text="Что может быть на трансляции?", callback_data=f"model_live")],
        [InlineKeyboardButton(text="Конфиденциальность", callback_data=f"model_conf")],
        [InlineKeyboardButton(text="Другие вакансии", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.vacancies.MODEL, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_home")
async def model_home(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что дает студия?", callback_data=f"studio_oportunities")],
        [InlineKeyboardButton(text="Сколько я буду зарабатывать?", callback_data=f"model_cash")],
        [InlineKeyboardButton(text="Что от меня требуется?", callback_data=f"model_home_requirements")],
        [InlineKeyboardButton(text="План действий", callback_data=f"model_home_plan")],
        [InlineKeyboardButton(text="Вернутся к вакансиям", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.HOME, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "studio_oportunities")
async def studio_oportunities(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_home")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.STUDIO_OPORTUNITIES, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_cash")
async def model_cash(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Процентная ставка", callback_data=f"model_percent")],
        [InlineKeyboardButton(text="Назад", callback_data=f"model")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.CASH, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_percent")
async def model_percent(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_home")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.PERCENT, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_home_requirements")
async def model_home_requirements(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_home")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.HOME_REQUIREMENTS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_home_plan")
async def model_home_plan(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_home")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.HOME_PLAN, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_studio")
async def model_studio(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сколько я буду зарабатывать?", callback_data=f"model_cash")],
        [InlineKeyboardButton(text="Как выглядит студия?", callback_data=f"model_studio_appereance")],
        [InlineKeyboardButton(text="Что от меня требуется?", callback_data=f"model_studio_requirements")],
        [InlineKeyboardButton(text="План действий", callback_data=f"model_studio_plan")],
        [InlineKeyboardButton(text="Вернутся к вакансиям", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.STUDIO, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_studio_appereance")
async def model_studio_appereance(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Примеры квартир", callback_data=f"model_studio_rooms")],
        [InlineKeyboardButton(text="Назад", callback_data=f"model_studio")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.STUDIO_APPEREANCE, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_studio_rooms")
async def model_studio_rooms(callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    media = [
        InputMediaPhoto(media=FSInputFile("media/rooms/room1.jpg")),
        InputMediaPhoto(media=FSInputFile("media/rooms/room2.jpg")),
        InputMediaPhoto(media=FSInputFile("media/rooms/room3.jpg")),
        InputMediaPhoto(media=FSInputFile("media//rooms/room4.jpg")),
    ]
    await bot.send_media_group(chat_id=chat_id, media=media)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_studio_appereance")],
        [InlineKeyboardButton(text="Вернутся к вакансиям", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.STUDIO_ROOMS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_studio_requirements")
async def model_studio_requirements(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_studio")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.STUDIO_REQUIREMENTS, reply_markup=keyboard)



@dp.callback_query(lambda c: c.data == "model_studio_plan")
async def model_studio_plan(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model_studio")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.STUDIO_PLAN, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_live")
async def model_live(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что могут попросить зрители?", callback_data=f"model_clients_ask")],
        [InlineKeyboardButton(text="Назад", callback_data=f"model_studio")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.WHAT_IS_IN_LIVE, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_clients_ask")
async def model_live(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Посмотреть список", callback_data=f"model_clients_ask_list")],
        [InlineKeyboardButton(text="Назад", callback_data=f"model_studio")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.CLIENT_REQUEST, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_clients_ask_list")
async def model_clients_ask_list(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вернутся к вакансии", callback_data=f"model")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.CLIENT_REQUEST_LIST, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "model_conf")
async def model_conf(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Даеонщики и шантажисты на сайтах", callback_data=f"bad_people")],
        [InlineKeyboardButton(text="Назад", callback_data=f"model")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.CONF, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "bad_people")
async def bad_people(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Как полностью себя обезопасить?", callback_data=f"how_to_secure")],
        [InlineKeyboardButton(text="Назад", callback_data=f"model")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.BAD_PEOPLE, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "how_to_secure")
async def how_to_secure(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"model")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.model.HOW_TO_SECURE_YS, reply_markup=keyboard)



##############
## OPERATOR ##
##############
@dp.callback_query(lambda c: c.data == "operator")
async def operator(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что нужно делать?", callback_data=f"operator_what_to_do")],
        [InlineKeyboardButton(text="Какие условия", callback_data=f"operator_conditions")],
        [InlineKeyboardButton(text="Что от меня требуется?", callback_data=f"operator_requirements")],
        [InlineKeyboardButton(text="Другие вакансии", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.vacancies.OPERATOR, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "operator_what_to_do")
async def operator_what_to_do(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"operator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.operator.WHAT_TO_DO, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "operator_conditions")
async def operator_conditions(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Процентная сетка", callback_data=f"operator_percent")],
        [InlineKeyboardButton(text="Назад", callback_data=f"operator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.operator.CONDITIONS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "operator_percent")
async def operator_percent(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"operator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.operator.PERCENT, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "operator_requirements")
async def operator_requirements(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"operator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.operator.REQUIREMENTS, reply_markup=keyboard)


###########
## AGENT ##
###########
@dp.callback_query(lambda c: c.data == "agent")
async def agent(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Где искать моделей?", callback_data=f"agent_find_models")],
        [InlineKeyboardButton(text="Какие модели подходят?", callback_data=f"agent_model_requirements")],
        [InlineKeyboardButton(text="Сколько я буду получать?", callback_data=f"agent_cash")],
        [InlineKeyboardButton(text="Как рассказать о студии?", callback_data=f"agent_describe_studio")],
        [InlineKeyboardButton(text="Другие вакансии", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.vacancies.AGENT, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "agent_find_models")
async def agent_find_models(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"agent")],        
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.WHERE_TO_FIND_MDOELS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "agent_model_requirements")
async def agent_model_requirements(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"agent")],        
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text="не хватает текста", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "agent_cash")
async def agent_cash(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"agent")],        
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.CASH, reply_markup=keyboard)  


@dp.callback_query(lambda c: c.data == "agent_describe_studio")
async def agent_describe_studio(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Для девушки с опытом", callback_data=f"agent_girl_with_exp")],       
        [InlineKeyboardButton(text="Для девушки без опыта", callback_data=f"agent_girl_without_exp")],   
        [InlineKeyboardButton(text="Назад", callback_data=f"agent")],     
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.HOW_TO_DESCRIBE_STUDIO, reply_markup=keyboard) 


@dp.callback_query(lambda c: c.data == "agent_girl_with_exp")
async def agent_girl_with_exp(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"agent_describe_studio")],       
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.GIRLS_WITH_EXPIRIENCE, reply_markup=keyboard) 


@dp.callback_query(lambda c: c.data == "agent_girl_without_exp")
async def agent_girl_without_exp(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[   
        [InlineKeyboardButton(text="Безопасность в интернете", callback_data=f"internet_security")], 
        [InlineKeyboardButton(text="Физическая безопасность", callback_data=f"physical_security")],    
        [InlineKeyboardButton(text="Назад", callback_data=f"agent_describe_studio")],       
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.GIRLS_WITHOUT_EXPIRIENCE, reply_markup=keyboard) 


@dp.callback_query(lambda c: c.data == "internet_security")
async def internet_security(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[    
        [InlineKeyboardButton(text="Назад", callback_data=f"agent_describe_studio")],       
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.INTERNET_SECURITY, reply_markup=keyboard) 


@dp.callback_query(lambda c: c.data == "physical_security")
async def physical_security(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[    
        [InlineKeyboardButton(text="Назад", callback_data=f"agent_describe_studio")],       
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.agent.PHYSICAL_SECURITY, reply_markup=keyboard) 


##################
## ADMINSTRATOR ##
##################
@dp.callback_query(lambda c: c.data == "administrator")
async def administrator(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что нужно делать?", callback_data=f"administrator_what_to_do")],
        [InlineKeyboardButton(text="Какие условия?", callback_data=f"administrator_conditions")],
        [InlineKeyboardButton(text="Что от меня требуется?", callback_data=f"administrator_reqirements")],
        [InlineKeyboardButton(text="Другие вакансии", callback_data=f"vacancies")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.vacancies.ADMINISTRATOR, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "administrator_what_to_do")
async def administrator_what_to_do(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"administrator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.administrator.WHAT_TO_DO, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "administrator_conditions")
async def administrator_conditions(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"administrator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.administrator.CONDITIONS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "administrator_reqirements")
async def administrator_reqirements(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data=f"administrator")],
        [InlineKeyboardButton(text="💁‍♀️СВЯЖИТЕСЬ СО МНОЙ💁‍♀️", callback_data=f"contact")]
    ])
    await callback_query.message.answer(text=text_constants.administrator.REQUIREMENTS, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "contact")
async def contact(callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Связаться", callback_data=f"contact_admin")],
        [InlineKeyboardButton(text="Главное меню", callback_data=f"vacancies")]
    ])
    await callback_query.message.answer(text=text_constants.common.CONTACT, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "contact_admin")
async def contact_admin(callback_query: CallbackQuery):
    username = callback_query.message.chat.username

    await bot.send_message(ADMIN_USER_ID, text=f"Запрос на сотрудничество от: {username}.")
    

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