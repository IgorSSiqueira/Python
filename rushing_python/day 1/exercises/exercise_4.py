import os

folder = 'Logs'

with open("exercise_4_arquive.txt", "w") as x:
    for logs in os.listdir(folder):
        arquive_path = os.path.join(folder, logs)    
        if os.path.isfile(arquive_path):
            with open(arquive_path, 'r') as f:
                for line in f.readlines():
                    if "[" not in line:
                        continue

                    if '(EE)' not in line:
                        continue

                    separeted_line = line.split()
                    time_stamp =  separeted_line[1]
                    time_stamp = time_stamp[0:-1]
                    error_msg = ' '.join(separeted_line[3:])                    
                    
                    x.write (f'At time {time_stamp}, error {error_msg}\n')
