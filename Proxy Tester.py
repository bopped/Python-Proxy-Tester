# Proxy Tester.py
# developer: @bopped /// twtiter : @backdoorcook
import requests , json , time , threading , sys

#Current Ms display
def millis():
    return int(round(time.time() * 1000))

#Current Time
def getCurrentTime():
    return time.strftime("%H:%M:%S")



with open('proxies.json') as json_data_file:
    proxies = json.load(json_data_file)

with open('sites.json') as json_data_file:
    sites = json.load(json_data_file)


if proxies == []:
    print ('0 PROXIES LOADED!')
    exit()

if sites == []:
    print ("0 Sites LOADED!")
    exit()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}
s = requests.session()
s.headers.update(headers)


if len(proxies) > 1:
    print '[%s] We currently have %s Proxies Loaded' % (getCurrentTime(),len(proxies))

elif len(proxies) == 1:
    print '[%s] We currently have %s Proxy Loaded' % (getCurrentTime(),len(proxies))



def sort(proxy,):
    proxies = {

        'http': 'http://' + proxy,

        'https': 'http://' + proxy

    }

    s.proxies.update(proxies)

    for site in sites:

        start = millis()

        try:
            response = s.get(site)

            if response.status_code == 200:

                sys.stdout.write('[%s] This thread is testing the following proxy: %s got an OK status on %s, it took %s MS to respond back \n' % (getCurrentTime(),(proxy),site,millis()-start))
                

            elif response.status_code != 200:

                sys.stdout.write('[%s] This thread is testing the following proxy: %s tested on %s , got a bad status, it took %s MS to respond back \n' % (getCurrentTime(), (proxy), site,millis() - start))


        except Exception as E:

            sys.stdout.write('[%s] This thread is testing the following proxy: %s tested on %s , did not return any status, it took %s MS to respond back \n' % (getCurrentTime(), (proxy), site, millis() - start))

threads = []

for i in range(len(proxies)):
    p = threading.Thread(target=sort, args=(proxies[i],))
    threads.append(p)
    p.start()
