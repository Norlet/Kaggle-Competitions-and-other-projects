def get_result(text: pd.Series) -> pd.Series:
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


features_train_idf, target_train_encoded, features_test_idf = preprocess_data(excel.csv)
best_model, predictions = train(features_train_idf, target_train_encoded, features_test_idf )
