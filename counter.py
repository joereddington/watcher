import datetime

#- 20/06/19 smallest next step:  
time_format ='%d/%m/%y'

def print_recent_dates(number_of_days_to_go_back=4,log_lines):
    for i in range(number_of_days_to_go_back+1):
        print ""
        print (datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i)).strftime(time_format)
        # count the log entries that go in  


def read_logs():
    #read workspace and historical notes 

print_recent_dates(10, read_logs()) 
