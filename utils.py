def get_temps(country_dict):
  # Se seleccionan solo las columnas que están identificadas para los años de registro.  
  filter_dict = {key:float(value) for key, value in country_dict.items() if key.isdigit()} 
  #print (type(filter_dict), " filter_dict =>", filter_dict)

  labels = filter_dict.keys()
  values = filter_dict.values()
  return labels, values

def temps_by_country(data, country):
  result = list(filter(lambda item: item['Country Name'] == country, data))
  return result

if __name__ == '__main__':
  country_dict =  {'\ufeffObjectId': '1', 'Country Name': 'Afghanistan, Islamic Rep. of', 'Unit': 'Degree Celsius', 'Change ': 'Surface Temperature Change', '1970': '0.898', '1971': '0.652', '1972': '-1.089', '1973': '0.262', '1974': '-0.47', '1975': '-0.468', '1976': '-0.295', '1977': '0.532', '1978': '0.105', '1979': '0.394', '1980': '0.69', '1981': '0.583', '1982': '-0.237', '1983': '0.213', '1984': '0.21', '1985': '0.361', '1986': '-0.048', '1987': '0.49', '1988': '0.988', '1989': '-0.122', '1990': '0.847', '1991': '-0.058', '1992': '-0.214', '1993': '0.292', '1994': '0.554', '1995': '0.474', '1996': '-0.016', '1997': '0.592', '1998': '0.795', '1999': '1.301', '2000': '1.109', '2001': '1.366', '2002': '1.384', '2003': '0.615', '2004': '1.427', '2005': '0.491', '2006': '1.78', '2007': '0.736', '2008': '0.804', '2009': '0.929', '2010': '1.646', '2011': '1.446', '2012': '0.234', '2013': '1.308', '2014': '0.457', '2015': '1.101', '2016': '1.607', '2017': '1.568', '2018': '1.58', '2019': '0.96', '2020': '0.544', '2021': '1.421'}
  
  get_temps(country_dict)
  