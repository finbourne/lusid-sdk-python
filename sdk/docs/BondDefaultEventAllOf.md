# BondDefaultEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Percentage or amount of each share held to be given to shareholders. | 
**coupon_paid_date** | **datetime** | Date that the missed coupon is paid if payment is made within grace period. | 
**default_status** | **str** | The status of the bond default (i.e., technical or default)    Supported string (enumeration) values are: [Technical, Default]. | 
**default_type** | **str** | The type of the default. (coupon payment, principal payment, covenant ...)    Supported string (enumeration) values are: [CouponPayment, CouponAndPrincipalPayment, PrincipalPayment, Covenant, Bankruptcy, BuyBackOption]. | 
**grace_end_date** | **datetime** | Date the grace period for making coupon payment ends. | 
**payment_date** | **datetime** | The date the coupon payment was missed. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent | 

## Example

```python
from lusid.models.bond_default_event_all_of import BondDefaultEventAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BondDefaultEventAllOf from a JSON string
bond_default_event_all_of_instance = BondDefaultEventAllOf.from_json(json)
# print the JSON string representation of the object
print BondDefaultEventAllOf.to_json()

# convert the object into a dict
bond_default_event_all_of_dict = bond_default_event_all_of_instance.to_dict()
# create an instance of BondDefaultEventAllOf from a dict
bond_default_event_all_of_form_dict = bond_default_event_all_of.from_dict(bond_default_event_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


