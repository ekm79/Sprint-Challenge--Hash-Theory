def get_indices_of_item_weights(weights, limit):
  weight_list = {}
  for i, weight in enumerate(weights):
    weight_list[weight] = i
  for i, weight in enumerate(weights):

    if limit - weight in weight_list:
      diff = weight_list[limit - weight]
      if i > diff:
        return (i, diff)
      else:
        return (diff, i)
    else:
      return ()


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  

  pass 