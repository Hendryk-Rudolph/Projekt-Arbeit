import time
import datetime as dt
import math
import random

Dateiname = 'fahrten.txt'
year = 2023
month = 5
stations = 10
sets = 100

def write_ln(datum, ID, s_station, e_station):
    my_file = open(Dateiname, 'a')
    my_string = str(ID) + ', ' + datum.strftime('%Y, %m, %d, %H, %M') + ', ' + str(s_station) + ', ' + str(e_station) + '\n'
    my_file.write(my_string)
    my_file.close()

def generate_stamp(year, month, day, hour, mu):
    start_h = -1
    while start_h not in range(23):
        start_h = math.trunc(random.gauss(hour,mu))
    start_m = math.trunc(random.randint(0,59))
    starttime = dt.datetime(year, month, day, start_h, start_m, 0, 0)
    return starttime

def commuter_stamp(year, month, day):
    if dt.date(year,month,day).weekday() < 5 and dt.date(year,month,day).weekday() >= 0 :
        if random.random() < 0.9:
            start_1 = generate_stamp(year, month, day, 7, 1)
            start_2 = generate_stamp(year, month, day, 18, 1)
            return start_1, start_2

    elif dt.date(year,month,day).weekday() <= 6 and dt.date(year,month,day).weekday() >= 5 :
        if random.random() < 0.25:
            start_1 = generate_stamp(year, month, day, 11, 1)
            start_2 = generate_stamp(year, month, day, 15, 1)
            return start_1, start_2
        
def leisure_stamp(year, month, day):
    if dt.date(year,month,day).weekday() < 5 and dt.date(year,month,day).weekday() >= 0 :
        if random.random() < 0.2:
            start_1 = generate_stamp(year, month, day, 11, 1)
            start_2 = generate_stamp(year, month, day, 15, 1)
            return start_1, start_2

    elif dt.date(year,month,day).weekday() <= 6 and dt.date(year,month,day).weekday() >= 5 :
        if random.random() < 0.5:
            start_1 = generate_stamp(year, month, day, 11, 1)
            start_2 = generate_stamp(year, month, day, 18, 1)
            return start_1, start_2
        
def pupil_stamp(year,month,day):
    if dt.date(year,month,day).weekday() < 5 and dt.date(year,month,day).weekday() >= 0 :
        if random.random() < 0.95:
            start_1 = generate_stamp(year, month, day, 7, 1)
            start_2 = generate_stamp(year, month, day, 14, 1)
            return start_1, start_2

    elif dt.date(year,month,day).weekday() <= 6 and dt.date(year,month,day).weekday() >= 5 :
        if random.random() < 0.5:
            start_1 = generate_stamp(year, month, day, 11, 1)
            start_2 = generate_stamp(year, month, day, 21, 1)
            return start_1, start_2
    
def err_stamp(year,month,day):
    if dt.date(year,month,day).weekday() < 5 and dt.date(year,month,day).weekday() >= 0 :
        if random.random() < 0.5:
            start_1 = generate_stamp(year, month, day, 7, 1)
            start_2 = generate_stamp(year, month, day, 14, 1)
            return start_1, start_2

    elif dt.date(year,month,day).weekday() <= 6 and dt.date(year,month,day).weekday() >= 5 :
        if random.random() < 0.5:
            start_1 = generate_stamp(year, month, day, 9, 2)
            start_2 = generate_stamp(year, month, day, 17, 2)
            return start_1, start_2

ID = 0
my_file = open(Dateiname, 'w')
my_file.close()
for lv in range(sets):
    decider = random.random()
    usual_station_start = random.randint(1,stations)
    usual_station_end = usual_station_start
    while usual_station_end == usual_station_start:
        usual_station_end = random.randint(1,stations)
    if decider<0.5:
        for lv in range(8,15):
            day = lv
            startstation = usual_station_start
            if dt.date(year,month,day).weekday() < 5 and dt.date(year,month,day).weekday() >= 0 :
                endstation = usual_station_end
            elif dt.date(year,month,day).weekday() <= 6 and dt.date(year,month,day).weekday() >= 5 :
                endstation = usual_station_start
                while endstation == usual_station_start:
                    endstation = random.randint(1,stations)
            stamps = commuter_stamp(year,month,day)
            if not stamps == None:
                write_ln(stamps[0], ID, startstation, endstation)
                write_ln(stamps[1], ID, endstation, startstation)
    elif decider >= 0.5 and decider < 0.7:
        for lv in range(8,15):
            day = lv            
            if dt.date(year,month,day).weekday() < 5 and dt.date(year,month,day).weekday() >= 0 :
                endstation = usual_station_end
            elif dt.date(year,month,day).weekday() <= 6 and dt.date(year,month,day).weekday() >= 5 :
                endstation = usual_station_start
                while endstation == usual_station_start:
                    endstation = random.randint(1,stations)
            stamps = pupil_stamp(year,month,day)
            if not stamps == None:
                write_ln(stamps[0], ID, startstation, endstation)
                write_ln(stamps[1], ID, endstation, startstation)
    elif decider >= 0.7 and decider <0.9:
        for lv in range(8,15):
            day = lv
            startstation = usual_station_start
            endstation = usual_station_start
            while endstation == usual_station_start:
                endstation = random.randint(1,stations)
            stamps = err_stamp(year,month,day)
            if not stamps == None:
                write_ln(stamps[0], ID, startstation, endstation)
                write_ln(stamps[1], ID, endstation, startstation)
    elif decider >= 0.9:
        for lv in range(8,15):
            day = lv
            startstation = usual_station_start
            endstation = usual_station_start
            while endstation == usual_station_start:
                endstation = random.randint(1,stations)
            stamps = commuter_stamp(year,month,day)
            if not stamps == None:
                write_ln(stamps[0], ID, startstation, endstation)
                write_ln(stamps[1], ID, endstation, startstation)
    else:
        print('ERROR')
        exit()
        
    ID += 1