import urllib2,urllib
import requests
base='https://aqs.epa.gov/api/rawData'
parameters={
'user':"EMAIL",
'pw':"rubyhare74",
'format':"DMCSV",
'param':"44201",
'bdate':"20110501",
'edate':"20110501",
'state':"37",
'county':"063"	
}



print "downloading the data"
x=requests.get(url=base,params=parameters)
print x.status_code
f=open('data.csv','w')
f.write(x.content)
