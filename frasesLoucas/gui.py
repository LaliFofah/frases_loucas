import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import choice
# biblioteca de python para chamar APIs
import requests

# The API endpoint
original_url:str = "https://dictionary-api-pt.onrender.com"

m = tk.Tk()
frame1 = tk.Frame(m, width = 400, height = 400)
frame1.pack()
adjetivo = tk.StringVar()
nomeComum1 = tk.StringVar()
nomeComum2 = tk.StringVar()
nomeComum3 = tk.StringVar()
nomeComum4 = tk.StringVar()
nomeComum5 = tk.StringVar()
nomeColetivo = tk.StringVar()
nomeProprio = tk.StringVar()
verbo1 = tk.StringVar()
verbo2 = tk.StringVar()
pronome1 = tk.StringVar()
pronome2 = tk.StringVar()
adverbio = tk.StringVar()
frase = ['','','','','']
randomNum = 0

# funcao para verificar se a palavra pertence à classe de palavras que queremos
def check_if_is_correct_word_class(palavra:str, classe_de_palavra:str) -> bool:

    # vai so chamar a api e pegar o resultado
    response = requests.get(f"{original_url}/api/{palavra}/{classe_de_palavra}") 
    # transforma o resultado em texto (o texto vai ser sempre true ou false)
    text_response = response.text
    if text_response == "true":
        return True
    else:
        return False

# escolhe a template de frase aleatoriamente
def pickFrase():
    global frase
    global pronome1, pronome2, verbo1, verbo2, adverbio, nomeComum1, nomeComum2, nomeComum3, nomeComum4, nomeComum5, nomeColetivo, adjetivo, nomeProprio
    global entry_labels
    global adjetivo_entry, nomeComum1_entry, nomeComum2_entry, nomeComum3_entry, nomeComum4_entry, nomeComum5_entry, nomeColetivo_entry, nomeProprio_entry, verbo1_entry, verbo2_entry, pronome1_entry, pronome2_entry, adverbio_entry
#    print(adjetivo_entry)
#    entry_labels = [adjetivo_entry, nomeComum1_entry, nomeComum2_entry, nomeComum3_entry, nomeComum4_entry, nomeComum5_entry, nomeColetivo_entry, nomeProprio_entry, verbo1_entry, verbo2_entry, pronome1_entry, pronome2_entry, adverbio_entry] 
    global sentence_labels
