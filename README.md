Embed resources into code
=========================

This is an Arduino IDE example project for embedding text resources into the binary automatically.
It makes the contents of all `.html`, `.css` and `.js` files from the `data/` directory available in the code. E.g. `data/page1.html` is embedded as `page1_html`.

**Important**: name the root folder `embed_resources_example` after downloading this project. With Github's _Download ZIP_ option, it's by default named `embed_resources_example-main`, which causes a compilation error in the Arduino IDE.