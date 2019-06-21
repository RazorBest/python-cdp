'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: target
Experimental: False
'''

from cdp.util import T_JSON_DICT
from dataclasses import dataclass
import enum
import typing

from .types import *


@dataclass
class AttachedToTarget:
    '''
    Issued when attached to target because of auto-attach or `attachToTarget` command.
    '''
    #: Issued when attached to target because of auto-attach or `attachToTarget` command.
    session_id: SessionID

    #: Issued when attached to target because of auto-attach or `attachToTarget` command.
    target_info: TargetInfo

    #: Issued when attached to target because of auto-attach or `attachToTarget` command.
    waiting_for_debugger: bool

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'attachedToTarget'

    @classmethod
    def from_json(cls, json: dict) -> 'AttachedToTarget':
        return cls(
            session_id=SessionID.from_json(json['sessionId']),
            target_info=TargetInfo.from_json(json['targetInfo']),
            waiting_for_debugger=bool(json['waitingForDebugger']),
        )


@dataclass
class DetachedFromTarget:
    '''
    Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    issued multiple times per target if multiple sessions have been attached to it.
    '''
    #: Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    #: issued multiple times per target if multiple sessions have been attached to it.
    session_id: SessionID

    #: Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    #: issued multiple times per target if multiple sessions have been attached to it.
    target_id: typing.Optional[TargetID] = None

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'detachedFromTarget'

    @classmethod
    def from_json(cls, json: dict) -> 'DetachedFromTarget':
        target_id = TargetID.from_json(json['targetId']) if 'targetId' in json else None
        return cls(
            session_id=SessionID.from_json(json['sessionId']),
            target_id=target_id,
        )


@dataclass
class ReceivedMessageFromTarget:
    '''
    Notifies about a new protocol message received from the session (as reported in
    `attachedToTarget` event).
    '''
    #: Notifies about a new protocol message received from the session (as reported in
    #: `attachedToTarget` event).
    session_id: SessionID

    #: Notifies about a new protocol message received from the session (as reported in
    #: `attachedToTarget` event).
    message: str

    #: Notifies about a new protocol message received from the session (as reported in
    #: `attachedToTarget` event).
    target_id: typing.Optional[TargetID] = None

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'receivedMessageFromTarget'

    @classmethod
    def from_json(cls, json: dict) -> 'ReceivedMessageFromTarget':
        target_id = TargetID.from_json(json['targetId']) if 'targetId' in json else None
        return cls(
            session_id=SessionID.from_json(json['sessionId']),
            message=str(json['message']),
            target_id=target_id,
        )


@dataclass
class TargetCreated:
    '''
    Issued when a possible inspection target is created.
    '''
    #: Issued when a possible inspection target is created.
    target_info: TargetInfo

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'targetCreated'

    @classmethod
    def from_json(cls, json: dict) -> 'TargetCreated':
        return cls(
            target_info=TargetInfo.from_json(json['targetInfo']),
        )


@dataclass
class TargetDestroyed:
    '''
    Issued when a target is destroyed.
    '''
    #: Issued when a target is destroyed.
    target_id: TargetID

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'targetDestroyed'

    @classmethod
    def from_json(cls, json: dict) -> 'TargetDestroyed':
        return cls(
            target_id=TargetID.from_json(json['targetId']),
        )


@dataclass
class TargetCrashed:
    '''
    Issued when a target has crashed.
    '''
    #: Issued when a target has crashed.
    target_id: TargetID

    #: Issued when a target has crashed.
    status: str

    #: Issued when a target has crashed.
    error_code: int

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'targetCrashed'

    @classmethod
    def from_json(cls, json: dict) -> 'TargetCrashed':
        return cls(
            target_id=TargetID.from_json(json['targetId']),
            status=str(json['status']),
            error_code=int(json['errorCode']),
        )


@dataclass
class TargetInfoChanged:
    '''
    Issued when some information about a target has changed. This only happens between
    `targetCreated` and `targetDestroyed`.
    '''
    #: Issued when some information about a target has changed. This only happens between
    #: `targetCreated` and `targetDestroyed`.
    target_info: TargetInfo

    # These fields are used for internal purposes and are not part of CDP
    _domain = 'Target'
    _method = 'targetInfoChanged'

    @classmethod
    def from_json(cls, json: dict) -> 'TargetInfoChanged':
        return cls(
            target_info=TargetInfo.from_json(json['targetInfo']),
        )

