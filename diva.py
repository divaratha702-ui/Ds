# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, r2_score

# # Dataset create
# data = {
#     "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "attendance": [60, 65, 70, 75, 80, 85, 90, 92, 95, 98],
#     "marks": [35, 45, 50, 60, 65, 70, 78, 85, 90, 95]
# }

# df = pd.DataFrame(data)

# # Features and target
# X = df[["study_hours", "attendance"]]
# y = df["marks"]

# # Train-Test Split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Prediction
# y_pred = model.predict(X_test)

# # Accuracy
# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Absolute Error:", mae)
# print("R2 Score:", r2)

# # Custom Prediction
# print("\n--- Student Mark Prediction ---")
# study = float(input("Study hours: "))
# attend = float(input("Attendance %: "))
# result = model.predict([[study, attend]])
# print("Predicted Mark:", round(result[0], 2))


# # test

# # print("Diva Git Test")

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
df = pd.read_csv(r"c:\Users\acer\Downloads\archive (3)\ai-impact-jobs-layoff-risk-dataset.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Encode Categorical Columns
label_encoders = {}

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and Target
X = df.drop("Layoff_Risk", axis=1)
y = df["Layoff_Risk"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Important Features:")
print(importance.head(10))