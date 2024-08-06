# LusidValidationProblemDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**error_details** | **List[Dict[str, str]]** |  | [optional] 
**code** | **int** |  | 
**errors** | **Dict[str, List[str]]** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LusidValidationProblemDetails from a JSON string
lusid_validation_problem_details_instance = LusidValidationProblemDetails.from_json(json)
# print the JSON string representation of the object
print LusidValidationProblemDetails.to_json()

# convert the object into a dict
lusid_validation_problem_details_dict = lusid_validation_problem_details_instance.to_dict()
# create an instance of LusidValidationProblemDetails from a dict
lusid_validation_problem_details_form_dict = lusid_validation_problem_details.from_dict(lusid_validation_problem_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


