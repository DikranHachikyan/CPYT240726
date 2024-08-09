import re


if __name__ == '__main__':
    
    log = '''
151.251.254.45 - - [13/Jul/2024:02:09:00 +0300] "GET /wp-content/uploads/2022/11/cropped-cropped-logo_trainingcenter-120x120-1-200x200.png HTTP/3.0" st=200 bd=7440 "https://expert-bg.org/?fbclid=IwZXh0bgNhZW0CMTEAAR19airoQAeC9ZwBjzqSdW8zkv8AJ6LVYfGbOO58383Vo5W3rsCuta4R3TQ_aem_3aJS9fcHqn02t-sfjG5wpQ" "Mozilla/5.0 (Linux; Android 14; SM-S918B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/470.0.0.61.82;]"rt=0.002 uct="-" uht="-" urt="-"
'''

    regex = r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s.+GET\s(?P<url>.*?)\s'
    
    pattern = re.compile(regex, re.M)

    for match in re.finditer( pattern, log):
        # print(f'span:{match.span()}')
        ip, url = match.group('ip'), match.group('url')
        print(f'request ip:{ip} url:{url}')
    
    print('--- end ---')