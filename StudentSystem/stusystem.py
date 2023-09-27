import os

FILE_NAME = 'student.txt'
ENCODE = 'utf-8'

def main():
    clean_output()
    while True:
        menu()
        choice = input('I want to(number): ')
        if choice.isnumeric():
            choice = int(choice)
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('Sure to exit ? y/n: ')
                if answer == 'y' or answer == 'Y':
                    print('Good bye')
                    break
                else:
                    clean_output()
                    continue
            else:
                match choice:
                    case 1:
                        insert()
                    case 2:
                        search()
                    case 3:
                        delete()
                    case 4:
                        edit()
                    case 5:
                        sort()
                    case 6:
                        total()
                    case 7:
                        show()
        else:
            clean_output()
            print("Oops!  That was no valid number.  Please try again...")
        
def menu():
    print('='*20,'Student Info System','='*20)
    print('-'*20,'Function Menu','-'*20)
    print('\t'*3,'1.Add student info')
    print('\t'*3,'2.Search student')
    print('\t'*3,'3.Delete student')
    print('\t'*3,'4.Edit student')
    print('\t'*3,'5.Sort students')
    print('\t'*3,'6.Total students')
    print('\t'*3,'7.Show all students')
    print('\t'*3,'0.Exit')
    print('-'*60,)

# Add student
def insert():
    student_list = []
    while True:
        id = input('Student ID(ex.1001): ')
        if not id:
            break
        name = input('Student name: ')
        if not name:
            break
        
        print('Key in the scores of this student')
        try:
            english = int(input('English: '))
            python = int(input('Python: '))
            java = int(input('Java: '))
        except:
            print("Oops!  That was not a integer.  Please try again...")
            continue
        
        # Save student info to a dictionary
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        
        # Save a student to student_list
        student_list.append(student)
        ans=input('Another student ? y/n: ')
        if ans == 'y' or ans == 'Y':
            print('\n')
            continue
        else:
            break
        
    # Call save()
    save(student_list)
    print('!!!Add student(s) complete !!!')
#  Save function for insert
def save(list):
    # Here use try to check file exist or not
    try:
        # Use add mode to open FILE_NAME(student.txt)
        stu_txt = open(FILE_NAME, 'a', encoding=ENCODE)
    except:
        # If FILE_NAME(student.txt) is not exist, create it
        stu_txt = open(FILE_NAME, 'w', encoding=ENCODE)
        
    for item in list:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()

# Search 
def search():
    student_query = []
    while True:
        search_id = ''
        search_name = ''
        if os.path.exists(FILE_NAME):
            mode = input('Which search mode?\n1.ID, 2.Name: \n')
            if mode == '1' or mode == '2':
                if mode == '1':
                    search_id = input('ID for search: ')
                
                elif mode == '2':
                    search_name = input('Name for search: ')
                
                with open(FILE_NAME, 'r', encoding=ENCODE) as rfile:
                    student_list = rfile.readlines()
                    for line in student_list:
                        d_line = dict(eval(line))
                        if search_id != '':
                            if d_line['id'] == search_id:
                                student_query.append(d_line)
                        elif search_name != '':
                            if d_line['name'] == search_name:
                                student_query.append(d_line)
                # Show search result
                    show_students(student_query)
                    student_query.clear()
                while True:
                    out_answer = input('Search another? y/n: ')
                    if out_answer == 'y' or out_answer == 'Y':
                        break
                    elif out_answer == 'n' or out_answer == 'N':
                        return
                    else:
                        continue
                # continue
                    
            else:
                while True:
                    clean_output()
                    out_answer = input('Exit search mode? y/n: ')
                    if out_answer == 'y' or out_answer == 'Y':
                        return
                    elif out_answer == 'n' or out_answer == 'N':
                        clean_output()
                        break
                    else:
                        continue
                
                
        else:
            print('Student info was not save')
            return

# Show student(s) info
def show_students(student_query):
    if len(student_query) == 0:
        print('No matches')
        return
    # Info title template
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', 'Name', 'English', 'Python', 'Java', 'Total score'))
    # Info data template
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in student_query:
        # item.get('?') equals to item['?'], both can get value from key
        print(format_data.format(item.get('id'),
                                item.get('name'),
                                item.get('english'),
                                item.get('python'),
                                item.get('java'),
                                int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                ))
    
