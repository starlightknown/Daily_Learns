class Human:
  def __init__(self,height,weight):
    self.height = height
    self.weight = weight
  
  def introduce(self):
    print("my weight is"+ self.weight)
 
k = Human(40, 30)
k.introduce()
