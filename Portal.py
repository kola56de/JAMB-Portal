import streamlit as st
import sqlite3
import pandas as pd

# DATABASE CONNECTION
mydatabase = sqlite3.connect("students.db", check_same_thread=False)
mycursor = mydatabase.cursor()

# CREATE TABLE
mycursor.execute("""
CREATE TABLE IF NOT EXISTS informations (
    reg_no INTEGER PRIMARY KEY,
    full_name TEXT,
    gender TEXT,
    state TEXT,
    email TEXT
)
""")

mydatabase.commit()


# REGISTER FUNCTION
def register():
    st.subheader("Register New Student")

    reg_no = st.number_input("Enter Registration Number:", min_value=1)
    full_name = st.text_input("Enter Full Name:")
    gender = st.selectbox("Select Gender:", ["Male", "Female"])
    state = st.text_input("Enter State of Origin:")
    email = st.text_input("Enter Email Address:")

    if st.button("Register"):

        if full_name and state and email:

            query = """
            INSERT INTO informations
            (reg_no, full_name, gender, state, email)
            VALUES (?, ?, ?, ?, ?)
            """

            values = (reg_no, full_name, gender, state, email)

            try:
                mycursor.execute(query, values)
                mydatabase.commit()
                st.success("Information successfully uploaded!")

            except sqlite3.IntegrityError:
                st.error("Registration number already exists.")

        else:
            st.error("Please fill in all fields.")


# SEARCH FUNCTION
def search():

    st.subheader("Search Student Record")

    reg_no = st.number_input(
        "Enter Registration Number to Search:",
        min_value=1
    )

    if st.button("Search"):

        query = "SELECT * FROM informations WHERE reg_no = ?"

        mycursor.execute(query, (reg_no,))

        result = mycursor.fetchall()

        if len(result) == 0:
            st.warning("Record not found.")

        else:
            df = pd.DataFrame(
                result,
                columns=[
                    "Reg No",
                    "Full Name",
                    "Gender",
                    "State",
                    "Email"
                ]
            )

            st.table(df)


# UPDATE FUNCTION
def update():

    st.subheader("Update Student Record")

    reg_no = st.number_input(
        "Enter Registration Number:",
        min_value=1
    )

    full_name = st.text_input("Enter Full Name:")
    gender = st.selectbox("Select Gender:", ["Male", "Female"])
    state = st.text_input("Enter State of Origin:")
    email = st.text_input("Enter Email Address:")

    if st.button("Update"):

        query = """
        UPDATE informations
        SET full_name = ?,
            gender = ?,
            state = ?,
            email = ?
        WHERE reg_no = ?
        """

        values = (
            full_name,
            gender,
            state,
            email,
            reg_no
        )

        mycursor.execute(query, values)
        mydatabase.commit()

        if mycursor.rowcount > 0:
            st.success("Record updated successfully!")
        else:
            st.warning("No record found with that registration number.")


# DELETE FUNCTION
def delete():

    st.subheader("Delete Student Record")

    reg_no = st.number_input(
        "Enter Registration Number to Delete:",
        min_value=1
    )

    if st.button("Delete"):

        query = "DELETE FROM informations WHERE reg_no = ?"

        mycursor.execute(query, (reg_no,))
        mydatabase.commit()

        if mycursor.rowcount > 0:
            st.success("Record deleted successfully!")
        else:
            st.warning("No record found with that registration number.")


# DISPLAY FUNCTION
def display():

    st.subheader("All Registered Students")

    query = "SELECT * FROM informations"

    mycursor.execute(query)

    result = mycursor.fetchall()

    if result:

        df = pd.DataFrame(
            result,
            columns=[
                "Reg No",
                "Full Name",
                "Gender",
                "State",
                "Email"
            ]
        )

        st.dataframe(df)

    else:
        st.info("No records found yet.")


# LOGOUT FUNCTION
def logout():
    st.info("You have logged out successfully.")


# MAIN APP
st.title("JAMB Student Portal")

menu = [
    "Register",
    "Search",
    "Update",
    "Delete",
    "Display All",
    "Logout"
]

choice = st.sidebar.selectbox(
    "Choose an Option",
    menu
)

if choice == "Register":
    register()

elif choice == "Search":
    search()

elif choice == "Update":
    update()

elif choice == "Delete":
    delete()

elif choice == "Display All":
    display()

elif choice == "Logout":
    logout()
