# NLP решение для отдела службы поддержки


## Цель работы
Для корректной маршрутизации на нужного специалиста колл-центра решено отказаться от кнопочного меню и внедрить NLP модель.
Для этого была проведена разметка данных. 
Клиенты компании оставляют обратную связь в виде текстового комментария/отзыва в свободной форме.
Необходимо обучить модель классификации негативных отзывов, которая позволит получать детальную аналитику по проблемам клиентов в автоматическом режиме.

## Данные

Набор данных представляет собой выборку отзывов клиентов с разметкой на 14 классов проблем.

text - текст отзыва клиента

label - метка класса на которую надо обучиться


## Описание

В ходе данного исследования была проведена обработка текста и создание новых столбцов-признаков для улучшения качества данных. Были обнаружены выбросы на графике длин текстов отзывов, дисбаланс классов. Далее были построены различные модели многоклассовой классификации для отзывов клиентов с учетом балансировки классов. Метрикой был выбран F1-score, так как, это среднее геометрическое precision и recall, которое является хорошим показателем общего качества модели. Также, одним из вариантов для выбора метрики был weighted accuracy - эта метрика учитывает дисбаланс классов, взвешивая каждый класс в соответствии с его долей в обучающем наборе данных. Лучшими оказались вариации BERT от Сбера и DeepPavlov с показателями F1-score равными 0.820 и 0.810 соответственно, в то время как показатель baseline от Dummy Classifier составил 0.365.

Другие модели проявили себя наилучшим образом при обработке текста с использованием TF-IDF и метода GridSearch для подбора параметров. Однако, итоговый результат можно улучшить с использованием дополнительных методов.

В качестве одного из потенциальных способов улучшения результатов можно использовать генерацию синтетических данных с помощью генеративно-состязательных сетей (GAN). GAN позволяют создавать новые примеры данных, имитирующие характеристики и распределение исходного набора данных. В случае данной задачи, GAN могут быть использованы для создания синтетических текстовых образцов, которые будут содержать схожие с исходными образцы языковых характеристик и структуру. Эти синтетические данные могут быть затем использованы для увеличения размера обучающего набора данных и улучшения обобщающей способности модели.

![Image alt](https://github.com/Norlet/Kaggle-Competitions-and-other-projects/blob/main/Customer%20Service%20NLP%20solution/graph.png)

## Используемые библиотеки

**BERT, LinearRegression, SVM, Naive Bayes, RandomForestClassifier,pandas, sklearn, numpy, tf-idf, nltk, Optuna**

