# UpsertInvestorRecordRequest

Request to create or update an investor record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investor Record. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investor Record. | [optional] 
**display_name** | **str** | The display name of the Investor Record | 
**description** | **str** | The description of the Investor Record | [optional] 
**investor** | [**UpsertInvestor**](UpsertInvestor.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_investor_record_request import UpsertInvestorRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertInvestorRecordRequest from a JSON string
upsert_investor_record_request_instance = UpsertInvestorRecordRequest.from_json(json)
# print the JSON string representation of the object
print UpsertInvestorRecordRequest.to_json()

# convert the object into a dict
upsert_investor_record_request_dict = upsert_investor_record_request_instance.to_dict()
# create an instance of UpsertInvestorRecordRequest from a dict
upsert_investor_record_request_form_dict = upsert_investor_record_request.from_dict(upsert_investor_record_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


