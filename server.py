from transliterate import translit, get_available_language_codes
from flask import *
import requests
app = Flask(__name__)

def create_new_lead(form_name,person_who_fill_form,form_answer):
    url = "https://milldent.amocrm.ru/api/v4/leads"

    payload = '[{"name": "'+form_name+'", "custom_fields_values": [{"field_id": 250045, "values": [{"value": "'+form_answer+'"}]}]}]'

    headers = {
      'Content-Type': 'application/json',
      'Cookie': 'user_lang=ru; session_id=ett2uk796lqlfqffgfjpjctdutch86sa'
    }
    response = requests.request("POST", url, headers=headers, data = payload.encode('utf8'))
    print(response.text.encode('utf8'))


@app.route("/", methods = ["POST"])
def hello():
    data = json.loads(request.data)

    if data["type"] == "confirmation":
        return Response('82a43778',status=200)
    elif (data["type"] == "message_reply")&(data['object']['peer_id'] == 8614541) :
        data_answer = data['object']
        parse = data_answer['text'].split('\n')

        form_name = str(parse[0].split(':')[1])
        person_who_fill_form = str(parse[1])
        full_form_answer = str(parse[3::1])
        form_answer = str(parse[28::1])

        print(form_answer)
        create_new_lead(form_name,person_who_fill_form,form_answer)

    return Response('ok',status=200)


if __name__ == "__main__":
    app.run(host='',port='5000',debug='True')
