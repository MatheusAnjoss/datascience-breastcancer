# ==========================================
# 1. IMPORTS
# ==========================================
import pandas as pd
import numpy as np
import zipfile

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


# ==========================================
# 2. ABRIR O ZIP E CARREGAR O DATASET
# ==========================================
zip_path = "heart disease.zip"  # <- ajuste se o path for outro

with zipfile.ZipFile(zip_path, 'r') as z:
    # arquivo recomendado (limpo)
    file_name = "processed.cleveland.data"
    with z.open(file_name) as f:
        dados = pd.read_csv(f, header=None)


# ==========================================
# 3. DEFINIR AS COLUNAS DO DATASET
# ==========================================
colunas = [
    "age","sex","cp","trestbps","chol","fbs","restecg","thalach",
    "exang","oldpeak","slope","ca","thal","target"
]

dados.columns = colunas

# Substituir "?" por NaN e remover linhas inválidas
dados = dados.replace("?", np.nan)
dados = dados.dropna()

# Converter colunas numéricas
for col in colunas:
    dados[col] = pd.to_numeric(dados[col])


# ==========================================
# 4. SEGMENTAR ATRIBUTOS E CLASSE
# ==========================================
dados_atributos = dados.drop(columns=["target"])
dados_classes = dados["target"]


# ==========================================
# 5. HOLD-OUT (70% treino / 30% teste)
# ==========================================
atributos_train, atributos_test, classes_train, classes_test = train_test_split(
    dados_atributos, dados_classes, test_size=0.3, random_state=42
)


# ==========================================
# 6. TREINAR MODELO (Decision Tree)
# ==========================================
tree = DecisionTreeClassifier()
heart_tree = tree.fit(atributos_train, classes_train)

print("Classes presentes no modelo:", heart_tree.classes_)


# ==========================================
# 7. PRETESTAR O MODELO
# ==========================================
predicoes = heart_tree.predict(atributos_test)

print("\nComparação entre classe real e prevista:")
for real, prev in zip(classes_test, predicoes):
    print(real, "-", prev)


# ==========================================
# 8. ACURÁCIA
# ==========================================
print("\nAcurácia global:", metrics.accuracy_score(classes_test, predicoes))


# ==========================================
# 9. MATRIZ DE CONFUSÃO
# ==========================================
print("\nMatriz de Confusão (numérica):")
print(confusion_matrix(classes_test, predicoes, labels=heart_tree.classes_))

print("\nExibindo matriz de confusão gráfica...")
cm = confusion_matrix(classes_test, predicoes, labels=heart_tree.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=heart_tree.classes_)
disp.plot()
plt.show()



# ==========================================
# 10. CLASSIFICAR UMA NOVA INSTÂNCIA
# ==========================================
# Exemplo fictício – substitua por novos valores
nova_instancia = [[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]

classe_inferida = heart_tree.predict(nova_instancia)
print("\nClasse inferida para nova instância:", classe_inferida)

