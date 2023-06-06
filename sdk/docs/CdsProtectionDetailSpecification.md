# CdsProtectionDetailSpecification

CDSs generally conform to fairly standard definitions, but can be tweaked in a number of different ways.  This class gathers a number of common features which may deviate. These will default to the market standard when  no overrides are provided.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seniority** | **str** | The seniority level of the CDS.    Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2]. | 
**restructuring_type** | **str** | The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR]. | 
**protect_start_day** | **bool** | Does the protection leg pay out in the case of default on the start date. | 
**pay_accrued_interest_on_default** | **bool** | Should accrued interest on the premium leg be paid if a credit event occurs. | 

## Example

```python
from lusid.models.cds_protection_detail_specification import CdsProtectionDetailSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of CdsProtectionDetailSpecification from a JSON string
cds_protection_detail_specification_instance = CdsProtectionDetailSpecification.from_json(json)
# print the JSON string representation of the object
print CdsProtectionDetailSpecification.to_json()

# convert the object into a dict
cds_protection_detail_specification_dict = cds_protection_detail_specification_instance.to_dict()
# create an instance of CdsProtectionDetailSpecification from a dict
cds_protection_detail_specification_form_dict = cds_protection_detail_specification.from_dict(cds_protection_detail_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


