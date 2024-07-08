import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("365x500")
        self.root.title("Scientific Calculator")
        
        self.calculation = ""
        
        self.create_widgets()
    
    def insert_text(self, value):
        self.te.insert(tk.END, value)
    
    def add_to_calc(self, symbol):
        self.calculation += str(symbol)
        self.te.delete(1.0, "end")
        self.te.insert(1.0, self.calculation)
    
    def evaluate_expression(self):
        try:
            result = eval(self.calculation)
            self.te.delete(1.0, "end")
            self.te.insert(1.0, result)
            self.calculation = str(result)  # Store the result for further calculations
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
    
    def handle_sqrt(self):
        try:
            sqrt_result = math.sqrt(eval(self.calculation))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, sqrt_result)
            self.calculation = str(sqrt_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
    
    def handle_sin(self):
        try:
            sin_result = math.sin(eval(self.calculation))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, sin_result)
            self.calculation = str(sin_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
    
    def handle_cos(self):
        try:
            cos_result = math.cos(eval(self.calculation))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, cos_result)
            self.calculation = str(cos_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
    
    def handle_tan(self):
        try:
            tan_result = math.tan(eval(self.calculation))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, tan_result)
            self.calculation = str(tan_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
            
    def handle_cosec(self):
        try:
            csc_result = 1/math.sin(math.radians(eval(self.calculation)))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, csc_result)
            self.calculation = str(csc_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
    
    def handle_sec(self):
        try:
            sec_result = 1/math.cos(math.radians(eval(self.calculation)))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, sec_result)
            self.calculation = str(sec_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
    
    def handle_cot(self):
        try:
            cot_result = 1/math.tan(math.radians(eval(self.calculation)))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, cot_result)
            self.calculation = str(cot_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
            
    def clear_field(self):
        self.te.delete(1.0,"end")
        self.calculation=""
        
    def square(self):
        try:
            sqr_result = eval(self.calculation)**2
            self.te.delete(1.0, "end")
            self.te.insert(1.0, sqr_result)
            self.calculation = str(sqr_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
            
    def rand_power(self):
        try:
            power_result = math.pow(eval(self.calculation),eval(self.calculation))
            self.te.delete(1.0, "end")
            self.te.insert(1.0, power_result)
            self.calculation = str(power_result)
        except Exception as e:
            self.te.delete(1.0, "end")
            self.te.insert(1.0, "Error")
            self.calculation = ""
              
    def ans_target(self):
        ans=self
        
    def log_ans(self):
        try:
            log_result = math.log(eval(self.calculation))
            self.te.delete(1.0,"end")
            self.te.insert(1.0,log_result)
            self.calculation= str(log_result)
        except Exception as e:
            self.te.delete(1.0,"end")
            self.te.insert(1.0,"erroe")
            self.calculation=""
            
    def ln_ans(self):
        try:
            ln_result = math.log1p(eval(self.calculation))
            self.te.delete(1.0,"end")
            self.te.insert(1.0,ln_result)
            self.calculation= str(ln_result)
        except Exception as e:
            self.te.delete(1.0,"end")
            self.te.insert(1.0,"erroe")
            self.calculation=""
            
    def e_val(self):
        try:
            evalue=math.e*eval(self.calculation)
            self.te.delete(1.0,"end")
            self.te.insert(1.0,evalue)
            self.calculation= str(evalue)
        except Exception as e:
            self.te.delete(1.0,"end")
            self.te.insert(1.0,"error")
            self.calculation=""
    
    def fact_value(self):
        try:
            factval= math.factorial(eval(self.calculation))
            self.te.delete(1.0,"end")
            self.te.insert(1.0,factval)
            self.calculation= str(factval)
        except Exception as e:
            self.te.delete(1.0,"end")
            self.te.insert(1.0,"error")
            self.calculation=""
           
    def roundoff(self):
        try:
            round_val= round(eval(self.calculation))
            self.te.delete(1.0,"end")
            self.te.insert(1.0,round_val)
            self.calculation= str(round_val)
        except:
            self.te.delete(1.0,"end")
            self.te.insert(1.0,"error")
            self.calculation=""
        
    def create_widgets(self):
        self.te = tk.Text(self.root, height=2, width=20, font=("arial", 24))
        self.te.grid(columnspan=6)
        
        scibuttons = [
            ("round", self.roundoff), ("sqrt", self.handle_sqrt), ("X^2", self.square), ("X^x", self.rand_power), ("DEL", None), ("AC", self.clear_field),
            ("sin", self.handle_sin), ("cos", self.handle_cos), ("tan", self.handle_tan),("Log", self.log_ans), ("ln", self.ln_ans), ("e", self.e_val),
            ("Cosec", self.handle_cosec), ("sec", self.handle_sec), ("cot", self.handle_cot), ("Fact!", self.fact_value), ("ANS", self.ans_target), ("=", self.evaluate_expression)
        ]
        rowval = 1
        colval = 0
        for va, command in scibuttons:
            b = tk.Button(self.root, text=va, font=("arial", 11), width=3, command=command)
            b.grid(row=rowval, column=colval, sticky="nsew", padx=3, pady=2)
            colval += 1
            if colval > 5:
                colval = 0
                rowval += 1
        
        buttons = [
            "7", "8", "9", "(", ")",
            "4", "5", "6", "*", "/",
            "1", "2", "3", "+", "-",
            "0", ".","_"
        ]
        row_val = 4
        col_val = 0
        for nums in buttons:
            b = tk.Button(self.root, text=nums, font=("arial", 15), width=4, command=lambda num=nums: self.add_to_calc(num))
            b.grid(row=row_val, column=col_val, sticky="nesw")
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1
        
        equals_button = tk.Button(self.root, text="=", font=("arial", 15), width=16, command=self.evaluate_expression)
        equals_button.grid(row=row_val, column=3, columnspan=3, sticky="w")
        
        equals_but = tk.Button(self.root, text="""mode """,font=("arial",15), width=5, height=5)
        equals_but.grid(row=4, column=5, rowspan=3, sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
