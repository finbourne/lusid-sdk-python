# UpsertValuationPointRequest

A definition for the period you wish to close

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code for the Valuation Point. | 
**name** | **str** | Identifiable Name assigned to the Valuation Point. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 

## Example

```python
from lusid.models.upsert_valuation_point_request import UpsertValuationPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertValuationPointRequest from a JSON string
upsert_valuation_point_request_instance = UpsertValuationPointRequest.from_json(json)
# print the JSON string representation of the object
print UpsertValuationPointRequest.to_json()

# convert the object into a dict
upsert_valuation_point_request_dict = upsert_valuation_point_request_instance.to_dict()
# create an instance of UpsertValuationPointRequest from a dict
upsert_valuation_point_request_form_dict = upsert_valuation_point_request.from_dict(upsert_valuation_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


