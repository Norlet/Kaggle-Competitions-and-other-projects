-------------------------------------------------------------------------------------- # оставить тут функцию DUMMY CLASSIFIER
def dummy_mod(model, params, features_train, target_train):
    grid = GridSearchCV(estimator=model, param_grid=params, scoring='f1_macro', cv=5)
    grid.fit(features_train_idf, target_train_encoded)
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train, target_train)
    
    return best_model
-------------------------------------------------------------------------------------- #добавить в ноутбук DUMMY CLASSIFIER 
dummy_grid = {
    'strategy': ['most_frequent', 'stratified', 'prior', 'uniform', 'constant'],
    'constant': ['Вежливость сотрудников магазина', 'Время ожидания у кассы']
}

dummy_model = DummyClassifier(random_state=42)
best_dummy_model = dummy_mod(dummy_model, dummy_grid, features_train, target_train) 

-------------------------------------------------------------------------------------- #оставить тут функцию LOGISTIC REGRESSION 
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
--------------------------------------------------------------------------------------#добавить в нотубук LOGISTIC REGRESSION
logreg_model = LogisticRegression(random_state=42, solver='liblinear', max_iter=1000)
param_grid = {'model__penalty': ['l1', 'l2'], 'model__C': list(range(1, 15, 3))}

best_logreg_model, logreg_predictions = logreg_mod(logreg_model, param_grid, features_train_idf, target_train_encoded, features_test_idf)



--------------------------------------------------------------------------------------#оставить тут функцию RANDOM FOREST
def calculate_f1_score(true, predicted):
    return f1_score(true, predicted, average='weighted')

# Функция для обучения модели и получения предсказаний
def rf_model(model, params, features_train_idf, target_train, features_test_idf, target_test):
    param_grid = {
        'n_estimators': [100, 200, 300], 
        'max_depth': [3, 5, 7, None]
    }
    
    grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, scoring=make_scorer(calculate_f1_score), cv=5)
    grid.fit(features_train_idf, target_train)
    
    print(f'Лучшие параметры: {grid.best_params_}')

    best_model = grid.best_estimator_
    best_model.fit(features_train_idf, target_train)
    predictions = best_model.predict(features_test_idf)
    
    f1 = calculate_f1_score(target_test, predictions)
    print("F1-score:", f1)
    
    return best_model, predictions


-------------------------------------------------------------------------------------- # добавить в ноутбук RANDOM FOREST

best_rf_model, rf_predictions = rf_model(features_train_idf, target_train, features_test_idf, target_test)




-------------------------------------------------------------------------------------- # оставить тут функцию KNN

# Определение функции для оценки модели и вывода F1-меры
def calculate_f1_score(true, predicted):
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


-------------------------------------------------------------------------------------- # добавить в ноутбук KNN

KNN_model = KNeighborsClassifier()
KNN_params = {'n_neighbors': np.arange(3, 50, 2)}

best_KNN_model, KNN_y = modeling(KNN_model, KNN_params, features_train_idf, target_train_encoded, features_test_idf)
f1 = calculate_f1_score(target_test_encoded, KNN_y)
print(f'F1-мера: {f1}')

------------------------------------------------------------------------------------- #оставить тут MNB
# Определение функции для оценки модели и вывода F1-меры
def calculate_f1_score(true, predicted):
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

--------------------------------------------------------------------------------------# добавить в ноутбук MNB

# Создание сетки параметров
mnb_grid = {
    'alpha': [0.1, 0.2, 0.5, 0.8, 1.0],
    'fit_prior': [True, False],
    'class_prior': [None]
}

mnb = MultinomialNB()

# Использование функции для обучения модели
best_mnb_model, mnb_predictions = mnb_model(mnb, mnb_grid, features_train_idf, target_train, features_test_idf, target_test)













__________________________________________________________________
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

