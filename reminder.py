import schedule
import time
import json


def load_goals():

    with open("goals.json", "r", encoding="utf-8") as f:
        return json.load(f)


def remind(goal):

    print(f"\n[REMINDER] 지금 학습할 시간입니다 → {goal}\n")


def setup_reminders():

    goals = load_goals()

    for g in goals:
        schedule.every().day.at(g["remind_time"]).do(remind, g["goal"])


def run_scheduler():

    setup_reminders()

    while True:
        schedule.run_pending()
        time.sleep(30)