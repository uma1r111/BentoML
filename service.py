# service.py is responsible for creating your entire API and 
# swagger UI (transforms JSON or YAML files into interactive interface)
# *NDArray : Represents a NumPy array with a specific data type (eg intergers, all floats)

import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

iris_clf_runner=bentoml.sklearn.get("iris_clf:latest").to_runner() #retrieves latest model

# creating service and model runner.
# here there is only one model but if we want multiple files we can do that as well by explicitly writing same code with different runners specified 
svc=bentoml.Service("iris_classifier", runners=[iris_clf_runner])

# creating API
@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result=iris_clf_runner.predict.run(input_series)
    return result