from bottle import get, post, request, run, route, template  # redirect
import requests, json

@get ('/ip')                          # or @route('/login')
def ip():
    return '''
        <form action = "/ip" method = "post">
            IP: <input name="ip" type="text" />  
            <input value = "IP" type = "submit" />
        </form>
    '''
#@post('ip')
@route('/ip', method = 'Post')
def ip_location():
    ip = request.forms.get('ip')
    #redirect ("http://ip-api.com/json/" + ip)

    response = requests.get('http://ip-api.com/json/'+ ip)    # get method used to get or retrieve data from specified resource
    text = response.text

    result = json.loads(text)
    return template('disp_table', rows=result)


run(host='localhost', port=8080, debug=True, reloader = True)