def reconstruct_trip(tickets):
  tix = {}
  route = []
  next_ticket = []
  for i in tickets:
    src = i[0]
    dest = i[1]
    #h = hash(i[0])
    tix[src]: dest
  current_ticket = tix[None]
  for j in tix:
    if j[0] == current_ticket[1]:
      next_ticket = j[0]
  while current_ticket != None:
    route.append(current_ticket)
    current_ticket = next_ticket
 
  return route


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
