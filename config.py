import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "7057648012:AAFf9H6_Afy4OIkUSC2qkSuqKI9mk_Xykrs")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "pot1") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001940437648"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001962418199")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002110504220"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "25"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#8888 #2211 #Boy #Girl #Ask #Spill #Random #Story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", "Hai {NAME}, untuk mengirim pesan atau foto & video kamu harap join terlebih dahulu ke channel dan group POT 😉, jika sudah tekan COBA LAGI atau /help")
start_msg = os.getenv("START_MSG", """
Selamat Datang {mention}

bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim pesan berupa foto dan video, gunakan hastag dibawah untuk mengirim pesan:

#Boy - untuk identitas cowo
#Girl - untuk identitas cewe
#Ask - digunakan untuk bertanya
#Spill - spill sesuatu
#Random - untuk kirim foto/video random
#Story - untuk bercerita
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#Boy - untuk identitas cowo
#Girl - untuk identitas cewe
#Ask - digunakan untuk bertanya
#Spill - spill sesuatu
#Random - untuk kirim foto/video random
#Story - untuk bercerita

jangan lupa join @TopGroupChat
""")
