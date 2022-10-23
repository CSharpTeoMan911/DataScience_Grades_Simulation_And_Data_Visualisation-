import sys
import pandas as pd
import random as rd
import matplotlib.pyplot as mt

subjects = ["C#", "Java", "Python", "MySql", "C++", "XAML"]


def math_plot_lib_year_grade_analiser(year1, year2, year3, year4):
    try:

        selected_year = input("Select the academic year: ")

        if selected_year == "1":

            mt.bar(subjects, year1)
            mt.show()

        elif selected_year == "2":

            mt.bar(subjects, year2)
            mt.show()

        elif selected_year == "3":

            mt.bar(subjects, year3)
            mt.show()

        elif selected_year == "4":

            mt.bar(subjects, year4)
            mt.show()


        else:
            print("[! ! ! ] WRONG INPUT [! ! !]")

        selected_operation = input("\n\nEnter [ SELECT ] to select another year or anything else to exit: ")

        if selected_operation == "SELECT":
            math_plot_lib_year_grade_analiser(year1, year2, year3, year4)

        else:
            sys.exit(0)

    except KeyboardInterrupt:
        sys.exit(0)


def pandas_grades_data_frame_generator(subjects_grades):
    try:
        year_indexes = []

        for index in range(0, 4, 1):
            year_indexes.append("Year " + str(index + 1) + ": ")

        data_frame = pd.DataFrame(subjects_grades, index=year_indexes)

        math_plot_lib_year_grade_analiser(data_frame.loc[data_frame.index[0]], data_frame.loc[data_frame.index[1]],
                                          data_frame.loc[data_frame.index[2]], data_frame.loc[data_frame.index[3]])

    except KeyboardInterrupt:
        sys.exit(0)


def generate_subject_grades(grades):
    try:
        subjects_grades = {}

        for index in range(0, len(subjects)):
            subjects_grades[subjects[index]] = grades[index]

        print(subjects_grades)
        return subjects_grades

    except KeyboardInterrupt:
        sys.exit(0)


def generate_grades():
    try:
        grades = []

        for x in range(0, 6):
            subject_grades = []

            subject_grades.append(rd.randint(0, 100))
            subject_grades.append(rd.randint(0, 100))
            subject_grades.append(rd.randint(0, 100))
            subject_grades.append(rd.randint(0, 100))

            grades.append(subject_grades)

        return grades

    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    try:
        pandas_grades_data_frame_generator(generate_subject_grades(generate_grades()))
    except KeyboardInterrupt:
        sys.exit(0)
