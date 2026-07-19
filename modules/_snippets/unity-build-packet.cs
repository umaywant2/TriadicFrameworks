private string BuildRTTPacket()
{
    var pos = player.position;

    var payload = new
    {
        rtt_version = "1.0",
        tick = tick,
        entities = new[]
        {
            new {
                id = "player",
                state = new {
                    position = new float[] { pos.x, pos.y, pos.z },
                    velocity = new float[] { 0f, 0f, 0f },
                    resonance = 0.42f
                }
            }
        },
        environment = new {
            field_strength = 0.18f,
            phase_noise = 0.02f
        },
        intent = "advance"
    };

    return JsonUtility.ToJson(payload);
}

