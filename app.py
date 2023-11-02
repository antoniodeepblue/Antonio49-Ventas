import gradio as gr
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

import pickle
with open('prueba.pkl', 'rb') as file:
  knn = pickle.load(file)

def modelo(Fresk, Milk, Grocery, Frozen, Detergents_Paper,Delicassen,Channel1,Channel2,Region1,Region2,Region3):
    species = ['Grupo 0','1', '2','3']
    i = kmprueba.predict([[Fresk, Milk, Grocery, Frozen,Detergents_Paper,Delicassen,Channel1,Channel2,Region1,Region2,Region3]])[0]
    return species[i]

interfaz = gr.Interface(
    fn=modelo,
    inputs=[
        gr.Slider(label='Fresk', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Milk', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Grocery', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Frozen', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Detergents_Paper', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Delicassen', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Channel1', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Channel2', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Region1', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Region2', minimum=0.0, maximum=8.0, step=0.1),
        gr.Slider(label='Region3', minimum=0.0, maximum=8.0, step=0.1),
    ],
    outputs=gr.Textbox(label='Kmeans Grupo:'),
    title='Ventas de productos',
    description='Este modelo está desarrollado para la agrupacion Kmeans de productos.',
    article='Antonio Fernandez Salcedo, Practicas Saturdays.AI. Aplicación desarrollada con fines docentes',
    theme='peach'

)

interfaz.launch()