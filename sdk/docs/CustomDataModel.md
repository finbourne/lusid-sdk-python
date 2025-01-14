# CustomDataModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_model_summary** | [**DataModelSummary**](DataModelSummary.md) |  | [optional] 
**inherited** | [**CustomDataModelCriteria**](CustomDataModelCriteria.md) |  | [optional] 
**incremental** | [**CustomDataModelCriteria**](CustomDataModelCriteria.md) |  | [optional] 
**applied** | [**CustomDataModelCriteria**](CustomDataModelCriteria.md) |  | [optional] 

## Example

```python
from lusid.models.custom_data_model import CustomDataModel

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataModel from a JSON string
custom_data_model_instance = CustomDataModel.from_json(json)
# print the JSON string representation of the object
print CustomDataModel.to_json()

# convert the object into a dict
custom_data_model_dict = custom_data_model_instance.to_dict()
# create an instance of CustomDataModel from a dict
custom_data_model_form_dict = custom_data_model.from_dict(custom_data_model_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


