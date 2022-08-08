from sqlite3 import Time
import requests,json
import datetime
import pandas as pd
user_id=[]
ass_id=[]
time=[]
def date(d):
	if d == "Programming Basics - 1":
		time = [2022, 8, 1, 9, 00, 00]
		return time
	elif d == "Programming Basics - 2":
		time = [2022, 8, 2, 9, 00, 00]
		return time
	elif d == "Programming Basics - 3":
		time = [2022, 8, 3, 9, 00, 00]
		return time
	elif d == "Programming Basics - 4":
		time = [2022, 8, 4, 9, 00, 00]
		return time
	elif d == "Programming Basics - 5":
		time = [2022, 8, 5, 9, 00, 00]
		return time

def total_time(start_time, end_time):
    a = datetime.datetime(end_time[0], end_time[1], end_time[2], end_time[3], end_time[4], end_time[5])
    b = datetime.datetime(start_time[0], start_time[1], start_time[2], start_time[3], start_time[4], start_time[5])
  
    # returns a timedelta object
    c = a-b 
  
    minutes = (c.seconds) // 60
    return minutes

course = {71:"Programming Basics - 1", 72:"Programming Basics - 2", 73:"Programming Basics - 3", 74:"Programming Basics - 4", 75:"Programming Basics - 5"}  

for c in course.keys():

	l = 1
	while True:

		URL = "https://msit.getlearning.app/api/v1/courses/"+str(c)+"/gradebook_history/feed?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0&page="+str(l)

		r = requests.get(url = URL)
		j = json.loads(r.content)
		#print(j)
		if len(j) == 0:
			break
		for i in j:
			#print(i)
			url2 = "https://msit.getlearning.app//api/v1/courses/"+ str(c) +"/assignments/"+ str(i['assignment_id'])+"?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0"
			
			r1 = requests.get(url = url2)
			z = json.loads(r1.content)
			#if str(i['user_name']) == 'bhanuprakash9666@msitprogram.net':
				#print(i)
			#print(str(c)+"|"+ course[c]+"|"+ str(i['user_id'])+"|"+ i['user_name']+"|"+ str(i['assignment_id'])+"|"+z['name']+"|"+ i['submitted_at']+"|"+ str(i['score']))
			if i['score'] == 10:
				k = str(i['submitted_at'])
				ls = k.replace("-"," ")
				ls = ls.replace("T", " ")
				ls = ls.replace(":", " ")
				ls = ls.replace("Z", " ")
				lis = ls.split()
				test_list = [int(i) for i in lis]
				open_date = date(course[c])
				#print(course[c])
				#print(open_date)
				time_in_minutes = total_time(open_date, test_list)
				#print(open_date)
				#print(test_list)
				#print(str(i['user_id'])+str(i['assignment_id'])+ time_in_minutes)
				# print()
				user_id.append(str(i['user_id']))
				ass_id.append(str(i['assignment_id']))
				time.append(time_in_minutes)




		l += 1
		
# sheet

# df = pd.DataFrame({"userId":user_id,"AssignementId":ass_id,"Time":time})

# df.to_excel('Times123.xlsx')

#print(df)
	



# URL = "https://msit.getlearning.app//api/v1/courses/71/assignments/87?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0"
# r = requests.get(url = URL)
# j = json.loads(r.content)
# print(j.keys())
# print(j["name"])
# # print(j[0].values())
#or i['score'] == 8 or i['score'] == 9