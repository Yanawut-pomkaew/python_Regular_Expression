# import ตัว Regular expression เข้ามา
import re
current = ''

# ตัวแปรเพื่อเก็บว่าผู้ใช้กรอกตัวแปรมาหรือไม่ ถ้ากรอกเข้ามาจะนำไปเก็บใน list Variable
hasVariable = False
Variable = []

List = []

ArithResult = ""

#class stack เพื่อเอาไว้เก็บค่าที่ผู้ใช้กรอกเข้ามา
class Stack:
      
  # constructor for the Stack class
  def __init__(self):
    # initialise an empty list
    self.stack = []
  
  
  # นำค่าใส่ลงใน stack
  def push(self, data):
    self.stack.append(data)
  # ลบค่าออกจาก stack
  def pop(self):
    #ถ้า stack เป็นค่าว่างให้บอกว่า stack ว่างอยู่
    if len(self.stack) <= 0:
      return "Stack is empty!"
    else:
      return self.stack.pop()
    
  # ดูค่าใน stack
  def size(self):
    return len(self.stack)
    
  # ดูค่าบนสุดของ stack
  def peek(self):
    return self.stack[-1]
    
  # ดูว่า stack นั้นว่างอยู่ไหม
  def isEmpty(self):
    if len(self.stack) <= 0:
      return True
    else:
      return False
  
  # แสดงค่าใน stack
  def show(self):
    return self.stack

