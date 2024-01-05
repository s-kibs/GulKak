import os
import discord
import requests
import json
import random
from replit import db

my_secret = os.environ['TOKENGUL']
intents = discord.Intents.all()
cuk_curse = [
    "shikas university", "fuzul university", "lanath hinsdustanas",
    "yich university gouch naar dyun"
]

cuk_descriptions = [
    "Baat agar iss university k teaching staff ki tou humare *IT DEPARTMENT * mai bs ginti k 4-5 teacher hai. Jo 1st semester to 8th semester khud he sab kuch pdhate hai. Sab ke sab all-rounders. Jo morning mai CP padhate hai sir wo hi afternoon mai CHEMISTRY bhi pdhayege. Aur agar exam hua tou duty bhi wahi denge. Aur phir agar viva hua tou viva bhi wahi lenge. Aur phir papers check bhi wahi krega.",
    "Hamare kashmir mein education system boht tarkee pai hai.Isi tarkee ki badolat aai hamare central university banwni .Jis k infrastructure ki baat karein to hai hi nahi. Baki administration k baat karein to administration k naam pai khali bus department hai.Library mere ghr k store room sai choti hai. Hostel facility mein teen k shed atein hai (barn). Over all mein apne pre primary school sai bhi isko compare nahi kar pa raha. But fir bhi kya karein competive exam de kar yehi milta hai. Isai acha tha mein exam du hi na or acha sa college  le lu kam sai kam odr canteen to hoga …:slight_smile:"
]

std_desc = [
    "__Daim__(**Manvar**) :yum:\n__DOB__ - 7-Oct-2002\n:zap: __**CAUTION**__:zap: : Always hungry proceed with caution.\n__Quote__ : 'bouchi ha leaj kyenh khyemaw','yeh kya bawaseer hai!'\n__Description__ : Yeh ek aisa manwar :japanese_ogre: hai jisko khaate khaate bhook lagti hai isski khaane ki salahiyat ko aaj tak koi paimayish nahi kar paya hai. Yeh jeew Srinagar k Amda Kadal :round_pushpin: ilake mai paya jaata hai. Shaam ko 9bje k baad yeh manvar offline hota hai due to some understandable reasons :eyes:.",
    "__Touseef__(**420,Retired Professor**) :man_teacher:\n __DOB__ - 5-April-2002\n:zap:__**CAUTION**__:zap: : Gets bored way to quickly and needs someone to talk to at night:eyes:.\n__Quote__ : 'Uska sharmana lazmi tha\n par woh nahi sharmaayi':person_facepalming:\n__Description__ : Yeh qabil-e-tareef insaan hai inke padhane ka tareeka puri duniya mai mashhoor hai:relieved: . Badqismati:cry: se yeh abh retire hochuke hai or apne shgirdon ko apne assistan k hawale kardiya hai. Abh inke padhne ki mahart sirf ek khaas insaan ko dekhno k milti hai:eyes:. Ussi khaas insaan ki wajah se inhoon nai apne langotiya yaar ka bhi saath choddiya hai:smiling_face_with_tear:. Aise toh abh yeh bht kam nazar aate hai par agar kismat achi huwi toh Srinagar ke Malabagh :round_pushpin: ilaqa mai inka deedar kiya jaa sakta hai",
    "__Shakir__(**Brightest Student, Shakeer**):student:\n__DOB__ - 23-June-2002\n:zap:__**CAUTION**__:zap: : Sensitive Person :no_mouth:\n__Quote__: \n__Description__ :Yeh shakhs kaafi honhaar or hoshiyaar hai:star_struck: bas ek kasar hai ki bht jaldi bura maanjata hai :frowning2:. Inko haal hi mai apne langotiya yaar se dokha mila hai kyu ki uss ki zindagi mai koi or aagaya hai:cry:.Yeh Srinagar k 90ft :round_pushpin:  ilaqe k rehne wale hai (JO EK HIGHWAY HAI! :stuck_out_tongue_winking_eye:) inki unke(S) baare mai zyada ilim nahi hai :smirk: :thumbsup: ",
    "__Naveed__(**Dr Er Prof**):teacher:\n__DOB__ - 17-March-2002\n:zap:__**CAUTION**__:zap: : Single Word Destruction :boom:\n__Quote__:'Being right is boring, stay worng.','The onlly way to live is without any rules.'WIP\n__Description__:Yeh insaan bohot kam baat karte hai :yawning_face: lekin jab bhi baat karta hai samne wala lajawab hojata hai:no_mouth:. Inke saath zabaan sambhal k baat karni chahiye warna baad mai pachtawa hoga:zipper_mouth:. Inki rafeeq-e-hayat :eyes: ki talash abhi jaari hai. Inke saath saath inke kapde :shirt: bhi inhi ki tarah kam hi lekin '**point**':face_with_monocle: bolte hai. Yeh aise toh Habak :round_pushpin: ke rehayeshi hai lekin apne courier dukandaar k paas jama karwate hai.:face_with_raised_eyebrow:",
    "__Sheikh Haseeb__(**HASEEB**):man_white_haired:\n __DOB__18-April-2002\n:zap:__**CAUTION**__:zap: : No Caution needed, harmless creature. :joy:\n__Quote__:'Ishq chum peekas pyeth':heartpulse:\n__Description__: Yeh haseeb hai waise itna kaafi hai par phir bhi agar thoda wazahat kare toh pehle kya hi wazahat karon :joy: ok ok jokes aside haseeb ko side pai rakhne ko nahi bola :joy: shhh shhh :face_with_hand_over_mouth: pehle se shuroo karte hai yeh shakhs kaafi fuzul si baatein bolte hai lekin kabhi kabhi galti se ek do baatein achi bhi boldeta hai(impactful). Yeh prandi aap ko Srinagar ke Habak :round_pushpin: ilaqe se taluk rakhta hai"
]

