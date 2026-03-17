---
categories:
  - DragonLib
---

# Networking
Networking in Minecraft is required so that client and server can communicate. Mod loaders already provide networking APIs, but DragonLib includes its own networking system built on top of vanilla Minecraft with the goal of being simple and consistent to use.

The following components are needed to transfer data.

## Network Manager
To use the networking system you must create a `DLNetworkManager`. Usually one network manager is created per mod, but it is also possible to use multiple managers.
```java
public static final DLNetworkManager MY_NETWORK_MANAGER = new DLNetworkManager(DLUtils.resourceLocation("my_mod_id", "network"), "v1");
```

A network manager uses a fixed `ResourceLocation` as its ID and also receives a protocol version.

!!! note
    The protocol version is used to compare versions when attempting to join a server.

## Packet Data
Network packet data is a small class that contains all data to be transmitted, and handles serialization and deserialization. The NBT format is used as the transfer medium. A packet data class must extend `NetworkPacketData`.

```java
public class MyNetworkPacketData extends NetworkPacketData {
        
    private UUID id;
    private String name;

    public MyNetworkPacketData(DLStatus status, UUID id, String name) {
        super(status);
        this.id = id;
        this.name = name;
    }

    @Override
    protected void write(CompoundTag nbt) {
        nbt.putUUID("Id", id);
        nbt.putString("Name", name);
    }

    @Override
    protected void read(CompoundTag nbt) {
        this.id = nbt.getUUID("Id");
        this.name = nbt.getString("Name");
    }
}
```

To simplify it, two constructors can be used: one for creating the class with data and one for creating an empty instance in the registration process.

```java
public class MyNetworkPacketData extends NetworkPacketData {

    public MyNetworkPacketData(DLStatus status) {
        super(status);
    }

    public MyNetworkPacketData(UUID id, String name) {
        super(DLStatus.OK); // <-- Depends on whether you want to use this
        this.id = id;
        this.name = name;
    }

    // ...
}
```
   

## Packet Type
DragonLib provides several ways to transfer data. While vanilla Minecraft only allows data to be sent from one sender to one receiver, DragonLib also supports requesting data from the other side, waiting for a response when sending data, or streaming data. The standard types are listed as inner classes in `NetworkPacketType`. The choice of type depends on the use case.

| Name | Description |
| - | - |
| Send | Sends data from a sender to a receiver, where it is processed. No response is returned. (Vanilla behavior) |
| Receive | Requests data from the other side, which will then send that data back. |
| Send and Receive | Sends data from a sender to a receiver, which processes it and sends a response back to the sender, with or without data. |
| Stream | Similar to `Send and Receive`, but sends smaller data chunks and only sends the next chunk after the other side responds. |

!!! warn
    For very large amounts of data (e.g., files) you should always use `Stream`! With other types, all data is fully cached in memory, and a response is only sent once all data has arrived. With `Stream`, the data can be processed immediately, and RAM consumption remains low. This theoretically allows for the transmission of infinitely large amounts of data.

## Packet Handler
A packet handler is basically a functional interface that takes the packet and processes it. For the different packet types there are specialized implementations, found as inner classes in `NetworkProcessor`.

| Name | Description |
| - | - |
| Send | Receives the input packet and has no return value. |
| Receive | Returns only the output packet. |
| Send and Receive | Receives the input packet and returns the output packet. |
| StreamProvider | Similar to `Send and Receive` with minor differences. |

```java
Output handle(Input packet, NetworkPacketContext context) {
    // ... do stuff ...
    return new Output(...);
}
```

!!! info
    Usually the network packet type determines which processor is needed. Custom network types, however, can be more flexible.

!!! tip
    For convenience, the handler can be implemented as a static method inside the input or output packet class to reduce the number of classes. For example:
    ```java
    public static class MyRequestPacket extends NetworkPacketData {

        // ...

        public static MyResponsePacket handle(MyRequestPacket packet, NetworkPacketContext context) {
            // ... do stuff ...
            return new ResponsePacket(...);
        }
    }
    ```

## Registering packets
To register a packet you need the created network manager instance. Use the appropriate `register` method that matches the required `NetworkPacketType`. As parameters, provide the packet name and the intended send direction (client -> server or server -> client). Then pass the handler(s) and supplier(s) to create empty data instances. It doesn't matter whether fields in the class are initialized, since the data will be populated during deserialization.

The return value is always an instance of the corresponding network packet type that should be stored for sending data later.

