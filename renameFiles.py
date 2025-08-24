import os
import re

if __name__ == "__main__":
    # Define the base directory and folders
    base_dir = os.getcwd()  # Current directory: Leetcode-SQL-Challange
    folders = ['Easy', 'Medium', 'Hard']

    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            print(f"Folder {folder} does not exist")
            continue

        # Iterate through .sql files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.sql'):
                file_path = os.path.join(folder_path, filename)

                # Read the first line and content
                with open(file_path, 'r', encoding='utf-8') as file:
                    first_line = file.readline().strip()
                    rest_of_content = file.readlines()

                # Extract "Question" and number using regex
                match = re.match(r'--\s*Question\s*(\d+)', first_line)
                if match:
                    question_num = match.group(1)
                    new_name = f"Question_{question_num}.sql"
                    new_file_path = os.path.join(folder_path, new_name)

                    questionName = filename.split(".")[0]
                    questionNum = question_num
                    print(f"Practice Question No. :- {questionNum}")
                    print(f"Practice Question Name :- {questionName}")

                    # Write new content with file name as first line
                    try:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(f"-- {questionName}\n")
                            #file.write(first_line + '\n')
                            file.writelines(rest_of_content)
                        print(f"Modified {filename} to include '-- {new_name}'")

                        # Rename the file
                        os.rename(file_path, new_file_path)
                        print(f"Renamed {filename} to {new_name}")
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

                else:
                    print(f"Could not parse first line of {filename}: {first_line}")

    print("Processing complete!")