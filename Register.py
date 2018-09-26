class Register:

    
    def register_user(self,name,username,age,email,password,gender):
        print(name,username,age,email,password,gender)

    def password_firstletter(self,password):

        for i in password:
            if i[0] == i[0].upper():
                return True
            else:
                return False    


    def password_len(self,password):
        return len(password)
    
    def password(self,password):
        return password    


    def Username(self,username,name):
        if username != name:
            return True
        else:
            return False

    def Useremail(self,email):
        
            return email
    