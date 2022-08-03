import csv

def update_users(f_name,l_name,new_first,new_last):
    with open('users.csv') as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    count = 0
    with open('users.csv','w') as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == f_name and user[1] == l_name:
                csv_writer.writerow([new_first,new_last])
                count += 1
            else:
                csv_writer.writerow(user)

    return f"{count} record(s) updated."

print(update_users('Emre','Ustundag','Connor','OBrienne'))


def delete_users(f_name,l_name):
    with open('users.csv') as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    count = 0
    with open('users.csv','w') as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == f_name and user[1] == l_name:
                count += 1
            else:
                csv_writer.writerow(user)

    return f"{count} record(s) deleted."

print(delete_users('Emre','Ustundag'))
