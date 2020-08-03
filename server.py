from flask import *
import requests
import os
import json
app = Flask(__name__)

def create_new_lead(form_name,person_who_fill_form,form_answer):
    url = "https://milldent.amocrm.ru/api/v4/leads"

    name_lead = person_who_fill_form[0]+' '+person_who_fill_form[1]
    link_lead = person_who_fill_form[2]

    payload = '[{"name": "Новый заказ '+name_lead +'","custom_fields_values": [{"field_id": 261925, "values": [{"value": "'+str(form_answer[2])+'"}]}, {"field_id": 261929, "values": [{"value":"'+str(form_answer[5])+'"}]},{"field_id": 261931, "values": [{"value":"'+str(form_answer[8])+'"}]},{"field_id": 261933, "values": [{"value": "'+str(form_answer[11])+'"}]},{"field_id": 261935, "values": [{"value":"'+str(form_answer[14])+'"}]},{"field_id": 261937, "values": [{"value": "'+str(form_answer[17])+'"}]},{"field_id": 261939, "values": [{"value": "'+str(form_answer[20])+'"}]},{"field_id": 262225, "values": [{"value": "'+name_lead+'"}]}, {"field_id": 262227, "values": [{"value": "'+link_lead+'"}]}, {"field_id": 262229, "values": [{"value": "'+form_answer[-1]+'"}]}  ]}]'

    token = os.environ.get('token', None)

    headers = {
  'Content-Type': 'application/json',
  'Authorization': token,
  'Cookie': 'user_lang=ru'
}


    response = requests.request("POST", url, headers=headers, data = payload.encode('utf8'))
    print(response.text)


@app.route("/", methods = ["POST"])
def hello():
    data = json.loads(request.data)

    if data["type"] == "confirmation":
        return Response('92a4dda6',status=200)
    elif (data["type"] == "message_reply")&(data['object']['peer_id'] == 250291635) :
        print("send data")
        data_answer = data['object']
        parse = data_answer['text'].split('\n')

        form_name = str(parse[0].split(':')[1])
        person_who_fill_form = parse[1].split(' ')
        full_form_answer = parse[3::1]

        create_new_lead(form_name,person_who_fill_form,full_form_answer)

    return Response('ok',status=200)


if __name__ == "__main__":
    app.run(host='',port='5000',debug='True')
