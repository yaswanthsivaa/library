class bank(object):
  def __init__(self,name,balance):
    self.acc_holder = name
    self.amount = balance
  
  def balance(self,amount):
    print(self.amount)

  def wd(self,amount):
    if amount < 0:
      raise ValueError('Can\'t enter negative number')
  
  def __repr__(self):
    return f'bank(account_holder={self.acc_holder}, amount={self.amount})'

bp = bank('Yaswanth',1000)

print(bp)
err = bp.wd(-2)
print(bp)
