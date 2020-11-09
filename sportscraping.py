import requests
from bs4 import BeautifulSoup
from csv import writer
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
#imports needed for program to operate


table = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2020_leaders.html")
response = requests.get("https://www.basketball-reference.com/leagues/NBA_2020_leaders.html")
#extracts/scrapes from this website


soup = BeautifulSoup(response.text, 'html.parser')

PPG = soup.find_all(id="leaders_pts_per_g")

RPG = soup.find_all(id="leaders_trb_per_g")

APG = soup.find_all(id="leaders_ast_per_g")

PER = soup.find_all(id="leaders_per")

#uses these 4 methods in the HTML code to find the statistical categories.

print(" ")

statInput = input("Which statistical category would you want a graph of? (Choose from (PPG, RPG, APG, or PER) ")
statInput = statInput.upper()
#prompts user with this question and makes it not case-sensitive.

data = []


if "PPG" in statInput:
    for PPGs in PPG:
        PPGtable = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2020_leaders.html",match = "Points Per Game")
        readPPG = PPGtable[0].to_csv("PPGtable.csv",header=["Rank", "Name", "PPG"], index = False)
        PPGread = pd.read_csv("PPGtable.csv")
        PPGread = PPGread.rename(columns =  { "Name " : "Name"})
        PPGread = PPGread.rename(columns =  { "PPG " : "PPG"})
        PPGread = PPGread.sort_values('PPG', ascending=True)
        plt.title("Top PPGs in the League")
        x = PPGread['Name']
        y = PPGread.PPG
        plt.xlabel("PPG")

elif "RPG" in statInput:  
    for RPGs in RPG:
        RPGtable = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2020_leaders.html",match = "Rebounds Per Game")
        readRPG = RPGtable[0].to_csv("RPGtable.csv",header=["Rank", "Name", "RPG"], index = False, encoding = "utf-8")
        RPGread = pd.read_csv("RPGtable.csv")
        RPGread = RPGread.rename(columns =  { "Name " : "Name"})
        RPGread = RPGread.rename(columns =  { "RPG " : "RPG"})
        RPGread = RPGread.sort_values('RPG', ascending=True)
        plt.title("Top RPG in the League")
        x = RPGread['Name']
        y = RPGread.RPG
        plt.xlabel("RPG")

elif "APG" in statInput:
    for APGs in APG:
        APGtable = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2020_leaders.html",match = "Assists Per Game")
        readAPG = APGtable[0].to_csv("APGtable.csv",header=["Rank", "Name", "APG"], index = False, encoding = "utf-8")
        APGread = pd.read_csv("APGtable.csv")
        APGread = APGread.rename(columns =  { "Name " : "Name"})
        APGread = APGread.rename(columns =  { "APG " : "APG"})
        APGread = APGread.sort_values('APG', ascending=True)
        plt.title("Top APGs in the League")
        x = APGread['Name']
        y = APGread.APG
        plt.xlabel("APG")

elif "PER" in statInput:
    for PERs in PER:
        PERtable = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2020_leaders.html",match = "Player Efficiency Rating")
        readPER = PERtable[0].to_csv("PERtable.csv",header=["Rank", "Name", "PER"], index = False, encoding = "utf-8")
        PERread = pd.read_csv("PERtable.csv")
        PERread = PERread.rename(columns =  { "Name " : "Name"})
        PERread = PERread.rename(columns =  { "PER" : "PER"})
        PERread = PERread.sort_values('PER', ascending=True)
        plt.title("Top PERs in the League")
        x = PERread['Name']
        y = PERread.PER
        plt.xlabel("PER")

else: 
    print("you didn't enter PPG, APG, RPG, or PPG! Try again!")
  

plt.barh(x,y, height=0.7, color=(0.2, 0.1, 0.6, 0.6))
for i, v in enumerate(y):
    plt.text(v, i, " "+str(v), color='black', va='center')
    plt.subplots_adjust(left=0.50,bottom=0.10,right=0.95,top=0.95)
plt.show()
