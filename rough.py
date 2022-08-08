from datetime import datetime
import requests, json
import pandas as pd

# Courses id and their names
courses = {
    71:"Programming Basics - 1", 
    72:"Programming Basics - 2", 
    73:"Programming Basics - 3", 
    74:"Programming Basics - 4",
    75:"Programming Basics - 5"
    }  
# Student's Data object
Student_info={
    "User_id":[],
    "User_name":[],
    "Assignment_id":[],
    "Assignment_Name":[],
    "Submitted_at":[],
    "Created_at":[],
    "Time_consumed":[]
}

# Extrcting  data from APIS and storing it in the Student_info object.

for course in courses:
    page=1
    while True:
        # Extracting all the data from the url and storing in the URL variable
        Course_url = "https://msit.getlearning.app/api/v1/courses/"+str(course)+"/gradebook_history/feed?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0&page="+str(page)
        
        # Converting the data to json using python json module
        data= requests.get(Course_url) 
        
        # pasrsing whole data to json readable format
        Course_json_data= json.loads(data.content)
        # print(Course_json_data)

        # Adding all the required data to the object
        if len(Course_json_data)==0:
            break
        
        for i in Course_json_data:
            Assigment_url = f"https://msit.getlearning.app//api/v1/courses/{course}/assignments/{i['assignment_id']}?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0"
            
            # Extracting the data from the url
            Assigment_data=requests.get(Assigment_url)
            
            # parsing the data from the Assigment_data
            Assigment_json_data= json.loads(Assigment_data.content)
            
            # Now we need to track the student's assignments

            # Adding user_id to student_info
            Student_info["User_id"].append(i["user_id"])

            # Adding User_name
            Student_info["User_name"].append(i["user_name"])

            # Adding Assignent_name
            Student_info["Assignment_id"].append(Assigment_json_data["course_id"])

            # Adding assignment_name
            Student_info["Assignment_Name"].append(i["assignment_name"])

            # Adding submitted_at to the object
            Student_info["Submitted_at"].append(i["submitted_at"])

            # Adding created_at to the object
            Student_info["Created_at"].append(Assigment_json_data["created_at"])

            # getting the time consumed by the student and adding it to the object
            Assigment_created=Assigment_json_data['updated_at']
            created_date = datetime.fromisoformat(f"{Assigment_created[:-1]}+00:00")
            
            #parsing the submited date to iso. SO that we can easily caluclate the time consumed by the student 
            Assigment_submitted= i['submitted_at']
            submitted_date = datetime.fromisoformat(f"{Assigment_submitted[:-1]}+00:00")

            # getting the time consumed by the student
            Time_consumed= submitted_date-created_date
           

            # Adding the Time_consumed to the object
            Student_info["Time_consumed"].append(Time_consumed)


        page+=1

# Now we are creating an excel sheet to add all the data to the worksheet

# creating data_frame and writing all the data to the workseet

df = pd.DataFrame({
    "user_id":Student_info["User_id"],
    "user_name":Student_info["User_name"],
    "Assigment_id":Student_info["Assignment_id"],
    "Assignment_name":Student_info["Assignment_Name"],
    "Created_at":Student_info["Created_at"],
    "Time_consumed":Student_info["Time_consumed"]

})

# Saving the file with MyConsolidateWork.xlsx
df.to_excel('MyConsolidateWork.csv')