import PySimpleGUI as sg
import PySimpleGUIQt as qt
from datetime import date
from Qfree import *
from BD import *
import sys
import ctypes


user32 = ctypes.windll.user32
screen_x = user32.GetSystemMetrics(0)
screen_y = user32.GetSystemMetrics(1)


def menu(Numero_Q,num):


    dados = Dados()
    if dados.q_id[num].text ==  read_data(dados.q_id[num].text):
        text = 'Já resolvida!'
        font="comic 7"
        text_color = 'blue'

    elif dados.q_id[num].text !=  read_data(dados.q_id[num].text) and dados.q_id[num].text == read_datat(dados.q_id[num].text) :
        text = 'Resolvi errado!'
        font="comic 7"
        text_color = 'dark red'

    else:
        text = ''
        font="comic 0"
        text_color = 'dark blue'


    layout = [[qt.Btn(image_filename='.\\imagens\\btn_green.png',size_px=(6,6)),qt.Btn(image_filename='.\\imagens\\btn_orange.png',size_px=(6,6))],
    [qt.Text(Numero_Q,font="comic 12 ",background_color='white',text_color = 'blue'),qt.Text(text = text,font= font,background_color='white',text_color = text_color)],
    [qt.Ok(button_text="Certo",auto_size_button=True),qt.Cancel(button_text="Errado",auto_size_button=True)]]
    
    janela = qt.Window('Resposta',layout,location=(screen_x/2.4,screen_y/1.23),no_titlebar=True,keep_on_top=True,font="comic 13 bold"
    					,background_color='white',alpha_channel=0.80,auto_size_text=True)#transparent_color='#FFFFFF'
    a,b = janela.Read()#transparent_color='#FFFFFF'
    a,b = janela.Read()    

    if a == 'Certo':
        janela.close()
        return 1
    elif a =='Errado':
        janela.close()
        return 0
    elif a =='':
    	janela.close()
    	iniciar()
    elif a =='0':
    	janela.close()
    	iniciar()


def acertou():
    
    layout = [[qt.Text('',size=(0,0))]]
    janela = qt.Window('Login',layout=layout,background_image='.\imagens\certo.png',size=(350,114),no_titlebar=True
                       ,alpha_channel=0.80,keep_on_top=True,grab_anywhere=True,auto_close_duration=1.7,
                       auto_close=True,location=(screen_x/1.5,screen_y/1.5),background_color='#FFFFFF')
    
    a,b = janela.read()
    janela.close()
    return b

def errou():

    
    layout = [[qt.Text('',size=(0,0))]]
    janela = qt.Window('Login',layout=layout,background_image='.\imagens\errado.png',size=(350,110),no_titlebar=True
                       ,alpha_channel=0.80,keep_on_top=True,grab_anywhere=True,auto_close_duration=1.7,
                       auto_close=True,location=(screen_x/11,screen_y/1.52),background_color='#FFFFFF')
    
    a,b = janela.read()
    janela.close()
    return b


def expirado():
    layout = [[sg.Text('Licença expirada',font="comic 13 bold",background_color='white',text_color="dark blue")]]
    janela = sg.Window('Erro',layout=layout,keep_on_top=True,background_color='white')
    janela.Read()


#if date.today().month < 12 and date.today().year == 2019:
#    pass
#else:
#	expirado()
#	sys.exit(1)



def iniciar():

	estatistica()

	while True:

		dados = Dados()

		logica = Logica()


		try:
			if logica.alfa() == menu('Questao '+dados.numero[0].text+':',0):
				acertou()
				Eacerto.append('A')
				data_entry(dados.q_id[0].text,'0','0')
				data_entry_total(dados.q_id[0].text,'0','0')
			else:
				errou()
				Eerro.append('A')
				data_entry_total(dados.q_id[0].text,'0','0')
		except:
			pass

		
		try:
			if logica.bravo() == menu('Questao '+dados.numero[1].text+':',1):
				acertou()
				Eacerto.append('A')
				data_entry(dados.q_id[1].text,'0','0')
				data_entry_total(dados.q_id[1].text,'0','0')
			else:
				errou()
				Eerro.append('A')
				data_entry_total(dados.q_id[1].text,'0','0')
		except:
			pass


		try:
			if logica.charlie() == menu('Questao '+dados.numero[2].text+':',2):
				acertou()
				Eacerto.append('A')
				data_entry(dados.q_id[2].text,'0','0')
				data_entry_total(dados.q_id[2].text,'0','0')
			else:
				errou()
				Eerro.append('A')
				data_entry_total(dados.q_id[2].text,'0','0')
		except:
			pass


		try:
			if logica.delta() == menu('Questao '+dados.numero[3].text+':',3):
				acertou()
				Eacerto.append('A')
				data_entry(dados.q_id[3].text,'0','0')
				data_entry_total(dados.q_id[3].text,'0','0')
			else:
				errou()
				Eerro.append('A')
				data_entry_total(dados.q_id[3].text,'0','0')
		except:
			pass


		try:
			if logica.echo() == menu('Questao '+dados.numero[4].text+':',4):
				acertou()
				Eacerto.append('A')
				data_entry(dados.q_id[4].text,'0','0')
				data_entry_total(dados.q_id[4].text,'0','0')
			else: 
				errou()
				Eerro.append('A')
				data_entry_total(dados.q_id[4].text,'0','0')
		except:
			pass


		try:
			chrome.get(chrome.find_element_by_css_selector("a.q-next.btn.btn-default").get_attribute('href'))
		except:
			iniciar()
					
		chrome.execute_script("for(let i = 0; i < document.getElementsByClassName('q-icon q-icon-bar-chart').length; i++){document.getElementsByClassName('q-icon q-icon-bar-chart')[i].click()}")
		sleep(2)
	



iniciar()



