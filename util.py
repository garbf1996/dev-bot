def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")

    else:
        print("sin mensaje")

    return text


def TextMessage(text, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "text": {"body": text},
        "type": "text",
    }
    return data


def TextFormatMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
            "body": "*Información importante*\n_Necesitas enviar tu correo_\n~Pero tiene que estar~\n```en diferente formato```"
        },
    }
    return data


def ImageMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
        },
    }
    return data


def AudioMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "audio",
        "audio": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
        },
    }
    return data


def VideoMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "video",
        "video": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
        },
    }
    return data


def DocumentMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "document",
        "document": {
            "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
        },
    }
    return data


def LocationMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "location",
        "location": {
            "latitude": "-12.067158831865067",
            "longitude": "-77.03377940839486",
            "name": "Estadio Nacional del Perú",
            "address": "C. José Díaz s/n, Cercado de Lima 15046",
        },
    }
    return data


def ButtonsMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": "*Selecciona el tipo de evento quiere realizar*"},
            "action": {
                "button": "Seleccionar",
                "sections": [
                    {
                        "title": "🎈 Opción 1 🎈",
                        "rows": [
                            {
                                "id": "1",
                                "title": "Fiesta de cumpleaños ",
                            }
                        ],
                    },
                    {"title": "💍 Opción 2 💍", "rows": [{"id": "2", "title": "Boda"}]},
                    {
                        "title": "🧏‍♂️ Opción 3 🧏‍♂️",
                        "rows": [{"id": "3", "title": "Reunión de empresa"}],
                    },
                ],
            },
        },
    }

    return data


def ListMessage(number):
    data = (
        {
            "messaging_product": "whatsapp",
            "to": "51943662964",
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {"text": "*opciones de buffet*"},
                "action": {
                    "button": "Seleccionar",
                    "sections": [
                        {
                            "title": "Opcion 1",
                            "rows": [
                                {
                                    "id": "1",
                                    "title": "Buffet de parrillada",
                                    "description": "Carne asada, pollo a la parrilla, cerdo, salchichas, etc, ",
                                }
                            ],
                        },
                        {
                            "title": "Opción 2",
                            "rows": [
                                {
                                    "id": "2",
                                    "title": "Buffet de tapas",
                                    "description": "Pequeñas porciones de platillos como albóndigas, croquetas, bruschettas",
                                }
                            ],
                        },
                        {
                            "title": "Opción 3",
                            "rows": [
                                {
                                    "id": "3",
                                    "title": "Buffet vegetariano",
                                    "description": "Platos vegetarianos y veganos como lasaña de verduras",
                                }
                            ],
                        },
                    ],
                },
            },
        },
    )

    return data
