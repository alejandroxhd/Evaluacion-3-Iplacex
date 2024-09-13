from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio() -> str:

    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET"])
def ejercicio1() -> str:


    return render_template("ejercicio1.html", formulario=["", "", "", ""])

@app.route("/ejercicio1", methods=["POST"])
def ejercicio1_action() -> str:
    form = request.form
    calificacion_1 = form["nota1"]
    calificacion_2 = form["nota2"]
    calificacion_3 = form["nota3"]
    asistencia = form["asistencia"]
    formulario = [calificacion_1, calificacion_2, calificacion_3, asistencia]
    try:

        calificacion_1 = int(calificacion_1)
        calificacion_2 = int(calificacion_2)
        calificacion_3 = int(calificacion_3)
        asistencia = int(asistencia)

        if not (10 <= calificacion_1 <= 70): raise Exception("Calificacion no valida")
        if not (10 <= calificacion_2 <= 70): raise Exception("Calificacion no valida")
        if not (10 <= calificacion_3 <= 70): raise Exception("Calificacion no valida")
        if not (0 <= asistencia <= 100): raise Exception("Asistencia no valida")
    except:

        respuesta = "verificar valores ingresados."
    else:

        promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3
        if promedio >= 40 and asistencia >= 75:
            respuesta = "Aprobado"
        else:
            respuesta = "Reprobado"

    return render_template("ejercicio1.html", promedio=promedio, respuesta=respuesta, formulario=formulario)

@app.route("/ejercicio2", methods=["GET"])
def ejercicio2() -> str:

    return render_template("ejercicio2.html", formulario=["", "", "", ""])

@app.route("/ejercicio2", methods=["POST"])
def ejercicio2_action() -> str:

    form = request.form
    nombre1 = form["nombre1"]
    nombre2 = form["nombre2"]
    nombre3 = form["nombre3"]
    formulario = [nombre1, nombre2, nombre3]

    nombre_largo = nombre1
    if len(nombre2) > len(nombre_largo):
        nombre_largo = nombre2
    if len(nombre3) > len(nombre_largo):
        nombre_largo = nombre3

    nombre_extenso = len(nombre_largo)

    return render_template(
        "ejercicio2.html",
        formulario=formulario,
        resultado_nombre=nombre_largo,
        resultado_largo=nombre_extenso
    )

if __name__ == '__main__':
    app.run(debug=True)