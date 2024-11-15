from django.shortcuts import render

import json

import urllib.request

def index(request):
    if request.method == 'POST':
        name = request.POST['city']

        source = urllib.request.urlopen(
            'https://api.weatherapi.com/v1/current.json?key=3b9843b2824740588ba90024241411&q='+name+'&aqi=no').read()
        
        list_of_data = json.loads(source)

        data = { 
            "country_code": str(list_of_data['location']['country']), 
            "coordinate": str(list_of_data['location']['lon']) + ' '
                        + str(list_of_data['location']['lat']), 
            "temp": str(list_of_data['current']['temp_f']) + 'k', 
            "pressure": str(list_of_data['current']['pressure_mb']), 
            "humidity": str(list_of_data['current']['humidity']), 
        } 
        print(data)
    else:
        data={}
    return render(request,"main/index.html",data)
