# CancelSingleHoldingAdjustmentRequest

This request specifies single target holding. i.e. holding data that the  system should match. And deletes previous adjustment made to that holding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**currency** | **str** | The Holding currency. | [optional] 

## Example

```python
from lusid.models.cancel_single_holding_adjustment_request import CancelSingleHoldingAdjustmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelSingleHoldingAdjustmentRequest from a JSON string
cancel_single_holding_adjustment_request_instance = CancelSingleHoldingAdjustmentRequest.from_json(json)
# print the JSON string representation of the object
print CancelSingleHoldingAdjustmentRequest.to_json()

# convert the object into a dict
cancel_single_holding_adjustment_request_dict = cancel_single_holding_adjustment_request_instance.to_dict()
# create an instance of CancelSingleHoldingAdjustmentRequest from a dict
cancel_single_holding_adjustment_request_form_dict = cancel_single_holding_adjustment_request.from_dict(cancel_single_holding_adjustment_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


