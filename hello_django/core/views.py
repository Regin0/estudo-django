from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, você tem {idade} anos, correto?</h1>')

def soma(request, numero1, numero2):
    resultado = numero1 + numero2
    return HttpResponse(f'<h1>A soma de {numero1} + {numero2} é igual a: {resultado} </h1>')


def sub(request, numero1, numero2):
    resultado = numero1 - numero2
    return HttpResponse(f'<h1>A subtração de {numero1} - {numero2} é igual a: {resultado} </h1>')

def divisao(request, numero1, numero2):
    resultado = numero1 / numero2
    return HttpResponse(f'<h1>A divisão de {numero1} / {numero2} é igual a: {resultado} </h1>')


def multi(request, numero1, numero2):
    resultado = numero1 * numero2
    return HttpResponse(f'<h1>A multiplicação de {numero1} x {numero2} é igual a: {resultado} </h1>')