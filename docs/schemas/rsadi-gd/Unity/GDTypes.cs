// docs/schemas/rsadi-gd/Unity/GDTypes.cs
using System;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class GDPosition
{
    public float x;
    public float y;
    public float z;

    public Vector3 ToVector3() => new Vector3(x, y, z);

    public static GDPosition FromVector3(Vector3 v) =>
        new GDPosition { x = v.x, y = v.y, z = v.z };
}

[Serializable]
public class GDClaritySample
{
    public string sample_id;      // uuid
    public string timestamp;      // ISO-8601
    public GDPosition position;
    public int clarity_score;     // 0–255
    public int stress_hint;       // 0–255
    public Dictionary<string, object> extensions;
}

[Serializable]
public class GDDriftVector
{
    public float dx;
    public float dy;
    public float dz;
    public float magnitude;
    public string units;          // "1/s"
}

[Serializable]
public class GDZoneState
{
    public string zone_id;
    public string timestamp;
    public int clarity_score;
    public int stress_hint;
    public string risk_level;     // "low" | "medium" | "high" | "critical"
    public GDDriftVector drift_vector;
    public Dictionary<string, object> extensions;
}

[Serializable]
public class GDRoutePoint
{
    public GDPosition position;
    public int clarity_score;
}

[Serializable]
public class GDRouteSuggestion
{
    public string route_id;
    public string timestamp;
    public GDPosition from_position;
    public GDPosition to_position;
    public List<GDRoutePoint> clarity_profile;
    public string risk_level;
    public List<string> instructions;
    public Dictionary<string, object> extensions;
}

// You can then add a simple “service” wrapper:
public interface IRSADIService
{
    GDZoneState GetZoneState(string zoneId);
    int GetClarity(Vector3 position);
    GDDriftVector GetDrift(Vector3 position);
    GDRouteSuggestion GetRoute(Vector3 from, Vector3 to);
}
