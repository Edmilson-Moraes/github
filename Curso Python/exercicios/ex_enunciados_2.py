"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, boa tarde 12:17 e Boa noite 18:23
"""
import datetime as dt
hora = dt.datetime.now().hour
print(f"São {hora} horas.", "bom dia" if hora < 12 else "boa tarde" if hora < 18 else "boa noite")