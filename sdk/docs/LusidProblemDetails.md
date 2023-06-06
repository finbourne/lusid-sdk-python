# LusidProblemDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**error_details** | **List[Dict[str, str]]** |  | [optional] 
**code** | **int** |  | 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from lusid.models.lusid_problem_details import LusidProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LusidProblemDetails from a JSON string
lusid_problem_details_instance = LusidProblemDetails.from_json(json)
# print the JSON string representation of the object
print LusidProblemDetails.to_json()

# convert the object into a dict
lusid_problem_details_dict = lusid_problem_details_instance.to_dict()
# create an instance of LusidProblemDetails from a dict
lusid_problem_details_form_dict = lusid_problem_details.from_dict(lusid_problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


