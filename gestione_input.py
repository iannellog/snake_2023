# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:00:31 2023

@author: angel
"""

import json
from PIL import Image
import sys
import os

from abc import ABC, abstractmethod


def convert_image_to_json(image_path):
    """
    Funzione che a partire da un'immagine costrusice il file JSON

    Parameters
    ----------
    image_path : str
        percorso del file dell'immagine con estensione .png

    Returns
    -------
    json_file_path : str
        persocorso del file JSON.

    """
    # Carica l'immagine
    image = Image.open(image_path)

    # Estrai le dimensioni dell'immagine
    cols, rows = image.size

    # Inizializza le liste per il cibo e i blocchi
    food = []
    blocks = []

    # Scansiona l'immagine pixel per pixel
    for y in range(rows):
        for x in range(cols):
            pixel_color = image.getpixel((x, y))

            if pixel_color == (255, 128, 0):
                food.append([y, x])
            elif pixel_color == (255, 0, 0):
                blocks.append([y, x])

    # Crea il dizionario JSON per questa immagine
    dati_immagine = {
        "rows": rows,
        "cols": cols,
        "food": food,
        "blocks": blocks
    }

    # Costruisci il nome del file JSON basato sul nome del file di origine
    nome_file_json = os.path.splitext(os.path.basename(image_path))[0] + ".json"

    # Salva i dati in un file JSON separato nella stessa directory dell'immagine
    json_file_path = os.path.join(os.path.dirname(image_path), nome_file_json)
    with open(json_file_path, "w") as json_file:
        json.dump(dati_immagine, json_file, indent=2)
        json_file.close()

    return json_file_path


class Strategy(ABC):
    @abstractmethod
    def execute(self, file_path):
        pass


class ImageProcessingStrategy(Strategy):
    def execute(self, campo_gioco):
        campo_gioco_convertito = convert_image_to_json(campo_gioco)
        g = open(campo_gioco_convertito)
        return g


class JsonProcessingStrategy(Strategy):
    def execute(self, campo_gioco):
        g = open(campo_gioco)
        return g


def type_of_input(campo_gioco):
    if campo_gioco.endswith((".png", ".json")):
        if campo_gioco.endswith(".png"):
            strategy = ImageProcessingStrategy()
        else:
            strategy = JsonProcessingStrategy()
        g = strategy.execute(campo_gioco)
        return g
    else:
        print("Formato file non supportato")
        sys.exit()


def carico_dati(game_file):
    """
    Funzione che legge i dati da un file JSON specificato e restituisce una tupla
    contenente diverse liste di dati che saranno utilizzati all'interno del programma
    principale del gioco per la gestione dello stesso. Se gli viene fornita un game_file
    sbagliato o non presente ti richiede di inserirlo fino a quando trova la directory;
    se si vuole fermare prima questo processo basta digitare no

    Parameters
    ----------
    game_file : file json
        un file nel quale sono contenute le informazione del campo da gioco,
        della posizione iniziale, la lista delle mosse e il file su cui salvare
        l'immagine finale.

    Returns
    -------
    una tupla con le liste dei dati estratti: start, mosse, food, blocks, righe, colonne, field_out.

    """
    while True:
        try:
            with open(game_file, 'r') as file:
                game = json.load(file)
                file.close()
                field_out = game['field_out']
                campo_gioco = game['field_in']
                # Richiamo Strategy Design Pattern
                g = type_of_input(campo_gioco)
                field = json.load(g)
                g.close()
                start = game['start']
                mosse = game['moves']
                righe = field['rows']
                colonne = field['cols']
                food = field['food']
                blocks = field['blocks']
                return start, mosse, food, blocks, righe, colonne, field_out
        except FileNotFoundError:
            print(
                "Il file non è stato trovato.\nControlla che il file è stato scritto correttamente ed è presente nella directory data.\nEsempio: data/gamefile_01.json")
        game_file = input("Inserisci il nome del file di gioco:\nPer uscire digitare no\n")
        if game_file.lower() == "no":
            print("Hai chiuso il gioco")
            sys.exit()


def restituisco_dati(corpo, scia_serpente, food, blocks, righe, colonne, final_field):
    """
    Funzione che restituisce la lunghezza del serpente e che genera un'immagine
    rappresentativa dello stato finale del gioco.
    Crea una rappresentazione visiva dell'ultima configurazione del gioco, dove
    il serpente è tracciato in verde, il cibo in arancione, i blocchi in rosso
    e la scia del serpente in grigio su uno sfondo nero.
    Questi dati possono essere utilizzati per valutare l'evoluzione del gioco.

    Parameters
    ----------
    final_field : str
        stringa che contiene il percorso del file dove si vuole salvare l'immagine

    Returns
    -------
    lunghezza_serpente: int
        numero di quadratini occupati dal serpente alla fine del gioco.

    """
    lunghezza_serpente = len(corpo)

    black_image = Image.new("RGB", (colonne, righe), (0, 0, 0))

    for x, y in scia_serpente:
        black_image.putpixel((y, x), (128, 128, 128))

    for x, y in corpo:
        black_image.putpixel((y, x), (0, 255, 0))

    for x, y in food:
        black_image.putpixel((y, x), (255, 128, 0))

    for x, y in blocks:
        black_image.putpixel((y, x), (255, 0, 0))

    black_image.save(final_field)
    return lunghezza_serpente
