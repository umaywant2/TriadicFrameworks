// RTTCoreClient.h
#pragma once

#include "CoreMinimal.h"
#include "RTTCoreClient.generated.h"

class URTTCoreConfig;

DECLARE_DYNAMIC_DELEGATE_OneParam(FRTTResponseDelegate, const FString&, ResponseJson);

UCLASS()
class URTTCoreClient : public UObject
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category="RTT")
    static void Step(const FString& JsonPayload, URTTCoreConfig* Config, FRTTResponseDelegate Callback);
};
