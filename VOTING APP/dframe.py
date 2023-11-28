import pandas as pd
from pathlib import Path


path = Path("database")

def count_reset():
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Aadhar Number', 'Name','Gender','Age', 'Zone','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        df['hasVoted'].iloc[index]=0
    df.to_csv(path/'voterList.csv')

    df=pd.read_csv(path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    for index, row in df.iterrows():
        df['Vote Count'].iloc[index]=0
    df.to_csv (path/'cand_list.csv')

#aadhar_num,name,age,sex,zone,city,passw
def reset_voter_list():
    df = pd.DataFrame(columns=['voter_id','Aadhar Number', 'Name','Gender','Age', 'Zone','City','Passw','hasVoted'])
    df=df[['voter_id','Aadhar Number', 'Name','Gender','Age', 'Zone','City','Passw','hasVoted']]
    df.to_csv(path/'voterList.csv')

def reset_cand_list():
    df = pd.DataFrame(columns=['Sign','Name','Vote Count'])
    df=df[['Sign','Name','Vote Count']]
    df.to_csv(path/'cand_list.csv')


def verify(vid,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Passw','hasVoted']]
    return any(
        df['voter_id'].iloc[index] == vid and df['Passw'].iloc[index] == passw
        for index, row in df.iterrows()
    )


def isEligible(vid):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Aadhar Number', 'Name','Gender','Age', 'Zone','City','Passw','hasVoted']]
    return any(
        df['voter_id'].iloc[index] == vid and df['hasVoted'].iloc[index] == 0
        for index, row in df.iterrows()
    )


def vote_update(st,vid):
    if not isEligible(vid):
        return False
    df=pd.read_csv (path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    for index, row in df.iterrows():
        if df['Sign'].iloc[index]==st:
            df['Vote Count'].iloc[index]+=1

    df.to_csv (path/'cand_list.csv')

    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Aadhar Number', 'Name','Gender','Age', 'Zone','City','Passw','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid:
            df['hasVoted'].iloc[index]=1

    df.to_csv(path/'voterList.csv')

    return True


def show_result():
    df=pd.read_csv (path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    v_cnt = {
        df['Sign'].iloc[index]: df['Vote Count'].iloc[index]
        for index, row in df.iterrows()
    }
    print(v_cnt)
    return v_cnt


def taking_data_voter(aadhar_num,name,age,gender,zone,city,passw):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','Aadhar Number', 'Name','Gender','Age', 'Zone','City','Passw','hasVoted']]
    row,col=df.shape
    if row==0:
        vid = 10001
        df = pd.DataFrame({"voter_id":[vid],
                    "Aadhar Number" : [aadhar_num],
                    "Name":[name],
                    "Age" : [age],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)
    else:
        vid=df['voter_id'].iloc[-1]+1
        df1 = pd.DataFrame({"voter_id":[vid],
                    "Aadhar Number" : [aadhar_num],
                    "Name":[name],
                    "Age" : [age],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "hasVoted":[0]},)

        df=df.append(df1,ignore_index=True)

    df.to_csv(path/'voterList.csv')

    return vid
