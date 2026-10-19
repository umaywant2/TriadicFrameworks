@echo off
echo Creating...
cd docs
md spine
cd spine
echo . > index.md
echo . > overview.md
cd..
md rtt
cd rtt
echo . > index.md
echo . > resonance-time-theory.md
cd..
md modules
cd modules
echo . > index.md
echo . > registry.md
md module-template
cd module-template
echo . > index.md
echo . > module.json
echo . > examples.md
cd..
cd..
md ideas
cd ideas
echo . > index.md
cd..
md operators
cd operators
echo . > index.md
cd..
md glossary
cd glossary
echo . > index.md
echo . > terms.md
cd..
md examples
cd examples
echo . > index.md
cd..
md ai-edition
cd ai-edition
echo . > index.md
echo . > contributing.md
cd..
cd i18n
cd es
cd docusaurus-plugin-content-docs
cd current
md ai-edition
cd ai-edition
echo . > index.md
cd..
md examples
cd examples
echo . > index.md
cd..
md glossary
cd glossary
echo . > index.md
cd..
md ideas
cd ideas
echo . > index.md
cd..
md modules
cd modules
echo . > index.md
echo . > registry.md
cd..
md operators
cd operators
echo . > index.md
cd..
md rtt
cd rtt
echo . > index.md
cd..
md spine
cd spine
echo . > index.md
cd..
echo . > contributing.md
md docusaurus-plugin-content-blog
cd docusaurus-plugin-content-blog
echo . > translated-blog-posts.md
cd..
md docusaurus-plugin-content-pages
cd docusaurus-plugin-content-pages
echo . > translated-static-pages.md
cd..
md fr
md de
md pt
md zh
md ja
md ar
md hi
md ru
md it
md ko
md nl
echo . > docusaurus.config.js
echo . > sidebars.js
echo . > package.json
