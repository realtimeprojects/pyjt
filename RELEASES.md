# v0.6.0
> 2023-08-07

-   Fix: Fixture.fill("") did not delete the text
-   Inspetor/xml: Fix empty values handling for existing attributes
-   Add `Fixture.dump()` for dumping tree to xml
-   Robot: `add Robot().typeVirtualKeys()` for typing virtual keys

# v0.5.2
> 2023-08-07

-   fix etree generation for empty titles and texts.
    Empty titles and texts now produce empty attributes,
    if the component has a getText() or getTitle() function.

# v0.5.1
> 2023-08-07

-   raise ElementNotFoundError on missed
    xpath searches

# v0.5.0
> 2023-08-07

-   support component lookup by xpath
-   Fix title/text mixup in Inspector

# v0.4.6
> 2023-08-04

-   release use markdown for README.

# v0.4.5
> 2023-08-04

-   revert v0.4.4 changes for pypi.org

# v0.4.4
> 2023-08-04

-   use rst for README.

# v0.4.3
> 2023-08-04

-   Fix quickstart instructions in README.md

# v0.4.2
> 2023-08-04

-   Fix quickstart instructions in README.md

# v0.4.1
> 2023-08-04

-   Fix `Frame.close()` not working
-   Proxy: Fix handling of properties

# v0.4.0
> 2023-08-04

-   Add `Proxy.isinstance()` function
-   Rename `Proxy.instance` property to `Proxy.object`
-   Add `Fixture.object` property
-   Improve docmentation.

# v0.3.1
> 2023-08-03

-   Improve documentation.

# v0.3.0
> 2023-08-03

-   Optimized find logic
-   Moved find method to Fixture
-   Fix locator bugs
-   Add `Locator.has()` to search for direct childs

# v0.2.1
> 2023-08-02

-   Robot.type(): Fix key events for some more special characters.

# v0.2.0
> 2023-08-02

-   `pyjt.init()`: Add `classpath` argument to set the classpath
    used for starting the JVM.

# v0.1.0
> 2023-08-02

-   `Fixture.fill()`: Support `FillMode.TYPE` for US keyboard layout
-   Add `Frame.dispose()`

# v0.0.1
> 2023-08-02

-   First basic release
