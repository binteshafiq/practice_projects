import requests                                # requests library -- de facto standart for making HTTP requests in python
  
response = requests.get('https://wttr.in/')    # get method used to get or retrieve data from specified resource

# print (response.content)                     # .content gives access to the raw bytes of the response payload
# text = response.text
# print (text)
print (response.text)                          # .text convert raw bytes into a string using a character encoding such as UTF-8