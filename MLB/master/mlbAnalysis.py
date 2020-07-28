#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


team_salary_df = pd.read_excel("TeamSalaries.xlsx")


# In[3]:


team_salary_df.head()


# In[6]:


team_salary_df["Team Name"].value_counts()


# In[47]:


for i, row in team_salary_df.iterrows():
    y = str(row["Team Name"])
    if y.endswith("Marlins"):
        y = "Miami Marlins"
    elif y.endswith("Diamondbacks"):
        y = "Arizona Diamondbacks"
    else:
        y = y.lstrip()
    team_salary_df.loc[i, "Team Name"] = y


# In[50]:


team_salary_df["Team Name"].value_counts()


# In[59]:


team_salary_df[team_salary_df["Team Name"] == "Miami Marlins"]


# In[62]:


bat_19_df = pd.read_excel("mlbHitters.xlsx", 0, 0, index_col="Rk")
bat_19_df.head(20)


# In[64]:


bat_18_df = pd.read_excel("mlbHitters.xlsx", 1, 0, index_col="Rk")
bat_17_df = pd.read_excel("mlbHitters.xlsx", 2, 0, index_col="Rk")
bat_16_df = pd.read_excel("mlbHitters.xlsx", 3, 0, index_col="Rk")
bat_15_df = pd.read_excel("mlbHitters.xlsx", 4, 0, index_col="Rk")
bat_14_df = pd.read_excel("mlbHitters.xlsx", 5, 0, index_col="Rk")
bat_13_df = pd.read_excel("mlbHitters.xlsx", 6, 0, index_col="Rk")
bat_12_df = pd.read_excel("mlbHitters.xlsx", 7, 0, index_col="Rk")
bat_11_df = pd.read_excel("mlbHitters.xlsx", 8, 0, index_col="Rk")
bat_10_df = pd.read_excel("mlbHitters.xlsx", 9, 0, index_col="Rk")


# In[66]:


bat_19_df_v = pd.read_excel("mlbHitters.xlsx", 10, 0, index_col="Rk")
bat_18_df_v = pd.read_excel("mlbHitters.xlsx", 11, 0, index_col="Rk")
bat_17_df_v = pd.read_excel("mlbHitters.xlsx", 12, 0, index_col="Rk")
bat_16_df_v = pd.read_excel("mlbHitters.xlsx", 13, 0, index_col="Rk")
bat_15_df_v = pd.read_excel("mlbHitters.xlsx", 14, 0, index_col="Rk")
bat_14_df_v = pd.read_excel("mlbHitters.xlsx", 15, 0, index_col="Rk")
bat_13_df_v = pd.read_excel("mlbHitters.xlsx", 16, 0, index_col="Rk")
bat_12_df_v = pd.read_excel("mlbHitters.xlsx", 17, 0, index_col="Rk")
bat_11_df_v = pd.read_excel("mlbHitters.xlsx", 18, 0, index_col="Rk")
bat_10_df_v = pd.read_excel("mlbHitters.xlsx", 19, 0, index_col="Rk")


# In[67]:


bat_10_df_v.head()


# In[68]:


pitch_19_df = pd.read_excel("mlbPitchers.xlsx", 0, 0, index_col="Rk")
pitch_18_df = pd.read_excel("mlbPitchers.xlsx", 1, 0, index_col="Rk")
pitch_17_df = pd.read_excel("mlbPitchers.xlsx", 2, 0, index_col="Rk")
pitch_16_df = pd.read_excel("mlbPitchers.xlsx", 3, 0, index_col="Rk")
pitch_15_df = pd.read_excel("mlbPitchers.xlsx", 4, 0, index_col="Rk")
pitch_14_df = pd.read_excel("mlbPitchers.xlsx", 5, 0, index_col="Rk")
pitch_13_df = pd.read_excel("mlbPitchers.xlsx", 6, 0, index_col="Rk")
pitch_12_df = pd.read_excel("mlbPitchers.xlsx", 7, 0, index_col="Rk")
pitch_11_df = pd.read_excel("mlbPitchers.xlsx", 8, 0, index_col="Rk")
pitch_10_df = pd.read_excel("mlbPitchers.xlsx", 9, 0, index_col="Rk")


# In[69]:


