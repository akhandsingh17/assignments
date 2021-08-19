"""
Given a multi-step product feature, write SQL to see how well this feature is doing
(loading times, step completion %). Then use Python to constantly update average step time as
new values stream in, given that there are too many to store in memory.

"""
import datetime
from collections import defaultdict


datetimestreams = [
  [1000, 123, 1, datetime.datetime(2014, 4, 11, 8, 0)],
  [1000, 123, 2, datetime.datetime(2014, 4, 11, 8, 10)],
  [1000, 123, 3, datetime.datetime(2014, 4, 11, 8, 20)],
  [1000, 123, 4, datetime.datetime(2014, 4, 11, 8, 30)],
  [1000, 123, 5, datetime.datetime(2014, 4, 11, 8, 31)],
  [1001, 125, 1, datetime.datetime(2014, 4, 11, 9, 10)],
  [1001, 125, 2, datetime.datetime(2014, 4, 11, 9, 30)],
  [1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 50)],
  [1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 51)],
  [1001, 125, 4, datetime.datetime(2014, 4, 11, 9, 52)],
  [1005, 129, 1, datetime.datetime(2014, 4, 11, 9, 8)],
  [1005, 129, 2, datetime.datetime(2014, 4, 11, 9, 10)],
  [1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 12)],
  [1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 13)],
  [1005, 129, 4, datetime.datetime(2014, 4, 11, 9, 14)],
  [1005, 129, 5, datetime.datetime(2014, 4, 11, 9, 18)]
]


def avg_time(streams):
    result_dict = {}
    time_spent = {}
    users_on_steps = {1:0, 2:0, 3:0, 4:0}
    for i in range(len(streams)):
        stream = streams[i]
        session_id, user_id, step_id, current_step_start_time = stream
        if ((session_id, user_id, step_id) not in result_dict):
            result_dict[(session_id, user_id, step_id)] = current_step_start_time
            if step_id > 1 and (session_id, user_id, step_id-1) in result_dict:
                users_on_steps[step_id-1] +=1
                previous_step_start_time = result_dict[(session_id, user_id, step_id-1)]
                if (step_id-1) not in time_spent:
                    time_spent[step_id-1] = (current_step_start_time - previous_step_start_time).total_seconds()
                else:time_spent[step_id-1] += (current_step_start_time - previous_step_start_time).total_seconds()
                print(result_dict)
            print("Users in each step", users_on_steps)
            print("Time spent in each step", time_spent)
            for step in time_spent:
                avg_time = time_spent[step]/users_on_steps[step]
                print("Avg. time spent on step {} is {} seconds".format(step, avg_time))

(avg_time(datetimestreams))