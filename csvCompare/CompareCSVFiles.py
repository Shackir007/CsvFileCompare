# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:30:40 2020
@author: Shackir
"""

import pandas as pd


def compare_csv_files(source_file, target_file, source_join_columns, target_join_columns, source_measure_columns,
                      target_measure_columns):
    df_source = pd.read_csv(source_file, header='infer')
    df_target = pd.read_csv(target_file, header='infer')
    # df_merged = pd.merge(df_source, df_target, how='left', left_on='[left df columns]', right_on='[right df columns]')
    df_merged = pd.merge(df_source, df_target, how='left', left_on=source_join_columns, right_on=target_join_columns)
    print(df_source)
    print(df_target)
    print(df_merged)

def read_header_csv(file_name):
    is_exist = False

    try:
        file = open(file_name, "r")
        is_exist = True
        header_line = file.readline()
        header_columns = header_line.split(",")
        print("Column:" + header_columns)

        file.close()

        return header_columns
    except NameError:
        print("Invalid Name:" + file_name)
    except:
        print("Some Error:" + file_name)

    return is_exist


def is_file_exist(file_name):
    is_exist = False
    try:
        file = open(file_name, "r")
        first_line = file.readline()
        is_exist = True
        print("Header:" + first_line)
        file.close()
    except NameError:
        print("Invalid Name:" + file_name)
    except:
        print("Some Error:" + file_name)

    return is_exist


source_file = "C:/Users/user/Documents/study material/Shacki-Python/RoomDeposits.csv"
# targetFile = "C:/Users/user/Documents/study material/Shacki-Python/Room expense-2017MAR-Food.csv"
target_file = "C:/Users/user/Documents/study material/Shacki-Python/RoomDeposits.csv"

isSourceFileValid = is_file_exist(source_file)
sourceColumns = read_header_csv(source_file)

isTargetFileValid = is_file_exist(target_file)
targetColumns = read_header_csv(target_file)

compare_csv_files(source_file, target_file, ['SL#','Name','flag'], ['SL#','Name','flag'], ['Amount'], ['Amount'])

