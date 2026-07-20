#pragma once

#include "Engine/DataAsset.h"
#include "RTTCoreConfig.generated.h"

UCLASS(BlueprintType)
class URTTCoreConfig : public UDataAsset
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="RTT")
    FString EndpointUrl = TEXT("http://localhost:5000/rtt/step");

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="RTT")
    bool bLogPackets = true;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="RTT")
    bool bLogResponses = true;
};
