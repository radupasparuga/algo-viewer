from algoViewer.sort.algo_switcher import create_algo_object

def clean_data(data):
  data = str(data)[2:-1]
  aux = data.replace('\\r\\n',' ')
  data_parsed = aux.split()
  num_array = []
  for string in data_parsed:
    if string.isdigit():
      num_array.append(int(string))
    else:
      return 1
  return num_array

def get_path(data, selection): 
  num_array = clean_data(data)
  switcher = create_algo_object(num_array)
  return switcher[selection].create_algo()

def sort_file_handler(data, selection):
  num_array = clean_data(data)
  switcher = create_algo_object(num_array)
  switcher[selection].create_algo()
  
  return 0