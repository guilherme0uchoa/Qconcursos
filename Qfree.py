from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import PySimpleGUI as sg
import PySimpleGUIQt as qt
from time import sleep
from BD import *


def login_gui():
    
    layout = [[qt.Text('',size=(0,0.1))],
              [qt.Text('Login',font="comic 12 bold",justification='center',text_color ='dark blue')],
              [qt.Text(''),qt.InputText(default_text='guilherme.uchoa@dr.com',font="comic 9 bold",justification='left',size=(36,1),text_color ='black',tooltip='Digite seu email Qconcursos'),qt.Text('')],
              [qt.Text('',size=(0,0.2))],
			  [qt.Text('Senha',font="comic 12 bold",justification='center',text_color ='dark blue')],
              [qt.Text(''),qt.InputText(default_text='guga1993',password_char='*',justification='left',size=(36,1),text_color ='black',tooltip='Digite sua senha Qconcursos'),qt.Text('')],
              [qt.Text('',size=(0,0.3))],
              [qt.Text(''),qt.OK('Acessar',size=(11,1),font="comic 10 bold"),qt.Text('')],
			  [qt.Text('',size=(0,0.1))]]


    janela = qt.Window('Login',layout=layout,size=(300,100),
    	no_titlebar=True,alpha_channel=0.85,keep_on_top=True,grab_anywhere=True)
    
    a,b = janela.read()
    janela.close()
    return b

#receptor de link
def menu_link():
	
	tab1_layout = [[qt.Text('Insira o Link',font="comic 12 bold",text_color="dark blue")],[qt.InputText()],
	[qt.Text('Acertos:',text_color="dark blue"),qt.Text(len(Eacerto))],[qt.Text('Erros:',text_color="dark red"),qt.Text(len(Eerro))],
	[qt.OK()]]

	try:
		certo_ = total_data_acertos()
		errado_ = total_data_total()-total_data_acertos()
		total_ = total_data_total()
		cespe_ = ((certo_ - errado_)/total_)*100
		outra_ = (certo_/total_)*100
		quadrix_ = ((((errado_/4)-certo_)/total_)*100)*-1
	except:
		certo_ = total_data_acertos()
		errado_ = total_data_total()-total_data_acertos()
		total_ = total_data_total()
		cespe_ = 0
		outra_ = 0
		quadrix_ = 0

	tab2_layout = [[qt.Text("")],
	[qt.Text('Total de acertos:',font="comic 12 bold",text_color="dark blue"),qt.Text(total_data_acertos())],
	[qt.Text('Total de erros:',font="comic 12 bold",text_color="dark blue"),qt.Text(total_data_total()-total_data_acertos())],
	[qt.Text('Total de questões:',font="comic 12 bold",text_color="dark blue"),qt.Text(total_data_total())]]

	tab3_layout = [[qt.Text("")],
	[qt.Text('Fator cespe:',font="comic 12 bold",text_color="dark blue"),qt.Text(''),qt.Text(int(cespe_)),qt.Text('%')],
	[qt.Text('Fator Quadrix:',font="comic 12 bold",text_color="dark blue"),qt.Text(''),qt.Text(int(quadrix_)),qt.Text('%')],
	[qt.Text('Banca diversa:',font="comic 12 bold",text_color="dark blue"),qt.Text(''),qt.Text(int(outra_)),qt.Text('%')]]


	layout = [[qt.TabGroup([[qt.Tab('Link', tab1_layout), qt.Tab('Histórico', tab2_layout),qt.Tab('Fator de Correção', tab3_layout)]],title_color='dark blue')]]

	janela = qt.Window('Link',layout,location=(0,0),no_titlebar=False,keep_on_top=True,alpha_channel=0.85,size=(350,114))

	a,b = janela.Read()

	janela.close()   

	return b[0]


options = Options()
options.add_argument('headless')
options.add_argument('disable-gpu')
#Login
logg= login_gui()

chrome = webdriver.Chrome(chrome_options=options)

chrome.get('https://www.qconcursos.com/conta/entrar') #deixar aqui é melhor, primeiro realiza o formulario e ai carrega o login no site mais rapido

login = chrome.find_element_by_name('user[email]')
login.send_keys(logg[0])


senha = chrome.find_element_by_name('user[password]')
senha.send_keys(logg[1])

#clicar
chrome.find_element_by_css_selector('input.btn.btn-lg.btn-primary.btn-block').click()

Eacerto=[]
Eerro=[]

#Estatisticas das questoes 
def estatistica():
	chrome.get(menu_link())
	#Executa esse codigo JS para abrir todas as estatisticas (Saber mais linguagens de programação te torna melhor)
	chrome.execute_script("for(let i = 0; i < document.getElementsByClassName('q-icon q-icon-bar-chart').length; i++){document.getElementsByClassName('q-icon q-icon-bar-chart')[i].click()}")
	sleep(2)	
#Scrapy de dados

