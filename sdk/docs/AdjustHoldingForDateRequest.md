# AdjustHoldingForDateRequest

This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **str** | The Effective date that the target holding will be adjusted at. | 
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#39;Transaction&#39; domain. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#39;Holding&#39; domain. | [optional] 
**tax_lots** | [**List[TargetTaxLotRequest]**](TargetTaxLotRequest.md) | The tax-lots that together make up the target holding. | 
**currency** | **str** | The Holding currency. This needs to be equal with the one on the TaxLot -&gt; cost if one is specified | [optional] 

## Example

```python
from lusid.models.adjust_holding_for_date_request import AdjustHoldingForDateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustHoldingForDateRequest from a JSON string
adjust_holding_for_date_request_instance = AdjustHoldingForDateRequest.from_json(json)
# print the JSON string representation of the object
print AdjustHoldingForDateRequest.to_json()

# convert the object into a dict
adjust_holding_for_date_request_dict = adjust_holding_for_date_request_instance.to_dict()
# create an instance of AdjustHoldingForDateRequest from a dict
adjust_holding_for_date_request_form_dict = adjust_holding_for_date_request.from_dict(adjust_holding_for_date_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


