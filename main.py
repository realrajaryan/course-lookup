import pandas as pd
import json, os, sys, re

pd.set_option("display.max_rows", None, "display.max_columns", None)

course_grades_dict = json.load(open(os.path.join("data", "course_grades_final.json")))
df = pd.read_csv(os.path.join("data", "aefis_courses_with_grades.csv"))

def sub_lookup(subject):
    global df
    sub_df = df.loc[(df["Subject Code"] == subject), ["Subject Code","Course Number","Name",
                                                      "Cumulative GPA"]].sort_values('Cumulative GPA', ascending=False)

    sub_df['Subject Code'] = sub_df['Subject Code'] + " " + sub_df['Course Number'].astype(str)
    sub_df.rename(columns = {'Subject Code': 'Course'}, inplace=True)
    sub_df.drop(['Course Number', 'Name'],inplace=True, axis=1)
    sub_df.reset_index(drop=True, inplace=True)

    return sub_df

def course_lookup(course):
    global df
    course_number = int(re.search(r'\d+', course).group())
    course_code = course.replace(str(course_number), "").strip()
    course_df = df.loc[((df["Subject Code"] == course_code) & (df["Course Number"] == course_number))]

    course_info_dict = {"Course": course_df.iloc[0]["Subject Code"]+ " " + course_df.iloc[0]['Course Number'].astype(str),
                        "Name": course_df.iloc[0]["Name"], "Department": course_df.iloc[0]["Dept Description"],
                        "Cumulative GPA": course_df.iloc[0]["Cumulative GPA"], "Description": course_df.iloc[0]["Description"]}

    return course_info_dict

def view_all():
    global df
    sub_df = df.sort_values('Cumulative GPA', ascending=False)
    sub_df['Subject Code'] = sub_df['Subject Code'] + " " + sub_df['Course Number'].astype(str)
    sub_df.rename(columns = {'Subject Code': 'Course'}, inplace=True)
    sub_df.drop(['Course Number', 'Name', 'Description', 'Dept Code', 'Dept Description', 'Unnamed: 0'],inplace=True, axis=1)
    sub_df.reset_index(drop=True, inplace=True)
    
    return sub_df

def subject_codes():
    sub_df = df[['Subject Code', 'Dept Description']]
    sub_df.drop_duplicates(subset ="Subject Code", keep = 'first', inplace = True)
    sub_df.reset_index(drop=True, inplace=True)
    
    return sub_df

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <COMMAND> Try 'main.py info' for a list of available commands.")

    elif (sys.argv[1] == "info"):
        print("view_all: main.py view_all")
        print("view_all: main.py subject_codes")
        print("subject_lookup: main.py subject_lookup \"<SUBJECT>\" i.e. main.py subject_lookup \"COMP SCI\"")
        print("course_lookup: main.py course_lookup \"<COURSE>\" i.e. main.py course_lookup \"COMP SCI 300\"")
           
    elif (sys.argv[1] == "view_all"):
        print(view_all())
        
    elif (sys.argv[1] == "subject_codes"):
        print(subject_codes())

    elif (sys.argv[1] == "subject_lookup"):
        if(sys.argv[2] in list(df['Subject Code'])):
            print(sub_lookup(sys.argv[2]))
        else:
            print("Usage: main.py subject_lookup \"<SUBJECT>\" i.e. main.py subject_lookup \"COMP SCI\"")

    elif (sys.argv[1] == "course_lookup"):
        course = sys.argv[2]
        course_info = course_lookup(course)
        for info in course_info:
            print(info + ": "+ str(course_info[info]) +"\n")

    else:
        print("Unknown command: " + sys.argv[1])

if __name__ == '__main__':
     main()
