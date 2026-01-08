// docs/schemas/rsadi-gd/Unreal/RSADI_GDTypes.h
#pragma once

#include "CoreMinimal.h"
#include "RSADI_GDTypes.generated.h"

USTRUCT(BlueprintType)
struct FGDPosition
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float X;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Y;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Z;
};

USTRUCT(BlueprintType)
struct FGDDriftVector
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Dx;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Dy;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Dz;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Magnitude;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString Units; // "1/s"
};

USTRUCT(BlueprintType)
struct FGDClaritySample
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString SampleId;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString Timestamp;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FGDPosition Position;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 ClarityScore;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 StressHint;
};

USTRUCT(BlueprintType)
struct FGDZoneState
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString ZoneId;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString Timestamp;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 ClarityScore;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 StressHint;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString RiskLevel; // "low" | "medium" | "high" | "critical"

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FGDDriftVector DriftVector;
};

USTRUCT(BlueprintType)
struct FGDRoutePoint
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FGDPosition Position;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 ClarityScore;
};

USTRUCT(BlueprintType)
struct FGDRouteSuggestion
{
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString RouteId;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString Timestamp;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FGDPosition FromPosition;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FGDPosition ToPosition;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    TArray<FGDRoutePoint> ClarityProfile;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString RiskLevel;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    TArray<FString> Instructions;
};

// You can expose a URSADIService UObject with BlueprintCallable methods that return these structs.
