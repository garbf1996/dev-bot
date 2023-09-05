import requests
import json


def SendMessageWhatsapp(data):
    try:
        token = "EAAMSX8cfWfABOyYArbDLsWzIZAL6T1kX12vlHbsxyVJxqzAtKZABjSOd32P1JtP9ntfsvNjp3Cmiy9n1zg4iINO6qtlcK4uZAWQ82qvk6JdStOTq8Hi4qHTMSuTtl6YuBlfhyvQY6ZA2QYLuTtC6u8qpesBz4hZBtlNIPyECOHobB8DO0ia5TZCBbN2P7Bhviq"
        api_url = "https://graph.facebook.com/v17.0/106867522510096/messages"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        }
        response = requests.post(api_url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            return True

        return False
    except Exception as exception:
        print(exception)
        return False
