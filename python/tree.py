def write(json_string):
  try:
      f=open('tree.json','w')
      f.write(json_string)
      f.close()
      return 0
  except:
    return -1
  
  
def read():
  try:
    f=open('tree.json','r')
    json_string=f.read()
    f.close()
    return json_string
  except:
    return -1
    
