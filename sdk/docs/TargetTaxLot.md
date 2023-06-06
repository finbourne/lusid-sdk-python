# TargetTaxLot

Used to specify holdings target amounts at the tax-lot level

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **float** | The number of units of the instrument in this tax-lot. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**portfolio_cost** | **float** | The total cost of the tax-lot in the transaction portfolio&#39;s base currency. | [optional] 
**price** | **float** | The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**purchase_date** | **datetime** | The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**settlement_date** | **datetime** | The settlement date of the tax-lot&#39;s opening transaction. | [optional] 

## Example

```python
from lusid.models.target_tax_lot import TargetTaxLot

# TODO update the JSON string below
json = "{}"
# create an instance of TargetTaxLot from a JSON string
target_tax_lot_instance = TargetTaxLot.from_json(json)
# print the JSON string representation of the object
print TargetTaxLot.to_json()

# convert the object into a dict
target_tax_lot_dict = target_tax_lot_instance.to_dict()
# create an instance of TargetTaxLot from a dict
target_tax_lot_form_dict = target_tax_lot.from_dict(target_tax_lot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


