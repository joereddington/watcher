import datetime

#- 20/06/19 smallest next step:  
time_format ='%d/%m/%y'

def print_recent_dates(number_of_days_to_go_back,log_lines):
#    for line in log_lines:
#        if "smallest next step:" in line:
#            print line
    results={}
    for i in range(number_of_days_to_go_back+1):
        target_date=(datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i)).strftime(time_format)
        results[target_date]=0
        for line in log_lines:
            if target_date in line:
                results[target_date]=results[target_date]+1
                    
    for i in range(number_of_days_to_go_back+1):
        target_date=(datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i)).strftime(time_format)
        print "{}: {}".format(target_date,results[target_date])
                
        # count the log entries that go in  


def read_file(filename):
    events=[]
    with open(filename, 'rU') as events_file:
        lines = events_file.readlines()
        for line in lines:
            if "smallest next step:" in line:
                events.append(line.strip())
    return events

all_logs=read_file("../workspace.md")
all_logs.extend(read_file("../historic_notes.md"))
print_recent_dates(30, all_logs)
