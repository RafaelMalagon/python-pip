def get_population(country_dict):
  population_dict = {
    '2022' : int(country_dict['2022 Population']),
    '2020' : int(country_dict['2020 Population']),
    '2015' : int(country_dict['2015 Population']),
    '2010' : int(country_dict['2010 Population']),
    '2000' : int(country_dict['2000 Population']),
    '1990' : int(country_dict['1990 Population']),
    '1980' : int(country_dict['1980 Population']),
    '1970' : int(country_dict['1970 Population'])
  }  
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

A = "Hola mundo"

def population_by_cuontry(data, country):
  result = list(filter(lambda item: item ['Country/Territory'] == country, data))
  return result
  
def get_World_Population_Percentage(data):
  percentage_dic ={
    item['Country/Territory'] : item['World Population Percentage'] for item in data
  }
  labels = percentage_dic.keys()
  values = percentage_dic.values()
  return labels,values