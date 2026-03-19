---
categories:
  - DragonLib
---

# Events
DragonLib includes a small event system that is used in several places and can also be used elsewhere.

## Defining events
An event is created very easily. You only need a simple class or record that provides the required parameters and implements `IEvent`.

```java
public record MyCustomEvent(String name, int number, boolean state) implements IEvent {}
```

## Event dispatcher
An event dispatcher is an object that can trigger events. It provides all necessary functions.
To do this, the class must implement the `IEventDispatcher<>` interface. This class is also responsible for storing the event listeners. In most cases this is straightforward.

```java
public class Dog implements IEventDispatcher<Dog> {    

    private final Map<Class<? extends IEvent>, PriorityQueue<EventListenerWrapper<?>>> eventListeners = new HashMap<>();

    @Override
    public Map<Class<? extends IEvent>, PriorityQueue<EventListenerWrapper<?>>> getEventListeners() {
        return eventListeners;
    }
}
```

Next, you must specify which events are supported. Use an annotation on the dispatcher class that lists the event classes.

```java
@SupportsEvents({
    BreathingEvent.class,
    BarkEvent.class,
    EatingEvent.class
})
public class Dog implements IEventDispatcher<Dog> { 
    // ...
}
```

!!! warning
    If events are used that are not supported by the respective dispatcher, an exception will be thrown!

!!! note
    `SupportsEvents` is inherited through class inheritance. For example, if a base class `Animal` supports `BreathingEvent`, then `Dog extends Animal` also supports it without needing to repeat the annotation in `Dog`.

## Triggering events
Events can be triggered through the event dispatcher using the `invokeEvent` method.

```java
invokeEvent(this, new BarkEvent(...));
```

The first parameter is usually the object on which the event is triggered. For example, when triggering a button click event, pass the button as the first parameter. This is the reference object that developers can retrieve to know which object triggered the event. The second parameter is the event instance with all required information.

!!! warning
    If an event class is passed that is not listed in the `@SupportedEvents` of the corresponding class, the game will throw an error at runtime.

## Adding event listeners
To react to events, you add an event listener with the `addEventListener` method.
A complete example:

```java
EventListenerId barkEventId = addEventListener(BarkEvent.class, (src, event) -> {
    playBarkSound();
    return false;
}, 100);
```

!!! warning
    If an event class is passed that is not listed in the `@SupportedEvents` of the corresponding class, the game will throw an error at runtime.

You can add any number of event listeners per event. The return value is important. Usually it is set to `false`, which means the execution chain is not stopped. If a listener returns `true`, all subsequent listeners with lower priority or that were added earlier will not be executed and the chain is stopped.

The last parameter defines the priority. Listeners are executed according to their natural order (smaller first). This parameter is optional and defaults to `0`.

When adding an event listener, an ID is returned. You can use this ID later to remove the listener, but you don't have to.

## Removing event listeners
To remove an event listener, use the `removeEventListener` method. Provide the event class and the listener ID.

```java
removeEventListener(BarkEvent.class, barkEventId);
```
