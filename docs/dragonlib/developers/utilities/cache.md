---
categories:
  - DragonLib
---

# Cache

Caches are used to store data temporarily. They are especially useful for expensive computations that don't need to be recalculated frequently. DragonLib provides several cache variants that share the same basic functionality.

## Cache

This is the standard cache class that stores a single value.

```java
Cache<MyObject> myCache = new Cache<>(() -> new MyObject(1, "Hello", true));
```

Call `get()` to retrieve the value. On the first call the supplier runs and the result is stored. Subsequent `get()` calls return the cached instance. Use `clear()` to empty the cache.

You can optionally set a caching priority. The DragonLib configuration can control which priorities are actually stored. Example:

```java
Cache<MyObject> myCache =
    new Cache<>(() -> new MyObject(1, "Hello", true), ECachingPriority.LOW);
```

If the config requires a minimum priority of `NORMAL`, caches with `LOW` (or lower) are not persisted and will be recomputed each time. This lets users reduce RAM usage a bit. `ALWAYS` forces the value to be cached regardless of config.

!!! note
    The effects depend on how intensively mod authors use the feature. If the cached amount of data isn't huge, no effects will be noticeable.

## DataCache

A variant of the standard cache that accepts an input parameter for computing its value.
The input value is provided when calling `get(...)`.

```java
Cache<MyObject, InputData> myCache =
    new Cache<>((inputData) -> new MyObject(2, inputData.text(), false));
```

## MapCache

This cache stores multiple values for different input keys — similar to a map.

```java
Cache<MyObject, InputHashObject, InputData> myCache =
    new Cache<>(
        (inputData) -> new MyObject(3, inputData.text(), false),
        (inputHashObject) -> inputHashObject.hashCode()     // Hash function
    );
```

Generic parameters:

- The cached value type.
- The class used to compute the hash (can be the same as the input data class).
- The input data class.

Use `clearAll()` to remove all cached entries. Remove individual entries with `clear(inputData)`.

## TimeCache

This cache stores the data only for a specific period before it is declared invalid and must be recalculated. For this purpose, a TTL (time to live) value in milliseconds is passed to the constructor, indicating how many milliseconds after the calculation the value remains valid. Internally, the time is set using `System.currentTimeMillis()` and this value is also used for verification.

```java
TimeCache<MyObject> myCache =
    new TimeCache<>(() -> new MyObject(1, "Hello", true), 200);
```

In this example, the data is valid for 200ms. If `get()` is called after that time, the data is recalculated. The cache then behaves as if there were no data in memory.