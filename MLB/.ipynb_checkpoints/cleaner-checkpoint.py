import os
import pandas as pd
import re 
from openpyxl import load_workbook

os.chdir(r"C:\Users\Kyle\Documents\project_ETL")

xlsx = pd.ExcelFile(r"mlb2019-2010_dirty_v01x.xlsx")

regex = re.compile(r"(.*)(\()(\d{4})(-?)(.*)")

signed_list = [0]

length_list = [0]

names_list = []

for index, sheet in enumerate(xlsx.sheet_names):
    if sheet.endswith("_salaries"):
        df = pd.read_excel(xlsx, sheet, index_col=0)
        singed_list = [0]
        length_list = [0]
        if len(signed_list) > 2:
            signed_list = [0]
        for i, row in df.iterrows():
            names_list.append(row["NAME"])
            string = row["YEARS"]
            length = regex.search(string).group(1).strip()
            yearSigned = regex.search(string).group(3)
            length_list.append(length)
            signed_list.append(yearSigned)
        new_df = df.join(pd.DataFrame.from_dict({"YearSigned": signed_list,
                                                 "ContractLength": length_list}))
        if index == 0:
            writer = pd.ExcelWriter(r"test.xlsx", engine="openpyxl")
            #wb = writer.book
            #new_df.to_excel(writer, sheet_name = ("x" + str(index)))
            new_df.to_excel(writer, sheet_name = (str(sheet)[:4]))
            writer.save()
            writer.close()
        else:
            book = load_workbook("test.xlsx")
            writer = pd.ExcelWriter(r"test.xlsx", engine="openpyxl")
            writer.book = book
            
            new_df.to_excel(writer, sheet_name = (str(sheet)[:4]))
            writer.save()
            writer.close()
    else:
        next

unique_names_df = pd.DataFrame.from_dict({"Names": names_list})
#print(unique_names_df.Names.count())
#unique_names_df = unique_names_df.drop_duplicates()
#print(unique_names_df.Names.count())

with open("highest_payed_players_this_decade.txt", 'w', newline='\n') as resultFile:
    resultFile.write(str(unique_names_df.Names.count()) + " \n")
    resultFile.write(str(unique_names_df.Names.value_counts())+ " \n")
    unique_names_df = unique_names_df.drop_duplicates()
    resultFile.write(str(unique_names_df.Names.value_counts())+ " \n")
    series = unique_names_df.Names.value_counts()
    for name, value in series.iteritems():
        resultFile.write(name + "\n")
    resultFile.close()



xlsx.close()

