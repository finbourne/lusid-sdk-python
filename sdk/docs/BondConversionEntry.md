# BondConversionEntry

Information required to specify a conversion event for a convertible bond.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date at which the bond can be converted | [optional] 
**denomination** | **float** | The number of shares to be issued on conversion will be equal to the denomination of the  bond divided by the conversion price.  Two (and only two) entries out of (Price, Ratio, Denomination) must be provided.  So, to allow one entry out of the three to not be provided, we make all the three  nullable defaulting to zero and during validation we check if there is exactly one  of the three equal to zero. | [optional] 
**price** | **float** | The conversion price  Two (and only two) entries out of (Price, Ratio, Denomination) must be provided.  So, to allow one entry out of the three to not be provided, we make all the three  nullable defaulting to zero and during validation we check if there is exactly one  of the three equal to zero. | [optional] 
**ratio** | **float** | The number of common shares received at the time of conversion for each convertible bond  Two (and only two) entries out of (Price, Ratio, Denomination) must be provided.  So, to allow one entry out of the three to not be provided, we make all the three  nullable defaulting to zero and during validation we check if there is exactly one  of the three equal to zero. | [optional] 

## Example

```python
from lusid.models.bond_conversion_entry import BondConversionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BondConversionEntry from a JSON string
bond_conversion_entry_instance = BondConversionEntry.from_json(json)
# print the JSON string representation of the object
print BondConversionEntry.to_json()

# convert the object into a dict
bond_conversion_entry_dict = bond_conversion_entry_instance.to_dict()
# create an instance of BondConversionEntry from a dict
bond_conversion_entry_form_dict = bond_conversion_entry.from_dict(bond_conversion_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


