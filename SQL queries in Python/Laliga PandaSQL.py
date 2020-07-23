import pandas as pd
import pandasql as pdsql



df=pd.read_csv("Laliga.csv")

headersdf=list(df.columns.values)

data=df[["Team","Position","Shirt number","Name","Passes","Yellow Cards","Red Cards","Goals scored","Penalties scored",
         "Successful tackles","Shots","Shots on target","Goals scored per attempt","Assists","Games played","Minutes played"]]

data.columns=["Team", "Position", "Shirt_number", "Name", "Passes", "Yellow_Cards", "Red_Cards", "Goals_scored",
              "Penalties_scored", "Successful_tackles", "Shots", "Shots_on_target", "Goals_scored_per_attempt",
              "Assists", "Games_played", "Minutes_played"]


data.set_index("Name",inplace=True)


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def sql_df(query):
    return pdsql.sqldf(query,globals())


q1="""Select Name, Team, Shirt_number from data order by Position limit 100"""


q3="""SELECT Team, sum(Goals_scored) as Team_Goals from data 
                               group by Team 
                               order by Team_Goals desc
                               """

q5="""SELECT Name, Team, Yellow_Cards as Yellow from data 
                        order by Yellow desc limit 5"""


q6="""SELECT Name, Team, Red_Cards as RED from data 
                        order by RED desc limit 10"""


q7="""SELECT Team, avg(Goals_scored) as Avereage_goals_by_team from data 
                        group by Team
                        order by Avereage_goals_by_team desc"""


q8="""SELECT Position, Team, avg(Goals_scored) as Average_Goals_per_Position from data 
                                    where Position!='Goalkeeper'
                                    group by Position, Team
                                    order by Team,Average_Goals_per_Position desc
                                    """


q11="SELECT Name, Shirt_number, Team from data where Shirt_number IS NULL"


def queries():
    print("1-Test query")
    print("2-Let you pick position and check who scored greater equal goals")
    print("3-Sum of goals scored by every team in La liga descending")
    print("4-Shows goals scored by each individual in a team descending")
    print("5-Shows who had the most yellow cards in given season descending limit 5")
    print("6-Shows who had the most red cards in given season descending limit 10")
    print("7-Shows average of goals scored by team, which is goals per team divided by numbers of players in team")
    print("8-Groups teams and positions and provides average of goals on each position in each team ,gk not included")
    print("9-Alteration of query above where you can pick one team")
    print("10-Groups teams and positions and provides most goals scored by player "
          "on each position in given team, gk not included")
    print("11-Prints players with no shirt number")
    print("'end' or random string - ends program")
    choice1=input("Choose query:\n")
    if choice1=="1":
        print("1-Test query")
        print(sql_df(q1))
        input("Press Enter to continue...")
        queries()


    elif choice1=="2":
        print("2-Let you pick position and check who scored greater equal goals")
        print(f"Positions: {data['Position'].unique()[1:]}")
        position_q2 = input("Input position:\n")
        goals_scored_q2 = input("How many goals?\n")
        q2 = "SELECT Name, Team ,Position, Goals_scored as Goals from data " \
                                "where Position='" + position_q2 + "'" \
                                "and Goals_scored >=" + goals_scored_q2 + " " \
                                "order by Goals desc"
        print(sql_df(q2))
        input("Press Enter to continue...")
        queries()


    elif choice1=="3":
        print("3-Sum of goals scored by every team in La liga descending")
        print(sql_df(q3))
        input("Press Enter to continue...")
        queries()


    elif choice1=="4":
        print("4-Shows goals scored by each individual in a team descending")
        print(f"Teams: {data['Team'].unique()}")
        team_q4 = input("Input Team name:\n")
        q4 = "SELECT Name, Position, Goals_scored as Goals from data" \
                                        " where Team='" + team_q4 + "' " \
                                        "order by Goals desc"
        print(sql_df(q4))
        input("Press Enter to continue...")
        queries()


    elif choice1=="5":
        print("5-Shows who had the most yellow cards in given season descending limit 5")
        print(sql_df(q5))
        input("Press Enter to continue...")
        queries()


    elif choice1=="6":
        print("6-Shows who had the most red cards in given season descending limit 10")
        print(sql_df(q6))
        input("Press Enter to continue...")
        queries()


    elif choice1=="7":
        print("7-Shows average of goals scored by team, which is goals per team divided by numbers of players in team")
        print(sql_df(q7))
        input("Press Enter to continue...")
        queries()


    elif choice1=="8":
        print(
            "8-Groups teams and positions and provides average of goals on each position in each team ,gk not included")
        print(sql_df(q8))
        input("Press Enter to continue...")
        queries()


    elif choice1=="9":
        print("9-Alteration of query above where you can pick one team")
        print(f"Teams: {data['Team'].unique()}")
        team_q9 = input("Input Team name:\n")
        q9 = "SELECT Position, Team, avg(Goals_scored) as Average_Goals_per_Position from data " \
             "where Team='" + team_q9 + "' and Position!='Goalkeeper'" \
                                        "group by Position " \
                                        "order by Average_Goals_per_Position desc"
        print(sql_df(q9))
        input("Press Enter to continue...")
        queries()


    elif choice1=="10":
        print("10-Groups teams and positions and provides most goals scored by player "
              "on each position in given team, gk not included")
        print(f"Teams: {data['Team'].unique()}")
        team_q10 = input("Input Team name:\n")
        q10 = "SELECT Name, Position, Team, max(Goals_scored) as Most_Goals_per_Position from data " \
              "where Team='" + team_q10 + "' and Position!='Goalkeeper' " \
                                          "group by Position " \
                                          "order by Most_Goals_per_Position desc"
        print(sql_df(q10))
        input("Press Enter to continue...")
        queries()


    elif choice1=="11":
        print("11-Prints players with no shirt number")
        print(sql_df(q11))
        input("Press Enter to continue...")
        queries()


    else:
        print("Done")

queries()



