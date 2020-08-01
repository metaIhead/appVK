from transliterate import translit, get_available_language_codes
from flask import *
import requests
app = Flask(__name__)

def create_new_lead(form_name,person_who_fill_form,form_answer):
    url = "https://milldent.amocrm.ru/api/v4/leads"

    payload = '[{"name": "'+form_name+'", "custom_fields_values": [{"field_id": 250045, "values": [{"value": "'+form_answer+'"}]}]}]'

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmZjdkZWYyOWRlNzIxNTAzYmI3OTY5YTAwMjczMjQxMmFjMTA0ODIxZWNmZmYwZTVjOTM3NzM5YjE2YTM2MWJmMWZkOTg1MDYwOWYyZmZhIn0.eyJhdWQiOiJhMWNkMGU3Mi1mN2U0LTRlMjEtYTE0ZS00N2I5ZGExMjE2NWMiLCJqdGkiOiJlZmY3ZGVmMjlkZTcyMTUwM2JiNzk2OWEwMDI3MzI0MTJhYzEwNDgyMWVjZmZmMGU1YzkzNzczOWIxNmEzNjFiZjFmZDk4NTA2MDlmMmZmYSIsImlhdCI6MTU5NjI1ODI0MywibmJmIjoxNTk2MjU4MjQzLCJleHAiOjE1OTYzNDQ2NDMsInN1YiI6IjYxNzcxMDYiLCJhY2NvdW50X2lkIjoyODk2NjQxNywic2NvcGVzIjpbImNybSJdfQ.mlIs-HbIvKu4s_khAFi53c_kzsJan0mmI9RuDV3vKjxAJxGpLeGaLv5fP0eTqxyhV7L9VQY6qI7h3w1LRdX9-K2yPWiVEfqaWgyFQ5vvrmavG5tS3lxw4BHyD4Fuw6OFnTDQJTo_Tv0cCjGK27tV6D9tpBp3UyBnWorJcvWGw7c79pafdYEI-q70iAu5ipCBYZJ0XdxEBVcebGX7q9WQ8lYLtSf8qDChzThDc0f90l61H9-UrIDR8lh0wabyYY2OWh4L6itBVV_HLMgOWgS3Q5aB005ws7qq8XMkWnoxSKWDKGMIGQV0wUijhQts3HwXMc-zK65LZJ2fGxBJYE8Nqg',
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
