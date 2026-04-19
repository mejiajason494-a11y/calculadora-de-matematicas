import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Configuración de la página
st.set_page_config(page_title="Calculadora Matemática Pro - UTEC", layout="wide")

# Estilo Estético (Dark Mode y Colores)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTextInput > div > div > input { background-color: #262730; color: white; border-radius: 10px; }
    .stAlert { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Calculadora Matemática Avanzada")
st.sidebar.header("Configuración")
st.sidebar.write("Proyecto de Matemática I")
st.sidebar.info("Uso de IA para optimización de diseño y cálculo.")

# Entrada de la función
st.subheader("1. Definición de la Función")
func_input = st.text_input("Ingresa tu función f(x):", "x**2 - 4*x + 3")

x = sp.symbols('x')

try:
    # Procesamiento Matemático
    f_expr = sp.sympify(func_input)
    f_num = sp.lambdify(x, f_expr, 'numpy')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("### ✅ Análisis de la Función")
        st.write(f"**Función:** $f(x) = {sp.latex(f_expr)}$")
        
        # Dominio (Simplificado para la entrega)
        st.write("**Dominio sugerido:** Reales (revisar asíntotas)")
        
        # Cortes
        cortes_x = sp.solve(f_expr, x)
        corte_y = f_expr.subs(x, 0)
        st.write(f"**Cortes en X:** {cortes_x}")
        st.write(f"**Corte en Y:** (0, {corte_y})")

    with col2:
        # Gráfica Mejorada
        st.success("### 📈 Representación Gráfica")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_num(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='f(x)', color='#1f77b4', linewidth=2)
        ax.axhline(0, color='white', linewidth=0.5)
        ax.axvline(0, color='white', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', alpha=0.3)
        ax.set_facecolor('#0e1117')
        fig.patch.set_facecolor('#0e1117')
        ax.tick_params(colors='white')
        st.pyplot(fig)

    # Sección de Inyectividad e Inversa
    st.divider()
    st.subheader("2. Inyectividad y Función Inversa")
    
    # Prueba de inyectividad (Derivada)
    derivada = sp.diff(f_expr, x)
    es_inyectiva = sp.is_increasing(f_expr, sp.Reals) or sp.is_decreasing(f_expr, sp.Reals)
    
    if es_inyectiva:
        st.balloons()
        st.write("✨ **La función es inyectiva.** Tiene función inversa.")
        # Cálculo de inversa simplificado
        y_sym = sp.symbols('y')
        inversa = sp.solve(sp.Eq(y_sym, f_expr), x)
        st.code(f"Función Inversa: f⁻¹(y) = {inversa}")
    else:
        st.warning("⚠️ **La función NO es inyectiva** en todo su dominio. No tiene una inversa única sin restringir el dominio.")

except Exception as e:
    st.error(f"Error en la expresión: {e}. Asegúrate de usar '*' para multiplicar (ejemplo: 2*x).")

st.sidebar.warning("Recuerda: Entrega Sábado 18 de Abril, 11:55 PM")