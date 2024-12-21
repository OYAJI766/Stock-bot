import asyncio
from telegram import Bot
from datetime import datetime

# إعداد التوكن والـ chat_id
TOKEN = "7592279525:AAHIJZpwrqjdUwDu3joVqa10JmzMedp3ohM"  # ضع التوكن الخاص بك هنا
CHAT_ID = 1021075445  # ضع chat_id الخاص بك هنا

# بيانات الاكتتابات
ipo_data = [
    {"company": "شركة المراعي", "offer_date": "2024-12-25"},
    {"company": "شركة الاتصالات السعودية", "offer_date": "2024-12-30"},
    {"company": "شركة أرامكو", "offer_date": "2025-01-05"}
]

bot = Bot(token=TOKEN)

# دالة إرسال التنبيهات التلقائية
async def send_notifications():
    while True:
        today = datetime.now().date()
        for ipo in ipo_data:
            offer_date = datetime.strptime(ipo['offer_date'], "%Y-%m-%d").date()
            days_left = (offer_date - today).days

            if days_left == 1:
                await bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"تذكير: سيتم طرح أسهم {ipo['company']} غدًا ({offer_date})."
                )
            elif days_left == 0:
                await bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"اليوم هو موعد طرح أسهم {ipo['company']} ({offer_date})."
                )

        # التحقق مرة يومياً
        await asyncio.sleep(24 * 60 * 60)

# تشغيل البوت
print("البوت يعمل الآن...")
asyncio.run(send_notifications())
