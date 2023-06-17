import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read the IPL data into a DataFrame
ipl_data = pd.read_csv(r'C:\Users\akhar\OneDrive\Desktop\ipl analysis\IPL - Player Performance Dataset\IPL\IPL_Matches_2008_2022.csv')
print(ipl_data)
print(ipl_data.info())
del ipl_data['method']
del ipl_data['SuperOver']
ipl_data.dropna(inplace = True)
features = ['Team1', 'Team2', 'City', 'TossWinner', 'TossDecision']
target = 'WinningTeam'
X = ipl_data[features]
y = ipl_data[target]
X_encoded = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.6, random_state=42)

# Initialize and train the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=1000, random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = rf_classifier.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
# Predict the winner for a new match
new_match = pd.DataFrame({
    'Team1': ['Mumbai Indians'],
    'Team2': ['Kolkata Knight Riders'],
    'City': ['Mumbai'],
    'TossWinner': ['Kolkata Knight Riders'],
    'TossDecision': ['bat']
})
new_match_encoded = pd.get_dummies(new_match)
new_match_encoded = new_match_encoded.reindex(columns=X_encoded.columns, fill_value=0)
winner_prediction = rf_classifier.predict(new_match_encoded)

print(f"Winner prediction: {winner_prediction}")

