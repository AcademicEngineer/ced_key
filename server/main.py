import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from apiclient import discovery
import time
import json
import requests
import schedule
import datetime

JSON_PATH = "./cedkey.json"
SETTING_PATH = "./setting.json"
UPDATE_SEC = 3


# スプレッドシートから情報取得
def get_sheet_data(gc):
    worksheet = gc.open(SHEET_NAME).sheet1
    all_dict_data = worksheet.get_all_records()

    return all_dict_data


# スプレッドシートの監視
def check_update():
    global data
    current_data = get_sheet_data(gc)
    if len(current_data) > len(data):
        diff = [d for d in current_data if d not in data]
        send_command_each(diff)
        data = current_data


# 各電子錠にリクエスト
def request_key(place, operation_type):
    endpoint = f"{place}:8000/{operation_type}"
    try:
        requests.post(endpoint)
    except Exception as e:
        print(e)


# 各電子錠に一斉に送信
def send_command_all(operation_type):
    for place in setting['place'].values():
        request_key(place, operation_type)
    return schedule.CancelJob()


# フォームで選択された電子錠に送信
def send_command_each(diff_list):
    for data in diff_list:
        operation_type = "open" if data["操作"] == "開錠" else "close"
        place_list = data["場所"].split(", ")

        for place in place_list:
            request_key(setting['place'][place], operation_type)


# カレンダーから当日の予定を取得
def get_schedule():
    time_min = datetime.datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0)
    time_max = time_min + datetime.timedelta(days=1)
    time_min = time_min.isoformat() + 'Z'
    time_max = time_max.isoformat() + 'Z'

    try:
        http = credentials.authorize(httplib2.Http())
        service = discovery.build(
            'calendar',
            'v3',
            http=http
        )

        events = service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True
        ).execute()
        items = events['items']

        schedule_list = []
        for item in items:
            schedule_dict = {
                "start": item["start"]["dateTime"],
                "end": item["end"]["dateTime"]
            }
            schedule_list.append(schedule_dict)

        return schedule_list
    except Exception as e:
        print(e)


# 0時の定期実行ジョブ
def job():
    schedule_list = get_schedule()
    for s in schedule_list:
        start = datetime.datetime.strptime(
            s["start"], "%Y-%m-%dT%H:%M:%S+09:00")
        start = start.strftime("%H:%M")
        end = datetime.datetime.strptime(s["end"], "%Y-%m-%dT%H:%M:%S+09:00")
        end = end.strftime("%H:%M")
        schedule.every().day.at(start).do(send_command_all, operation_type="open")
        schedule.every().day.at(end).do(send_command_all, operation_type="close")


setting = json.load(open(SETTING_PATH, "r"))
SHEET_NAME = setting["sheetName"]
CALENDAR_ID = setting["calendarId"]

# スプレッドシートとの接続
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive",
         "https://www.googleapis.com/auth/calendar.readonly"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    JSON_PATH, scope)
gc = gspread.authorize(credentials)

schedule.every().day.at("00:00").do(job)
# schedule.every(10).seconds.do(job)
schedule.every(UPDATE_SEC).seconds.do(check_update)


data = get_sheet_data(gc)
while True:
    schedule.run_pending()
    time.sleep(1)


# pprint.pprint(check_update(gc))

# pprint.pprint(get_schedule())
