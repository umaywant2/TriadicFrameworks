# docs/schemas/rsadi-gd/godot/rsadi_gd_types.gd
class_name GDPosition
extends RefCounted

var x: float
var y: float
var z: float

func to_vector3() -> Vector3:
    return Vector3(x, y, z)

static func from_vector3(v: Vector3) -> GDPosition:
    var p := GDPosition.new()
    p.x = v.x
    p.y = v.y
    p.z = v.z
    return p


class_name GDDriftVector
extends RefCounted

var dx: float
var dy: float
var dz: float
var magnitude: float
var units: String = "1/s"


class_name GDClaritySample
extends RefCounted

var sample_id: String
var timestamp: String
var position: GDPosition
var clarity_score: int
var stress_hint: int
var extensions := {}


class_name GDZoneState
extends RefCounted

var zone_id: String
var timestamp: String
var clarity_score: int
var stress_hint: int
var risk_level: String
var drift_vector: GDDriftVector
var extensions := {}


class_name GDRoutePoint
extends RefCounted

var position: GDPosition
var clarity_score: int


class_name GDRouteSuggestion
extends RefCounted

var route_id: String
var timestamp: String
var from_position: GDPosition
var to_position: GDPosition
var clarity_profile: Array[GDRoutePoint] = []
var risk_level: String
var instructions: Array[String] = []
var extensions := {}
