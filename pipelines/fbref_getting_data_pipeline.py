import soccerdata as sd
import pandas as pd

def process_team_season_stats(fbref, stat_type):

    team_season_stats = fbref.read_team_season_stats(stat_type=stat_type)
    try:
        team_season_stats2 = team_season_stats.droplevel(0, axis=1)
        team_season_stats2.columns = [col[0] + "_" + col[1] for col in team_season_stats.columns]
    except:
        pass

    team_season_stats2 = team_season_stats2.reset_index()

    #team_season_stats2.to_csv("../data/team_season_stats_" + stat_type + ".csv", index=False)
    file_name="team_season_stats_" + stat_type + ".csv"

    original_data=pd.read_csv('abfs://fbref-data@storaccoprojectsdataeng.dfs.core.windows.net/raw_data/' + file_name,
                storage_options={
                    'account_key': 'DClO+P5yffQRLw2poxM4/meEQiSKI3HlbYxcPjX+l2RP04l7i3/lcqjnCuna6rSIejapOqMiLBwD+AStuGjjGA=='
                })
    concat_data=pd.concat([original_data,team_season_stats2],axis=0)

    #check for duplicated rows
    concat_data.drop_duplicates(inplace=True)

    concat_data.to_csv('abfs://fbref-data@storaccoprojectsdataeng.dfs.core.windows.net/raw_data/' + file_name,
                storage_options={
                    'account_key': 'DClO+P5yffQRLw2poxM4/meEQiSKI3HlbYxcPjX+l2RP04l7i3/lcqjnCuna6rSIejapOqMiLBwD+AStuGjjGA=='
                }, index=False)




def process_players_season_stats(fbref, stat_type):
    players_season_stats = fbref.read_player_season_stats(stat_type=stat_type)
    try:
        players_season_stats2 = players_season_stats.droplevel(0, axis=1)
        players_season_stats2.columns = [col[0] + "_" + col[1] for col in players_season_stats.columns]
    except:
        pass

    players_season_stats2 = players_season_stats2.reset_index()

    players_season_stats2.to_csv("../data/players_season_stats_" + stat_type + ".csv", index=False)

def process_players_match_stats(fbref, stat_type):
    players_match_stats = fbref.read_player_match_stats(stat_type=stat_type)
    try:
        players_match_stats2 = players_match_stats.droplevel(0, axis=1)
        players_match_stats2.columns = [col[0] + "_" + col[1] for col in players_match_stats.columns]
    except:
        pass

    players_match_stats2 = players_match_stats2.reset_index()

    players_match_stats2.to_csv("../data/players_match_stats_" + stat_type + ".csv", index=False)

