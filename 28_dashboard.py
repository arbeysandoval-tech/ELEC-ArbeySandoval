import sreamlit as st

st.title("Analisis de Distancia")
st.write("Bienvenido a mi dashboard")

distacia = st.slider("Selecciona la distancia minima", 0, 30, 20)
st.write("La distancia seleccionada es: ", distacia)

if distacia > 20:
    st.write("objeto cercano")  
else:
    st.write("objeto lejano")

datos = {
    "Medicion": [1,2,3,4,5,6,7,8],
    "Distancia": [15,18,22,12,30,25,10,20]
}
tabla_datos = pd.DataFrame(datos)

st.subheader("registro de mediciones")
st.dataframe(tabla_datos)

st.subheader("grafica de distancias")

st.line_chart(tabla_datos, x="Medicion", y="Distancia")
tabla_datos.to_csv["distancia ajustada"]=tabla_datos["Distancia"]+2