pitch_19_df_v = pd.read_excel("mlbPitchers.xlsx", 10, 0, index_col="Rk")
pitch_18_df_v = pd.read_excel("mlbPitchers.xlsx", 11, 0, index_col="Rk")
pitch_17_df_v = pd.read_excel("mlbPitchers.xlsx", 12, 0, index_col="Rk")
pitch_16_df_v = pd.read_excel("mlbPitchers.xlsx", 13, 0, index_col="Rk")
pitch_15_df_v = pd.read_excel("mlbPitchers.xlsx", 14, 0, index_col="Rk")
pitch_14_df_v = pd.read_excel("mlbPitchers.xlsx", 15, 0, index_col="Rk")
pitch_13_df_v = pd.read_excel("mlbPitchers.xlsx", 16, 0, index_col="Rk")
pitch_12_df_v = pd.read_excel("mlbPitchers.xlsx", 17, 0, index_col="Rk")
pitch_11_df_v = pd.read_excel("mlbPitchers.xlsx", 18, 0, index_col="Rk")
pitch_10_df_v = pd.read_excel("mlbPitchers.xlsx", 19, 0, index_col="Rk")


# In[257]:


pitch_14_df_v.head()


# In[74]:


hitters_regular = [bat_19_df, bat_18_df, bat_17_df, bat_16_df, bat_15_df, bat_14_df, bat_13_df, bat_12_df, bat_11_df, bat_10_df]
hitters_value = [bat_19_df_v, bat_18_df_v, bat_17_df_v, bat_16_df_v, bat_15_df_v, bat_14_df_v, bat_13_df_v, bat_12_df_v, bat_11_df_v, bat_10_df_v]
pitchers_regular = [pitch_19_df, pitch_18_df, pitch_17_df, pitch_16_df, pitch_15_df, pitch_14_df, pitch_13_df, pitch_12_df, pitch_11_df, pitch_10_df]
pitchers_value = [pitch_19_df_v, pitch_18_df_v, pitch_17_df_v, pitch_16_df_v, pitch_15_df_v, pitch_14_df_v, pitch_13_df_v, pitch_12_df_v, pitch_11_df_v, pitch_10_df_v]


# In[176]:


years = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]


# In[193]:


for tup in zip(years, hitters_regular, hitters_value):
    for item in tup:
        if type(item) == int:
            year = item
            next
        else:
            for i, row in item.iterrows():
                name = row["Name"]
                name = name.strip()
                if "*" in name or "#" in name:
                    name = name[:-1]
                item.loc[i, "Name"] = name
                item.loc[i, "Year"] = year


# In[200]:


for tup in zip(years, pitchers_regular, pitchers_value):
    for item in tup:
        if type(item) == int:
            year = item
            next
        else:
            for i, row in item.iterrows():
                name = str(row["Name"])
                name = name.strip()
                if "*" in name or "#" in name:
                    name = name[:-1]
                item.loc[i, "Name"] = name
                item.loc[i, "Year"] = year


# In[202]:


pitch_16_df.head()


# In[237]:


for tup in zip(hitters_full, hitters_regular, hitters_value):
    df_main = tup[1]
    df_v = tup[2]
    df_full = tup[0]
    df_full = df_main.merge(df_v, on="Name", how="inner", suffixes=("_reg","_v"))
    df_full.head()


# In[238]:


