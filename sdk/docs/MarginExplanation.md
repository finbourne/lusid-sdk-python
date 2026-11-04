# MarginExplanation

How the margin figures of a call or a line were arrived at: the working behind each figure as a tree of components,  with the working of portfolios the caller may not read replaced by a redacted component.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of this explanation. | [optional] 
**run_id** | **str** | The run whose figures are explained. | 
**agreement_id** | [**ResourceId**](ResourceId.md) |  | 
**item** | **str** | The margin item of the call explained or, for a line, of the line. | [optional] 
**margin_type** | **str** | The margin type of the call explained. Null when a line is explained. | [optional] 
**direction** | **str** | Who posts under the call explained: WePost, TheyPost or None. Null when a line is explained. | [optional] 
**line_key** | **str** | The key of the line explained. Null when a call is explained. | [optional] 
**currency** | **str** | The agreement&#39;s base currency, in which a component&#39;s value is expressed unless the component names another. | 
**scenario** | [**ResourceId**](ResourceId.md) |  | [optional] 
**components** | [**List[MarginExplanationComponent]**](MarginExplanationComponent.md) | The working behind each figure explained, one root component per figure: for a call its required amount, named InitialMarginRequired, and for a line each figure asked for that the run explained, named VariationMargin or InitialMargin. | 
## Example

```python
from lusid.models.margin_explanation import MarginExplanation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
run_id: StrictStr = "example_run_id"
agreement_id: ResourceId = # Replace with your value
item: Optional[StrictStr] = "example_item"
margin_type: Optional[StrictStr] = "example_margin_type"
direction: Optional[StrictStr] = "example_direction"
line_key: Optional[StrictStr] = "example_line_key"
currency: StrictStr = "example_currency"
scenario: Optional[ResourceId] = None
components: List[MarginExplanationComponent] = # Replace with your value
margin_explanation_instance = MarginExplanation(href=href, run_id=run_id, agreement_id=agreement_id, item=item, margin_type=margin_type, direction=direction, line_key=line_key, currency=currency, scenario=scenario, components=components)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

