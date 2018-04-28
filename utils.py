# -*- coding: utf-8 -*-

from urlparse import urljoin
import requests
import pprint
import arrow

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from config import history_base_url, mark_list_url, USDT_PRICE, MAIL_ADDR, MAIL_PASSWD

def get_traded_history(pair):
    url = urljoin(history_base_url, pair)
    r = requests.get(url)
    pprint.pprint(r.json())
    trade_list = r.json()['data']
    for trade in trade_list:
        time = arrow.get(trade['timestamp']).to('local').format('YYYY-MM-DD HH:mm:ss')
        rate = trade['rate']
        total = trade['total']
        type = trade['type']
        print time, type, rate, total

    print len(trade_list)


def get_marklist():
    url = mark_list_url
    r = requests.get(url)
    mark_list = r.json()['data']
    return mark_list

def get_cur_price(pair):
    mark_list = get_marklist()
    for coin_info in mark_list:
        if coin_info['pair'] == pair:
            return float(coin_info['rate']) * USDT_PRICE

    return -1



def send_mail(message, to=MAIL_ADDR):
    server = smtplib.SMTP("smtp.163.com", 25)
    server.set_debuglevel(3)
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(u'EOS 价格')
    server.login(MAIL_ADDR, MAIL_PASSWD)
    server.sendmail(msg=msg.as_string(), from_addr=MAIL_ADDR, to_addrs=[to] )
    server.quit()


if __name__ == '__main__':
    pprint.pprint(get_marklist())