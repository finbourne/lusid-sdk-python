# ResourceListOfDataModelSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[DataModelSummary]**](DataModelSummary.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_data_model_summary import ResourceListOfDataModelSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfDataModelSummary from a JSON string
resource_list_of_data_model_summary_instance = ResourceListOfDataModelSummary.from_json(json)
# print the JSON string representation of the object
print ResourceListOfDataModelSummary.to_json()

# convert the object into a dict
resource_list_of_data_model_summary_dict = resource_list_of_data_model_summary_instance.to_dict()
# create an instance of ResourceListOfDataModelSummary from a dict
resource_list_of_data_model_summary_form_dict = resource_list_of_data_model_summary.from_dict(resource_list_of_data_model_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


