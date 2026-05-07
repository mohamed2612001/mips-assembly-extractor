import re
import pandas as pd

# patterns to get the address, code, and the remainder from each line 
base_pattern = re.compile(r'^(0x[0-9a-fA-F]+)\s+(0x[0-9a-fA-F]+)(.*)$')

# Looks for digits, spaces, then get the source code 
source_pattern = re.compile(r'\d+\s+([a-zA-Z_\.].*)$') 


parsed_data = []


file_path = r"D:\project_arch\text_segment.txt"

try:

    with open(file_path, 'r',) as f:
        for line in f:
            line = line.strip() # remove \n, \r
            
    
            if not line or line.startswith('Address'):
                continue
                
            match = base_pattern.match(line)
            if match:
                address = match.group(1)
                code = match.group(2)
                remainder = match.group(3).strip()
                
           
                # Search the remainder of the line for the actual source code
                source_match = source_pattern.search(remainder)
                if source_match:
                    source = source_match.group(1).strip()
                    parsed_data.append({"Address": address, "Code": code, "Source": source})
            
         

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")

# load into a Pandas DataFrame
df = pd.DataFrame(parsed_data)

# Print the result 
if df.empty:
    print("\nThe DataFrame is empty. Please check the file contents.")
else:
    print("\nData extracted successfully:\n")
    print(df)
df.to_excel(r"D:\project_arch\parsed_data.xlsx", index=False)
    

