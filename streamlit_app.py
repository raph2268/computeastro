# main_app.py
import streamlit as st
import home
import lecture1_linear_regression
import lecture2_logistic_regression
import lecture3_clustering_kmeans
import lecture3_clustering_gmm
import lecture4_pca
import lecture5_pytorch
import lecture5_multilayer_perceptron
import lecture7_gaussian_process_regression
import lecture8_gaussian_process_classification
import lecture9_sampling
import lecture10_markov_chain_monte_carlo

def main():
    st.sidebar.title('Course Content')
    page = st.sidebar.radio("Go to", ["Home", "Chaper 1: Linear Regression", "Chaper 2: Logistic Regression", "Chaper 3: Clustering - K-Means", "Chaper 3: Clustering - Gaussian Mixture Models", "Chaper 4: Dimension Reduction - Principal Component Analysis", "Chaper 5: Neural Networks - Pytorch Basics", "Chaper 5: Neural Networks - Multilayer Perceptron", "Chaper 5: Neural Networks - Autoencoder", "Chaper 7: Gaussian Process Regression", "Chaper 8: Gaussian Process Classification", "Chaper 9: Sampling", "Chaper 10: Markov Chain Monte Carlo"])

    if page == "Home":
        home.show_page()
    elif page == "Chaper 1: Linear Regression":
        lecture1_linear_regression.show_page()
    elif page == "Chaper 2: Logistic Regression":
        lecture2_logistic_regression.show_page()
    elif page == "Chaper 3: Clustering - K-Means":
        lecture3_clustering_kmeans.show_page()
    elif page == "Chaper 3: Clustering - Gaussian Mixture Models":
        lecture3_clustering_gmm.show_page()
    elif page == "Chaper 4: Dimension Reduction - Principal Component Analysis":
        lecture4_pca.show_page()
    elif page == "Chaper 5: Neural Networks - Pytorch Basics":
        lecture5_pytorch.show_page()
    elif page == "Chaper 5: Neural Networks - Multilayer Perceptron":
        lecture5_multilayer_perceptron.show_page()
    elif page == "Chaper 6: Neural Networks - Autoencoder":
        lecture6_autoencoder.show_page()
    elif page == "Chaper 7: Gaussian Process Regression":
        lecture7_gaussian_process_regression.show_page()
    elif page == "Chaper 8: Gaussian Process Classification":
        lecture8_gaussian_process_classification.show_page()
    elif page == "Chaper 9: Sampling":
        lecture9_sampling.show_page()
    elif page == "Chaper 10: Markov Chain Monte Carlo":
        lecture10_markov_chain_monte_carlo.show_page()
        
if __name__ == "__main__":
    main()
