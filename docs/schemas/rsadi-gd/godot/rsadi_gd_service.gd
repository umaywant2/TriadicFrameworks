# rsadi_gd_service.gd
class_name RSADIGDService
extends Node

func get_clarity(pos: Vector3) -> int:
    # stub: plug into your RSADI core
    return 200

func get_drift(pos: Vector3) -> GDDriftVector:
    var d := GDDriftVector.new()
    d.dx = 0.0
    d.dy = 0.0
    d.dz = 0.0
    d.magnitude = 0.0
    return d
