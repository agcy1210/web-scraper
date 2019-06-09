import csv
from googlesearch import search

#this will do a google search with speaker name, designation and company for his linkedin profile
with open('speakers.csv','r') as file:
    data = csv.DictReader(file)
    social = "linkedin"
    links = []
    for row in data:
        base_url = row['Speaker Name']+row['Designation']+row['Company']+social
        for url in search(base_url,stop=1):
            links.append(url)



#now writing the data with linkedin link to a new csv file
#previous data is first read from speakers.csv which was scraped through spider

with open('speakers.csv') as file:
    data = csv.DictReader(file)

    with open('all_details.csv','w') as file:
        headers = ['Event Name','Speaker Name','Display Pic url', 'Designation', 'Company', 'Linkedin']
        csv_writer = csv.DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for row,link in zip(data,links):
            csv_writer.writerow({
                    'Event Name': 'AI & Big Data Expo',
                    'Speaker Name':row['Speaker Name'],
                    'Display Pic url': row['Display Pic url'],
                    'Designation': row['Designation'],
                    'Company': row['Company'],
                    'Linkedin': link
                })









