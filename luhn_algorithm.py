def is_luhn_valid(acc):
  d = list(map(int, str(acc)))

  i = 0 
  s = 0 

  l = len(d)
  while i < l:
    if i % 2 == 0:
      d[i] = d[i] * 2
      print(f"{d[i]} = {d[i] * 2}")
      if d[i] > 9:
        d[i] = d[i] - 9
    s += d[i] 
    i += 1

  if s % 10 == 0:
    return True
  else:
    return False


## 543210******1234
s1 = "543210"
s3 = "1234"

for x in range(999999):
  s = s1 + (str(x).zfill(6)) + s3
  #print("this is " + s)
  if int(s) % 123457 == 0:
    if is_luhn_valid(s):
      print("{}".format(s))



