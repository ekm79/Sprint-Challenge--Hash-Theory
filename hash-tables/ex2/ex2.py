def reconstruct_trip(tickets):
  tix = {}
  route = []
  next_ticket = []
  for i in tickets:
    src = i[0]
    dest = i[1]
    tix.update({src: dest})
  current_ticket = tix[None]
  for j in tix:
    if tix[j] == current_ticket:
      next_ticket = j
  while current_ticket != None:
    route.append(current_ticket)
    current_ticket = next_ticket
  print(route)
  return route

tickets = [
  ('PIT', 'ORD'),
  ('XNA', 'CID'),
  ('SFO', 'BHM'),
  ('FLG', 'XNA'),
  (None, 'LAX'), 
  ('LAX', 'SFO'),
  ('CID', 'SLC'),
  ('ORD', None),
  ('SLC', 'PIT'),
  ('BHM', 'FLG'),
]
reconstruct_trip(tickets)

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
