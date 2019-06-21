'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: page
Experimental: False
'''

from cdp.util import T_JSON_DICT
from dataclasses import dataclass
import enum
import typing

from ..network import types as network


class FrameId(str):
    '''
    Unique frame identifier.
    '''
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> 'FrameId':
        return cls(json)

    def __repr__(self):
        return 'FrameId({})'.format(super().__repr__())


class ScriptIdentifier(str):
    '''
    Unique script identifier.
    '''
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> 'ScriptIdentifier':
        return cls(json)

    def __repr__(self):
        return 'ScriptIdentifier({})'.format(super().__repr__())


class TransitionType(enum.Enum):
    '''
    Transition type.
    '''
    LINK = "link"
    TYPED = "typed"
    ADDRESS_BAR = "address_bar"
    AUTO_BOOKMARK = "auto_bookmark"
    AUTO_SUBFRAME = "auto_subframe"
    MANUAL_SUBFRAME = "manual_subframe"
    GENERATED = "generated"
    AUTO_TOPLEVEL = "auto_toplevel"
    FORM_SUBMIT = "form_submit"
    RELOAD = "reload"
    KEYWORD = "keyword"
    KEYWORD_GENERATED = "keyword_generated"
    OTHER = "other"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> 'TransitionType':
        return cls(json)


class DialogType(enum.Enum):
    '''
    Javascript dialog type.
    '''
    ALERT = "alert"
    CONFIRM = "confirm"
    PROMPT = "prompt"
    BEFOREUNLOAD = "beforeunload"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> 'DialogType':
        return cls(json)


class ClientNavigationReason(enum.Enum):
    FORM_SUBMISSION_GET = "formSubmissionGet"
    FORM_SUBMISSION_POST = "formSubmissionPost"
    HTTP_HEADER_REFRESH = "httpHeaderRefresh"
    SCRIPT_INITIATED = "scriptInitiated"
    META_TAG_REFRESH = "metaTagRefresh"
    PAGE_BLOCK_INTERSTITIAL = "pageBlockInterstitial"
    RELOAD = "reload"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> 'ClientNavigationReason':
        return cls(json)


@dataclass
class Frame:
    '''
    Information about the Frame on the page.
    '''
    #: Frame unique identifier.
    id: str

    #: Identifier of the loader associated with this frame.
    loader_id: network.LoaderId

    #: Frame document's URL.
    url: str

    #: Frame document's security origin.
    security_origin: str

    #: Frame document's mimeType as determined by the browser.
    mime_type: str

    #: Parent frame identifier.
    parent_id: typing.Optional[str] = None

    #: Frame's name as specified in the tag.
    name: typing.Optional[str] = None

    #: If the frame failed to load, this contains the URL that could not be loaded.
    unreachable_url: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'id': self.id,
            'loaderId': self.loader_id.to_json(),
            'url': self.url,
            'securityOrigin': self.security_origin,
            'mimeType': self.mime_type,
        }
        if self.parent_id is not None:
            json['parentId'] = self.parent_id
        if self.name is not None:
            json['name'] = self.name
        if self.unreachable_url is not None:
            json['unreachableUrl'] = self.unreachable_url
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'Frame':
        parent_id = json['parentId'] if 'parentId' in json else None
        name = json['name'] if 'name' in json else None
        unreachable_url = json['unreachableUrl'] if 'unreachableUrl' in json else None
        return cls(
            id=json['id'],
            parent_id=parent_id,
            loader_id=network.LoaderId.from_json(json['loaderId']),
            name=name,
            url=json['url'],
            security_origin=json['securityOrigin'],
            mime_type=json['mimeType'],
            unreachable_url=unreachable_url,
        )

@dataclass
class FrameResource:
    '''
    Information about the Resource on the page.
    '''
    #: Resource URL.
    url: str

    #: Type of this resource.
    type: network.ResourceType

    #: Resource mimeType as determined by the browser.
    mime_type: str

    #: last-modified timestamp as reported by server.
    last_modified: typing.Optional[network.TimeSinceEpoch] = None

    #: Resource content size.
    content_size: typing.Optional[float] = None

    #: True if the resource failed to load.
    failed: typing.Optional[bool] = None

    #: True if the resource was canceled during loading.
    canceled: typing.Optional[bool] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'url': self.url,
            'type': self.type.to_json(),
            'mimeType': self.mime_type,
        }
        if self.last_modified is not None:
            json['lastModified'] = self.last_modified.to_json()
        if self.content_size is not None:
            json['contentSize'] = self.content_size
        if self.failed is not None:
            json['failed'] = self.failed
        if self.canceled is not None:
            json['canceled'] = self.canceled
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'FrameResource':
        last_modified = network.TimeSinceEpoch.from_json(json['lastModified']) if 'lastModified' in json else None
        content_size = json['contentSize'] if 'contentSize' in json else None
        failed = json['failed'] if 'failed' in json else None
        canceled = json['canceled'] if 'canceled' in json else None
        return cls(
            url=json['url'],
            type=network.ResourceType.from_json(json['type']),
            mime_type=json['mimeType'],
            last_modified=last_modified,
            content_size=content_size,
            failed=failed,
            canceled=canceled,
        )

@dataclass
class FrameResourceTree:
    '''
    Information about the Frame hierarchy along with their cached resources.
    '''
    #: Frame information for this tree item.
    frame: Frame

    #: Information about frame resources.
    resources: typing.List['FrameResource']

    #: Child frames.
    child_frames: typing.Optional[typing.List['FrameResourceTree']] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'frame': self.frame.to_json(),
            'resources': [i.to_json() for i in self.resources],
        }
        if self.child_frames is not None:
            json['childFrames'] = [i.to_json() for i in self.child_frames]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'FrameResourceTree':
        child_frames = [FrameResourceTree.from_json(i) for i in json['childFrames']] if 'childFrames' in json else None
        return cls(
            frame=Frame.from_json(json['frame']),
            child_frames=child_frames,
            resources=[FrameResource.from_json(i) for i in json['resources']],
        )

@dataclass
class FrameTree:
    '''
    Information about the Frame hierarchy.
    '''
    #: Frame information for this tree item.
    frame: Frame

    #: Child frames.
    child_frames: typing.Optional[typing.List['FrameTree']] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'frame': self.frame.to_json(),
        }
        if self.child_frames is not None:
            json['childFrames'] = [i.to_json() for i in self.child_frames]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'FrameTree':
        child_frames = [FrameTree.from_json(i) for i in json['childFrames']] if 'childFrames' in json else None
        return cls(
            frame=Frame.from_json(json['frame']),
            child_frames=child_frames,
        )

@dataclass
class NavigationEntry:
    '''
    Navigation history entry.
    '''
    #: Unique id of the navigation history entry.
    id: int

    #: URL of the navigation history entry.
    url: str

    #: URL that the user typed in the url bar.
    user_typed_url: str

    #: Title of the navigation history entry.
    title: str

    #: Transition type.
    transition_type: TransitionType

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'id': self.id,
            'url': self.url,
            'userTypedURL': self.user_typed_url,
            'title': self.title,
            'transitionType': self.transition_type.to_json(),
        }
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'NavigationEntry':
        return cls(
            id=json['id'],
            url=json['url'],
            user_typed_url=json['userTypedURL'],
            title=json['title'],
            transition_type=TransitionType.from_json(json['transitionType']),
        )

@dataclass
class ScreencastFrameMetadata:
    '''
    Screencast frame metadata.
    '''
    #: Top offset in DIP.
    offset_top: float

    #: Page scale factor.
    page_scale_factor: float

    #: Device screen width in DIP.
    device_width: float

    #: Device screen height in DIP.
    device_height: float

    #: Position of horizontal scroll in CSS pixels.
    scroll_offset_x: float

    #: Position of vertical scroll in CSS pixels.
    scroll_offset_y: float

    #: Frame swap timestamp.
    timestamp: typing.Optional[network.TimeSinceEpoch] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'offsetTop': self.offset_top,
            'pageScaleFactor': self.page_scale_factor,
            'deviceWidth': self.device_width,
            'deviceHeight': self.device_height,
            'scrollOffsetX': self.scroll_offset_x,
            'scrollOffsetY': self.scroll_offset_y,
        }
        if self.timestamp is not None:
            json['timestamp'] = self.timestamp.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ScreencastFrameMetadata':
        timestamp = network.TimeSinceEpoch.from_json(json['timestamp']) if 'timestamp' in json else None
        return cls(
            offset_top=json['offsetTop'],
            page_scale_factor=json['pageScaleFactor'],
            device_width=json['deviceWidth'],
            device_height=json['deviceHeight'],
            scroll_offset_x=json['scrollOffsetX'],
            scroll_offset_y=json['scrollOffsetY'],
            timestamp=timestamp,
        )

@dataclass
class AppManifestError:
    '''
    Error while paring app manifest.
    '''
    #: Error message.
    message: str

    #: If criticial, this is a non-recoverable parse error.
    critical: int

    #: Error line.
    line: int

    #: Error column.
    column: int

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'message': self.message,
            'critical': self.critical,
            'line': self.line,
            'column': self.column,
        }
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'AppManifestError':
        return cls(
            message=json['message'],
            critical=json['critical'],
            line=json['line'],
            column=json['column'],
        )

@dataclass
class LayoutViewport:
    '''
    Layout viewport position and dimensions.
    '''
    #: Horizontal offset relative to the document (CSS pixels).
    page_x: int

    #: Vertical offset relative to the document (CSS pixels).
    page_y: int

    #: Width (CSS pixels), excludes scrollbar if present.
    client_width: int

    #: Height (CSS pixels), excludes scrollbar if present.
    client_height: int

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'pageX': self.page_x,
            'pageY': self.page_y,
            'clientWidth': self.client_width,
            'clientHeight': self.client_height,
        }
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'LayoutViewport':
        return cls(
            page_x=json['pageX'],
            page_y=json['pageY'],
            client_width=json['clientWidth'],
            client_height=json['clientHeight'],
        )

@dataclass
class VisualViewport:
    '''
    Visual viewport position, dimensions, and scale.
    '''
    #: Horizontal offset relative to the layout viewport (CSS pixels).
    offset_x: float

    #: Vertical offset relative to the layout viewport (CSS pixels).
    offset_y: float

    #: Horizontal offset relative to the document (CSS pixels).
    page_x: float

    #: Vertical offset relative to the document (CSS pixels).
    page_y: float

    #: Width (CSS pixels), excludes scrollbar if present.
    client_width: float

    #: Height (CSS pixels), excludes scrollbar if present.
    client_height: float

    #: Scale relative to the ideal viewport (size at width=device-width).
    scale: float

    #: Page zoom factor (CSS to device independent pixels ratio).
    zoom: typing.Optional[float] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'offsetX': self.offset_x,
            'offsetY': self.offset_y,
            'pageX': self.page_x,
            'pageY': self.page_y,
            'clientWidth': self.client_width,
            'clientHeight': self.client_height,
            'scale': self.scale,
        }
        if self.zoom is not None:
            json['zoom'] = self.zoom
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'VisualViewport':
        zoom = json['zoom'] if 'zoom' in json else None
        return cls(
            offset_x=json['offsetX'],
            offset_y=json['offsetY'],
            page_x=json['pageX'],
            page_y=json['pageY'],
            client_width=json['clientWidth'],
            client_height=json['clientHeight'],
            scale=json['scale'],
            zoom=zoom,
        )

@dataclass
class Viewport:
    '''
    Viewport for capturing screenshot.
    '''
    #: X offset in device independent pixels (dip).
    x: float

    #: Y offset in device independent pixels (dip).
    y: float

    #: Rectangle width in device independent pixels (dip).
    width: float

    #: Rectangle height in device independent pixels (dip).
    height: float

    #: Page scale factor.
    scale: float

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'scale': self.scale,
        }
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'Viewport':
        return cls(
            x=json['x'],
            y=json['y'],
            width=json['width'],
            height=json['height'],
            scale=json['scale'],
        )

@dataclass
class FontFamilies:
    '''
    Generic font families collection.
    '''
    #: The standard font-family.
    standard: typing.Optional[str] = None

    #: The fixed font-family.
    fixed: typing.Optional[str] = None

    #: The serif font-family.
    serif: typing.Optional[str] = None

    #: The sansSerif font-family.
    sans_serif: typing.Optional[str] = None

    #: The cursive font-family.
    cursive: typing.Optional[str] = None

    #: The fantasy font-family.
    fantasy: typing.Optional[str] = None

    #: The pictograph font-family.
    pictograph: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
        }
        if self.standard is not None:
            json['standard'] = self.standard
        if self.fixed is not None:
            json['fixed'] = self.fixed
        if self.serif is not None:
            json['serif'] = self.serif
        if self.sans_serif is not None:
            json['sansSerif'] = self.sans_serif
        if self.cursive is not None:
            json['cursive'] = self.cursive
        if self.fantasy is not None:
            json['fantasy'] = self.fantasy
        if self.pictograph is not None:
            json['pictograph'] = self.pictograph
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'FontFamilies':
        standard = json['standard'] if 'standard' in json else None
        fixed = json['fixed'] if 'fixed' in json else None
        serif = json['serif'] if 'serif' in json else None
        sans_serif = json['sansSerif'] if 'sansSerif' in json else None
        cursive = json['cursive'] if 'cursive' in json else None
        fantasy = json['fantasy'] if 'fantasy' in json else None
        pictograph = json['pictograph'] if 'pictograph' in json else None
        return cls(
            standard=standard,
            fixed=fixed,
            serif=serif,
            sans_serif=sans_serif,
            cursive=cursive,
            fantasy=fantasy,
            pictograph=pictograph,
        )

@dataclass
class FontSizes:
    '''
    Default font sizes.
    '''
    #: Default standard font size.
    standard: typing.Optional[int] = None

    #: Default fixed font size.
    fixed: typing.Optional[int] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = {
        }
        if self.standard is not None:
            json['standard'] = self.standard
        if self.fixed is not None:
            json['fixed'] = self.fixed
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'FontSizes':
        standard = json['standard'] if 'standard' in json else None
        fixed = json['fixed'] if 'fixed' in json else None
        return cls(
            standard=standard,
            fixed=fixed,
        )

