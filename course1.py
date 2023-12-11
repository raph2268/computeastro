# course1.py
import streamlit as st

def app():

st.markdown(r'''# Linear Regression

- By Yuan-Sen Ting, August 2023, for ASTR 4004/8004.''')

st.markdown(r'''Welcome to today's enriching lab session! Our mission is to explore the intricacies of machine learning, specifically focusing on applying linear regression models to interpret astronomical data. We'll be working with spectra data from the Sloan Digital Sky Survey's Apache Point Observatory Galactic Evolution Experiment (SDSS APOGEE). Our goal is to employ linear regression, regularization techniques, and Bayesian Linear Regression to predict and understand the effective temperature of stars.

## Prerequisites

### Knowledge Assumptions

To fully benefit from this lab, you should have a firm grounding in the following subjects:

1. **Maximum Likelihood Solutions in Linear Regression**: Know-how of solving linear regression problems using the maximum likelihood estimation (MLE) approach is necessary. This includes familiarity with both vanilla and regularized versions. (Covered in lectures)

2. **Matrix Operations using NumPy**: Being comfortable with matrix calculations using the NumPy library is crucial, as our data manipulations and model computations will be matrix-centric. (Covered in lab and pre-course material)

3. **Theoretical Foundations of Regularization**: A sound understanding of regularization methods such as Ridge Rigression is vital, as we will leverage these techniques to refine our linear regression models. (Covered in lectures)

4. **Basics of Bayesian Linear Regression**: An elementary grasp of Bayesian Linear Regression will help you understand how it complements and extends traditional linear regression methods, especially when working with complex datasets like stellar spectra. (Covered in lectures)


### Skills You Will Gain

Upon completing this lab, you should gain expertise in:

1. **Interpreting Astronomical Data through Linear Regression**: This lab will provide you with hands-on experience in using linear regression to analyze SDSS APOGEE spectra and infer stellar properties.

2. **Regularization in Complex Models**: You'll become adept at selecting the most appropriate regularization parameter to improve the performance and generalizability of your machine learning models, especially in the complex field of astronomical data.

3. **Integrating Bayesian Methods and Regularization**: One of the highlights of this lab is exploring how Ridge Regression can be thought of as a special case of Bayesian Linear Regression, offering you deeper insights into the connection between probabilistic methods and traditional machine learning techniques.

4. **Understanding and Utilizing Predictive Distributions**: You'll learn how to make probabilistic predictions using Bayesian linear regression, enabling you to not only produce point estimates but also to assess the associated uncertainty. This skill is particularly useful for real-world applications that require risk assessment and decision-making under uncertainty.

Let's dive in and turn the theoretical knowledge you've acquired into practical skills for tackling real-world data science challenges!
''')


# Call the app function
app()