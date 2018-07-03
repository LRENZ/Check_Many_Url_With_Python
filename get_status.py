import requests
from mongoengine import *
import pandas as pd
import os
import  click
import yagmail
import multiprocessing as mp

connect(
    db='urlcheck_5',
)

import datetime

def geturllist():
    df = pd.read_table('remove.txt', encoding="ISO-8859-1", names=['url'])
    df.drop_duplicates()
    return df['url'].tolist()

class Domain(DynamicDocument):
    status_code = StringField()
    #keyword = StringField()
    url = StringField()
    final_url = StringField()
    #time = DateTimeField()
    is_requests = BooleanField()


def get_status_code(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        r = requests.get(convert(url), headers=headers, timeout = 5)
            # print(r.status_code)
        return (str(r.status_code),str(r.url))
        # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        #print("failed to connect")
        return "failed to connect"

def getkeyword(url):
    pass

def savestatus(url):
    try:
        if  Domain.objects(url=url).first():
            print('Already in Database')

        else:
            status = get_status_code(convert(url))[0]
            final_url = get_status_code(convert(url))[1]
            Domain(status_code=str(status),
                   # keyword='test1',
                   url=str(url),
                   final_url=final_url,
                   # time=datetime.datetime.now(),
                   is_requests=True).save()
            print('{} : {}   has saved \n'.format(str(status), str(url)))


    except:
        print('save fail')

def getcsv():
    d = Domain.objects().all()
    data = [(x.url, x.status_code,x.final_url,x.is_requests) for x in d]
    df1 = pd.DataFrame(data, columns=['url', 'status_code','final_url','is_requests'])
    df1.drop_duplicates()
    df1.to_csv('urlcheck.csv')
    return df1.shape


	
def convert(url):
    if url.startswith('https://www.'):
        return url
    if url.startswith('http://www.'):
        return 'http://' + url[len('http://www.'):]
    if url.startswith('www.'):
        return 'http://' + url[len('www.'):]
    if not url.startswith('http://'):
        return 'http://' + url
    return url



@click.command()
@click.option('--dele', default='no_del',prompt='( del ) To Delete,( no_del ) To Hold On, Default no_del', help='del Or no_del' )

def deleted(dele):
    if dele == 'del':
        d = Domain.objects().all()
        for x in d:
            d.delete()
        print('delete all records in database')
        return run()
    else:
        return run()


def run():
    
    urllist = geturllist()
    pool = mp.Pool(processes=8)
    p = pool.map(savestatus,urllist)
    pool.close()
    pool.join()
    shape = getcsv()



if __name__ == '__main__':
    deleted()

    