class Dados:

	def __init__(self):		
		#Dados gerais
		
		try:
			self.dados0 = chrome.find_elements_by_css_selector('#js-income-percentage-chart')[0]
			self.dados2_0 = chrome.find_elements_by_css_selector('#js-most-answered-alternatives-chart')[0]
		except:
			pass
		try:
			self.dados1 = chrome.find_elements_by_css_selector('#js-income-percentage-chart')[1]
			self.dados2_1 = chrome.find_elements_by_css_selector('#js-most-answered-alternatives-chart')[1]
		except:
			pass
		try:
			self.dados2 = chrome.find_elements_by_css_selector('#js-income-percentage-chart')[2]
			self.dados2_2 = chrome.find_elements_by_css_selector('#js-most-answered-alternatives-chart')[2]
		except:
			pass
		try:
			self.dados3 = chrome.find_elements_by_css_selector('#js-income-percentage-chart')[3]
			self.dados2_3 = chrome.find_elements_by_css_selector('#js-most-answered-alternatives-chart')[3]
		except:
			pass
		try:
			self.dados4 = chrome.find_elements_by_css_selector('#js-income-percentage-chart')[4]
			self.dados2_4 = chrome.find_elements_by_css_selector('#js-most-answered-alternatives-chart')[4]
		except:
			pass

		self.q_id = chrome.find_elements_by_class_name('q-id')
	
		#Dados



		try:
			self.acertos0 =float( self.dados0.get_attribute('data-hits'))#porcentagem de acertos
			self.erros0 =float( self.dados0.get_attribute('data-mistakes'))#porcentagem de erros
			self.certo0 =int ( self.dados2_0.get_attribute('data-alternatives-count').split()[2][:-1])#quantidade de certos
			self.errado0 =int ( self.dados2_0.get_attribute('data-alternatives-count').split()[4])#quantidade de errado
		except:
			pass


		#Dados_1

		try:
			self.acertos1 =float( self.dados1.get_attribute('data-hits'))#porcentagem de acertos
			self.erros1 =float(self.dados1.get_attribute('data-mistakes'))#porcentagem de erros
			self.certo1 =int ( self.dados2_1.get_attribute('data-alternatives-count').split()[2][:-1])#quantidade de certos
			self.errado1 =int ( self.dados2_1.get_attribute('data-alternatives-count').split()[4])#quantidade de errado
		except:
			pass


		#Dados_2


		try:
			self.acertos2 =float( self.dados2.get_attribute('data-hits'))#porcentagem de acertos
			self.erros2 =float( self.dados2.get_attribute('data-mistakes'))#porcentagem de erros
			self.certo2 =int ( self.dados2_2.get_attribute('data-alternatives-count').split()[2][:-1])#quantidade de certos
			self.errado2 =int ( self.dados2_2.get_attribute('data-alternatives-count').split()[4])#quantidade de errado
		except:
			pass


		#Dados_3


		try:
			self.acertos3 =float( self.dados3.get_attribute('data-hits'))#porcentagem de acertos
			self.erros3 =float( self.dados3.get_attribute('data-mistakes'))#porcentagem de erros
			self.certo3 =int ( self.dados2_3.get_attribute('data-alternatives-count').split()[2][:-1])#quantidade de certos
			self.errado3 =int ( self.dados2_3.get_attribute('data-alternatives-count').split()[4])#quantidade de errado
		except:
			pass


		#Dados_4

		try:
			self.acertos4 =float( self.dados4.get_attribute('data-hits'))#porcentagem de acertos
			self.erros4 =float( self.dados4.get_attribute('data-mistakes'))#porcentagem de erros
			self.certo4 =int ( self.dados2_4.get_attribute('data-alternatives-count').split()[2][:-1])#quantidade de certos
			self.errado4 =int ( self.dados2_4.get_attribute('data-alternatives-count').split()[4])#quantidade de errado
		except:
			pass



		#Numero da questao

		self.numero=chrome.find_elements_by_class_name('q-index')


#Logica coração s2

class Logica:

	def __init__(self):
		Dados.__init__(self)

	
	def alfa(self):

		if self.acertos0 > self.erros0:
			if self.certo0 > self.errado0:
				return 1
			if self.certo0 < self.errado0:
				return 0
		else:
			if self.certo0 > self.errado0:
				return 0
			if self.certo0 < self.errado0:
				return 1

	def bravo(self):

		if self.acertos1 > self.erros1:
			if self.certo1 > self.errado1:
				return 1
			if self.certo1 < self.errado1:
				return 0
		else:
			if self.certo1 > self.errado1:
				return 0
			if self.certo1 < self.errado1:
				return 1

	def charlie(self):

		if self.acertos2 > self.erros2:
			if self.certo2 > self.errado2:
				return 1
			if self.certo2 < self.errado2:
				return 0
		else:
			if self.certo2 > self.errado2:
				return 0
			if self.certo2 < self.errado2:
				return 1

	def delta(self):

		if self.acertos3 > self.erros3:
			if self.certo3 > self.errado3:
				return 1
			if self.certo3 < self.errado3:
				return 0
		else:
			if self.certo3 > self.errado3:
				return 0
			if self.certo3 < self.errado3:
				return 1

	def echo(self):

		if self.acertos4 > self.erros4:
			if self.certo4 > self.errado4:
				return 1
			if self.certo4 < self.errado4:
				return 0
		else:
			if self.certo4 > self.errado4:
				return 0
			if self.certo4 < self.errado4:
				return 1