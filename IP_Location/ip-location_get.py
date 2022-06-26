from bottle import get, request, run, template  
import requests, json

@get('/ip')                           
def ip():
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

run(host='localhost', port=8080, debug=True, reloader = True)
