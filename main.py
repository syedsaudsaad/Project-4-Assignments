## assignment 1 to 6
## Build a Python Website in 15 Minutes With Streamlit project 9

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="student Data Generator", layout="wide")
st.title("Student CSV File Generator")

names = ["Ali","Syed","Saud","Saad","Arman","Hussain","Hassan","Taha","Talha","Dawood","Tariq","Bilal","Usman","Fasial","Osman"]
student = []
for i in range(1,16):
    students = {
        "ID": i,
        "Name":random.choice(names),
        "Age":random.randint(18, 25),
         "Grade":random.choice(["A","B","C","D","E","F"]),
         "Marks":random.randint(40,100)
    }
    student.append(student)

df = pd.DataFrame(student)
st.subheader("Generator Student Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")
st.success("Student Record Genrated Successfully!")
