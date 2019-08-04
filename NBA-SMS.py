from flask import Flask, request
import json, ast
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from nba_py import game, team, player
import nba_py
import pandas as pd


app = Flask('YoungWonks SMS Bot Webinar')

@app.route('/nba', methods=['POST'])

def nba():
    body = request.values['Body']
    nba_players = player.PlayerList(league_id='00', season='2018-19', only_current=1).info()
    pid = nba_players[nba_players.DISPLAY_FIRST_LAST == str(body)]['PERSON_ID']
    info = player.PlayerGameLogs(pid, season = '2018-19').info()
    numbers = '\n' + '2018-19 Stats' + '\n' + 'PTS: ' + str(info.PTS.mean().round(1)) + '\n' + 'AST: ' + str(info.AST.mean().round(1)) + '\n' + 'REB: '+ str(info.REB.mean().round(1)) + '\n' + 'STL: ' + str(info.REB.mean().round(1)) + '\n' + 'BLK: ' + str(info.STL.mean().round(1))
    ps = player.PlayerSummary(pid)  
    ps = ps.info()
    ps = ps.to_dict()
    psa = str(body) + '\n' + 'TEAM: ' + str(ps['TEAM_NAME'][0]) + '\n' + 'HEIGHT: ' + str(ps['HEIGHT'][0]) + '\n' + 'POSITION: ' + str(ps['POSITION'][0])
    fr = str(psa) + str(numbers)
    r = MessagingResponse()
    res = str(fr)
    r.message(res)
    return str(r)

if __name__ == '__main__':
    app.run()
    
