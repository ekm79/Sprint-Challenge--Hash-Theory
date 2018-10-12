def get_indices_of_item_weights(weights, limit):
  weight_list = {}
  for i, weight in enumerate(weights):
    weight_list.update({weight: i})
  print(weight_list)
  for i, weight in enumerate(weight_list):
    diff = limit - weight
    print (diff)
    if diff in weight_list:
      diff = weight_list[diff]
      if i > diff:
        return (i, diff)
      else:
        return (diff, i)
  return ()


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  

  pass 