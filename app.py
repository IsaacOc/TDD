from task import Task # import other functions as well
from account import Account  # import the function as well

class App:

    def Add_Account(self,name,password):

        acount = Account()
        return acount.add_account(name,password)
        
    def Account_login(self,name,password):

         acount = Account()
         return acount.login(name,password)

    def Tsks(self):
        tsk = Task()
        return tsk.tasks()

    def Create_task(self,task):

        tsk = Task()
        return tsk.create_task(task)

    def Delete_task(self,task): 
        tsk = Task()
        return tsk.delete_task(task)

    def Mark_as_finished(self,task,string_finish):
        tsk = Task()
        return tsk.mark_as_finished(task,string_finish)

    def Delete_all_tasks(self): 
        tsk = Task()
        return tsk.delete_all_tasks()

    

   