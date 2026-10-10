import streamlit as st
import matplotlib.pyplot as plt

def plot_bar(df, x, y):
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y])
    st.pyplot(fig)

def plot_line(df, x, y):
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])
    st.pyplot(fig)

def plot_scatter(df, x, y):
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    st.pyplot(fig)