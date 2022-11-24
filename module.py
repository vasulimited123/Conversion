import yaml
from yaml.loader import SafeLoader
import json
import configparser

filepath = input("Please Enter the file path....\n")

def read_write(filepath):
    """
    Here user's filepath will be taken as input and according to extension it will go to
    specific if-else condition. And file will be generated.
    """
    # Check the extension of file.
    file_extension = filepath.split(".")[-1]
    if file_extension == "yml" or file_extension == "yaml":
        with open(filepath) as f:
            data = yaml.load(f, Loader=SafeLoader)
        with open('yml_to_json.json','w') as json_file:
            json.dump(data, json_file)
        print("Yml to json has been converted. File name world be yml_to_json.json")
    
    
    elif file_extension == "conf":
        f = open(filepath, "r")
        lines = f.readlines()
        # Conversion of .conf to .env 
        new_lines =[]
        for line in lines:
            if line == "":
                pass
            else:
                line = line.replace("\n","")
                line = line.replace(";","")
                line = line.strip()
                line = line.replace(" "," = ")
                if line == "" or "#" in line:
                    pass
                else:
                    new_lines.append(line)
        st = ""
        m = 0
        for i in range(m,len(new_lines)):
            with open("conf_to_env.env","a+") as file:
                if "{" in new_lines[i]:
                    st = st + new_lines[i] + "\n"
                    for j in range(i+1,len(new_lines)):
                        st = st + new_lines[j] + "\n"
                        if "}" in new_lines[j]:
                            m =j
                            break
                    file.write(st)
                    st = "" 
                else:
                    if (m + 1) > i:
                        pass
                    else:
                        file.write(new_lines[i])
                        file.write("\n") 
                file.close()  
        print("Conf to env has been converted") 
        
    # Conversion of .cfg,.ini file into .env
    elif file_extension == "cfg" or file_extension == "ini":
        parser = configparser.ConfigParser()
        parser.read(filepath)
        for sect in parser.sections():
            print('Section:', sect)
            with open("cfg_to_env.env","a+") as file:
                for k,v in parser.items(sect):
                    file.write(' {} = {}'.format(k,v))
        print("Conf to env has been converted")            
    
read_write(filepath)