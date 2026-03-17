---
categories:
  - DragonLib
---

# Properties

DragonLib provides a small property system with several specialized property types. In Java you often add many getters and setters for fields that only store or return a value. Properties reduce boilerplate and add useful features like default values and numeric ranges.

## Defining Properties
Properties are usually declared as public final fields so they remain accessible. Control is handled inside the property object, so exposing the field is fine.

Example:

```java
public final Property<MyType> myProperty =
    new Property<MyType>(new MyType(...));
```

For specialized types the constructor differs:

```java
public final NumberProperty<Integer> myProperty =
    new NumberProperty<Integer>(20, 0, 100);
```

## Default Values
The value passed to the constructor is the default. Use `reset()` to restore it, or `getDefaultValue()` to fetch it without changing the property.

## Callbacks
Properties can register two callbacks that run before/after a value changes:

```java
<P extends IProperty<T>> P withAfterPropertyChangedCallback(IPropertyAfterUpdateCallback<T> callback);
<P extends IProperty<T>> P withModificationCallback(IPropertyUpdateCallback<T> callback);
```

Example:

```java
public final Property<ILayoutManager> layout =
    new Property<ILayoutManager>(NoLayout.INSTANCE)
        .withAfterPropertyChangedCallback((oldValue, newValue) -> newValue.arrangeComponents(this));
```

!!! tip
    Callbacks are useful in GUIs. For example, after changing a size property you can update the layout.

## Specialized Properties
DragonLib includes several specialized property classes for common use cases (numbers, booleans, lists). Use them directly where appropriate.

## Use Cases
Properties are used heavily in DragonLib's GUI system, where many settings are exposed as properties. They are also used by components like `BERLabel`.

!!! warning "Please keep in mind!"
    Properties are not always a replacement for getters/setters. They are best for compactly managing single values and related behaviors.