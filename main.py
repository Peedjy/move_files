import os
import shutil
import logging
from datetime import datetime, timedelta
from list import item_list

# Configuration of logging mode (Levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig (level=logging.INFO,
                     filename="debug_msg.log",
                     filemode="a",
                     format= '%(asctime)s : %(levelname)s : %(message)s')

def get_items():
    return item_list

def move_files():
    logging.info("START TO MOVE FILES")
    items = get_items()
    #print ("items =", items)

    for item in items:
        item_type, src_folder, dest_folder = item
        files_to_move = []

        # Check each file in the source directory
        for file_name in os.listdir(src_folder):
            file_path = os.path.join(src_folder, file_name)
            
            # Check if the files has the required extensions
            if os.path.isfile(file_path) and file_name.lower().endswith(('.xlsx', '.xlsm', '.doc', '.txt', '.ppt''.jpg','.png', '.pdf', '.pst')): # Add or remove the extensions you want to use
                
                # Check if the file date is less than 2 months old
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                period_to_keep = datetime.now() - timedelta(days=60) # We move only the files older than 60 days
                
                if file_time < period_to_keep:
                    print("to move")
                    print (files_to_move)
                    files_to_move.append(file_path)

        # Move the files to the destination folder
        for file_path in files_to_move:
            shutil.move(file_path, dest_folder)
            logging.info(f"File moved from: {file_path} to {dest_folder}")

    print(f"Task completed!")

if __name__ == "__main__":
    move_files()