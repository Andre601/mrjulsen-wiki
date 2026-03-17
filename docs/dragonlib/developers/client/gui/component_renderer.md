---
categories:
  - DragonLib
---

# Component renderer
Some components offer a `componentRenderer` property. A component renderer is a small class that renders a base component externally — similar to skins or a resource pack.

The renderer receives the component and its current state (e.g. pressed, hovered, disabled). States are usually represented by an enum and can differ between components. For `DLButton` this would be `ButtonState`, covering all possible button states. You can render each state individually and are not limited to a single texture — you can draw textures, solid colors, text or even items.

A component renderer avoids creating a new subclass just to change rendering. Swap the skin instead of subclassing. For major changes, creating a subclass might still be necessary.

Every component renderer implements `IStateRenderer` with the appropriate enum type for the states.

Example of a simple button renderer:
```java
public class CustomButtonRenderer implements IStateRenderer<ButtonState> {

    public static final CustomButtonRenderer INSTANCE = new CustomButtonRenderer();

    private CustomButtonRenderer() {
    }

    @Override
    public void renderSprite(DLGuiGraphics graphics, int x, int y, int w, int h, DLGuiComponent component, ButtonState state) {
        AbstractSprite sprite = switch (state) {
            case SELECTED -> DefaultGuiTextures.VANILLA_BUTTON.getSprite("selected");
            case DOWN -> DefaultGuiTextures.VANILLA_BUTTON.getSprite("down");
            case DISABLED -> DefaultGuiTextures.VANILLA_BUTTON.getSprite("disabled");
            case DOWN_SELECTED -> DefaultGuiTextures.VANILLA_BUTTON.getSprite("down_selected");
            case DISABLED_SELECTED -> DefaultGuiTextures.VANILLA_BUTTON.getSprite("disabled_selected");
            default -> DefaultGuiTextures.VANILLA_BUTTON.getSprite("normal");
        };
        sprite.render(graphics, x, y, w, h);
    }
}
```