hoy = "hoy", "Hoy", "Hoy!", "HOY", "HOY!", "hoy hoy", "hoy hoy hoy", "hoy!", "hoy :person_raising_hand:", "hoy :woman_raising_hand:"
bye = "bye", "BYE", "Bye", "bye:wave:", "bye!", "BYE:wave:", "BYE!", "tata", "Bye:wave:", "Bye!", "Bye chuw", "Khuda hafiz", "byeh khudayas hawal", "byeh byeh", "aloha", "Allah hafiz", "duaon mai yaad rakhna waise bot k liye kya hi dua ki jaasakti hai :thinking:"


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_curse(curse_messages):
    if "curse" in db.keys():
        curse = db["curse"]
        curse.append(curse_messages)
        db["curse"] = curse
    else:
        db["curse"] = [curse_messages]


def del_curse(index):
    curse = db["curse"]
    if len(curse) > index:
        del curse[index]
        db["curse"] = curse


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('oo maama waraya'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msgch = message.channel

    if msg.startswith(hoy):
        await msgch.send(random.choice(hoy))
    if msg.endswith(bye):
        await msgch.send(random.choice(bye))

    if msg.startswith('sed lyf'):
        quote = get_quote()
        await msgch.send(quote)

    if msg.endswith('describe daim'):
        await msgch.send(std_desc[0])
    elif msg.endswith('describe touseef'):
        await msgch.send(std_desc[1])
    elif msg.endswith('describe shakir'):
        await msgch.send(std_desc[2])
    elif msg.endswith('describe naveed'):
        await msgch.send(std_desc[3])
    elif msg.endswith('describe sheikh haseeb'):
        await msgch.send(std_desc[4])
    elif msg.endswith('describe kibs' or 'describe kibriya'):
        await msgch.send('**Error 404** :_)')

    if msg.startswith('describe cuk'):
        await msgch.send(random.choice(cuk_descriptions))

    options = cuk_curse
    if "curse" in db.keys():
        options = options + list(db["curse"])

    if msg.startswith('cuk'):
        await msgch.send(random.choice(options))

    if msg.startswith('#wohwoh'):
        newcurse_message = msg.split("#wohwoh ", 1)[1]
        update_curse(newcurse_message)
        await msgch.send("alayii newa woh woh.")

    if msg.startswith("del"):
        curses = []
        if "curses" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_curse(index)
            curses = db["curses"]
            await msgch.send(curses)


client.run(my_secret)
