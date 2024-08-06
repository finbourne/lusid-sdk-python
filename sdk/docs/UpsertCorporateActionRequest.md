# UpsertCorporateActionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_code** | **str** | The unique identifier of this corporate action | 
**description** | **str** | The description of the corporate action. | [optional] 
**announcement_date** | **datetime** | The announcement date of the corporate action | 
**ex_date** | **datetime** | The ex date of the corporate action | 
**record_date** | **datetime** | The record date of the corporate action | 
**payment_date** | **datetime** | The payment date of the corporate action | 
**transitions** | [**List[CorporateActionTransitionRequest]**](CorporateActionTransitionRequest.md) | The transitions that result from this corporate action | 

## Example

```python
from lusid.models.upsert_corporate_action_request import UpsertCorporateActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCorporateActionRequest from a JSON string
upsert_corporate_action_request_instance = UpsertCorporateActionRequest.from_json(json)
# print the JSON string representation of the object
print UpsertCorporateActionRequest.to_json()

# convert the object into a dict
upsert_corporate_action_request_dict = upsert_corporate_action_request_instance.to_dict()
# create an instance of UpsertCorporateActionRequest from a dict
upsert_corporate_action_request_form_dict = upsert_corporate_action_request.from_dict(upsert_corporate_action_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


