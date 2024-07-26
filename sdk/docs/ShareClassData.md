# ShareClassData

The data for a Share Class. Includes Valuation Point Data and instrument information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_breakdown** | [**ShareClassBreakdown**](ShareClassBreakdown.md) |  | 
**share_class_details** | [**ShareClassDetails**](ShareClassDetails.md) |  | [optional] 

## Example

```python
from lusid.models.share_class_data import ShareClassData

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassData from a JSON string
share_class_data_instance = ShareClassData.from_json(json)
# print the JSON string representation of the object
print ShareClassData.to_json()

# convert the object into a dict
share_class_data_dict = share_class_data_instance.to_dict()
# create an instance of ShareClassData from a dict
share_class_data_form_dict = share_class_data.from_dict(share_class_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


