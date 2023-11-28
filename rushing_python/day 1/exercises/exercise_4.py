# import os

# def parse_logs_of_a_folder(folder):
#     """
#     This parses an input folder full of logs
#     """

#     with open("exercise_4_archive.txt", "w") as x:
#         for logs in os.listdir(folder):
#             archive_path = os.path.join(folder, logs)    
#             if os.path.isfile(archive_path):
#                 with open(archive_path, 'r') as f:
#                     for line in f.readlines():
#                         if "[" not in line:
#                             continue

#                         if '(EE)' not in line:
#                             continue

#                         separeted_line = line.split()
#                         time_stamp =  separeted_line[1]
#                         time_stamp = time_stamp[0:-1]
#                         error_msg = ' '.join(separeted_line[3:])                    
                        
#                         # x.write (f'At time {time_stamp}, error {error_msg}\n')
#                         print(f'At time {time_stamp}, error {error_msg}\n')

# folder = 'Logs'
# parse_logs_of_a_folder(folder)


import os


def parse_log_file(filepath):
    msg = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if '[' not in line:
                continue

            if '(EE)' not in line:
                continue

            separeted_line = line.split()
            time_stamp = separeted_line[1]
            time_stamp = time_stamp[0:-1]
            error_msg = ' '.join(separeted_line[3:])
            msg.append(f"At time {time_stamp}, error {error_msg}\n")

    return msg


def sort_msg(msgs):
    splited_msgs = []
    time_stamp_list = []

    #Getting the time_stamp and converting to float
    for msg in msgs:
        splited_msgs.append(msg.split())
        splited = msg.split()
        time_stamp = splited[2]
        time_stamp = time_stamp[0:-1]
        time_stamp_list.append(float(time_stamp))

    #sorting
    for n in range(len(splited_msgs)) :
        min_n = n
        for j in range(n+1, len(splited_msgs)):
            if time_stamp_list[j] < time_stamp_list[min_n]:
                min_n = j

        time_stamp_list[n], time_stamp_list[min_n] = time_stamp_list[min_n], time_stamp_list[n]
        msgs[n], msgs[min_n] = msgs[min_n], msgs[n]

    return(msgs)


def create_new_archive(msgs):
    with open('exercise_4_archive.txt', 'w') as archive:
        for msg in msgs:
            archive.write(f'{msg}\n')


def parse_logs_of_a_folder(folder):
    """
    This parses an input folder full of logs
    """
    all_messages = []

    # Read all logs
    for logs in os.listdir(folder):
        logfile_path = os.path.join(folder, logs)    
        
        #exit early
        if not os.path.isfile(logfile_path):
            continue 

        msg = parse_log_file(logfile_path)
        all_messages.extend(msg)

    all_messages_sorted = sort_msg(all_messages)
    
    create_new_archive(all_messages_sorted)


folder = 'Logs'
parse_logs_of_a_folder(folder)