# Delete student by id
def delete():
    show()
    while True:
        delete_id = input('Which ID of student you want to delete? :\n')
        
        # Here use os.path.exists to check file exist or not
        if delete_id != '':
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, 'r', encoding=ENCODE) as file:
                    students_old = file.readlines()
            else:
                # If the delete_id was not in file, set student_old to a empty list
                students_old = []
            # Flag for delete or not
            flag = False 
            
            # If students_old have something, mean there are student info inside the file 
            if students_old:
                # Use W mode to open file, so the file will be empty,
                # But don't worry the whole file was backup in students_old list
                with open(FILE_NAME, 'w', encoding=ENCODE)as wfile:
                    # Create a dict for temp the one student info
                    d_line = {}
                    # For each student info(one text line in txt file)
                    for line in students_old:
                        # Convert line(student info) to dictionary and put into d_line
                        d_line = dict(eval(line))
                        # Check the key'id' in d_line(student info)
                        # If the ID not matches, write the line back to the wfile(student.txt)   
                        if d_line['id'] != delete_id:
                            wfile.write(str(d_line) + '\n')
                        # If the ID matches, skip the entire line, 
                        # and set the flag to True (indicating ID of student has been found and deleted).
                        else:
                            flag = True
                            
                    if flag:
                        print(f"ID '{delete_id}' student has been delete.")
                    else:
                        print(f"ID '{delete_id}' student does not exist, try again.")
                        
            # Code will run to here just because file is empty and create a empty list student_old
            else:
                print('Student info empty')
                break
            # After delete student show all students on screen
            show()
            answer = input('Delete another ? y/n: ')
            print('\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
            
# Edit student info by id
def edit():
    show()
    while True:
        edit_id = input('Which ID of student you want to edit? :\n')
        complete_flag = False
        if edit_id != '' and os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r', encoding=ENCODE) as rfile:
                students_old = rfile.readlines()
            try:
                with open(FILE_NAME, 'w', encoding=ENCODE)as wfile:
                    for line in students_old:
                        d_line = dict(eval(line))
                        if d_line['id'] == edit_id:
                            print('Found it, you can now edit the info')
                            while True:
                                print('Here are ', list(d_line.keys()), '\n')
                                edit_answer = input('Which part you want to edit: ')
                                if edit_answer in d_line:
                                    d_line[edit_answer] = input(f'Change {edit_answer} from {d_line[edit_answer]} to: ')
                                    print('Complete!')
                                    break
                                else:
                                    print("Can't found it, try another one.")
                                    continue
                            wfile.write(str(d_line) + '\n')
                            print('Edit complete!')
                        else:
                            wfile.write(str(d_line) + '\n')
                clean_output()
                answer = input('Edit another student ? y/n: ')
                print('\n')
                if answer == 'y' or answer == 'Y':
                    edit()
                else:
                    complete_flag = True
                    break
            except:
                when_except(students_old)
        else:
            clean_output()
            out_answer = input('Exit edit mode ? y/n: ')
            if out_answer == 'y' or out_answer == 'Y' or complete_flag:
                break
            else:
                continue
                
def sort():
    while True:
        clean_output()
        show()
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r', encoding=ENCODE) as rfile:
                students = rfile.readlines()
            students_new = []
            for line in students:
                d_line = dict(eval(line))
                students_new.append(d_line)
        else:
            print('Data was empty...')
        
        asc_or_desc = input('Sort by(0.ASC, 1.DESC): ')
        if asc_or_desc == '0':
            asc_or_desc_bool = False
        elif asc_or_desc == '1':
            asc_or_desc_bool = True
        else:
            print('Again')
            continue
        mode = input('Use (1.English, 2.Python, 3.Java, 0. Total score) to sort: \n')
        if mode == '1':
            students_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
        elif mode =='2':
            students_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
        elif mode =='3':
            students_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
        elif mode =='0':
            students_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
        else:
            print('Again')
            continue
        clean_output()
        show_students(students_new)
        break

# Count total students
def total():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding=ENCODE) as rfile:
            students = rfile.readlines()
            if students:
                print(f'Here are {len(students)} student'+('s\n' if len(students)>1 else '\n'))
            else:
                print('No student here')
    else:
        print('Data was empty...')

def show():
    students_list = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding=ENCODE) as rfile:
            students = rfile.readlines()
            for line in students:
                students_list.append(eval(line))
            if students_list:
                show_students(students_list)
    else:
        print('Data was empty...')

def when_except(students_old):
    with open(FILE_NAME, 'w', encoding=ENCODE)as wfile:
        for line in students_old:
            wfile.write(str(line) + '\n')

def clean_output():
    os.system('cls||clear')
    return

if __name__ == '__main__':
    main()