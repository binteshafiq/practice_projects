from bottle import get, post, request, run, route, template  # redirect
import requests, json

@route('/')
@route('/<ip>')
#@get('/ip')                           #@route('/ip')
def ip(ip='1.2.3.4'):
    if request.query.get('ip'):

        ip = request.query.get('ip')
        response = requests.get(f"http://ip-api.com/json/{ip}")    # get method used to get or retrieve data from specified resource
        text = response.text
        result = json.loads(text)
        return template('disp_table', rows=result)
   
    return '''
        <form action = "/ip" method = "get">
            IP: <input name="ip" type="text" />  
            <input value = "IP" type = "submit" />
        </form>
        
    '''   
    
    #redirect ("http://ip-api.com/json/" + ip)


run(host='localhost', port=8080, debug=True, reloader = True)