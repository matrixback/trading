# -*- coding: utf-8 -*-

from utils import get_cur_price, send_mail
import time
import arrow

from config import CRAWL_INTERNAL

def main():
    while True:
        f = open('price.log', 'a')
        cur_time = arrow.now().to('local').format('YYYY-MM-DD HH:mm:ss')
        eos_price = get_cur_price('eos_usdt')
        f.write('{},{}\n'.format(cur_time, eos_price))
        print eos_price
        if eos_price < 125:
           msg = u'时间：{}， 当前价格：{}\n, drop it quickly!'.format(cur_time, eos_price)
           send_mail(msg)
        time.sleep(CRAWL_INTERNAL)

main()