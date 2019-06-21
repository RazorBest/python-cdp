'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: layer_tree
Experimental: True
'''

from cdp.util import T_JSON_DICT
from dataclasses import dataclass
import enum
import typing

from .types import *
from ..dom import types as dom



@dataclass
class LayerPainted:
    layer_id: LayerId

    clip: dom.Rect

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'LayerTree'
    _method = 'layerPainted'

    @classmethod
    def from_json(cls, json: dict) -> 'LayerPainted':
        return cls(
            layer_id=LayerId.from_json(json['layerId']),
            clip=dom.Rect.from_json(json['clip']),
        )


@dataclass
class LayerTreeDidChange:
    layers: typing.Optional[typing.List['Layer']] = None

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'LayerTree'
    _method = 'layerTreeDidChange'

    @classmethod
    def from_json(cls, json: dict) -> 'LayerTreeDidChange':
        layers = [Layer.from_json(i) for i in json['layers']] if 'layers' in json else None
        return cls(
            layers=layers,
        )

