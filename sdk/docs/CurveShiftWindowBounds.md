# CurveShiftWindowBounds

Which bounds of a curve shift's tenor window admit a pillar sitting exactly on them.  Inclusive - the closed window [StartTenor, EndTenor], and the behaviour of every scenario  stored before this field existed - is the default. An exclusive bound rejects the pillar  sitting exactly on it, which is what lets two adjacent windows share a boundary tenor  without both shifting that pillar: a shift over [A, B) composed with one over [B, C]  moves the pillar at B exactly once, where two inclusive windows would both match it and  their amounts would add.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