pitchers_19 = pitch_19_df.merge(pitch_19_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_18 = pitch_18_df.merge(pitch_18_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_17 = pitch_17_df.merge(pitch_17_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_16 = pitch_16_df.merge(pitch_16_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_15 = pitch_15_df.merge(pitch_15_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_14 = pitch_14_df.merge(pitch_14_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_13 = pitch_13_df.merge(pitch_13_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_12 = pitch_12_df.merge(pitch_12_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_11 = pitch_11_df.merge(pitch_11_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
pitchers_10 = pitch_10_df.merge(pitch_10_df_v, on="Name", how="inner", suffixes=("_reg","_v"))


# In[239]:


batters_19 = bat_19_df.merge(bat_19_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_18 = bat_18_df.merge(bat_18_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_17 = bat_17_df.merge(bat_17_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_16 = bat_16_df.merge(bat_16_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_15 = bat_15_df.merge(bat_15_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_14 = bat_14_df.merge(bat_14_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_13 = bat_13_df.merge(bat_13_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_12 = bat_12_df.merge(bat_12_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_11 = bat_11_df.merge(bat_11_df_v, on="Name", how="inner", suffixes=("_reg","_v"))
batters_10 = bat_10_df.merge(bat_10_df_v, on="Name", how="inner", suffixes=("_reg","_v"))


# In[241]:


batters_10.tail(10)


# In[245]:


top_50Players_2019_df = pd.read_excel("mlb_cleanest_4.xlsx", 4, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2018_df = pd.read_excel("mlb_cleanest_4.xlsx", 5, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2017_df = pd.read_excel("mlb_cleanest_4.xlsx", 6, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2016_df = pd.read_excel("mlb_cleanest_4.xlsx", 7, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2015_df = pd.read_excel("mlb_cleanest_4.xlsx", 8, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2014_df = pd.read_excel("mlb_cleanest_4.xlsx", 9, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2013_df = pd.read_excel("mlb_cleanest_4.xlsx", 10, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2012_df = pd.read_excel("mlb_cleanest_4.xlsx", 11, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2011_df = pd.read_excel("mlb_cleanest_4.xlsx", 12, skiprows=[0, 1, 2], index_col="RANK")
top_50Players_2010_df = pd.read_excel("mlb_cleanest_4.xlsx", 13, skiprows=[0, 1, 2], index_col="RANK")


# In[255]:


pitcher_stats_precontract = pd.read_excel("mlb_cleanest_4.xlsx", 3).drop(['Unnamed: 0'], axis=1)
batter_stats_precontract = pd.read_excel("mlb_cleanest_4.xlsx", 2).drop(['Unnamed: 0'], axis=1)


# In[256]:


pitcher_stats_precontract.head()


# In[258]:


master_pitchers_all = pd.concat([pitchers_19, pitchers_18, pitchers_17, pitchers_16, pitchers_15, pitchers_14, pitchers_13, pitchers_12, pitchers_11, pitchers_10])
master_batters_all = pd.concat([batters_19, batters_18, batters_17, batters_16, batters_15, batters_14, batters_13, batters_12, batters_11, batters_10])


# In[262]:


master_pitchers_all.shape


# In[285]:


master_pitchers_all.columns


# In[263]:


master_batters_all.shape 


# In[270]:


master_batters_all.columns


# In[282]:


key_columns_bat = ["Name", "Age_reg", "Tm_reg", "G_reg", "PA_reg", "AB", "R", "H",
                  "HR", "RBI", "SO", "BA", "OBP", "SLG", "OPS", "Pos Summary_reg",
                  "Year_reg", "Rbat", "RAA", "WAA", "RAR", "WAR", "waaWL%", "162WL%",
                  "Salary", "Acquired"]


# In[283]:


master_bats = master_batters_all.loc[:, key_columns_bat]
master_bats.shape


# In[284]:


master_bats.head()


# In[286]:


key_columns_pitch = ["Name", "Age_reg", "Tm_reg", "W", "L", "W-L%", "ERA", "G_reg", "GS_reg", "GF",
                    "SV", "IP_reg", "H", "R_reg", "ER", "HR", "BB", "SO", "WHIP", "H9", "HR9", "SO9",
                    "Year_reg", "RA9", "RA9opp", "RA9_avg", "RAA", "WAA", "WAR", "RAR", "waaWL%", "162WL%",
                    "Salary", "Acquired"]


# In[287]:


master_pitch = master_pitchers_all.loc[:, key_columns_pitch]
master_pitch.shape


# In[290]:


bins = [0, 10, 25, 50]
labels = ["top 10", "11-25", "26-50"]


# In[297]:


top_50Players_2019_df.head()


# In[305]:


top_50Players_2019_df = top_50Players_2019_df.assign(bin_groups = pd.cut(top_50Players_2019_df.index, bins=bins, labels=labels))
top_50Players_2018_df = top_50Players_2018_df.assign(bin_groups = pd.cut(top_50Players_2018_df.index, bins=bins, labels=labels))
top_50Players_2017_df = top_50Players_2017_df.assign(bin_groups = pd.cut(top_50Players_2017_df.index, bins=bins, labels=labels))
top_50Players_2016_df = top_50Players_2016_df.assign(bin_groups = pd.cut(top_50Players_2016_df.index, bins=bins, labels=labels))
top_50Players_2015_df = top_50Players_2015_df.assign(bin_groups = pd.cut(top_50Players_2015_df.index, bins=bins, labels=labels))
top_50Players_2014_df = top_50Players_2014_df.assign(bin_groups = pd.cut(top_50Players_2014_df.index, bins=bins, labels=labels))
top_50Players_2013_df = top_50Players_2013_df.assign(bin_groups = pd.cut(top_50Players_2013_df.index, bins=bins, labels=labels))
top_50Players_2012_df = top_50Players_2012_df.assign(bin_groups = pd.cut(top_50Players_2012_df.index, bins=bins, labels=labels))
top_50Players_2011_df = top_50Players_2011_df.assign(bin_groups = pd.cut(top_50Players_2011_df.index, bins=bins, labels=labels))
top_50Players_2010_df = top_50Players_2010_df.assign(bin_groups = pd.cut(top_50Players_2010_df.index, bins=bins, labels=labels))


# In[313]:


top_50Players_2019_df.groupby("Pitcher?").mean()["RA9"]


# In[321]:


master_bats.describe()


# In[323]:


top_50Players_2019_df.head()


# In[330]:


top_50Players_2019_df = top_50Players_2019_df.assign(In_The_Year = 2019)
top_50Players_2018_df = top_50Players_2018_df.assign(In_The_Year = 2018)
top_50Players_2017_df = top_50Players_2017_df.assign(In_The_Year = 2017)
top_50Players_2016_df = top_50Players_2016_df.assign(In_The_Year = 2016)
top_50Players_2015_df = top_50Players_2015_df.assign(In_The_Year = 2015)
top_50Players_2014_df = top_50Players_2014_df.assign(In_The_Year = 2014)
top_50Players_2013_df = top_50Players_2013_df.assign(In_The_Year = 2013)
top_50Players_2012_df = top_50Players_2012_df.assign(In_The_Year = 2012)
top_50Players_2011_df = top_50Players_2011_df.assign(In_The_Year = 2011)
top_50Players_2010_df = top_50Players_2010_df.assign(In_The_Year = 2010)


# In[332]:


master_top50 = pd.concat([top_50Players_2019_df, top_50Players_2018_df, top_50Players_2017_df, top_50Players_2016_df,
                         top_50Players_2015_df, top_50Players_2014_df, top_50Players_2013_df, top_50Players_2012_df,
                         top_50Players_2011_df, top_50Players_2010_df])


# In[337]:


master_top50.shape


# In[368]:


working_bench_df = master_top50


# In[369]:


working_bench_df = working_bench_df.reset_index()
working_bench_df = working_bench_df.drop_duplicates("NAME")


# In[374]:


# Split Players Up by Position
fifty_pitch_df = working_bench_df[working_bench_df["Pitcher?"] == 1]
fifty_bat_df = working_bench_df[working_bench_df["Pitcher?"] == 0]


# In[381]:


bat_equivalent_cols = ["NAME", "YearSigned", "TEAM", "POS", "SALARY", "YEARS", "TOTAL VALUE", "AVG ANNUAL", "Pitcher?",
                        "ContractLength", "Year", "Age", "Tm", "G", "PA", "AB", "R", "H", "HR", "RBI", "SO", "BA", "OBP",
                        "SLG", "OPS", "Pos", "Awards", "Rbat", "RAA", "WAA", "RAR", "WAR", "waaWL%", "162WL%", "Awards.1"]


# In[382]:


pitch_equivalent_cols = ["NAME", "YearSigned", "TEAM", "POS", "SALARY", "YEARS", "TOTAL VALUE", "AVG ANNUAL", "Pitcher?",
                        "ContractLength", "Year.2", "Age.2", "Tm.2", "W", "L", "W-L%", "ERA", "G.2", "GS", "GF", "SV", "IP",
                        "H.1", "R.1", "ER", "HR.1", "BB.1", "SO.1", "WHIP", "H9", "HR9", "SO9", "RA9", "RA9opp", "RA9avg",
                        "RAA.1", "WAA.1", "waaWL%", "162WL%", "Awards.3", "bin_groups", "In_The_Year"]


# In[384]:


revised_fifty_pitch = fifty_pitch_df.loc[:, pitch_equivalent_cols]
revised_fifty_bats = fifty_bat_df.loc[:, bat_equivalent_cols]


# In[385]:


revised_fifty_bats.shape


# In[388]:


revised_fifty_pitch.shape


# In[393]:


precontract_filter_pitcher = ["Name", "YearRANGE", "Tm", "W", "L", "W-L%", "ERA", "G", "GS", "GF", "SV", "IP", "H",
                             "R", "ER", "HR", "BB", "SO", "WHIP", "H9", "HR9", "SO9", "RA9", "RA9opp", "RA9avg", "RAA", "WAA",
                             "waaWL%", "162WL%", "Salary(total)"]
precontract_filter_hitters = ["Name", "YearRANGE", "Tm", "G", "PA", "AB", "R", "H", "HR", "RBI", "SO", "BA", "OBP", "SLG",
                             "OPS", "Rbat", "RAA", "WAA", "RAR", "WAR", "waaWL%", "162WL%", "Salary(total)"]


# In[394]:


revised_precontract_range_stats_p = pitcher_stats_precontract.loc[:, precontract_filter_pitcher]
revised_precontract_range_stats_h = batter_stats_precontract.loc[:, precontract_filter_hitters]


# In[395]:


revised_fifty_bats.head()


# In[396]:


top_payed_batters_list = [x for x in revised_fifty_bats.NAME]
top_payed_pitchers_list = [x for x in revised_fifty_pitch.NAME]


# In[398]:


len(top_payed_batters_list)


# In[560]:


master_bats_clean = master_bats.sort_values("Name").reset_index()


# In[561]:


names_list = []
for index, row in master_bats_clean.iterrows():
    name = str(row["Name"])
    name = unicodedata.normalize("NFKD", name)
    names_list.append(name)


# In[562]:


import unicodedata


# In[563]:


names_series = pd.Series(names_list)


# In[564]:


master_bats_clean["Namex"] = names_series


# In[565]:


master_pitch_clean = master_pitch.sort_values("Name").reset_index()
names_list = []
for index, row in master_pitch_clean.iterrows():
    name = str(row["Name"])
    name = unicodedata.normalize("NFKD", name)
    names_list.append(name)
names_series = pd.Series(names_list)
master_pitch_clean["Namex"] = names_series


# In[566]:


master_pitch_clean.head()


# In[567]:


master_bats_clean.head()


# In[568]:


master_bats_clean.drop(["index", "Name"], axis=1, inplace=True)


# In[572]:


master_bats_clean.rename({"Namex": "Name"}, axis="columns", inplace=True)


# In[573]:


master_bats_clean.head()


# In[576]:


master_pitch_clean.rename({"Namex": "Name"}, axis="columns", inplace=True)


# In[577]:


master_pitch_clean.head()


# In[580]:


master_pitch_clean.columns


# In[583]:


revised_fifty_pitch.columns


# In[596]:


master_pitch_clean[(~master_pitch_clean["Name"].isin(top_payed_pitchers_list)) & (master_pitch_clean["Year_reg"] == 2012)].describe()


# In[598]:


master_bats_clean.columns


# In[599]:


master_bats_clean[(~master_bats_clean["Name"].isin(top_payed_batters_list)) & (master_bats_clean["Year_reg"] == 2012)].describe()


# In[605]:


master_pitch_clean_v2 = master_pitch_clean[master_pitch_clean["IP_reg"] >= 30]
master_bats_clean_v2 = master_bats_clean[master_bats_clean["AB"] >= 220]


# In[606]:


master_pitch_clean_v2.describe()


# In[607]:


revised_fifty_bats.shape


# In[611]:


master_top50.head()


# In[613]:


master_top50.groupby("In_The_Year").sum()


# In[623]:


total_team_salaries = team_salary_df[team_salary_df["Team Name"] == "TOTAL"]
highest_payed_players = master_top50.groupby("In_The_Year").sum().reset_index()


# In[ ]:





# In[634]:


fig, axes = plt.subplots(1, 2, figsize=(20, 8), sharex=True)
ax1 = axes[0]
ax2 = axes[1]
ax1.plot(total_team_salaries["Year"], total_team_salaries["Payroll"], "k")
ax1.set_title("MLB Total Team Salaries Over the 2010s")
ax1.set_xticks(np.arange(2010, 2020, 1))
ax2.plot(highest_payed_players["In_The_Year"], highest_payed_players["SALARY"], "m--")
ax2.set_title("Total Salaries of Top 50 Paid Players in MLB in the 2010s")
ax2.set_xticks(np.arange(2010, 2020, 1))


# In[ ]:




