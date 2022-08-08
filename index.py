import requests,json
import pandas as pd
# Course ids
course = {71:"Programming Basics - 1", 72:"Programming Basics - 2", 73:"Programming Basics - 3", 74:"Programming Basics - 4",75:"Programming Basics - 5"}  
userId=[] #All uderId including dups
AssId=[]
AssName=[]
SubmittedAt=[]
userName=[]
dic={}

for c in course.keys():
	l = 1
	while True:

		URL = "https://msit.getlearning.app/api/v1/courses/"+str(c)+"/gradebook_history/feed?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0&page="+str(l)

		r = requests.get(url = URL)
		j = json.loads(r.content)
		if len(j) == 0:
			break
		for i in j:
			url2 = "https://msit.getlearning.app//api/v1/courses/"+ str(c) +"/assignments/"+ str(i['assignment_id'])+"?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0"
			r1 = requests.get(url = url2)
			z = json.loads(r1.content)
			# print(str(c)+"|"+ course[c]+"|"+ str(i['user_id'])+"|"+ i['user_name']+"|"+ str(i['assignment_id'])+"|"+z['name']+"|"+ i['submitted_at'])
		l += 1
	



# URL = "https://msit.getlearning.app//api/v1/courses/71/assignments/87?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0"
# r = requests.get(url = URL)
# j = json.loads(r.content)
# print(j.keys())
# print(j["name"])
# print(j[0].values())


