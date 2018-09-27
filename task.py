class Task:
    
    todo_list = []

    def tasks(self):

        return self.todo_list

    def create_task(self,task):                
    
        self.todo_list.append(task)
        
        return self.todo_list
        

    def delete_task(self,task):    
        
        self.todo_list.remove(task)

        return self.todo_list

    def mark_as_finished(self,task,string_finish):
    
        for i in range(len(self.todo_list)):
            
            if self.todo_list[i] == task:
                
                self.todo_list.insert(i,self.todo_list[i].__add__("."+ string_finish))
                self.todo_list.remove(task)
                return self.todo_list
                
          
                
               
               

    def delete_all_tasks(self):    

        self.todo_list.clear()
        return self.todo_list



