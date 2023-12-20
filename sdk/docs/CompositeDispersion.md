# CompositeDispersion

A list of Dispersion calculations for the given years.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The date for which dipsersion calculation has been done. This should be 31 Dec for each given year. | 
**dispersion_calculation** | **float** | The result for the dispersion calculation on the given effectiveAt. | [optional] 
**variance** | **float** | The variance on the given effectiveAt. | [optional] 
**first_quartile** | **float** | First Quartile (Q1) &#x3D;  (lower quartile) &#x3D; the middle of the bottom half of the returns. | [optional] 
**third_quartile** | **float** | Third Quartile (Q3) &#x3D;  (higher quartile) &#x3D; the middle of the top half of the returns. | [optional] 
**range** | **float** | Highest return - Lowest return. | [optional] 
**constituents_in_scope** | [**List[ResourceId]**](ResourceId.md) | List containing Composite members which are part of the dispersion calcualtion. | [optional] 
**constituents_excluded** | [**List[ResourceId]**](ResourceId.md) | List containing the Composite members which are not part of the dispersion calculation | [optional] 

## Example

```python
from lusid.models.composite_dispersion import CompositeDispersion

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeDispersion from a JSON string
composite_dispersion_instance = CompositeDispersion.from_json(json)
# print the JSON string representation of the object
print CompositeDispersion.to_json()

# convert the object into a dict
composite_dispersion_dict = composite_dispersion_instance.to_dict()
# create an instance of CompositeDispersion from a dict
composite_dispersion_form_dict = composite_dispersion.from_dict(composite_dispersion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


