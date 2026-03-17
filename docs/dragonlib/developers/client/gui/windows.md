---
categories:
  - DragonLib
---

# DLWindow

Windows are the foundation of DragonLib's GUI system. Components cannot be displayed or used without an underlying window.
To open a window use the `DLWindowManager`. There are two common ways to open windows described below.

## Structure

There is no single global window stack. Instead DragonLib uses modal layers where each modal layer contains its own window stack.
You can interact with all windows on the same modal layer. The window with focus is brought to the front and covers the windows behind it.
Windows on different modal layers are still rendered but cannot be interacted with — useful for dialogs.
Each `DLWindowManager` provides a default modal layer where windows are placed by default.

## Creating windows

There are several ways to open a new window.
If no Screen is open yet, you can create a new window via `DLScreen` or use the shortcut on `DLWindow`.

Using `DLScreen`:
```java
DLScreen<?> screen = new DLScreen<>(null, (manager) -> new MyWindow(manager));
Minecraft.getInstance().setScreen(screen);
```

Shortcut via `DLWindow`:
```java
DLWindow.openWindow((manager) -> new MyWindow(manager));
```

If a Screen is already open and you want to open another window, use the `DLWindowManager`:
```java
getWindowManager().createWindow((manager) -> new MyWindow(manager));
getWindowManager().createModal((manager) -> new MyWindow(manager));
```

- `createWindow` adds the window to the current modal layer's stack.
- `createModal` creates a new modal layer and adds the window to that layer.

## Advanced properties

Some window properties affect behavior. For example, `topLevel` keeps a window always on top.