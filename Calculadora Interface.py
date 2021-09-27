import PySimpleGUI as sg
sg.theme('Black')
class Calculadora:
    def __init__(self):
# ---layout--- elementos dentro da janela.
        self.layout = [
            [sg.Sizegrip('-------------------')],
            [sg.Text('Valor 1:'),sg.Input(do_not_clear=True,size=(10,0,),key='valor1')],
            [sg.Radio(' +','radio1' ,key='soma')],
            [sg.Radio(' -', 'radio1',key='sub')],
            [sg.Radio(' *','radio1',key='mult')],
            [sg.Radio(' /','radio1',key='div')],
            [sg.Text('Valor 2:'),sg.Input(do_not_clear=True,size=(10,0),key='valor2')],
            [sg.Text('')],
            [sg.Button('Resultado')],
            [sg.Sizegrip('-------------------')],
            [sg.Text('')],
            [sg.Exit('Sair')],
            [sg.Text('')],
            [sg.Text('                                               J. Rafael')]
        ]

#  ---JANELA--- definindo o tamanho da janela, e posicionamento dos elementos.
        self.janela = sg.Window('Calculadora Simples', size=(270,350), element_justification='Center').layout(self.layout)


# ---EXTRAINDO DADOS DA JANELA---
#O LOOP WHILE SERVE PARA MANTER A JANELA SEMPRE ABERTA
#ATÉ QUE O USUARIO FECHE.


        while True:
            self.button, self.values = self.janela.read()
            if self.button == 'Resultado':
                if (self.values['valor1'] == '') and (self.values['valor2'] == '') and self.values['valor1'] not in ['1234567890'] and self.values['valor2'] not in ['1234567890']:
                    sg.popup_auto_close('Valores inválidos. :(\n\n O programa será finalizado.')
                    break
            valor1 = self.values['valor1']
            valor2 = self.values['valor2']
            soma = self.values['soma']
            sub = self.values['sub']
            mult = self.values['mult']
            div = self.values['div']
            if self.button == 'Sair':
                sg.popup_auto_close('Nunca é um adeus!')
                break
            else:
                valor_1 = float(valor1)
                valor_2 = float(valor2)


            if self.button == 'Resultado':
                if soma == True:
                    sg.popup_auto_close(f'A soma deu: {(valor_1)+(valor_2)}')
                if sub == True:
                    sg.popup_auto_close(f'A subtração deu: {(valor_1)-(valor_2)}')
                if mult == True:
                    sg.popup_auto_close(f'A multiplicação deu: {(valor_1)*(valor_2):.4f}')
                if div == True:
                    sg.popup_auto_close(f'A divisão deu: {(valor_1)/(valor_2):.4f}')
                elif (soma == False) and (sub == False) and (mult == False) and (div == False):
                    sg.popup_auto_close('Selecione uma operação.')

#CHAMANDO A ---CLASSE--- CALCULADORA
#PARA QUE A TELA SEJA EXECUTADA.

tela = Calculadora()
