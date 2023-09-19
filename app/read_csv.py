import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    #print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      #print("******")
      #print(row)
      #print(country_dict)
      data.append(country_dict)
    return data

def findBy(data):
  data_Country =[]
  if data['Country/Territory'=='Zimbabwe']:
    print("encontrado")    
  else:
    print("no ta")
    
  return data_Country
  

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  country_data = findBy("Zimbabwe")
  print(data[0])