#    sentence_labels = [sentence_label, adjetivo_label, nomeComum1_label, nomeComum2_label, nomeComum3_label, nomeComum4_label, nomeComum5_label, nomeColetivo_label, nomeProprio_label, verbo1_label, verbo2_label, pronome1_label, pronome2_label, adverbio_label]
    '''frase = [
             f'{pronome1.get()} {verbo1.get()} {adverbio.get()} como {pronome2.get()} {nomeComum1.get()}', 
             f'se {pronome1} {verbo1} {nomeComum1} {pronome2} {verbo2} {nomeComum2}', 
             f'Sabes qual é a coisa que mais gosto em ti, {nomeProprio}? É o facto de seres {adverbio} {adjetivo}', 
             f'{pronome1} {nomeComum1} dançou salsa com {nomeComum2} enquanto usava um {nomeComum3} {adjetivo}', 
             f'Numa reviravolta bizarra, todos os {nomeComum1} do mundo formaram uma aliança para exigir {nomeComum2} 24 horas por dia, 7 dias por semana, {nomeComum3} com sabor a {nomeColetivo} e sessões obrigatórias de {nomeComum4} com humanos, declarando-se os senhores supremos da {nomeComum5}.'
             ]
    '''
    numFrases = [0, 1, 2, 3, 4]
    global randomNum
    randomNum = choice(numFrases)
    if (randomNum == 0):
        pronome1_label = tk.Label(frame2, text = 'Pronome', font=('calibre',15, 'bold'))
        pronome1_entry = tk.Entry(frame2,textvariable = pronome1, font=('calibre',15,'normal'))
        verbo1_label = tk.Label(frame2, text = 'Verbo', font=('calibre',15, 'bold'))
        verbo1_entry = tk.Entry(frame2,textvariable = verbo1, font=('calibre',15,'normal'))
        adverbio_label = tk.Label(frame2, text = 'Advérbio', font=('calibre',15, 'bold'))
        adverbio_entry = tk.Entry(frame2,textvariable = adverbio, font=('calibre',15,'normal'))
        pronome2_label = tk.Label(frame2, text = 'Pronome indefinido', font=('calibre',15, 'bold'))
        pronome2_entry = tk.Entry(frame2,textvariable = pronome2, font=('calibre',15,'normal'))
        nomeComum1_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum1_entry = tk.Entry(frame2,textvariable = nomeComum1, font=('calibre',15,'normal'))
        
        pronome1_label.pack()
        pronome1_entry.pack()
        verbo1_label.pack()
        verbo1_entry.pack()
        adverbio_label.pack()
        adverbio_entry.pack()
        pronome2_label.pack()
        pronome2_entry.pack()
        nomeComum1_label.pack()
        nomeComum1_entry.pack()

        submit_button = tk.Button(frame2, width=15, height = 2, text = 'Submit', command=submit_frase)
        submit_button.pack()
    elif (randomNum == 1):
        pronome1_label = tk.Label(frame2, text = 'Pronome', font=('calibre',15, 'bold'))
        pronome1_entry = tk.Entry(frame2,textvariable = pronome1, font=('calibre',15,'normal'))
        verbo1_label = tk.Label(frame2, text = 'Verbo', font=('calibre',15, 'bold'))
        verbo1_entry = tk.Entry(frame2,textvariable = verbo1, font=('calibre',15,'normal'))
        nomeComum1_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum1_entry = tk.Entry(frame2,textvariable = nomeComum1, font=('calibre',15,'normal'))
        pronome2_label = tk.Label(frame2, text = 'Pronome', font=('calibre',15, 'bold'))
        pronome2_entry = tk.Entry(frame2,textvariable = pronome2, font=('calibre',15,'normal'))
        verbo2_label = tk.Label(frame2, text = 'Verbo', font=('calibre',15, 'bold'))
        verbo2_entry = tk.Entry(frame2,textvariable = verbo2, font=('calibre',15,'normal'))
        nomeComum2_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum2_entry = tk.Entry(frame2,textvariable = nomeComum2, font=('calibre',15,'normal'))
        
        pronome1_label.pack()
        pronome1_entry.pack()
        verbo1_label.pack()
        verbo1_entry.pack()
        nomeComum1_label.pack()
        nomeComum1_entry.pack()
        pronome2_label.pack()
        pronome2_entry.pack()
        verbo2_label.pack()
        verbo2_entry.pack()
        nomeComum2_label.pack()
        nomeComum2_entry.pack()
        
        submit_button = tk.Button(frame2, width=15, height = 2, text = 'Submit', command=submit_frase)
        submit_button.pack()
    elif (randomNum == 2):
        nomeProprio_label = tk.Label(frame2, text = 'Nome Próprio', font=('calibre',15, 'bold'))
        nomeProprio_entry = tk.Entry(frame2,textvariable = nomeProprio, font=('calibre',15,'normal'))
        adverbio_label = tk.Label(frame2, text = 'Advérbio', font=('calibre',15, 'bold'))
        adverbio_entry = tk.Entry(frame2,textvariable = adverbio, font=('calibre',15,'normal'))
        adjetivo_label = tk.Label(frame2, text = 'Adjetivo', font=('calibre',15, 'bold'))
        adjetivo_entry = tk.Entry(frame2,textvariable = adjetivo, font=('calibre',15,'normal'))
        
        nomeProprio_label.pack()
        nomeProprio_entry.pack()
        adverbio_label.pack()
        adverbio_entry.pack()
        adjetivo_label.pack()
        adjetivo_entry.pack()
        
        submit_button = tk.Button(frame2, width=15, height = 2, text = 'Submit', command=submit_frase)
        submit_button.pack()
    elif (randomNum == 3):
        nomeComum1_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum1_entry = tk.Entry(frame2,textvariable = nomeComum1, font=('calibre',15,'normal'))
        nomeComum2_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum2_entry = tk.Entry(frame2,textvariable = nomeComum2, font=('calibre',15,'normal'))
        nomeComum3_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum3_entry = tk.Entry(frame2,textvariable = nomeComum3, font=('calibre',15,'normal'))
        adjetivo_label = tk.Label(frame2, text = 'Adjetivo', font=('calibre',15, 'bold'))
        adjetivo_entry = tk.Entry(frame2,textvariable = adjetivo, font=('calibre',15,'normal'))
        
        nomeComum1_label.pack()
        nomeComum1_entry.pack()
        nomeComum2_label.pack()
        nomeComum2_entry.pack()
        nomeComum3_label.pack()
        nomeComum3_entry.pack()
        adjetivo_label.pack()
        adjetivo_entry.pack()
        
        submit_button = tk.Button(frame2, width=15, height = 2, text = 'Submit', command=submit_frase)
        submit_button.pack()
    elif (randomNum == 4):
        nomeComum1_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum1_entry = tk.Entry(frame2,textvariable = nomeComum1, font=('calibre',15,'normal'))
        nomeComum2_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum2_entry = tk.Entry(frame2,textvariable = nomeComum2, font=('calibre',15,'normal'))
        nomeComum3_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum3_entry = tk.Entry(frame2,textvariable = nomeComum3, font=('calibre',15,'normal'))
        nomeComum4_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum4_entry = tk.Entry(frame2,textvariable = nomeComum4, font=('calibre',15,'normal'))
        nomeComum5_label = tk.Label(frame2, text = 'Nome Comum', font=('calibre',15, 'bold'))
        nomeComum5_entry = tk.Entry(frame2,textvariable = nomeComum5, font=('calibre',15,'normal'))
        nomeColetivo_label = tk.Label(frame2, text = 'Nome Coletivo', font=('calibre',15, 'bold'))
        nomeColetivo_entry = tk.Entry(frame2,textvariable = nomeColetivo, font=('calibre',15,'normal'))
        
        nomeComum1_label.pack()
        nomeComum1_entry.pack()
        nomeComum2_label.pack()
        nomeComum2_entry.pack()
        nomeComum3_label.pack()
        nomeComum3_entry.pack()
        nomeComum4_label.pack()
        nomeComum4_entry.pack()
        nomeComum5_label.pack()
        nomeComum5_entry.pack()
        nomeColetivo_label.pack()
        nomeColetivo_entry.pack()
        
        submit_button = tk.Button(frame2, width=15, height = 2, text = 'Submit', command=submit_frase)
        submit_button.pack()
        
