# CSV files: comma seperated values. to put data in a plain text. what seperates the values is the delimiter (usually comma)
import csv  # we could use string split method but if the delimiter is in the data csv module is easier

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # it return each line as an iterable list

    with open('new_names.csv', 'w') as new_file:  # we want to write the data into a new csv file with tab delimiter
        csv_writer = csv.writer(new_file, delimiter='\t')

        # next(csv_reader)  # to skip the first line
        for line in csv_reader:  # each line is a list (each member of the list is the values seperated by the delimiter)
            csv_writer.writerow(line)  # writerow method takes a list and writes it to the file. if the members of the input list happens to have the delimiter in them, this method adds "" and then writes it
            print(line[0])

#-------------------------
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')  # if you do not introduce the delimiter which is by default is comma, it returns wrong results
    for line in csv_reader:
        print(line)

#--- using DictReader and DictWriter
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # it return each line as an iterable dictionary in which the key value is read from the first row

    with open('new_names.csv', 'w') as new_file:  # with dictionary writer, we have to specify the field names.
        fieldnames = ['first_name', 'last_name'] # if we dont want the email in our output file, we delete it from the fieldnames here and we should del it from each line (which is a dictionary)
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()  # this is optional, if we want to have the header in our file

        for line in csv_reader:
            del(line['email'])
            csv_writer.writerow(line)
