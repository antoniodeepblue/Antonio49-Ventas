import gradio as gr
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

import pickle
with open('prueba.pkl', 'rb') as file:
  kmprueba = pickle.load(file)

def modelo(Fresk, Milk, Grocery, Frozen, Detergents_Paper,Delicassen,Channel1,Channel2,Region1,Region2,Region3):
    species = ['Grupo 0','Grupo 1', 'Grupo 2','Grupo 3']
    i = kmprueba.predict([[Fresk, Milk, Grocery, Frozen,Detergents_Paper,Delicassen,Channel1,Channel2,Region1,Region2,Region3]])[0]
    return species[i]

interfaz = gr.Interface(
    fn=modelo,
    inputs=[
        gr.Slider(label='Fresk', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Milk', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Grocery', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Frozen', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Detergents_Paper', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Delicassen', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Channel1', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Channel2', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Region1', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Region2', minimum=0.0, maximum=5.0, step=0.05),
        gr.Slider(label='Region3', minimum=0.0, maximum=5.0, step=0.05),
    ],
    outputs=gr.Textbox(label='Kmeans Grupo:'),
    title='Ventas de productos. K-means',
    description='Este modelo está desarrollado para la agrupacion Kmeans de productos.',
    article= 'Autor: <a href=\"https://huggingface.co/Antonio49\>Antonio Fernández</a>. de <a href=\"https://saturdays.ai/\">SaturdaysAI</a>. Aplicación desarrollada con fines docentes',
    theme='peach'
    examples = [[0,'Fresk', 0,'Milk', 0,'Grocery', 0,'Frozen', 0,'Detergents_Paper', 0, 'Delicassen', 0,'Channel1',0,'Channel2',0,'Region1',0,'Region2',0,'Region3'],
            [0,'Fresk', 1,'Milk', 2,'Grocery', 4,'Frozen', 1,'Detergents_Paper', 0, 'Delicassen', 0,'Channel1',0,'Channel2',0,'Region1',0,'Region2',0,'Region3']]
             
)

interfaz.launch()