import read_csv
import utils
import charts
  
def stats_by_country(data):
  print()  
  country = input('Seleccione el pais => ')
  result = utils.temps_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_temps(country)
    charts.generate_bar_chart(labels, values, country['Country Name'])

def stats_by_continent(data):
  continentes = list(set(item['Continent'] for item in data))
  print()
  print("Seleccione el continente:")
  menu = 1
  for continente in continentes:
    print(f"{menu} {continente}")
    menu += 1
    
  print()
  opcion = input("=>")

  if not opcion.isdigit():
    print("Opción inválida!")
  elif int(opcion) < len(continentes):
    data = list(filter(lambda item : item['Continent'] == continentes[int(opcion)-1],data))
  
    countries = list(map(lambda x: x['Country Name'], data))
    percentages = list(map(lambda x: x['Average'], data))
    charts.generate_pie_chart(countries, percentages)  
  else:
    print("Opción inválida!")


def run():

  data = read_csv.read_csv('./tempStats/GlobalTempAnnualCountryRecords-2.csv')

  while True:
    print("-"*41)
    print("|"+(" "*10)+"T E M P * S T A T S"+(" "*10)+"|")
    print("-"*41)
    print()
    print("1. Variación de la temperatura por pais")
    print("2. Variación de la temperatura por continente")
    print()
    print("9. Salir")
    print()
    print("-"*41)
    
    opcion = input("Seleccione la opción deseada => ")
  
    if opcion.isdigit():
      if int(opcion) == 1:
        stats_by_country(data)
      elif int(opcion) == 2:
        stats_by_continent(data)
        continue
      else:
        break    
    else:
      print("Opción inválida!")

if __name__ == '__main__':
  run()
