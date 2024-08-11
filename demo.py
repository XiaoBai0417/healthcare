import requests

# 发送API请求
def send_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return {'url': url, 'result': response.json()}
    except requests.RequestException as e:
        return {'url': url, 'result': {'error': str(e)}}

def main(file_name):
    results = []
    with open(file_name, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    for url in urls:
        result = send_request(url)
        results.append(result)
    return results

if __name__ == '__main__':
    results = main('./api_links.txt')
    print(results)
