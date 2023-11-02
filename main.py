from subprocess import Popen, PIPE
import requests
def execute_return(cmd):
    args = cmd.split()
    proc = Popen(args, stdout=PIPE,stderr=PIPE)
    out, err, = proc.communicate()
    return out,err

def make_request(error):
    resp=requests.get("https://api.stackexchange.com/"+"/2.3/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(error))
    # print("response: " , resp)
    # print("response: " , resp.json())
    return resp.json()

def get_url(json_dict):
    url_list=[]
    count=0
    for i in json_dict['items']:
        count+=1
        if count>=3:
            break
        if i['is_answered']:
            # print(i['link'])
            url_list.append(i['link'])
        
        
    # print(url_list)
    import webbrowser
    for i in url_list:
        webbrowser.open(i)
        
# def open(url_list):
   
    
    
        
    
if __name__=="__main__":
    op, err = execute_return("python test.py")
    error_message=err.decode("utf-8").strip().split("\r\n")[-1]
    print(type(error_message))
    print(error_message)  
    if error_message:
        filter_err = error_message.split(":")
        # print("File Error: " , filter_err)
        # print("File Error: " , filter_err[0])
        # print("File Error: " , filter_err[1])
        json1 = make_request(filter_err[0])
        json2 = make_request(filter_err[1])
        json = make_request(error_message)
        # print("Json:",json)
        # print("Json1:",json1)
        # print("Json2:",json2)
        get_url(json1)
        get_url(json2)
        get_url(json)
    else :
        print("No Error")
        
        