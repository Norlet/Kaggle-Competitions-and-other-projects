import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def dummy_mod(model, params, features_train, target_train):
    grid = GridSearchCV(estimator=model, param_grid=params, scoring='f1_macro', cv=5)
    grid.fit(features_train_idf, target_train_encoded)
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train, target_train)
    
    return best_model

def calculate_f1_score_logreg(true, predicted):
    return f1_score(true, predicted, average='weighted')

# Функция для обучения модели и получения предсказаний
def logreg_mod(model, params, features_train_idf, target_train_encoded, features_test_idf):
    grid = GridSearchCV(estimator=model, param_grid=params, scoring='f1_macro', cv=5)
    grid.fit(features_train_idf, target_train_encoded)
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train_idf, target_train_encoded)
    predictions = best_model.predict(features_test_idf)
    return best_model, predictions


def calculate_f1_score_rf(true, predicted):
    return f1_score(true, predicted, average='weighted')

# Функция для обучения модели и получения предсказаний
def rf_model(model, params, features_train_idf, target_train, features_test_idf, target_test):
    param_grid = {
        'n_estimators': [100, 200, 300], 
        'max_depth': [3, 5, 7, None]
    }
    
    grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, scoring=make_scorer(calculate_f1_score_rf), cv=5)
    grid.fit(features_train_idf, target_train)
    
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train_idf, target_train)
    predictions = best_model.predict(features_test_idf)
    
    f1 = calculate_f1_score_rf(target_test, predictions)
    print("F1-score:", f1)
    
    return best_model, predictions


# Определение функции для оценки модели и вывода F1-меры
def calculate_f1_score_knn(true, predicted):
    return f1_score(true, predicted, average='weighted')

# Функция для обучения модели и получения предсказаний
def knn_model(model, params, features_train_idf, target_train_encoded, features_test_idf):
    grid = GridSearchCV(estimator=model, param_grid=params, scoring='f1_macro', cv=5)
    grid.fit(features_train_idf, target_train_encoded)
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train_idf, target_train_encoded)
    predictions = best_model.predict(features_test_idf)
    return best_model, predictions

# Определение функции для оценки модели и вывода F1-меры
def calculate_f1_score_mnb(true, predicted):
    return f1_score(true, predicted, average='weighted')

# Функция для обучения модели и получения предсказаний
def mnb_model(model, params, features_train_idf, target_train_encoded, features_test_idf):
    grid = GridSearchCV(estimator=model, param_grid=params, scoring='f1_macro', cv=5)
    grid.fit(features_train_idf, target_train_encoded)
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train_idf, target_train_encoded)
    predictions = best_model.predict(features_test_idf)
    
    f1 = calculate_f1_score(target_test, predictions)
    print("F1-score:", f1)
    
    return best_model, predictions


def train(model_name, features_train_idf, target_train_encoded, features_test_idf):
    """
    Train your model
    Supported models: KNN,
                    и тд
    """
    SUPPORTED_MODELS = ['KNN', 'SVM','Logistic Regression', 'MNB', 'Random Forest', 'Dummy Classifier']
    if model_name not in [SUPPORTED_MODELS]:
        print(f'model are not supported, choose one from {SUPPORTED_MODELS}')
        
    if model_name == 'KNN':
        best_model, predictions = knn_model(features_train_idf, target_train_encoded, features_test_idf)
        
    if model_name == 'SVM':
        best_model, predictions = svm_model(features_train_idf, target_train_encoded, features_test_idf)
        
    if model_name == 'Logistic Regression':
        best_model, predictions = logreg_mod(features_train_idf, target_train_encoded, features_test_idf)
    
    if model_name == 'MNB':
        best_model, predictions = mnb_model(features_train_idf, target_train_encoded, features_test_idf)

    if model_name == 'Random Forest':
        best_model, predictions = rf_model(features_train_idf, target_train_encoded, features_test_idf)

    if model_name == 'Dummy Classifier':
        best_model, predictions = dummy_mod(features_train_idf, target_train_encoded, features_test_idf)
    
    return best_model, predictions

