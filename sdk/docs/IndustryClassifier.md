# IndustryClassifier

Object describing a particular industry classifier, which comprises a classification code and the name of the classification system to which the code belongs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_system_name** | **str** | The name of the classification system to which the classification code belongs (e.g. GICS). | 
**classification_code** | **str** | The specific industry classification code assigned to the legal entity. | 
## Example

```python
from lusid.models.industry_classifier import IndustryClassifier
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

classification_system_name: StrictStr = "example_classification_system_name"
classification_code: StrictStr = "example_classification_code"
industry_classifier_instance = IndustryClassifier(classification_system_name=classification_system_name, classification_code=classification_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

