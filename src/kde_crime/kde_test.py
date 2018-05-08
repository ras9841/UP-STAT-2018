from spatial_kde import *
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

data_loc = "../../data/RPD_crime2011toNow.csv"
data = process_RPD_data(data_loc)
print("Loaded data")

Y = data[["class"]]
X = data[["X", "Y"]]

print("Starting Predictions")
n_trials = 25
results = np.zeros([2,n_trials])

for test in range(2):
    print("Running test #%d"%(test+1))
    for i in range(n_trials):
        print("\nRunning trial %d/%d"%(i+1, n_trials))
        # Setup Data 
        if test == 0:
            X_tr, X_te, Y_tr, Y_te = train_test_split(X, Y, test_size=0.30)
        else:
            X_tr, X_te, Y_tr, Y_te = train_test_split(X, Y, test_size=0.30,\
                    stratify=Y)
        train_df = pd.concat([X_tr, Y_tr], axis=1)
        y = Y_te.values.reshape(Y_te.shape[0],)

        print("Starting KDE")
        kde = KDE()
        kde.train(train_df)
        print("Making predictions")
        yhat = kde.predict(X_te)
        results[test, i] = compute_accuracy(y, yhat)*100
        print("Accuracy: %d%%"%(results[test,i]))

results = results.T
print("NS Accuracy: (%.3f +/- %.3f)%%"%(results[:,0].mean(),\
    results[:,0].std()))
print("STRAT Accuracy: (%.3f +/- %.3f)%%"%(results[:,1].mean(),\
    results[:,1].std()))
results_df = pd.DataFrame(results, columns=["Random", "Stratified"])
results_df.boxplot()
plt.grid(False)
plt.ylabel("Accuracy (%)")
plt.show()
