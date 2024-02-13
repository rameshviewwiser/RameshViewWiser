import re
from datetime import datetime

responses=[]
urls=[]

c=0
c1=0
c2=0

file_path = "details.txt"                

            
log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d+\.\d+\.\d+\.\d+) - (\w+) (\S+) - (\d+)')

with open(file_path, "r") as file:
        for line in file:
            
             #print(line.strip()) 
            match = log_pattern.match(line) 
            if match:
                # Extract components from the matched groups
                log_date_time_str, ip_address, http_method, url, status_code = match.groups()

                responses.append(status_code)
                data=url.split("/")[-1]
               
                if data not in urls:
                    urls.append(data)
                      
            else:
                print("Log entry does not match the expected format.")


for i in responses:
    i=int(i)
    if i==200:
          c=c+1
    elif i==404:
          c1=c1+1
    else:
         c2=c2+1




print("Total errors : ",(c1+c2))
print("Error code 200 : ",c)
print("Error code 404 : ",c1)
print("Error code 500 : ",c2)

for i in urls:
    print(f"api/v1/organisations/"+i)












# log_entry = "2024-02-05 23:19:30 - 254.188.10.174 - DELETE /api/v1/organisations - 500"

# log_date_time = datetime.strptime(log_date_time_str, "%Y-%m-%d %H:%M:%S")  #25 line

# # Match the log entry against the pattern
# match = log_pattern.match(log_entry)

# if match:
#     # Extract components from the matched groups
#     log_date_time_str, ip_address, http_method, url, status_code = match.groups()

#     # Convert the date and time string to a datetime object
#     log_date_time = datetime.strptime(log_date_time_str, "%Y-%m-%d %H:%M:%S")

#     # Print the extracted information
#     print("Date and Time:", log_date_time)
#     print("IP Address:", ip_address)
#     print("HTTP Method:", http_method)
#     print("URL:", url)
#     print("Status Code:", status_code)
# else:
#     print("Log entry does not match the expected format.")

# path_components = url_path.split("/")

# # Extract the organization (assuming it's the last component)
# organization = path_components[-1]
