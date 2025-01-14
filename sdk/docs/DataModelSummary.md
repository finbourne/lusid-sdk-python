# DataModelSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | The name of the Custom Data Model. | [optional] 
**description** | **str** | A description for the Custom Data Model. | [optional] 
**entity_type** | **str** | The entity type that the Custom Data Model binds to. | 
**type** | **str** | Either Root or Leaf or Intermediate. | [optional] 
**precedence** | **int** | Where in the hierarchy this model sits. | [optional] 
**children** | [**List[DataModelSummary]**](DataModelSummary.md) | Child Custom Data Models that will inherit from this data model. | [optional] 

## Example

```python
from lusid.models.data_model_summary import DataModelSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DataModelSummary from a JSON string
data_model_summary_instance = DataModelSummary.from_json(json)
# print the JSON string representation of the object
print DataModelSummary.to_json()

# convert the object into a dict
data_model_summary_dict = data_model_summary_instance.to_dict()
# create an instance of DataModelSummary from a dict
data_model_summary_form_dict = data_model_summary.from_dict(data_model_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


