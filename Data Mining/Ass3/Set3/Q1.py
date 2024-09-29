'''Write a Python program to build SVM model to Cancer dataset. The 
dataset is available in the scikit-learn library. Check the accuracy of model 
with precision and recall. '''

# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# Step 1: Load the cancer dataset
cancer = datasets.load_breast_cancer()

# Step 2: Define features (X) and target (y)
X = cancer.data  # Features
y = cancer.target  # Target labels (Malignant=0, Benign=1)

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train the SVM model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Step 6: Calculate accuracy, precision, and recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Step 7: Output the results
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# Optional: Detailed classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred))
