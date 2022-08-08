import requests
from datetime import datetime
import pandas as pd

courses = {71: "Programming Basics - 1",
           72: "Programming Basics - 2",
           73: "Programming Basics - 3",
           74: "Programming Basics - 4",
           75: "Programming Basics - 5"}

courses_list = [71, 72, 73, 74, 75]

# temp database
def get_data():
    collected_data = {
        "course_id": [],
        "user_id": [],
        "user_name": [],
        "assignment_id": [],
        "assignment_name": [],
        "assignment_created_at": [],
        "assignment_updated_at": [],
        "assignment_spent_time": [],
    }

    entries = 0

    for course in courses_list:
        page_number = 1
        while True:
            course_api_url = f"https://msit.getlearning.app/api/v1/courses/{course}/gradebook_history/feed?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0&page={page_number}"
            courses_data = requests.get(course_api_url).json()
            if courses_data:
                for course_data in courses_data:
                    collected_data["course_id"].append(course)

                    user_id = course_data['user_id']
                    collected_data["user_id"].append(user_id)

                    assignment_id = course_data['assignment_id']
                    collected_data["assignment_id"].append(assignment_id)

                    user_name = course_data['user_name']
                    collected_data["user_name"].append(user_name)

                    # --> GET ASSIGNMENTS DATA <---
                    assignment_api_url = f"https://msit.getlearning.app//api/v1/courses/{course}/assignments/{assignment_id}?access_token=a9nKjKIp4ELlcLxgEtFCQgRBgg4X1DBsq1OaHQbyYsx118GRiACBOv41UYgCQak0"
                    assignment_data = requests.get(assignment_api_url).json()

                    # print(datetime.fromisoformat(assignment_data['created_at'][:-1]),"****************")
                    assignment_created_at = datetime.fromisoformat(f"{assignment_data['created_at'][:-1]}+00:00")
                    collected_data["assignment_created_at"].append(assignment_created_at)

                    assignment_updated_at = datetime.fromisoformat(f"{assignment_data['updated_at'][:-1]}+00:00")
                    collected_data["assignment_updated_at"].append(assignment_updated_at)

                    assignment_name = assignment_data['name']
                    collected_data["assignment_name"].append(assignment_name)

                    assignment_spent_time = assignment_updated_at - assignment_created_at
                    collected_data["assignment_spent_time"].append(assignment_spent_time)

                    entries += 1
                page_number += 1

            else:
                break

    # --> CREATE CSV FILE FROM COLLECTED DATA <---
    collected_data_df = pd.DataFrame()
    for column in collected_data:
        collected_data_df[column] = collected_data[column]
    collected_data_df.to_csv(f"all_courses_data1.csv", index=False)
    return


def main():
    get_data()
    pass


if __name__ == '__main__':
    main()
