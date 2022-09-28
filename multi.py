"""
Entendendo na prática como funciona o multithreading,
para usar no crawler de telefones.
"""


from time import sleep
from threading import Thread


def fazer_requisição_web():
    print('Fazendo requisição web...')
    sleep(5)
    print('Terminei a requisição')


thread1 = Thread(target=fazer_requisição_web)
thread1.start()

print('Passou por aqui antes de terminar a requisição da thread1')

thread2 = Thread(target=fazer_requisição_web)
thread2.start()

print('Passou por aqui antes de terminar a requisição da thread2')

thread3 = Thread(target=fazer_requisição_web)
thread3.start()

print('Passou por aqui antes de terminar a requisição da thread3')