---
categories:
  - DragonLib
---

# Rendering
Rendering in DragonLib GUIs happens on several layers, each with its own purpose.

- **Back layer**  
  The background layer. Not used by default, but useful to render a component's background independently. The drawing area is limited by the rendering bounds.
- **Main layer**  
  The default layer where the component itself is drawn (e.g. texture and label). The drawing area is limited by the rendering bounds.
- **Front layer**  
  Renders on top of all other components. No rendering bounds apply, so you can use the whole screen — ideal for tooltips.
- **Overlay layer**  
  A special layer used in specific situations with special behavior. Special layers cannot be used like normal layers. For example, the overlay layer is shown when moving a component.

## Standard methods
Each component must be rendered, so there are several render methods you can override. Even though a `RenderEvent` exists, overriding a component's render method is usually preferred when implementing a component.

If rendering should be influenced externally, use the Render Event.

!!! warning  
    In `RenderEvent` it is important to check the current layer at the beginning to avoid rendering the same content multiple times, which also helps performance.  
    This would be wrong:
    ```java
    addEventListener(DLGuiStandardEvents.RenderEvent.class, (sender, event) -> {
        // render stuff here
        return false;
    });
    ```
    Correct:
    ```java
    addEventListener(DLGuiStandardEvents.RenderEvent.class, (sender, event) -> {
        if (event.layer() == RenderLayer.MAIN) {
            // render stuff here
        }
        return false;
    });
    ```
    (Exceptions are possible depending on the use case.)


