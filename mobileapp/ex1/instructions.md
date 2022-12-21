# Ex2 - Device Manager

Une api qui peut detecter des devices via un utilitaire (qu'on fourni avec le projet).
Il faut detecter les device periodiquement dans un thread.

Example:

```
./device_detector [IOS|Android|Any]
- IOS: 88129301-123717237 Iphone 10X
- Android: asid912838asdsad Samsung Galaxy S10e
```

```
./stream_device [UUID]
FRAME (255, 0, 12) (255, 12, 44) (12, 0, 1)
FRAME (255, 0, 12) (255, 12, 44) (12, 0, 1)
FRAME (255, 0, 12) (255, 12, 44) (12, 0, 1)
No frame detected - Device unavailable
FRAME (255, 0, 12) (255, 10, 55) (0, 11, 10)
```

Api:

```
GET /devices?filter=[IOS|Android|Any] => JSON
```


