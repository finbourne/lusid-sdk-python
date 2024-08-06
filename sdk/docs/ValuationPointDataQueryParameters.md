# ValuationPointDataQueryParameters

The parameters used in getting the ValuationPointData.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 

## Example

```python
from lusid.models.valuation_point_data_query_parameters import ValuationPointDataQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ValuationPointDataQueryParameters from a JSON string
valuation_point_data_query_parameters_instance = ValuationPointDataQueryParameters.from_json(json)
# print the JSON string representation of the object
print ValuationPointDataQueryParameters.to_json()

# convert the object into a dict
valuation_point_data_query_parameters_dict = valuation_point_data_query_parameters_instance.to_dict()
# create an instance of ValuationPointDataQueryParameters from a dict
valuation_point_data_query_parameters_form_dict = valuation_point_data_query_parameters.from_dict(valuation_point_data_query_parameters_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