# verifica se a frase é válida
def submit_frase():
    error_label = tk.Label(frame2, text = 'ERRO! A palavra que introduziu ou está na classe errada, ou não existe!', font=('calibre',15, 'bold'), foreground= 'red')
    global pronome1, pronome2, verbo1, verbo2, adverbio, nomeComum1, nomeComum2, nomeComum3, nomeComum4, nomeComum5, nomeColetivo, adjetivo, nomeProprio
    randomNum = 0
    if randomNum == 0:
        # A GET request to the API
        response_pronome1 = check_if_is_correct_word_class(pronome1.get(), "pronome")
        response_verbo1 = check_if_is_correct_word_class(verbo1.get(), "verbo")
        response_adverbio = check_if_is_correct_word_class(adverbio.get(), "adverbio")
        response_pronome2 = check_if_is_correct_word_class(pronome2.get(), "pronome indefinido")
        response_nomeComum1 = check_if_is_correct_word_class(nomeComum1.get(), "nome comum")
        
        if response_pronome1 == False or response_verbo1 == False or response_adverbio == False or response_pronome2 == False or response_nomeComum1 == False:
            error_label.pack()
            return
        
        frase[0] = f'{pronome1.get()} {verbo1.get()} {adverbio.get()} como {pronome2.get()} {nomeComum1.get()}'
        sentence = frase[0]
    elif randomNum == 1:
        response_pronome1 = check_if_is_correct_word_class(pronome1.get(), "pronome")
        response_verbo1 = check_if_is_correct_word_class(verbo1.get(), "verbo")
        response_verbo2 = check_if_is_correct_word_class(verbo2.get(), "verbo")
        response_pronome2 = check_if_is_correct_word_class(pronome2.get(), "pronome")
        response_nomeComum1 = check_if_is_correct_word_class(nomeComum1.get(), "nome comum")
        response_nomeComum2 = check_if_is_correct_word_class(nomeComum2.get(), "nome comum")
        
        if response_pronome1 == False or response_verbo1 == False or response_pronome2 == False or response_nomeComum1 == False or response_verbo2 == False or response_nomeComum2 == False:
            error_label.pack()
            return
        
        frase[1] = f'se {pronome1.get()} {verbo1.get()} {nomeComum1.get()} {pronome2.get()} {verbo2.get()} {nomeComum2.get()}'
        sentence = frase[1]
    elif randomNum == 2:
        response_adverbio = check_if_is_correct_word_class(adverbio.get(), "adverbio")
        response_adjetivo = check_if_is_correct_word_class(adjetivo.get(), "adjetivo")
        
        if response_adverbio == False or response_adjetivo == False:
            error_label.pack()
            return
        
        frase[2] = f'Sabes qual é a coisa que mais gosto em ti, {nomeProprio.get()}? É o facto de seres {adverbio.get()} {adjetivo.get()}'
        sentence = frase[2]
    elif randomNum == 3:
        response_nomeComum1 = check_if_is_correct_word_class(nomeComum1.get(), "nome comum")
        response_nomeComum2 = check_if_is_correct_word_class(nomeComum2.get(), "nome comum")
        response_nomeComum3 = check_if_is_correct_word_class(nomeComum3.get(), "nome comum")
        response_adjetivo = check_if_is_correct_word_class(adjetivo.get(), "adjetivo")
        
        if response_nomeComum1 == False or response_nomeComum2 == False or response_nomeComum3 == False or response_adjetivo == False:
            error_label.pack()
            return
        
        frase[3] = f'O {nomeComum1.get()} dançou salsa com {nomeComum2.get()} enquanto usava um {nomeComum3.get()} {adverbio.get()}'
        sentence = frase[3]
    elif randomNum == 4:
        response_nomeComum1 = check_if_is_correct_word_class(nomeComum1.get(), "nome comum")
        response_nomeComum2 = check_if_is_correct_word_class(nomeComum2.get(), "nome comum")
        response_nomeComum3 = check_if_is_correct_word_class(nomeComum3.get(), "nome comum")
        response_nomeComum4 = check_if_is_correct_word_class(nomeComum4.get(), "nome comum")
        response_nomeComum5 = check_if_is_correct_word_class(nomeComum5.get(), "nome comum")
        
        if response_nomeComum1 == False or response_nomeComum2 == False or response_nomeComum3 == False or response_nomeComum4 == False or response_nomeComum5 == False:
            error_label.pack()
            return
        
        frase[4] = f'Numa reviravolta bizarra, todos os {nomeComum1.get()} do mundo formaram uma aliança para exigir {nomeComum2.get()} 24 horas por dia, 7 dias por semana, {nomeComum3.get()} com sabor a {nomeComum4.get()}\n e sessões obrigatórias de {nomeComum5.get()} com humanos, declarando-se os senhores supremos da {nomeColetivo.get()}.'
        sentence = frase[4]
    global sentence_label
    sentence_label = ttk.Label(frame2, text=sentence)
    sentence_label.pack()
    voltar_btn = tk.Button(frame2, width=15, height = 2, text = 'Voltar', command = switch_to_frame1)
    voltar_btn.pack()
        
