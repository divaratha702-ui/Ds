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

print("Diva Git Test")