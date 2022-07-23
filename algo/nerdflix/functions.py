def strinput(text: str) -> str or None:
  val = input(text)
  if val == '':
    return None
  return val

def intinput(text: str) -> int or None:
  val = input(text)
  if val == '':
    return None
  elif val.isnumeric() == False:
    print("\nERROR: Valor invalido. (igualado a None)")
    return None
  return int(val)

def floatinput(text: str) -> float or None:
  val = input(text)
  if val == '':
    return None
  elif val.isnumeric() == False:
    print("\nERROR: Valor invalido. (igualado a None)")
    return None
  return float(val)

  