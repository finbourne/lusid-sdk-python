# MarginExplanationComponent

One step in the working behind a margin figure: a value and, unless it is a leaf, the arithmetic over its  sub-components that gives it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the component within its explanation: its position in the tree as dot-separated indexes from the root, such as 0.1.3, the first index being the root&#39;s place among the explanation&#39;s components. | 
**component** | **str** | A stable name for what the component is, such as PvInBase. A component whose rows the caller may not read is named Redacted. | 
**display_name** | **str** | A human-readable name for the component. | 
**type** | **str** | How the component takes its value. One of DerivedProperty, PartialFormula, Variable or Literal. | 
**value** | **float** | The figure the engine used for the component, as it was computed. Null where the component has none or, for a redacted component, where the rows it stands in for do not share a unit and currency. | [optional] 
**unit** | **str** | What the value measures. One of Currency, Percentage, Factor, Units or Years. Null where the value is unitless. | [optional] 
**currency** | **str** | The currency of a Currency value when it is not the explanation&#39;s currency. | [optional] 
**derivation_formula** | **str** | Plain arithmetic over the sub-components that gives the component&#39;s value. Null for a component with no sub-components. | [optional] 
**sub_components** | [**List[MarginExplanationComponent]**](MarginExplanationComponent.md) | The components the derivation formula reads. Null for a component that cannot be broken down further. | [optional] 
**redacted** | **bool** | True for a component that stands in for the working of portfolios the caller may not read. The caller sees that those portfolios contributed and, when their rows share a unit and currency, their combined value, so that the parent still adds up to the figure; never which portfolios or holdings they were. Null otherwise. | [optional] 
## Example

```python
from lusid.models.margin_explanation_component import MarginExplanationComponent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
component: StrictStr = "example_component"
display_name: StrictStr = "example_display_name"
type: StrictStr = "example_type"
value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unit: Optional[StrictStr] = "example_unit"
currency: Optional[StrictStr] = "example_currency"
derivation_formula: Optional[StrictStr] = "example_derivation_formula"
sub_components: Optional[List[MarginExplanationComponent]] = # Replace with your value
redacted: Optional[StrictBool] = # Replace with your value
redacted:Optional[StrictBool] = None
margin_explanation_component_instance = MarginExplanationComponent(id=id, component=component, display_name=display_name, type=type, value=value, unit=unit, currency=currency, derivation_formula=derivation_formula, sub_components=sub_components, redacted=redacted)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

