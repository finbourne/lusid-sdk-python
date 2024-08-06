# IndustryClassifier

Object describing a particular industry classifier,  which comprises a classification code and the name of the classification system to which the code belongs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_system_name** | **str** | The name of the classification system to which the classification code belongs (e.g. GICS). | 
**classification_code** | **str** | The specific industry classification code assigned to the legal entity. | 

## Example

```python
from lusid.models.industry_classifier import IndustryClassifier

# TODO update the JSON string below
json = "{}"
# create an instance of IndustryClassifier from a JSON string
industry_classifier_instance = IndustryClassifier.from_json(json)
# print the JSON string representation of the object
print IndustryClassifier.to_json()

# convert the object into a dict
industry_classifier_dict = industry_classifier_instance.to_dict()
# create an instance of IndustryClassifier from a dict
industry_classifier_form_dict = industry_classifier.from_dict(industry_classifier_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


