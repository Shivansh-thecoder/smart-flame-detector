import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv('flame_training_data.csv')
X=df[['Flame_Value']]
y=df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(
    n_estimators=150,        # More trees for stability
    max_depth=8,             # Balanced complexity
    min_samples_split=4,     
    min_samples_leaf=2,      
    max_features='sqrt',     # Works great for single-feature data
    bootstrap=True,
    random_state=42
)
model.fit(X_train,y_train)

preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Model trained with accuracy: {acc*100:.2f}%")

joblib.dump(model, "flame_model.pkl")
print("Model saved as flame_model.pkl")

