from algoViewer.sort.algo_switcher import create_algo_object

def sort_file_handler(data, selection):
  data = str(data)[2:-1]
  data_parsed = data.split(' ')
  num_array = []
  for string in data_parsed:
    if string.isdigit():
      num_array.append(int(string))
    else:
      return 1

  switcher = create_algo_object(num_array)
  switcher[selection].create_algo()
  f = open("output.txt", "w+")
  for num in switcher[selection].input:
    f.write(str(num) + ' ')
  f.close()
  
  return 0