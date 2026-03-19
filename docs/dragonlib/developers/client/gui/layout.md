---
categories:
  - DragonLib
---

# Layout
To simplify arranging components in GUIs, DragonLib offers a layout system with predefined layout managers such as `FlowLayout`, `GridLayout` and others.

## Setting a layout
Set a layout manager using the `layout` property on any `DLGuiComponent`.

```java
FlowLayout flowLayout = new FlowLayout();
// ... change layout properties ...
this.layout.set(flowLayout);
```

When a new layout is set, all child components are rearranged according to that layout.

## Layout constraints
Some layouts require child components to provide additional information so the layout manager knows how to handle them. For example, `TableLayout` requires each child to know the target column.

This is done via the `layoutConstraint` property. This flexible property can hold any value; each layout manager defines what it expects.

!!! note
    The `layoutConstraint` property must be set on the child components, not on the component that holds the layout!

Because there is no type checking, incorrect values can be used. Layout managers should validate constraints and document the expected data.

```java
this.layoutConstraint.set(FlowLayout.LayoutConstraint.FILL);
```

## Updating layouts
Layouts update automatically on certain events, such as adding/removing components or changing a child's position or size. Pay attention to the order of operations: if you add a component before setting its layout constraint, the constraint might not be considered during the immediate update.

Avoid:
```java
DLButton button = addComponent(new DLButton(10, 10));
button.layoutConstraint.set(FlowLayout.LayoutConstraint.FILL);
```

Prefer:
```java
DLButton button = new DLButton(10, 10);
button.layoutConstraint.set(FlowLayout.LayoutConstraint.FILL);
addComponent(button);
```

## Creating custom layouts
If built-in layouts are not enough, create your own by implementing `ILayoutManager`.

```java
public class CustomLayout implements ILayoutManager {

    public final NumberProperty<Integer> someValue = new NumberProperty<>(0); 

    @Override
    public LayoutResult arrangeComponents(DLGuiComponent host) {
        List<DLGuiComponent> children = host.getComponents();
        
        // ... place components ...
    }
    
    // Optional: a safe method to read the layoutConstraint. Your implementation may differ.
    private String getConstraintOrDefault(DLGuiComponent child, String def) {
        if (child.layoutConstraint != null && child.layoutConstraint.get() instanceof String) {
            return (String)child.layoutConstraint.get();
        }
        return def;
    }
}
```

In `arrangeComponents` you must position the child components. Only the host component is provided as a parameter, so you can access other properties via the host.