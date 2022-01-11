**The app will return the data inside of an json file,**
**when presented with the ip that corresponds with the json key**

The app works as follows:
	- When going to your local ip in your browser you will be
	  presented with a screen that shows a "manual search option"
	  this option allows you to submit the get form to be processed by the server
	  the url will then redirect to /data...(with the suffix after the ?lookup= being the get form data)
	
	- If you want to use the app as an api do as follows:
		- use the url http://127.0.0.1:5000/data?lookup=...
		- in replacement of the ... add an ip for lookup
		  e.g. http://127.0.0.1:5000/data?lookup=10.49.111.222
		  refer to the eof for the list of ip's you can lookup.
		  
	- To add more ip's to the json do as follows:
		- before the closing square bracket edit and paste line 18.
		,{"ip"{"name":"name", "age":00, "location":"location"}}
		
List of predefined ip's in the json:
	10.49.111.222
	10.49.333.444
	10.49.555.666
		  
:eof