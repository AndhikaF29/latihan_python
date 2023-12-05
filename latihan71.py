import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("progdas pertemuan 7\soal.csv")

# Membersihkan data dari nilai-nilai yang hilang
df_bersihkandata = df.dropna()

# Menghitung median dari kolom 'Age' dan 'Score'
usia_median = df_bersihkandata['Age'].median()
skor_median = df_bersihkandata['Score'].median()

# Membuat gambar dan sumbu (subplots) menggunakan matplotlib
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot untuk kolom 'Age'
axs[0].bar(df_bersihkandata['Name'], df_bersihkandata['Age'], color='#DD7700', label='Usia')
axs[0].axhline(usia_median, color='red', linestyle='dashed', label=f'Median: {usia_median}')
axs[0].set_xticklabels(df_bersihkandata['Name'], rotation=45, ha='right')
axs[0].set_title('Usia')
axs[0].legend()

# Plot untuk kolom 'Score'
axs[1].bar(df_bersihkandata['Name'], df_bersihkandata['Score'], color='#DD0077', label='Skor')
axs[1].axhline(skor_median, color='red', linestyle='dashed', label=f'Median: {skor_median}')
axs[1].set_xticklabels(df_bersihkandata['Name'], rotation=45, ha='right')
axs[1].set_title('Skor')
axs[1].legend()

# Menampilkan plot
plt.tight_layout()
plt.show()