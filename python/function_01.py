def avg_number(*args):
  result = 0
  for i in args:
    result += i
    return result / len(args)