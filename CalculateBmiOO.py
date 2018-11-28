class human: #{1}
    def __init__(self,height=0,weight=0): #{2}
      self.__height = height #{3}
      self.__weight=weight

    def calculateBMI(self,sample=0):#有給定初始值的就可以不丟參數
      try:
        return self.__weight / ((self.__height/100)**2)#{5}
      except ZeroDivisionError as err:
        return err,'你的建構子無輸入身高及體重'

def main():
    h = human(180,60) #{6}
    print(h.calculateBMI()) #{7}

if __name__=="__main__": #{8}
    main()
