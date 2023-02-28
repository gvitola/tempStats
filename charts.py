import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, region):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  ax.set(xlabel='Años', ylabel='Grados Celsius', title='Variaciones en Temperatura\n'+region)
  plt.xticks(rotation=90)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

