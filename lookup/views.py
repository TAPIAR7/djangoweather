from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		#return render(request, 'home.html', {'zipcode':zipcode})

		try:
			api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=5&API_KEY=526848FB-0241-447B-B1C3-3D43100E4ADB")
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
			
		try:
			if api[0]['Category']['Name'] == "Good":
				category_description = "(0 - 50)"
				category_color = "good"
			elif api[0]['Category']['Name'] == "Moderate":
				category_description = "(51 - 100)"
				category_color = "moderate"
				
			elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
				category_description = "(101 - 150)"
				category_color = "usg"
			elif api[0]['Category']['Name'] == "Unhealthy":
				category_description = "(151 - 200)"
				category_color = "unhealthy"
			elif api[0]['Category']['Name'] == "Very Unhealthy":
				category_description = "(201 - 300)"
				category_color = "veryunhealthy"
			elif api[0]['Category']['Name'] == "Hazardous":
				category_description = "(301 - 500)"
				category_color = "hazardous"
			
		except Exception as e:
			category_description = "No data to show,  incorrect zipcode"
			category_color = "No data to show, incorrect zipcode"
			api = "Error..."


		return render(request,'home.html',{
			'api': api,
			'category_description:': category_description,
			'category_color': category_color
			})
	else:
		try:
			api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=526848FB-0241-447B-B1C3-3D43100E4ADB")
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		
			
		
		try:
			if api[0]['Category']['Name'] == "Good":
				category_description = "(0 - 50)"
				category_color = "good"
			elif api[0]['Category']['Name'] == "Moderate":
				category_description = "(51 - 100)"
				category_color = "moderate"
			elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
				category_description = "(101 - 150)"
				category_color = "usg"
			elif api[0]['Category']['Name'] == "Unhealthy":
				category_description = "(151 - 200)"
				category_color = "unhealthy"
			elif api[0]['Category']['Name'] == "Very Unhealthy":
				category_description = "(201 - 300)"
				category_color = "veryunhealthy"
			elif api[0]['Category']['Name'] == "Hazardous":
				category_description = "(301 - 500)"
				category_color = "hazardous"
		except Exception as e:
			category_description = "No data to show,  incorrect zipcode"
			category_color = "No data to show, incorrect zipcode"



		return render(request,'home.html',{
			'api': api,
			'category_description:': category_description,
			'category_color': category_color
			})


def about(request):
	return render(request,'about.html',{})