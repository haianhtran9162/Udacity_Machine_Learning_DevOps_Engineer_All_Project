# Model Card
## Model Details
    Development by AnhTH

    Model Date: 10 September 2023

    Model Version: 1.0.0

    Model Type: Random Forest Classifier

    Information: 
        1. Training model base on Sklearn Library
        2. The dataset is the Census Income dataset (https://archive.ics.uci.edu/ml/datasets/census+income)

    License: MIT License

## Intended Use
    Primary intended uses: Predict whether income exceeds $50K/yr based on census data.

    Primary intended users: Manager, HR, Anyone who has curious and want to know about the salary in jobs market.

    Out-of-scope use casesL: Maybe the model will not be able to predict the income of employees at some jobs market with high accuracy.

## Training Data
    Target predict: >50K, <=50K.
    List parameters:
        1. age: continuous.
        2. workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
        3. fnlwgt: continuous.
        4. education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
        5. education-num: continuous.
        6. marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
        7. occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
        8. relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
        9. race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
        10. sex: Female, Male.
        11. capital-gain: continuous.
        12. capital-loss: continuous.
        13. hours-per-week: continuous.
        14. native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
## Evaluation Data
    Datasets: Split origin datasets to 2 part Train and Test base on ratio 8:2
## Metrics
    Metrics List:
        1. Precision:0.7324695121951219
        2. Recall:0.6301639344262295
        3. Fbeta:0.6774762072611914

## Ethical Considerations
    This dataset was done by Barry Becker from the 1994 Census database. So the data input comes from the nowadays maybe is not working well.
## Caveats and Recommendations
    This dataset is provided by the archive.ics.uci.edu so the problem about the ethical concerns can be solved.