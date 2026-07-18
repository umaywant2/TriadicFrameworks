using System.Threading.Tasks;
using UnityEngine;

public class RTT_DemoController : MonoBehaviour
{
    public RTTCoreConfig config;
    public Transform player;

    private int tick = 0;

    async void Update()
    {
        var packet = BuildPacket();
        if (config.logPackets) Debug.Log($"RTT packet: {packet}");

        var response = await RTTCoreClient.StepAsync(packet, config);
        if (response == null) return;

        if (config.logResponses) Debug.Log($"RTT response: {response}");

        ApplyResponse(response);
        tick++;
    }

    private string BuildPacket()
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

    private void ApplyResponse(string json)
    {
        // For a real integration, define DTOs instead of dynamic parsing.
        // Here we just show the hook point.
        // Example: update player position / resonance based on RTT output.
    }
}