```java
public static final NetworkPacketType.Send<NetworkDirection.C2S, MySendData> SEND_PACKET =
    NETWORK.registerSendOnly(
        "send",                 // The name of the packet
        NetworkDirection.C2S,   // The direction (Client to server or server to client)
        MySendData::handle,     // The packet handler
        MySendData::new         // The packet instance supplier
    );

public static final NetworkPacketType.Receive<NetworkDirection.C2S, MyResponseData> RECEIVE_PACKET =
    NETWORK.registerReceiveOnly(
        "receive",              // The name of the packet
        NetworkDirection.C2S,   // The direction (Client to server or server to client)
        MyResponseData::handle, // The packet handler
        MyResponseData::new     // The packet instance supplier
    );

public static final NetworkPacketType.SendAndReceive<NetworkDirection.C2S, MyNetworkPacket.Request, MyNetworkPacket.Response> SEND_AND_RECEIVE_PACKET =
    NETWORK.registerSendAndReceivePacket(
        "send_and_receive",             // The name of the packet
        NetworkDirection.C2S,           // The direction (Client to server or server to client)
        MyNetworkPacket::handle,        // The packet handler
        MyNetworkPacket.Request::new,   // The request packet instance supplier
        MyNetworkPacket.Response::new   // The response packet instance supplier
    );
```

## Using a packet
Use the result of the registered packet and call its `send` method. The first parameter determines the destination, which is fixed according to the registered network direction (C2S or S2C). Several standard methods can be found in the `NetworkDirection` class. Here, `toServer()` is used because it's a `C2S` packet. For `S2C`, a player would need to be selected as the destination, e.g., `toPlayer(serverPlayer)`.

```java
SEND_PACKET.send(
    NetworkDirection.toServer(),    // The destination provider. Here it's simple, but players could be filtered by position, for example.
    new MyPacketData(...)           // The input data class
);

RECEIVE_PACKET.send(
    NetworkDirection.toServer(),    // The destination provider. Here it's simple, but players could be filtered by position, for example.
    (response) -> { /* response callback */ },
    () -> { /* error callback */ }
);

SEND_AND_RECEIVE_PACKET.send(
    NetworkDirection.toServer(),    // The destination provider. Here it's simple, but players could be filtered by position, for example.
    new MyPacketData(...),          // The input data class
    (response) -> { /* response callback */ },
    () -> { /* error callback */ }
);
```

!!! Warning
    Ensure that the packet is sent from the intended side. If your packet is registered as `C2S`, it should be sent from the **client** to the server, not from the dedicated **server** to players.

Custom implementations are also possible, which would then return either a `C2S` or `S2C` object.

## Sequencing und size limits
In vanilla Minecraft, it's crucial keep an eye on payload and packet size limits, especially when transferring large amounts of data. Otherwise, the worst-case scenario is a failed transfer, resulting in server crashes or player kicks.

DragonLib handles this, allowing you to send any amount of data in one single pass without any concerns.

DragonLib internally divides the data and sends multiple chunks, which are then reassembled on the other end. Processing begins once all the data is transferred.

## Status
In addition to the user-defined data, a status is transmitted, which can be retrieved during processing using `data.getStatus()`. For example, if an unhandled exception is thrown somewhere, an error status with details is returned as a substitute response. It is good practice to always check the status beforehand to avoid any unexpected errors.

Developers can also intentionally set a status by using the status variable when creating a data class. Usually `DLStatus.OK` will be used there.

```java
public MyNetworkPacket(DLStatus status) {
    super(status);
}
```

!!! Note
    If an error status is transmitted in a response, this will trigger the error callback!

## Tips
To reduce the number of classes—especially for transfers that have both input and output packets—it is recommended to group related parts as inner classes within a parent class.

```java
public class RequestAndReceivePacket {

    public static class Request extends NetworkPacketData {
        public Request(DLStatus status) {
            super(status);
        }

        @Override
        protected void write(CompoundTag nbt) {
            // ...
        }

        @Override
        protected void read(CompoundTag nbt) {
            // ...
        }
    }

    public static class Response extends NetworkPacketData {
        public Response(DLStatus status) {
            super(status);
        }

        @Override
        protected void write(CompoundTag nbt) {
            // ...
        }

        @Override
        protected void read(CompoundTag nbt) {
            // ...
        }              
    }

    public static Response handle(Request packet, NetworkPacketContext context) {
        // ...
        return new Response(...);
    }    

}
```