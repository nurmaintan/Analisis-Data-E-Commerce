import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#memuat data

def load_data():
    df = pd.read_csv("all_data.csv")
    return df

df = load_data()

if 'price' in df.columns and 'freight_value' in df.columns:
    df['order_total'] = df['price'] + df['freight_value']
elif 'payment_value' in df.columns:
    df['order_total'] = df['payment_value']
else:
    print("Kolom untuk menghitung nilai total pesanan tidak ditemukan.")
    print("Kolom yang tersedia:", df.columns)

print(df.columns)

# Streamlit Layout

st.title("Analisis Data E-Commerce :sparkles:")

st.header("Hubungan Jumlah Item dengan Skor Ulasan")
fig, ax = plt.subplots()
sns.boxplot(x='review_score', y='item_count', data=df)
ax.set_title('Jumlah Item Berdasarkan Skor Ulasan')
ax.set_xlabel('Skor Ulasan')
ax.set_ylabel('Jumlah Item')
st.pyplot(fig)

st.header("Metode Pembayaran vs Nilai Total Pesanan")
fig, ax = plt.subplots()
sns.boxplot(x='payment_type', y='order_total', data=df)
ax.set_title('Nilai Pesanan Berdasarkan Metode Pembayaran')
ax.set_xlabel('Metode Pembayaran')
ax.set_ylabel('Nilai Total Pesanan')
st.pyplot(fig)

st.header("Distribusi Nilai Pesanan Berdasarkan Metode Pembayaran")
fig, ax = plt.subplots()
sns.histplot(data=df, x='order_total', hue='payment_type', kde=True, element="step", alpha=0.5)
ax.set_title('Distribusi Nilai Pesanan Berdasarkan Metode Pembayaran')
ax.set_xlabel('Nilai Pesanan')
st.pyplot(fig)

# Tampilkan data frame
st.subheader("Dataframe:")
st.dataframe(df)

# Filter data berdasarkan skor ulasan
st.sidebar.header("Filter Data")
selected_review_score = st.sidebar.selectbox("Pilih Skor Ulasan", sorted(df['review_score'].unique(), reverse=True))

filtered_data = df[df['review_score'] == selected_review_score]
st.write(f"Menampilkan data untuk Skor Ulasan: {selected_review_score}")
st.dataframe(filtered_data)

# Filter berdasarkan metode pembayaran
selected_payment_type = st.sidebar.selectbox("Pilih Metode Pembayaran", df['payment_type'].unique())
filtered_payment_data = df[df['payment_type'] == selected_payment_type]
st.write(f"Menampilkan data untuk Metode Pembayaran: {selected_payment_type}")
st.dataframe(filtered_payment_data)







