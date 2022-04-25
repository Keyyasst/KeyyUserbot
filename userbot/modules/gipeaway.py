# @greyyvbss
#cilik-userbot
# Recode by @mfbyh


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, keyy_cmd


@keyy_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**ANJAY ADA GIPEAWAY NIH**")


@keyy_cmd(pattern="b(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BABI SOALNYA GA DANTA BET**")


@keyy_cmd(pattern="c(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**ANJING LAMA BET, TURUNIN SOALNYA**")


@keyy_cmd(pattern="d(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MANA SOALNYA BUJED, GUA NUNGGUIN DARI TADI**")


@keyy_cmd(pattern="e(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MINIMAL KALO HADIAHNYA DIKIT, SOALNYA DANTA DIKIT YA ANJENG 😁!!**")


@keyy_cmd(pattern="f(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**HETT GIPEAWAY NYA DIKIT BET, DASAR GC MISKIN CUIHHH!!**")


@keyy_cmd(pattern="g(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**KALO GIPEAWAY SOALNYA YANG BENER YA NGENTOTTT**")


@keyy_cmd(pattern="h(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MINGGIR-MINGGIR DONATUR MAU LEWAT**")


@keyy_cmd(pattern="i(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**MISKIN MISKIN AJA TOD, GAUSAH SOK SOK AN JADI DONATUR!!**")


@keyy_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GCAST DULU AHHHHH, KALI AJA MENANG GIPEAWAY!!**")


@keyy_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**JAWABAN YANG BENER YANG MANA ANJENG**")


@keyy_cmd(pattern="m(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**PAANSI SOALNYA PRIK BANGET!!**")


@keyy_cmd(pattern="n(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**NAJISSS GIPEAWAY NYA CUMAN CEBAN YANG BANYAKAN NAPAH!!**")


@keyy_cmd(pattern="o(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**OMEGAT GUA MENANG GIPEAWAY, MAYAN BUAT PICIES!!** 🥵🥵")


@keyy_cmd(pattern="r(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**RAME JUGA DISINI, IKUTAN AHHH!!**")


@keyy_cmd(pattern="s(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GC ANJING SOALNYA GA DANTA SEMUA DAHLAH!!**")


@keyy_cmd(pattern="t(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**HETTT SOALNYA GAMPANG BET, BARI MEREM GE BISA INI MAH** 🥱")


@keyy_cmd(pattern="u(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**UDAH UDAH GIPEAWAY NYA UDAHAN, YAH KASIAN BET KETINGGALAN**")


@keyy_cmd(pattern="v(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CAPE CAPE GIKES SOALNYA GA DANTA KONTOLL**")


@keyy_cmd(pattern="w(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CLUE NYA APA ANJENG, SOALNYA GAJELAS**")

    
@keyy_cmd(pattern="x(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**DIMANA ADA GIPEAWAY DISITU ADA GUA WHAHAHAHAHA**")
    
   
@keyy_cmd(pattern="z(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GUA MAU NURUNIN SOAL NIH , BENTAR MIKIR DULU**")  
    

CMD_HELP.update(
    {
        "gipeaway": f"**Plugin : **`gipeaway`\
        \n\nㅤㅤ•**Syntax** : {cmd}a-z\
        \n•**Function : **Kata-Kata buat giveaway\
    "
    })

