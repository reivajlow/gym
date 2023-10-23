"""
This module contains a Flask application that serves a web page for a training plan diagnostic.

Created by: Javier Saavedra (GitHub)[https://github.com/reivajlow]
Date: 2021-01-01
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def diagnostico():
    """ _description_ :
    Diagnóstico para plan de entrenamiento

    Returns:
        _type_: plan de entrenamiento semanal
    """
    return render_template('index.html', title='Diagnóstico')


@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    """_summary_: Procesa los datos enviados por el usuario
        y los guarda en un diccionario.

    Returns:
        dict: _description_: Diccionario con los datos de los ejercicios
                - _key_: nombre del ejercicio
                - _value_: diccionario con los datos del ejercicio
                    - peso_maximo: peso máximo levantado
                    - peso_medio: mitad del peso maximo levantado
                    - peso_cuarto: 1/4 del peso maximo levantado
                    - rep_maxima: repeticiones con el peso máximo levantado
                    - rep_media: repeticiones con el peso medio levantado
                    - rep_cuarto: repeticiones con el peso 1/4 levantado
                    - numero_id: número del ejercicio
    """
    # Crea un diccionario para almacenar los datos de los ejercicios
    datos_ejercicios = {}
    print(request.form)
    # Itera a través de los ejercicios del 1 al 8
    for i in range(1, 9):
        # Forma los nombres de los campos para el ejercicio actual
        nombre_ejercicio = request.form.get(
            f'ejercicio{i}', default=f"ejercicio{i}")
        peso_maximo = request.form.get(f'peso_max_ejercicio{i}', default=0)
        peso_medio = request.form.get(f'peso_med_ejercicio{i}', default=0)
        peso_cuarto = request.form.get(f'peso_cu_ejercicio{i}', default=0)
        rep_maxima = request.form.get(f'rep_max_ejercicio{i}', default=0)
        rep_media = request.form.get(f'rep_med_ejercicio{i}', default=0)
        rep_cuarto = request.form.get(f'rep_cu_ejercicio{i}', default=0)

        # Almacena los datos en el diccionario
        datos_ejercicios[nombre_ejercicio] = {
            'peso_maximo': peso_maximo,
            'peso_medio': peso_medio,
            'peso_cuarto': peso_cuarto,
            'rep_maxima': rep_maxima,
            'rep_media': rep_media,
            'rep_cuarto': rep_cuarto,
            'numero_id': i
        }

    # Ejemplo de cómo imprimir los datos:
    # for ejercicio_num, datos in datos_ejercicios.items():
    #       print(f'Ejercicio {ejercicio_num}: {datos["nombre"]},
    #       Peso Máximo: {datos["peso_maximo"]},
    #       Repeticiones Máximas: {datos["rep_maxima"]}')

    # Puedes redirigir a una página de confirmación o hacer lo que necesites con los datos
    print(datos_ejercicios)
    return "Datos procesados con éxito"
