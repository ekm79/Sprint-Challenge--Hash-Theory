def reconstruct_trip(tickets):
  tix = {}
  route = ['']* (len(tickets)-1)
  for ticket in tickets:
    tix[ticket[0]] = ticket[1]
    if ticket[0] is None:
      route[0] = ticket[1]
  for i in range(1, len(route)):
    if route[i-1] in tix:
      route[i] = tix[route[i-1]]
    else:
      return []
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
