import requests

def main():
    headers = {
        'Content-Type': 'application/json'
    }
    sample_dict = {"year":2021,"month":10,"stateDescription":42,"sectorName":2}
    url = "http://0.0.0.0:4000/predict"
    post_response = requests.post(url, json=sample_dict,headers=headers)
    print(post_response.status_code)
    print(post_response.content)


if __name__ == "__main__":
    main()