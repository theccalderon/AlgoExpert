from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler


# https://www.codespeedy.com/logistic-regression-using-pyspark-in-python/
# https://spark.apache.org/docs/3.5.0/ml-features.html#vectorassembler
def predict_cancellations(user_interaction_df):
    my_final_data = user_interaction_df.select(['user_id','month_interaction_count',
                           'week_interaction_count',
                           'day_interaction_count', "cancelled_within_week"])
    assembler = VectorAssembler(inputCols=['month_interaction_count',
                                           'week_interaction_count',
                                           'day_interaction_count'], outputCol='features')

    output = assembler.transform(my_final_data)

    lr = LogisticRegression(maxIter=10, threshold=0.6, regParam=0.1, elasticNetParam=1, labelCol="cancelled_within_week")

    # Fit the model
    lrModel = lr.fit(output)

    return lrModel.transform(output).select(['user_id','rawPrediction',
                           'probability',
                           'prediction'])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("PEPE")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
