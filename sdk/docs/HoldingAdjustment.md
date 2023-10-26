# HoldingAdjustment

The target holdings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. | [optional] 
**instrument_scope** | **str** | The scope of the instrument that the holding adjustment is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#39;Transaction&#39; domain. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#39;Holding&#39; domain. | [optional] 
**tax_lots** | [**List[TargetTaxLot]**](TargetTaxLot.md) | The tax-lots that together make up the target holding. | 
**currency** | **str** | The Holding currency. | [optional] 

## Example

```python
from lusid.models.holding_adjustment import HoldingAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingAdjustment from a JSON string
holding_adjustment_instance = HoldingAdjustment.from_json(json)
# print the JSON string representation of the object
print HoldingAdjustment.to_json()

# convert the object into a dict
holding_adjustment_dict = holding_adjustment_instance.to_dict()
# create an instance of HoldingAdjustment from a dict
holding_adjustment_form_dict = holding_adjustment.from_dict(holding_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


