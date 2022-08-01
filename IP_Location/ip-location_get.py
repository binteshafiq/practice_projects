from bottle import get, request, run, template
import requests, json

@get('/ip')
@get('/ip/<ip_address>')
def ip(ip_address=None):

    result = None
    if ip_address is not None:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")    # get method used to get or retrieve data from specified resource
        text = response.text

        result = json.loads(text)

    return template('input_form.tpl', ip_address=ip_address, result=result)

run(host='localhost', port=8080, debug=True, reloader = True)
