from flask import Flask, request
import util
import whatsappservice


app = Flask(__name__)


@app.route("/welcome", methods=["GET"])
def index():
    return "welcome developer"


@app.route("/whatsapp", methods=["GET"])
def VerifyToken():
    try:
        accessToken = "78SAJSNJANS76S8DSHDBSBDS"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400


@app.route("/whatsapp", methods=["POST"])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.GetTextUser(message)

        ProcessMessages(text, number)
        # print (text)

        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"


def ProcessMessages(text, number):
    text = text.lower()
    listData = []

    if "Hola" in text:
        data = util.TextMessage(
            "Hola! Gracias por contactarnos. Estamos encantados de ayudarte con tu reserva, Escriba la siguiente palabra  *GOD* para hacer su reservación",
            number,
        )
    elif "GOD" in text:
        dataMenu = util.ListMessage(number)
        listData.append(data)
        listData.append(dataMenu)

    elif "menu" in text:
        data = util.TextMessage("👨‍👨‍👧‍👦 Cantidad de invitados 👨‍👨‍👧‍👦", number)
    elif "menu" in text:
        listData.append(data)
        listData.append(dataMenu)

    elif "menu" in text:
        data = util.TextMessage("👲 Cantidad de niños 👲", number)

    elif text > 0:
        data = util.TextMessage("¿Desea un espacio para los niños?", number)

    elif "Si" in text:
        data = util.TextMessage("🎇 ¿Desea fuego artificial? 🎇", number)

    elif "Si" in text:
        data = util.TextMessage(
            "https://elsoldesantiago.com/wp-content/uploads/2020/03/Banda-Real.jpg",
            number,
        )
    elif "Si" in text:
        data = util.TextMessage(
            "🎇 ¿Desea banda real para su evento?, Con un costo de 10,00 peso. 🎇", number
        )
        listData.append(data)

    elif "Si" in text:
        data = util.TextMessage(
            "Gracias por su reservación, en breve le estaremos contactando para confirmar su reservación.",
            number,
        )

    else:
        data = util.TextMessage("I'm sorry, I cant't understand you", number)
        listData.append(data)

    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)


def GenerateMessage(text, number):
    text = text.lower()
    if "text" in text:
        data = util.TextMessage("Text", number)
    if "format" in text:
        data = util.TextFormatMessage(number)

    if "image" in text:
        data = util.ImageMessage(number)

    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)

    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonsMessage(number)
    if "list" in text:
        data = util.ListMessage(number)

    whatsappservice.SendMessageWhatsapp(data)


if __name__ == "__main__":
    app.run()