# class ที่จะใช้ในการคำนวณค่าที่ผู้ใช้กรอกเข้ามา
class Calculation:
      
    #ฟังก์ชันที่จะนำค่าที่ผู้ใช้กรอกเข้ามาคำนวณกัน
  def applyOp(op, var2, var1):
      
    # ถ้าเจอเครื่องหมายบวก, ลบ , คูณ , หารหรือยกกำลังก็ให้ค่าทั้ง 2 บวก, ลบ , คูณ , หารหรือยกกำลังกัน
    if op == '+':
      x = lambda var1 , var2 : float(var1) + float(var2)
      return x(var1, var2)
    elif op == '-':
      x = lambda var1 , var2 : float(var1) - float(var2)
      return x(var1, var2)
    elif op == '*':
      x = lambda var1 , var2 : float(var1) * float(var2)
      return x(var1, var2)
    elif op == '/':
      #ถ้าค่าส่วนเป็น 0 ให้บอกว่าไม่สามารถหารได้
      if var2 == 0:
            return "Error, can't devide with zero number"
      else:
      
        x = lambda var1 , var2 : float(var1) / float(var2)
        return x(var1, var2)
    elif op == '^':
      
      x = lambda var1 , var2 : float(var1) ** float(var2)
      return x(var1, var2)
    else:
      return 0
  
  # ฟังก์ชันที่บอกว่าส่วนไหนของค่าที่จะต้องทำก่อนโดย
  def hasPrecedence(op1, op2):
    # ถ้าเจอเครื่องหมายวงเล็บ ให้ทำในวงเล็บก่อน
    if op2 == '(' or op2 == ')':
      return False
    # ถ้าเจอตัวเลขที่ติดลบให้มองเป็นลบ ไม่ใช่เครื่องหมาย
    elif '-' in op1 and len(op1) > 1:
      return False
    # ถ้าเจอคูณหารให้ทำก่อนบวกลบ
    elif (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
      return False
 
    else:
      return True
  
  #เป็นฟังก์ชันที่จะคำนวณค่า
  def Calculate(self , List):
        skip = 0
        for i in range(len(List)):
        # if skip is more than 0 skip the iteration
            if skip >= 1:
            # decrement skip flag
                skip -= 1
                continue
            # ถ้าเจอตัวเลขให้เก็บไว้ที่ num
            
            if List[i] >= '0' and List[i] <= '9':
                num = List[i]
                
            # เช็คว่ามีตัวเลขหรือจุดทศนิยมตามหลังหรือไม่
                for j in range(i+1, len(List)):
                    #ถ้ามีตัวเลขก็ให้บวกเพิ่มเข้าไป
                    if List[j] >= '0' and List[j] <= '9':
                        num = num + List[j]
                        skip += 1
                    #ถ้ามีจุดทศนิยมก็ให้บวกเพิ่มเข้าไป
                    elif List[j] == '.':
                        num = num + "."
                        skip += 1
                    # ถ้าเป็นช่องว่างก็ให้หยุด เพราะครบตัวเลขนึงแล้ว
                    else:
                        break
                        # นำตัวเลขเหล่านั้นใส่ใน value 
                value.push(num)
                
                
                #print(value.show())
                
                # ถ้าเจอ ( ให้เก็บไว้ใน operation
            elif List[i] == '(':
            
                operation.push(List[i])
  
                # ถ้าเจอ ) 
            elif List[i] == ')':
                
                #ถ้ามีค่าที่ยังคำนวณไม่เสร็จใน () ให้คำนวณต่อไปเรื่อย ๆ จนกว่าจะหมด
                while operation.peek() != '(':

                    val = Calculation.applyOp(operation.pop(), value.pop(), value.pop())
                    if(val == "infinity"):
                        print("Invalid Expression")
                        break
                    else:
                        #print(val)
                        value.push(val)
                operation.pop()
            
            # ถ้าเจอค่าติดลบให้เก็บใน value
            elif '-' in List[i] and len(List[i]) > 1:
              num = List[i] 
              value.push(num)
               
              1 + 2
            # ถ้าเจอเครื่องหมาย ให้เช็คลำดับการทำงานและค่อบคำนวณแล้วนำค่าไปเก็บใน value พร้อมกับนำเครื่องหมายไปเก็บใน operation
            elif List[i] in ('^','*','/' , '+','-'):
                
                while operation.isEmpty() is False and Calculation.hasPrecedence(List[i], operation.peek()):
                  x = Calculation.applyOp(operation.pop(), value.pop(), value.pop())
                  
                  value.push(x)
                  
                
                operation.push(List[i])
                
        # ถ้ามีเครื่องหมายที่ยังไม่คำนวณ ให้คำนวณ
        while(operation.isEmpty() is False):
              x = Calculation.applyOp(operation.pop(), value.pop(),value.pop())
              
              value.push(x)
              
      
        return str(value.pop())

# เป็น class ที่จะจัดเตรียมข้อมูลให้พร้อมสำหรับการคำนวณ    
class Setup:
    global current
    global regex
    global hasVariable
    global ArithResult
    def SetVariable(self , arithmetic):
        global current
        global regex
        global hasVariable
        global ArithResult
        for i , c in enumerate(arithmetic):
            # ถ้าผู้ใช้กรอกข้อมูลมาเป็นตัวอักษร จะต้องให้ผู้ใช้กรอกค่าของตัวอักษรนั้นด้วย ถ้าไม่ก็ไม่ต้องกรอก
            if (ord(c) >= 65 and ord(c)<= 90) or (ord(c) >= 97 and ord(c)<= 122): 
                print("Enter a value of variable" ,c, ":" , end = ' ')
                new = input()
                hasVariable = True
                Variable.append(new)
                current = current + str(new)
                ArithResult = ArithResult + str(new)
            else:
                ArithResult = ArithResult+c
                current = current + c
        return current        
    # ใช้ regex เพื่อแบ่งข้อมูลที่รับมาจากผู้ใช้ โดยแบ่งเป็น เครื่องหมายกับตัวเลขแล้วเก็บลง List เพื่อนำไปทำ arithmetic expression ต่อไป
    def split(self , arithmetic):
        regex = r'[-+]?\d*\.?\d+|(\d+)|(-\d+)|[-+*/^()]'
        for i in re.finditer(regex, arithmetic):
            
            List.append(i.group(0))

value = Stack()
operation = Stack()
print("c: Calculate Arithmetic Expression")
print("q: Quit ")
print("Please Enter Your Choice:" , end = ' ')
select = input()

setUp = Setup()
cal = Calculation();

# ถ้าผู้ใช้กรอกไม่ให้หยุดโปรแกรมโดยการพิมพ์ตัวอักษร 'q' โปรแกรมก็จะให้ผู้ใช้กรอกข้อมูลต่อไป
while select != 'q':
    
    List = []
    print("Enter an arithmetic expression:" , end = ' ') 
    arithmetic = input()
    current = ''
    
    arithmetic = setUp.SetVariable(arithmetic)
    setUp.split(arithmetic)
    
    #print(List)
    ans = cal.Calculate(List);
    aaa = float(ans)
    
    kkk= 0
    unary = False
    
    
    if aaa != 0: 
      #เช็คว่าค่าที่คำนวณติดลบหรือไม่
      if aaa < 0:
        unary = True
    
      while abs(aaa) >= 10:
        aaa = float(abs(aaa) / 10.0)
        kkk = kkk + 1
      #ถ้าค่าที่คำนวณติดลบ ก็ให้ค่าเป็นบวก
      if unary == True:
        aaa = float(aaa * -1.0)

      # คำนวณเพื่อหาว่าค่านี้ยกกำลังเท่าไหร่
      while abs(aaa) < 1:
        x = lambda aaa : float(abs(aaa) * 10.0)
        #aaa = float(abs(aaa) * 10.0)
        kkk = kkk -1
        x(aaa)
      
    
    if hasVariable == True :
          print("Arithmetic Expression to Evaluate: " , end = " " )
          print(ArithResult , end = " ")
          print("= " , ans , " = " , str(aaa) + "e"+ str(kkk))
            
    else: 
      print("Result = ", ans , " = ", str(aaa) + "e"+ str(kkk))
    
    Variable = []
    hasVariable = False
    ArithResult = ""
    
    print("c: Calculate Arithmetic Expression")
    print("q: Quit ")
    print("Please Enter Your Choice:" , end = ' ')
    select = input()
    
print("<End of Program>")

