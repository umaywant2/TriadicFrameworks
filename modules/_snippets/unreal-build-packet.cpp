FString BuildRTTPacket(int32 TickCount, const FVector& Pos)
{
    return FString::Printf(
        TEXT("{\"rtt_version\":\"1.0\",\"tick\":%d,"
             "\"entities\":[{\"id\":\"actor\",\"state\":{"
             "\"position\":[%.3f,%.3f,%.3f],"
             "\"velocity\":[0,0,0],"
             "\"resonance\":0.42}}],"
             "\"environment\":{\"field_strength\":0.18,\"phase_noise\":0.02},"
             "\"intent\":\"advance\"}"),
        TickCount, Pos.X, Pos.Y, Pos.Z
    );
}

