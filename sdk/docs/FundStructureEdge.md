# FundStructureEdge

A link from one member of a Fund Structure to another, and how that link is held.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The node code of the member that holds the link: the investor or the owner. | 
**to** | [**FundStructureEdgeTarget**](FundStructureEdgeTarget.md) |  | 
**linkage_type** | **str** | How the link is held. DedicatedShareClass (the default) means the source invests into a share class of the target; DirectEquityInstrument, GPInterest, LPInterest and CarryInterest mean the source holds that interest in the target through the instrument in viaInstrumentId. Available values: DedicatedShareClass, DirectEquityInstrument, GPInterest, LPInterest, CarryInterest. | [optional] 
**via_instrument_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**sharing_percentage** | **float** | The holder&#39;s ILPA sharing percentage in the target member, adjusted for transfers and equalisation but not reduced by ordinary distributions. Between 0 and 1 inclusive; the percentages declared into any one member must sum to no more than 1. Defaults to 1 (sole ownership) when not supplied. A value of 0 records a full exit: keep the edge and set it to 0 from the date the interest ended, so that the change in percentage from one version of the structure to the next tells the P&amp;L flow what was disposed of. Each disposal or acquisition trade of the holder&#39;s needs its own version of the structure, effective on that trade&#39;s date: proceeds received on a date with no change in percentage are taken as a distribution on the retained interest, not a disposal. A change in percentage with no trade of the holder&#39;s on its date takes effect at the holder&#39;s next transaction on the member or period close, whichever comes first. | [optional] 
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
sharing_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_structure_edge_instance = FundStructureEdge(var_from=var_from, to=to, linkage_type=linkage_type, via_instrument_id=via_instrument_id, sharing_percentage=sharing_percentage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

