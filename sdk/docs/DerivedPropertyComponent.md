# DerivedPropertyComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | The component of the formula which is being evaluated. | [optional] 
**type** | **str** | The type of the formula component. This can be a Literal, Variable, DerivedProperty, or PartialFormula. | [optional] 
**value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**derivation_formula** | **str** | The derivation formula of the component. This field will only be populated if the component is a derived property. | [optional] 
**sub_components** | [**List[DerivedPropertyComponent]**](DerivedPropertyComponent.md) | Any sub-components of this formula. If this formula cannot be further decomposed, this collection will be null. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.derived_property_component import DerivedPropertyComponent
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

component: Optional[StrictStr] = "example_component"
type: Optional[StrictStr] = "example_type"
value: Optional[PropertyValue] = None
derivation_formula: Optional[StrictStr] = "example_derivation_formula"
sub_components: Optional[conlist(DerivedPropertyComponent)] = # Replace with your value
links: Optional[conlist(Link)] = None
derived_property_component_instance = DerivedPropertyComponent(component=component, type=type, value=value, derivation_formula=derivation_formula, sub_components=sub_components, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

