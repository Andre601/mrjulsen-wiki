---
categories:
  - DragonLib
---

# GUI

DragonLib provides its own GUI system that works independently from vanilla widgets. The goal is a consistent, feature-rich and easy-to-use framework that in some places resembles classic GUI toolkits. It is not compatible with vanilla GUIs, so they cannot be mixed directly.

## DLGuiComponent

Every component and window is based on the base class `DLGuiComponent`. Therefore all components inherit the functionality provided by that class and support the standard events.

If you need a custom component that is not covered by built-in ones, extend `DLGuiComponent`. Each component has position and size initialized in the constructor.

## Windows

Vanilla opens a new Screen for each GUI. DragonLib uses windows inside a special Screen (`DLScreen`). Multiple windows can be open and switched between — similar to desktop environments. A window is the primary container for components. To use components you must open a window first.

## DLWindowManager

This class is the central manager for windows. It receives input (mouse, keyboard, rendering) and dispatches events to the GUI system. The window manager controls windows and provides utilities, for example to get the current mouse position on the screen.

!!! warning
    The window manager is available from any component that is part of a window/other component. If your component is not yet added to a window/other component, the manager is not available, returning `null`.

### Coordinate systems

Unlike vanilla (which uses screen coordinates), DragonLib components use local coordinates. For example, the top-left corner inside a button is at 0,0. You can still obtain screen coordinates via `DLWindowManager` when necessary.

### Properties

Components are configured using Properties instead of getters/setters. Properties reduce boilerplate and provide features like value ranges for numeric types.

Exceptions are position and size — due to complexity these are still handled via methods (e.g., `setX(...)`, `y()`, `setSize(...)`, `setHeight(...)`).

### Events

Most interactions are handled via events: mouse clicks, keyboard input, property changes, component position/size changes, etc. `DLGuiComponent` already defines many standard events that are safe to use in all components. These events are listed in `DLGuiStandardEvents`.

Example:

```java
DLPanel myPanel = new DLPanel(0, 0, 50, 50);
myPanel.addEventListener(DLGuiStandardEvents.ClickEvent.class, (sender, event) -> {
    System.out.println("Clicked on " + sender);
    return false;
});
```

Components may also expose component-specific events (e.g., `ValueChangedEvent` for `DLNumberPicker`). Custom components can define their own events, following the event system rules.

## DLScreen and DLContainerScreen

These classes bridge Minecraft's Screen API and DragonLib's `DLWindowManager`. They forward input and rendering to the window manager. Most users don't need to interact with these classes, except for special cases where vanilla and DragonLib GUIs are combined.