def gerarFrase():
    help_button.pack(side='right')
    for widget in frame2.winfo_children():
        if widget != button_gerar and widget != help_button:
            if type(widget) == Entry:
                widget.delete(0, tk.END)   
            widget.destroy()   
    pickFrase()
    
def help():
    switch_to_frame3()
    for widget in frame3.winfo_children():
        widget.destroy()   
    basic_help_label = tk.Label(frame3, text= 'Este programa cria frases loucas a partir do que insere nos campos gerados.\nVocê apenas tem de completar os campos corretamente, conforme pedido, e ver a frase louca que criou!') 
    voltar_btn = tk.Button(frame3, width=15, height = 2, text = 'Voltar', command = switch_to_frame2)
    basic_help_label.pack()
    voltar_btn.pack()
    
frame2 = tk.LabelFrame(m, width = 400, height = 400)
frame3 = tk.LabelFrame(m, width = 400, height = 400)

def switch_to_frame2():
    frame1.forget()
    frame3.forget()
    frame2.pack()
    
def switch_to_frame1():
    frame2.pack_forget()
    frame1.pack()
    
def switch_to_frame3():
    frame2.pack_forget()
    frame3.pack()

title_label = tk.Label(frame1, text = 'Frases Loucas', padx=10, pady=30,font=('calibre',20, 'bold'))
title_label.pack()
start_button = tk.Button(frame1, width=15, height = 2, text = 'Start', command=switch_to_frame2)
start_button.pack()

button_gerar = tk.Button(frame2, width=15, height = 2, text = 'Gerar', command = gerarFrase)
button_gerar.pack()

help_button = tk.Button(frame2, text = '?', height = 2, width= 2, padx = 2, pady= 2,command = help)

m.mainloop()
