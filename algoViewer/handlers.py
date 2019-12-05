from algoViewer.sort.algo_switcher import create_algo_object
import re

def sort_file_handler(formData):
  data = formData["file"].read()
  data = str(data)[2:-1]
  test = re.match(r"([0-9]+?;,\s)*[0-9]+", data)
  if test:
    print(test.groups())
  else:
    print("false")
  data_parsed = data.split(' ')
  num_array = []
  for string in data_parsed:
    if string.isdigit():
      num_array.append(int(string))

  switcher = create_algo_object(num_array)
  switcher[formData["selection"]].create_algo()
  f = open("output.txt", "w+")
  for num in switcher[formData["selection"]].input:
    f.write(str(num) + ' ')
  f.close()