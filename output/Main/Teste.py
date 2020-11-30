from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import PySimpleGUI as sg
import PySimpleGUIQt as qt
from time import sleep
from BD import *
import sys
import ctypes



user32 = ctypes.windll.user32
screen_x = user32.GetSystemMetrics(0)
screen_y = user32.GetSystemMetrics(1)


def menu(Numero_Q,num):

    text = 'Já resolvida!'
    font="comic 7 bold"
    text_color = 'blue'


    layout = [[qt.Btn(image_filename='.\\imagens\\btn_green.png',size_px=(6,6)),qt.Btn(image_filename='.\\imagens\\btn_orange.png',size_px=(6,6))],
    [qt.Text(Numero_Q,font="comic 12 ",background_color='white',text_color = 'blue'),qt.Text(text = text,font= font,background_color='white',text_color = text_color)],
    [qt.Ok(button_text="Certo",auto_size_button=True),qt.Cancel(button_text="Errado",auto_size_button=True)]]
    
    janela = qt.Window('Resposta',layout,location=(screen_x/2.4,screen_y/1.23),no_titlebar=True,keep_on_top=True,font="comic 13 bold"
    					,background_color='white',alpha_channel=0.80,auto_size_text=True,auto_size_buttons=True)#transparent_color='#FFFFFF'
    a,b = janela.Read()      


menu("Questão 10","10")