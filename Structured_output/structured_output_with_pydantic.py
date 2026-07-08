from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Employee(BaseModel):
    name:str=Field(min_length=3) # here we check field_constraints
    employee_id:Optional[int]=100 # here it is optional if we cant give it , it still run and used by default value 
    salary:float  # here if user give integer value pydantic auto convert it into float
    company_name:str="TCS" # here it is by default value if user cant give
    email:EmailStr

user_name=input("Enter your name :")
# user_emp_id=input("Enter your employee id :")
user_salary=input("Enter your salary :")
# user_company=input("Enter your company name :")


# new_employee=Employee(name=user_name, employee_id=user_emp_id, salary=user_salary)

# new_employee=Employee(name=user_name, employee_id=user_emp_id, salary=user_salary,company_name=user_company)

new_employee=Employee(name=user_name, salary=user_salary, email="abc@gmail.com") # if 'Optional' and 'default value' used
print(new_employee)
