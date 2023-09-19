import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  #labels = ['a','b','c']
  #values = [100,200,300]
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'./img/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values,labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':

  labels = ['a','b','c','d']
  values = [100,47,45,23.5]
  #generate_bar_chart(labels,values)
  generate_pie_chart(labels,values)

  


