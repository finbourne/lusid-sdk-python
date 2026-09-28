# FundStructureEdge

A link from one member of a Fund Structure to another, and how that link is held.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The node code of the member that holds the link: the investor or the owner. | 
**to** | [**FundStructureEdgeTarget**](FundStructureEdgeTarget.md) |  | 
**linkage_type** | **str** | How the link is held. DedicatedShareClass (the default) means the source invests into a share class of the target; DirectEquityInstrument, GPInterest, LPInterest and CarryInterest mean the source holds that interest in the target through the instrument in viaInstrumentId. Available values: DedicatedShareClass, DirectEquityInstrument, GPInterest, LPInterest, CarryInterest. | [optional] 
**via_instrument_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.fund_structure_edge import FundStructureEdge
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_from: StrictStr = "example_var_from"
to: FundStructureEdgeTarget
linkage_type: Optional[StrictStr] = "example_linkage_type"
via_instrument_id: Optional[ResourceId] = # Replace with your value
fund_structure_edge_instance = FundStructureEdge(var_from=var_from, to=to, linkage_type=linkage_type, via_instrument_id=via_instrument_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

