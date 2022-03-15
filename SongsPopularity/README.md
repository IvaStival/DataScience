# Songs Popularity Study
I used this projct to study the regression, supervisioning process, analize the data using plots, the metrics, and a way to improve the model performance.
I follow this kaggle code (https://www.kaggle.com/yasserh/song-popularity-prediction-best-ml-models) to better process understand.

The objective is predict the popularity of a song based on some features, like:
  - song_duration_ms;
  - acousticness;
  - danceability;
  - energy;
  - instrumentalness;
  - key;
  - liveness;
  - loudness;
  - audio_mode;
  - speechiness;
  -	tempo;
  -	time_signature;
  -	audio_valence;

The ideia is use many regression models to analise the performance of each one.
And use many metrics errors to analise eacho model and learn how they works.

The regression models used are:
  - LinearRegression, LogisticRegression, BayesianRidge, ElasticNet, XGBoost, GradientBoostingRegressor, HistGradientBoostingRegressor, LGBMRegressor, CatBoostRegressor.

And the metrics:
  - MSE, RMSE, RSS, R2, MAE

And the last thing that was done is a study about how to emprove the XGboost performance changing the hyperparameters using hyperopt lib.

This was only a study to understand all the process used to solve a DataScience regression problem.
The best thing for me was the understand of the errors metrics. I could learn all math involved and how each one can be applied.

# References
https://www.kaggle.com/yasserh/song-popularity-prediction-best-ml-models
https://www.kaggle.com/prashant111/a-guide-on-xgboost-hyperparameters-tuning
https://www.analyticsvidhya.com/blog/2021/05/know-the-best-evaluation-metrics-for-your-regression-model/
https://neptune.ai/blog/performance-metrics-in-machine-learning-complete-guide
