import bentoml

from sklearn import svm
from sklearn import datasets

# load iris dataset
iris=datasets.load_iris()
X, y = iris.data, iris.target

# train model
clf=svm.SVC(gamma='scale')
clf.fit(X, y)

# save model to BentoML local model store
saved_model=bentoml.sklearn.save_model("iris_clf", clf)
print(f"model saved: {saved_model}")

# tag="iris_clf:rsrj3n2ttorvpeap"
# C: -> users -> bentoml -> models -> iris_clf -> rsrj3n2ttorvpeap"