import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import RocCurveDisplay, PrecisionRecallDisplay, ConfusionMatrixDisplay

st.title("Binary Classification WebApp")
st.markdown("Are your mushrooms edible or poisonous? 🍄")

st.sidebar.title("Binary Classification")
st.sidebar.markdown("Are your mushrooms edible or poisonous?")

@st.cache_data
def load_data():
    try:
        data = pd.read_csv('mushrooms.csv')
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data
    except FileNotFoundError:
        return None  # Allow the app to continue running

@st.cache_data
def split(df):
    y = df['type']
    x = df.drop(columns=['type'])
    return train_test_split(x, y, test_size=0.3, random_state=0)

def plot_metrics(metrics_list, model, x_test, y_test, y_pred):
    for metric in metrics_list:
        st.subheader(metric)
        fig, ax = plt.subplots()

        if metric == 'Confusion Matrix':
            cm = confusion_matrix(y_test, y_pred)
            ConfusionMatrixDisplay(cm).plot(ax=ax)

        if metric == 'ROC Curve':
            RocCurveDisplay.from_estimator(model, x_test, y_test, ax=ax)

        if metric == 'Precision-Recall Curve':
            PrecisionRecallDisplay.from_estimator(model, x_test, y_test, ax=ax)

        st.pyplot(fig)

df = load_data()

if df is None:
    st.error("Error: `mushrooms.csv` not found! Please upload the dataset.")
    st.stop()  # Stop execution cleanly

x_train, x_test, y_train, y_test = split(df)

st.sidebar.subheader("Choose Classifier")
classifier = st.sidebar.selectbox("Classifier",
                                  ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

if classifier == "Support Vector Machine (SVM)":
    C_svm = st.sidebar.slider("C (Regularization parameter)", 0.01, 10.0, 1.0, step=0.01)
    kernel = st.sidebar.radio("Kernel", ("rbf", "linear"))
    gamma = st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"))

    metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

    if st.sidebar.button("Classify"):
        try:
            st.subheader("Support Vector Machine (SVM) Results")
            model = SVC(C=C_svm, kernel=kernel, gamma=gamma)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Accuracy:", model.score(x_test, y_test))
            st.write("Precision:", precision_score(y_test, y_pred))
            st.write("Recall:", recall_score(y_test, y_pred))
            plot_metrics(metrics, model, x_test, y_test, y_pred)
        except Exception as e:
            st.error(f"Error: {e}")

elif classifier == "Logistic Regression":
    C_lr = st.sidebar.slider("C (Regularization parameter)", 0.01, 10.0, 1.0, step=0.01)
    max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, 200)

    metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

    if st.sidebar.button("Classify"):
        try:
            st.subheader("Logistic Regression Results")
            model = LogisticRegression(C=C_lr, max_iter=max_iter)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Accuracy:", model.score(x_test, y_test))
            st.write("Precision:", precision_score(y_test, y_pred))
            st.write("Recall:", recall_score(y_test, y_pred))
            plot_metrics(metrics, model, x_test, y_test, y_pred)
        except Exception as e:
            st.error(f"Error: {e}")

elif classifier == "Random Forest":
    n_estimators = st.sidebar.slider("Number of Trees", 100, 5000, 100, step=10)
    max_depth = st.sidebar.slider("Max Depth", 1, 20, 10)
    bootstrap = st.sidebar.radio("Bootstrap samples", (True, False))

    metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))

    if st.sidebar.button("Classify"):
        try:
            st.subheader("Random Forest Results")
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap, n_jobs=-1)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Accuracy:", model.score(x_test, y_test))
            st.write("Precision:", precision_score(y_test, y_pred))
            st.write("Recall:", recall_score(y_test, y_pred))
            plot_metrics(metrics, model, x_test, y_test, y_pred)
        except Exception as e:
            st.error(f"Error: {e}")

if st.sidebar.checkbox("Show raw data"):
    st.subheader("Mushroom Data Set (Classification)")
    st.write(df)
