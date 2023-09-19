import utils
import read_csv
import charts


def run():
  
  data = read_csv.read_csv('data.csv')
  labels,values = utils.get_World_Population_Percentage(data)
  charts.generate_pie_chart(labels,values)
  
  
  data = read_csv.read_csv('data.csv')
  country = input("Type country => " )
  result = utils.population_by_cuontry(data,country)
  
  if len(result) > 0 :
    country = result[0]
    labels, values = utils.get_population(country)
    print(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)
    print("Test")
    #print (labels, values)
    #print(utils.A)   
    #print(data)
    #print(result)
  
  
if __name__ == '__main__':
  run()