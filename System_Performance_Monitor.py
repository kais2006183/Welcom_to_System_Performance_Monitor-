"""That's a program to know 
about your compeuter """
import psutil
import os
import subprocess
print("=== Welcom to System Performance Monitor ===")

def User_chois () :
    while True :
        chiose = input("Pleas choose what you need  : \n1 - check the memory status \n2 - Cleaning temporary files \n3 - Get OS info (C++)\n4 - Exit\n")
        if chiose == "1" :

            Total_pytes = psutil.virtual_memory().total / 1024 ** 3
            Total_pytes = round(Total_pytes, 2)

            Total_pytes_free = psutil.virtual_memory().free / 1024 ** 3
            Total_pytes_free = round(Total_pytes_free, 2)

            Total_pytes_available = psutil.virtual_memory().available / 1024 ** 3
            Total_pytes_available = round(Total_pytes_available, 2)

            Total_percent = psutil.virtual_memory().percent

            Total_pytes_Used = psutil.virtual_memory().used / 1024 ** 3
            Total_pytes_Used = round(Total_pytes_Used, 2)
            
            return f"ok Ther is Your memory status : \nTotal GB : {Total_pytes}GB \nAvailable mem : {Total_pytes_available}GB\nPercent : {Total_percent}%\nUsed : {Total_pytes_Used}GB\nFree mem : {Total_pytes_free}GB"

        elif chiose == "2" :

            temp_path = os.environ.get('TEMP')
            files = os.listdir(temp_path) 
            for file in files :
    
                full_path = os.path.join(temp_path, file)
                try :
                        os.remove(full_path)

                        print(f"Deleted: {file}")

                except Exception :
                    pass 

            return "=== Cleaning Process Finished Successfully! ==="
        
        elif chiose == "3" :
            cpp_output = subprocess.check_output("sys_info.exe")
            clean = cpp_output.decode()
            
        
            return f"OS Info from C++: {clean}"
        elif chiose == "4" :
            return "Ok, Thank you Please rate our app for more professional work !!"

        else :
            print("=" * 50)
            print("Warning, Invaild Choise Please Choose '1', '2' or '3', Try again .")
            print("=" * 50)


ch = User_chois()
print(ch)