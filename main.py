import logging

from aiogram import Bot, Dispatcher, executor, types
from button import *

API_TOKEN = '6290512650:AAEBHMfJQl4NDRXyVozQ4AYo2BC_LTD-oxI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Tumanni tanlang", reply_markup=bosh_menu_inline_keyboard)



@dp.callback_query_handler(text="1")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://static1.tgstat.ru/channels/_0/b2/b2ac5ff87694da7a8d388af17e6def62.jpg", caption="""Bektemir tumani""", reply_markup=Bektemir_tuman_inline_keyboard)

@dp.callback_query_handler(text="20")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://cf.bstatic.com/xdata/images/hotel/max1024x768/218049243.jpg?k=101a350f18c58eb7ea4e087e63a167d97278ad276c83c979021465250ca336c7&o=&hp=1", caption=""" Лотте Сити Хотел Ташкент Палас
    Yarim asrdan ortiq vaqtdan beri Lotte City Hotel Tashkent Palace yuqori darajadagi xizmatlari, shinam xonalarining zamonaviy interyeri, shuningdek, poytaxtimizning qoq markazida har ikki sayyoh uchun qulay joylashuvi bilan o‘z mehmonlarini xushnud etib kelmoqda. va ishbilarmonlar. Mehmonxona 1958-yilda qurilgan va 2013-yilda toʻliq taʼmirlangan. Mehmonxona tashqi koʻrinishining klassik arxitekturasi ichki dekoratsiyaning nafisligi bilan muvaffaqiyatli uygʻunlashgan va shahar landshaftiga mukammal uygʻunlashgan. Bino O‘zbekistonning madaniy merosi sifatida ham tan olingan.""", reply_markup=tashkent_plast_inline_keyboard)
    await call.message.answer_location(41.31474036568887, 69.27206899878206)

@dp.callback_query_handler(text="21")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://1001hotels.uz/image/cache/data/hotels/uzbekistan/tashkent/le_grande_plaza_hotel/legrandeplaza-800x600.jpg", caption="""Le Grand Plaza Hotel
    Hashamatli Le Grande Plaza mehmonxonasi Toshkentning qoq markazida joylashgan bo‘lib, unda xalqaro, xitoy, yapon va koreys taomlarini taklif qiluvchi restoranlar mavjud. Unda to'liq jihozlangan sport zali, sauna, issiq vanna va basseyn mavjud.
    """, reply_markup=grand_plaza_inline_keyboard)
    await call.message.answer_location(41.31680327514442, 69.28683187714205)
















@dp.message_handler(text="Ortga")
async def echo(message: types.Message):
    await message.answer("...", reply_markup=Bektemir_tuman_inline_keyboard)


@dp.callback_query_handler(text="2")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://storage.kun.uz/source/5/Kwa7ud4HcUSUDuGSta9zkDO04Pg3CjCe.jpg", caption="""Mirobod tumani""", reply_markup=Mirobod_tuman_inline_keyboard)

@dp.callback_query_handler(text="3")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://www.gazeta.uz/media/img/2020/02/ZGp3at15809931945070_l.jpg", caption="""Mirzo Ulug‘bek tumani""", reply_markup=Mirzo_Ulugbek_tuman_inline_keyboard)

@dp.callback_query_handler(text="4")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://podrobno.uz/upload/iblock/139/46078059_ddbd_d973_0fd9_8f198d7c42b0_lists_slider_4711.jpg", caption="""Sergeli tumani""", reply_markup=Sergeli_tuman_inline_keyboard)

@dp.callback_query_handler(text="5")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://studio-olmazor-city-tashkent.nochi.com/data/Photos/OriginalPhoto/11404/1140456/1140456898/Studio-Olmazor-City-Tashkent-Exterior.JPEG", caption="""Olmazor tumani""", reply_markup=Olmazor_tuman_inline_keyboard)

@dp.callback_query_handler(text="6")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://uchtepatumani.uz/images/2020/01/16/e99d7aea-f473-4e0d-9836-7e65d59317ac.jpeg", caption="""Uchtepa tumani""", reply_markup=Uchtepa_tuman_inline_keyboard)

@dp.callback_query_handler(text="7")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://www.uzdaily.uz/storage/img/Askar-foto-3/1585307082.1079.jpg", caption="""Shayxontohur tumani""", reply_markup=Shayxontohur_tuman_inline_keyboard)

@dp.callback_query_handler(text="8")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://www.norma.uz/img/51/ba/08334932f3590c451b8eff154e58.jpg", caption="""Yashnobod tumani""", reply_markup=Yashnobod_tuman_inline_keyboard)

@dp.callback_query_handler(text="9")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://www.gazeta.uz/media/img/2017/12/LNGKJZ15131711840459_b.jpg", caption="""Chilonzor tumani""", reply_markup=Chilonzor_tuman_inline_keyboard)

@dp.callback_query_handler(text="10")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://i.mycdn.me/i?r=AzGs3FHe7oNI_DMOh1R7TNAdqG46nZB1Fj-8cF5kDCK67WjgRY-n1U-4m-c2vsMWY_4", caption="""Yunusobod tumani""", reply_markup=yunusobod_tuman_inline_keyboard)

@dp.callback_query_handler(text="11")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://domtut.uz/resources/uploads/property/glinka-premium/main_3.jpg", caption="""Yakkasaroy tumani""", reply_markup=Yakkasaroy_tuman_inline_keyboard)

@dp.callback_query_handler(text="12")
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://yuz.uz/imageproxy/1200x/https://yuz.uz/file/news/cbc688b85c3de85b5294d949f507ce49.jpg", caption="""Yangihayot tumani""", reply_markup=Yangihayot_tuman_inline_keyboard)














if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)