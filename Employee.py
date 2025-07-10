class Employee:
    def work(self):
        print("software")
class Manager(Employee):
    def manage(self):
        print(f"i will manage both")
b=Manager()
b.manage()
b.work()