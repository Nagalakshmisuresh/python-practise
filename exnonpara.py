class student:
    def __init__(self):
        self.name="suresh"
        self.id=1
        self.branch="mechanical"
        self.floor=3
    def display(self):
        print(self.name,self.id,self.branch,self.floor)
st1=student()
st1.display()