// RTTDemoActor.cpp
#include "RTTDemoActor.h"
#include "RTTCoreClient.h"
#include "RTTCoreConfig.h"

ARTTDemoActor::ARTTDemoActor()
{
    PrimaryActorTick.bCanEverTick = true;
    TickCount = 0;
}

void ARTTDemoActor::BeginPlay()
{
    Super::BeginPlay();
}

void ARTTDemoActor::Tick(float DeltaSeconds)
{
    Super::Tick(DeltaSeconds);

    if (!Config) return;

    const FVector Pos = GetActorLocation();

    // Minimal JSON; in production, use a JSON library to build this safely.
    FString Payload = FString::Printf(
        TEXT("{\"rtt_version\":\"1.0\",\"tick\":%d,\"entities\":[{\"id\":\"actor\",\"state\":{\"position\":[%.3f,%.3f,%.3f],\"velocity\":[0,0,0],\"resonance\":0.42}}],\"environment\":{\"field_strength\":0.18,\"phase_noise\":0.02},\"intent\":\"advance\"}"),
        TickCount, Pos.X, Pos.Y, Pos.Z
    );

    FRTTResponseDelegate Callback;
    Callback.BindUObject(this, &ARTTDemoActor::HandleRTTResponse);
    URTTCoreClient::Step(Payload, Config, Callback);

    TickCount++;
}

void ARTTDemoActor::HandleRTTResponse(const FString& Json)
{
    // Hook point: parse JSON and update actor state / trigger events.
}
