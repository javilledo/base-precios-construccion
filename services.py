
import requests

URL_ROOT_ADIF = "https://bpa.adif.es/bp1/findCategoryByConceptCode?conceptCode=R_A_I_Z%23%23"

def getRootADIF():
    
    response = requests.get(URL_ROOT_ADIF, verify=False)
    
    if response.status_code == 200:
        data = response.json()
    else:
        print(f'Error: {response.status_code}')
    
    return data