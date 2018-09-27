from flask import request,jsonify
import json

class Account:
        
    accounts = {}
        
    def add_account(self,name,password):
        self.accounts[password] = name     
       
        return self.accounts[password]

    def login(self,name,password):
        for k,v in self.accounts.items():
            
            if k == password and v == name  :
                return True

