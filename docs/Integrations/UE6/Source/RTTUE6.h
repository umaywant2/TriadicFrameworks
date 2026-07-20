// RTTUE6.h
// C++ RTT operator binding stubs for Unreal Engine 6

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "RTTUE6.generated.h"

USTRUCT(BlueprintType)
struct FRTTResonanceFrame
{
    GENERATED_BODY()

    UPROPERTY(BlueprintReadOnly)
    float Amplitude = 0.0f;

    UPROPERTY(BlueprintReadOnly)
    float Frequency = 0.0f;

    UPROPERTY(BlueprintReadOnly)
    float Phase = 0.0f;
};

USTRUCT(BlueprintType)
struct FRTTEntropySignature
{
    GENERATED_BODY()

    UPROPERTY(BlueprintReadOnly)
    FVector Location = FVector::ZeroVector;

    UPROPERTY(BlueprintReadOnly)
    float Radius = 0.0f;

    UPROPERTY(BlueprintReadOnly)
    float Intensity = 0.0f;
};

UCLASS(ClassGroup=(RTT), meta=(BlueprintSpawnableComponent))
class URTTComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    URTTComponent();

    UFUNCTION(BlueprintCallable, Category="RTT|Operators")
    void RTT_ApplyPhiField(UPrimitiveComponent* Target);

    UFUNCTION(BlueprintCallable, Category="RTT|Operators")
    void RTT_ApplyVarianceStabilizer(UPrimitiveComponent* Target);

    UFUNCTION(BlueprintCallable, Category="RTT|Operators")
    FRTTResonanceFrame RTT_ProbeResonance(UObject* Context);

    UFUNCTION(BlueprintCallable, Category="RTT|Entropy")
    FRTTEntropySignature RTT_TraceEntropy(UObject* WorldContext);

    UFUNCTION(BlueprintCallable, Category="RTT|Hybrid")
    void RTT_ApplyHybridOperator(UObject* Context);
};
