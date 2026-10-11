import numpy as np
from sklearn.linear_model import LinearRegression
def predire_vitesse(df):
    X = np.arange(
        len(df)
    ).reshape(-1,1)
    y = df["vitesse_corrigee"]
    model = LinearRegression()
    model.fit(X,y)
    futur = np.arange(
        len(df),
        len(df)+10
    ).reshape(-1,1)
    prediction = model.predict(futur)
    return prediction