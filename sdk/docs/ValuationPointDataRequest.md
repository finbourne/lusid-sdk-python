# ValuationPointDataRequest

The ValuationPointDataRequest.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code for the Valuation Point. | 

## Example

```python
from lusid.models.valuation_point_data_request import ValuationPointDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValuationPointDataRequest from a JSON string
valuation_point_data_request_instance = ValuationPointDataRequest.from_json(json)
# print the JSON string representation of the object
print ValuationPointDataRequest.to_json()

# convert the object into a dict
valuation_point_data_request_dict = valuation_point_data_request_instance.to_dict()
# create an instance of ValuationPointDataRequest from a dict
valuation_point_data_request_form_dict = valuation_point_data_request.from_dict(valuation_point_data_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


