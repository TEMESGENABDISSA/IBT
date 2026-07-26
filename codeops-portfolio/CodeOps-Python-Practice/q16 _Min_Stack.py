class MinStack:
    
    def __init__(self):

        self.stack=[]
        self.minimum=[]


    def push(self,val):

        self.stack.append(val)

        if not self.minimum or val <= self.minimum[-1]:

            self.minimum.append(val)



    def pop(self):

        value=self.stack.pop()

        if value==self.minimum[-1]:

            self.minimum.pop()

        return value



    def top(self):

        return self.stack[-1]



    def get_min(self):

        return self.minimum[-1]