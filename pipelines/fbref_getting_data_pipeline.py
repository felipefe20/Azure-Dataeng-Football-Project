import soccerdata as sd
import pandas as pd
from sqlalchemy import create_engine

import os
from sqlalchemy import create_engine
import pandas as pd

# Get environment variables
db_user = "airflow"
db_password = "airflow"
db_host = "football_data_postgresql-docker-airflow-postgres-1"
db_port = "5432"
db_name = "postgres"
storage_account_key = "F9CEgDc62GjYYB7LZ4IBbvjjLlwIxG17yrnyFGNQWGSnOhos9PS43WzzBKrAZI/PUu8IcjsGE5ry+AStxWsGVQ=="
azure_blob_connection_string = 'abfs://myfilesystem@staccfelipefootball.dfs.core.windows.net/mydirectory/'


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

    # Use environment variables in the create_engine function
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')

   
    team_season_stats2.to_csv(azure_blob_connection_string + file_name,
                storage_options={
                    'account_key': storage_account_key
                }, index=False)
    
    
    concat_data=team_season_stats2
    concat_data.drop_duplicates(inplace=True)
    
    # Write the DataFrame to a table in PostgreSQL
    concat_data.to_sql("team_season_stats_" + stat_type, engine, if_exists='append', index=False)



def process_players_season_stats(fbref, stat_type):
    players_season_stats = fbref.read_player_season_stats(stat_type=stat_type)
    try:
        players_season_stats2 = players_season_stats.droplevel(0, axis=1)
        players_season_stats2.columns = [col[0] + "_" + col[1] for col in players_season_stats.columns]
    except:
        pass

    players_season_stats2 = players_season_stats2.reset_index()

    file_name="player_season_stats_" + stat_type + ".csv"

       # Use environment variables in the create_engine function
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')

    try:
        original_data = pd.read_csv(
        azure_blob_connection_string + file_name,
        storage_options={
            'account_key': storage_account_key
        }
)
        
        concat_data=pd.concat([original_data,players_season_stats2],axis=0)
    
        #check for duplicated rows
        concat_data.drop_duplicates(inplace=True)

        concat_data.to_csv(azure_blob_connection_string + file_name,
                    storage_options={
                        'account_key': storage_account_key
                    }, index=False)
    
    except:
        concat_data=players_season_stats2
        concat_data.drop_duplicates(inplace=True)
    
    # Write the DataFrame to a table in PostgreSQL
    concat_data.to_sql("player_season_stats_" + stat_type, engine, if_exists='append', index=False)




def process_players_match_stats(fbref, stat_type):
    players_match_stats = fbref.read_player_match_stats(stat_type=stat_type)
    try:
        players_match_stats2 = players_match_stats.droplevel(0, axis=1)
        players_match_stats2.columns = [col[0] + "_" + col[1] for col in players_match_stats.columns]
    except:
        pass

    players_match_stats2 = players_match_stats2.reset_index()

    file_name="player_match_stats_" + stat_type + ".csv"

       # Use environment variables in the create_engine function
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')

    try:
        original_data = pd.read_csv(
        azure_blob_connection_string + file_name,
        storage_options={
            'account_key': storage_account_key
        }
)
        
        concat_data=pd.concat([original_data,players_match_stats2],axis=0)
    
        #check for duplicated rows
        concat_data.drop_duplicates(inplace=True)

        concat_data.to_csv(azure_blob_connection_string + file_name,
                    storage_options={
                        'account_key': storage_account_key
                    }, index=False)
    
    except:
        concat_data=players_match_stats2
        concat_data.drop_duplicates(inplace=True)
    
    # Write the DataFrame to a table in PostgreSQL
    concat_data.to_sql("player_match_stats_" + stat_type, engine, if_exists='append', index=False)
