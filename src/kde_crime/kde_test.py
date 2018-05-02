from spatial_kde import *
import pandas as pd
from sklearn.model_selection import train_test_split

data_loc = "../../data/RPD_crime2011toNow.csv"
data = process_RPD_data(data_loc)
print("Loaded data")

Y = data[["class"]]
X = data[["X", "Y"]]

print("Starting Predictions")
n_trials = 25
results = np.zeros(n_trials)

for i in range(n_trials):
    print("\nRunning trial %d/%d"%(i+1, n_trials))
    # Setup Data 
    X_tr, X_te, Y_tr, Y_te = train_test_split(X, Y, test_size=0.25)
    train_df = pd.concat([X_tr, Y_tr], axis=1)
    y = Y_te.values.reshape(Y_te.shape[0],)

    print("Starting KDE")
    kde = KDE()
    kde.train(train_df)
    print("Making predictions")
    yhat = kde.predict(X_te)
    results[i] = compute_accuracy(y, yhat)
    print("Accuracy: %d%%"%(results[i]*100))
