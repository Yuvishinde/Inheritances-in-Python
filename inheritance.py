class Demo:
    def DemoMethod(self):
     print("Demo class method")

class User(Demo):
    def UserMethod(self):
        print("User class method")

class Info(User):
        def InfoMethod(self):
         print("Info class method")

i=Info()
i.InfoMethod()
i.UserMethod()        
i.DemoMethod()
