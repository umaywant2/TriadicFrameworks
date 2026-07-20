// RTTDemoActor.h
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "RTTDemoActor.generated.h"

class URTTCoreConfig;

UCLASS()
class ARTTDemoActor : public AActor
{
    GENERATED_BODY()

public:
    ARTTDemoActor();

    UPROPERTY(EditAnywhere, Category="RTT")
    URTTCoreConfig* Config;

protected:
    virtual void Tick(float DeltaSeconds) override;
    virtual void BeginPlay() override;

private:
    int32 TickCount;
    void HandleRTTResponse(const FString& Json);
};
