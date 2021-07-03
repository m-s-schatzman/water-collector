#!/usr/bin/env python3
import sys
from database import HealthDatabase
from water import Water
from datetime import datetime, timedelta
import time

def build_water_entry(size):
    return Water(size)

def get_unix_start_of_day_and_next_day():
    today = datetime.now()
    start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_next_day = start_of_day + timedelta(1)

    unix_start_of_day = time.mktime(start_of_day.timetuple())
    unix_start_of_next_day = time.mktime(start_of_next_day.timetuple())
    
    return (unix_start_of_day, unix_start_of_next_day)

# calculate todays water entries
def calculate_days_water_intake(health_db):
    start, end = get_unix_start_of_day_and_next_day()
    sql = "SELECT SUM(fluid_oz) FROM water_entries WHERE timestamp >= {} AND timestamp < {}".format(int(start), int(end))
    db_response = health_db.query(sql)
    amount_drank = db_response[0][0]
    return amount_drank

def clear_todays_entries(health_db):
    start, end = get_unix_start_of_day_and_next_day()
    sql = "DELETE FROM water_entries WHERE timestamp >= {} AND timestamp < {}".format(int(start), int(end))
    health_db.query(sql)
    health_db.conn.commit()
    
def get_todays_water_intake(health_db):
    water_intake = calculate_days_water_intake(health_db)
    water_val = water_intake if water_intake else 0
    print(f"You have drank {water_val} floz of water today")
    
def create_water_entry(health_db, entry):
    health_db.create_water_entry(entry)
    
def handle_bad_input():
    print("Please enter a number in the prompt!\n")
    
def user_prompt(health_db):
    print("1. Create water entry\n")
    print("2. See today's water intake\n")
    print("3. Clear today's entries")
    user_input = input("Enter your value: ")
    
    if user_input is "1":
        water_fl_oz = input("Enter water amount in floz: ")
        water_entry = build_water_entry(water_fl_oz)
        create_water_entry(health_db=health_db, entry=water_entry)
    elif user_input is "2":
        get_todays_water_intake(health_db=health_db)
    elif user_input is "3":
        clear_todays_entries(health_db=health_db)
    else:
        handle_bad_input()
        
    user_input = input("Would you like to do anything else? (y/n)")
    if user_input in ("Y", "y"):
        user_prompt(health_db)
    
    

def main():
    health_db = HealthDatabase()
    print("Hello! What would you like to do. Select from following:\n")
    user_prompt(health_db=health_db)
    health_db.close_connection()
    
main()
    
    



